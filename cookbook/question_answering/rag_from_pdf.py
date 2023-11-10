from pprint import pprint

import openai

from lyzr import QuestionAnswering

openai.api_key = "sk-"

path = ""

rag = QuestionAnswering.from_pdf(
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = ""

rag = rag.query(_query)

pprint(rag.response)
