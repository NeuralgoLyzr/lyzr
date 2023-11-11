import os
from datetime import datetime
from typing import Optional, Union

import pandas as pd

from lyzr.base.file_utils import read_file
from lyzr.base.llms import LLM, Prompt


def get_analysis(
    query: Optional[str] = None,
    model: Optional[LLM] = None,
    model_name: Optional[str] = None,
    model_type: Optional[str] = None,
    api_key: Optional[str] = None,
    df: Optional[pd.DataFrame] = None,
    description: Optional[str] = None,
    prompt: Optional[Union[Prompt, str]] = None,
    **kwargs,
):
    if df is None:
        df = os.getenv("DATAFRAME")
    if not isinstance(df, pd.DataFrame):
        if not os.path.exists(df):
            raise ValueError(
                "Please provide a valid filepath or a pandas DataFrame object."
            )
        else:
            df = read_file(df, **kwargs)

    if prompt is None:
        prompt = os.getenv("PROMPT") or "analysis_steps_pt"
    if model is None:
        model = LLM(
            api_key=api_key or os.getenv("API_KEY"),
            model_type=model_type or os.getenv("MODEL_TYPE") or "openai",
            model_name=model_name or os.getenv("MODEL_NAME") or "gpt-3.5-turbo",
            prompt=prompt if isinstance(prompt, Prompt) else Prompt(prompt),
        )
    empty_variables = model.prompt.get_variables()
    if empty_variables != []:
        schema = [
            {
                "step1": "cleaning, groupby, kmneans, logisticregression, etc.",
                "parameters": {
                    "columns to group on": ["col1", "col2"],
                    "agg func": "mean, sum, etc.",
                    "columns to agg on": ["col1", "col2"],
                },
            },
            {"step2": "2nd analysis", "parameters": {...}},
        ]
        model.set_prompt(
            prompt_name=prompt,
            date=datetime.now().strftime("%Y-%m-%d"),
            schema=schema,
            df_head=df.head(),
            description=description,
            df_dtypes=df.dtypes,
            query=query,
        )

    model.set_prompt(date=datetime.now().strftime("%Y-%m-%d"))
    output = model.run()

    print(output)
    return output["choices"][0]["message"]["content"]
