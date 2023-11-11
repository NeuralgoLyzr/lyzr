from pprint import pprint

import openai

from lyzr import QABot

openai.api_key = "sk-"

path = ""

rag = QABot.pdf_qa(
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = ""

rag = rag.query(_query)

pprint(rag.response)
