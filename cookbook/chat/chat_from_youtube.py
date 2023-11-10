from pprint import pprint

import openai

from lyzr import Chat

openai.api_key = "sk-"

link = ["https://www.youtube.com/watch?v=fcfVjd_oV1I"]

chatbot = Chat.from_youtube(
    urls=link,
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = "what does googler do?"

response = chatbot.chat(_query)

pprint(response.response)

_query = "what did i asked above?"
response = chatbot.chat(_query)
pprint(response.response)
