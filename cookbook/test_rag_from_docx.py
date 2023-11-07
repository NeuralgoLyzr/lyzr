import openai
from lyzr import QuestionAnswering
from pprint import pprint

openai.api_key = "sk-"

path = ""

rag = QuestionAnswering.from_docx(
    input_files=[path],
    llm_params={"model": "gpt-3.5-turbo"},
)

_query = ""

rag = rag.query(_query)

pprint(rag.response)
