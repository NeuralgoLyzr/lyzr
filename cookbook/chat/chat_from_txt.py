from pprint import pprint

import openai

from lyzr import Chat

openai.api_key = "sk-"

path = ""

rag = Chat.from_txt(
    input_files=[path],
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = ""

rag = rag.chat(_query)

pprint(rag.response)
