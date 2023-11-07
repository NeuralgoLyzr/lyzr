import openai
from lyzr import QuestionAnswering
from pprint import pprint

openai.api_key = "sk-"

path = ""

rag = QuestionAnswering.from_pdf(          
    input_files=[path],
    llm_params={"model": "gpt-3.5-turbo"},
)

rag = rag.query("Tell me about infninity stone?")

pprint(rag.response)