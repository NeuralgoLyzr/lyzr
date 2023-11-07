import logging
from typing import List
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from llama_index.schema import Document
from tqdm import tqdm

from lyzr.utils.web_page_reader import WebPageReader

logger = logging.getLogger(__name__)

class WebDocsReader:
    def __init__(self):
        self.visited_links = set()

    def _get_child_links_recursive(self, url):
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        current_path = parsed_url.path

        response = requests.get(url)
        if response.status_code != 200:
            logger.warning(f"Failed to fetch the website: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        all_links = [link.get("href") for link in soup.find_all("a")]

        child_links = set()
        for link in all_links:
            if not link or link.startswith("#") or link == current_path:
                continue
            full_link = urljoin(base_url, link)
            if urlparse(full_link).netloc == parsed_url.netloc:
                child_links.add(full_link)

        for link in child_links:
            if link not in self.visited_links:
                self.visited_links.add(link)
                self._get_child_links_recursive(link)

    def _get_all_urls(self, url):
        self.visited_links = set()
        self._get_child_links_recursive(url)
        urls = [
            link
            for link in self.visited_links
            if urlparse(link).netloc == urlparse(url).netloc
        ]
        return urls

    def load_data(self, url: str) -> List[Document]:
        all_urls = self._get_all_urls(url)
        logger.info(f"Total URLs to process: {len(all_urls)}")

        web_reader = WebPageReader()
        documents = []
        for u in tqdm(all_urls, desc="Processing URLs"):
            documents.extend(web_reader.load_data(u))

        return documents
