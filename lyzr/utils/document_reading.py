import logging
from typing import List, Sequence, Optional

from llama_index.schema import Document

from lyzr.utils.pdf_reader import LyzrPDFReader
from lyzr.utils.docx_reader import LyzrDocxReader
from lyzr.utils.txt_reader import LyzrTxtReader
from llama_index.readers.file.base import SimpleDirectoryReader


logger = logging.getLogger(__name__)


def read_pdf_as_documents(
    input_dir: Optional[str] = None,
    input_files: Optional[List] = None,
    exclude_hidden: bool = True,
    filename_as_id: bool = True,
    recursive: bool = True,
    required_exts: Optional[List[str]] = None,
    **kwargs,
) -> Sequence[Document]:
    file_extractor = {".pdf": LyzrPDFReader()}

    reader = SimpleDirectoryReader(
        input_dir=input_dir,
        exclude_hidden=exclude_hidden,
        file_extractor=file_extractor,
        input_files=input_files,
        filename_as_id=filename_as_id,
        recursive=recursive,
        required_exts=required_exts,
        **kwargs,
    )

    documents = reader.load_data()

    logger.info(f"Found {len(documents)} 'documents'.")
    return documents


def read_docx_as_documents(
    input_dir: Optional[str] = None,
    input_files: Optional[List] = None,
    exclude_hidden: bool = True,
    filename_as_id: bool = True,
    recursive: bool = True,
    required_exts: Optional[List[str]] = None,
    **kwargs,
) -> Sequence[Document]:
    file_extractor = {".docx": LyzrDocxReader()}

    reader = SimpleDirectoryReader(
        input_dir=input_dir,
        exclude_hidden=exclude_hidden,
        file_extractor=file_extractor,
        input_files=input_files,
        filename_as_id=filename_as_id,
        recursive=recursive,
        required_exts=required_exts,
        **kwargs,
    )

    documents = reader.load_data()

    logger.info(f"Found {len(documents)} 'documents'.")
    return documents


def read_txt_as_documents(
    input_dir: Optional[str] = None,
    input_files: Optional[List] = None,
    exclude_hidden: bool = True,
    filename_as_id: bool = True,
    recursive: bool = True,
    required_exts: Optional[List[str]] = None,
    **kwargs,
) -> Sequence[Document]:
    file_extractor = {".txt": LyzrTxtReader()}

    reader = SimpleDirectoryReader(
        input_dir=input_dir,
        exclude_hidden=exclude_hidden,
        file_extractor=file_extractor,
        input_files=input_files,
        filename_as_id=filename_as_id,
        recursive=recursive,
        required_exts=required_exts,
        **kwargs,
    )

    documents = reader.load_data()

    logger.info(f"Found {len(documents)} 'documents'.")
    return documents
