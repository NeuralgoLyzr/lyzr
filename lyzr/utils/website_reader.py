import logging
import requests
from tqdm import tqdm
from typing import List
from bs4 import BeautifulSoup
from llama_index.schema import Document

from lyzr.utils.webpage_reader import LyzrWebPageReader

logger = logging.getLogger(__name__)


class LyzrWebsiteReader:
    def __init__(self):
        self.visited_links = set()

    def load_data(self, url: str) -> List[Document]:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, "html.parser")

        all_urls = set()
        for link in soup.find_all("a"):
            href = link.get("href")
            if href is not None:
                all_urls.add(url + href)

        logger.info(f"Total URLs to process: {len(all_urls)}")
        web_reader = LyzrWebPageReader()
        documents = []
        for u in tqdm(all_urls, desc="Processing URLs"):
            documents.extend(web_reader.load_data(u))

        return documents
