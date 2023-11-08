import openai
from lyzr import QuestionAnswering
from pprint import pprint

openai.api_key = "sk-"

link = "https://www.nelsongp.com/"

rag = QuestionAnswering.from_website(
    url=link,
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = "what does nelson do?"

rag = rag.query(_query)

pprint(rag.response)
