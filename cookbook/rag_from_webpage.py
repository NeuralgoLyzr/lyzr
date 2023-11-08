import openai
from lyzr import QuestionAnswering
from pprint import pprint

openai.api_key = "sk-"

link = "https://en.wikipedia.org/wiki/Akinobu_Okada"

rag = QuestionAnswering.from_webpage(
    url=link,
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = "what does akinobu do?"

rag = rag.query(_query)

pprint(rag.response)
