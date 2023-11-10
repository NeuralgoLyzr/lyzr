from typing import Union, Optional, List

from llama_index import ServiceContext, VectorStoreIndex
from llama_index.embeddings.utils import EmbedType
from llama_index.chat_engine.types import BaseChatEngine


from lyzr.utils.chat_utils import (
    pdf_chat,
    txt_chat,
    docx_chat,
    webpage_chat,
    website_chat,
    youtube_chat,
)


class Chat:
    @staticmethod
    def from_instances(
        vector_store_index: VectorStoreIndex, service_context: ServiceContext, **kwargs
    ) -> BaseChatEngine:
        return vector_store_index.as_chat_engine(
            service_context=service_context, **kwargs
        )

    @staticmethod
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
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return pdf_chat(
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
            chat_engine_params=chat_engine_params,
        )

    @staticmethod
    def from_docx(
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
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return docx_chat(
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
            chat_engine_params=chat_engine_params,
        )

    @staticmethod
    def from_txt(
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
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return txt_chat(
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
            chat_engine_params=chat_engine_params,
        )

    @staticmethod
    def from_webpage(
        url: Optional[str] = None,
        system_prompt: str = None,
        query_wrapper_prompt: str = None,
        embed_model: Union[str, EmbedType] = "default",
        llm_params: dict = None,
        vector_store_params: dict = None,
        service_context_params: dict = None,
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return webpage_chat(
            url=url,
            system_prompt=system_prompt,
            query_wrapper_prompt=query_wrapper_prompt,
            embed_model=embed_model,
            llm_params=llm_params,
            vector_store_params=vector_store_params,
            service_context_params=service_context_params,
            chat_engine_params=chat_engine_params,
        )

    @staticmethod
    def from_website(
        url: Optional[str] = None,
        system_prompt: str = None,
        query_wrapper_prompt: str = None,
        embed_model: Union[str, EmbedType] = "default",
        llm_params: dict = None,
        vector_store_params: dict = None,
        service_context_params: dict = None,
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return website_chat(
            url=url,
            system_prompt=system_prompt,
            query_wrapper_prompt=query_wrapper_prompt,
            embed_model=embed_model,
            llm_params=llm_params,
            vector_store_params=vector_store_params,
            service_context_params=service_context_params,
            chat_engine_params=chat_engine_params,
        )

    @staticmethod
    def from_youtube(
        urls: List[str] = None,
        system_prompt: str = None,
        query_wrapper_prompt: str = None,
        embed_model: Union[str, EmbedType] = "default",
        llm_params: dict = None,
        vector_store_params: dict = None,
        service_context_params: dict = None,
        chat_engine_params: dict = None,
    ) -> BaseChatEngine:
        return youtube_chat(
            urls=urls,
            system_prompt=system_prompt,
            query_wrapper_prompt=query_wrapper_prompt,
            embed_model=embed_model,
            llm_params=llm_params,
            vector_store_params=vector_store_params,
            service_context_params=service_context_params,
            chat_engine_params=chat_engine_params,
        )
