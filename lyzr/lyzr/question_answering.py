from typing import Sequence, Union, Optional, List

from llama_index import Document, ServiceContext, VectorStoreIndex
from llama_index.embeddings.utils import EmbedType
from llama_index.indices.query.base import BaseQueryEngine

from lyzr.lyzr.llm import LyzrLLMFactory

from lyzr.lyzr.service import LyzrService
from lyzr.lyzr.vector_store import LyzrVectorStoreIndex
from lyzr.utils.env_utils import find_and_load_dotenv
from lyzr.utils.document_reading import read_pdf_as_documents, read_docx_as_documents

def pdf_rag(
    input_dir: Optional[str] = None,
    input_files: Optional[List] = None,
    exclude_hidden: bool = True,
    filename_as_id: bool = True,
    recursive: bool = True,
    required_exts: Optional[List[str]] = None,
    system_prompt: str = None,
    query_wrapper_prompt: str = None,
    embed_model: Union[str, EmbedType] = "default",
    llm_params: dict = None,
    vector_store_params: dict = None,
    service_context_params: dict = None,
    query_engine_params: dict = None,
) -> BaseQueryEngine:
    
    documents = read_pdf_as_documents(
        input_dir=input_dir,
        input_files=input_files,
        exclude_hidden=exclude_hidden,
        filename_as_id=filename_as_id,
        recursive=recursive,
        required_exts=required_exts,
    )

    llm_params = {} if llm_params is None else llm_params
    vector_store_params = (
        {"vector_store_type": "LanceDBVectorStore"}
        if vector_store_params is None
        else vector_store_params
    )
    service_context_params = (
        {} if service_context_params is None else service_context_params
    )
    query_engine_params = {} if query_engine_params is None else query_engine_params

    llm = LyzrLLMFactory.from_defaults(**llm_params)
    service_context = LyzrService.from_defaults(
        llm=llm,
        embed_model=embed_model,
        system_prompt=system_prompt,
        query_wrapper_prompt=query_wrapper_prompt,
        **service_context_params,
    )

    vector_store_index = LyzrVectorStoreIndex.from_defaults(
        **vector_store_params, documents=documents, service_context=service_context
    )

    return vector_store_index.as_query_engine(**query_engine_params)

class QuestionAnswering:
    @staticmethod
    def from_instances(
        vector_store_index: VectorStoreIndex, service_context: ServiceContext, **kwargs
    ) -> BaseQueryEngine:
        return vector_store_index.as_query_engine(
            service_context=service_context, **kwargs
        )

    def from_pdf(
        input_dir: Optional[str] = None,
        input_files: Optional[List] = None,
        exclude_hidden: bool = True,
        filename_as_id: bool = True,
        recursive: bool = True,
        required_exts: Optional[List[str]] = None,
        system_prompt: str = None,
        query_wrapper_prompt: str = None,
        embed_model: Union[str, EmbedType] = "default",
        llm_params: dict = None,
        vector_store_params: dict = None,
        service_context_params: dict = None,
        query_engine_params: dict = None,
    ) -> BaseQueryEngine:
        return pdf_rag(
            input_dir=input_dir,
            input_files=input_files,
            exclude_hidden=exclude_hidden,
            filename_as_id=filename_as_id,
            recursive=recursive,
            required_exts=required_exts,
            system_prompt=system_prompt,
            query_wrapper_prompt=query_wrapper_prompt,
            embed_model=embed_model,
            llm_params=llm_params,
            vector_store_params=vector_store_params,
            service_context_params=service_context_params,
            query_engine_params=query_engine_params,
        )