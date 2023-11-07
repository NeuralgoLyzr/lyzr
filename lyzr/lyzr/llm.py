from llama_index.llms import LiteLLM
from llama_index.llms.base import LLM

class LyzrLLMFactory:
    @staticmethod
    def from_defaults(model: str = "gpt-3.5-turbo", **kwargs) -> LLM:
        return LiteLLM(model=model, **kwargs)
