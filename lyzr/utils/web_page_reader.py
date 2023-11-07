import logging
from typing import List

import requests
from bs4 import BeautifulSoup
from llama_index.schema import Document
 
SELECTORS = [
    "article.bd-article",
    'article[role="main"]',
    "div.md-content",
    'div[role="main"]',
    "div.container",
    "div.section",
    "article",
    "main",
]

IGNORED_TAGS = [
    "nav",
    "aside",
    "form",
    "header",
    "noscript",
    "svg",
    "canvas",
    "footer",
    "script",
    "style",
]

logger = logging.getLogger(__name__)

class WebPageReader: 

    def load_data(self, url: str) -> List[Document]:

        response = requests.get(url)
        if response.status_code != 200:
            logger.info(f"Failed to fetch the website: {response.status_code}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")

        for selector in SELECTORS:
            element = soup.select_one(selector)
            if element:
                content = element.prettify()
                break
        else:
            logger.info(f"Failed to find any element for URL: {url}")
            content = soup.get_text()

        soup = BeautifulSoup(content, "html.parser")
        for tag in soup(IGNORED_TAGS):
            tag.decompose()

        content = " ".join(soup.stripped_strings)
        document = Document(text=content, metadata={"url": url})
        return [document]