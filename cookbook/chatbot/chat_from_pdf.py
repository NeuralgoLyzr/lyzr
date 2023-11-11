from pprint import pprint

import openai

from lyzr import ChatBot

openai.api_key = "sk-"

path = ""

rag = ChatBot.pdf_chat(
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = ""

rag = rag.chat(_query)

pprint(rag.response)
