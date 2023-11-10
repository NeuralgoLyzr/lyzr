from pprint import pprint

import openai

from lyzr import Chat

openai.api_key = "sk-"

link = "https://www.nelsongp.com/"

rag = Chat.from_website(
    url=link,
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = "what does nelson do?"

rag = rag.chat(_query)

pprint(rag.response)
