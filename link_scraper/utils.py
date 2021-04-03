"""Utilities functions of the link scraper."""

from typing import *  # pylint: disable=wildcard-import,unused-wildcard-import
from urllib.parse import urlparse, urljoin

import requests
import AdvancedHTMLParser


def scrape_links(url: str) -> List[Tuple[str, str]]:
    """Extracts links from a webpage.

    Args:
      url: the String representing the url.

    Returns:
      a List of Tuples containing names and urls of each link.

    """
    try:
        page = requests.get(url)
    except requests.exceptions.RequestException:
        return []
    url_parts = urlparse(url)
    base_url = "%s://%s" % (url_parts.scheme, url_parts.netloc)
    parser = AdvancedHTMLParser.AdvancedHTMLParser()
    parser.parseStr(page.text)
    link_elements = parser.getElementsByTagName("a")
    non_empty_links = filter(lambda x: len(x.getAttribute("href")) > 0, link_elements)
    link_map = map(
        lambda x: (x.innerText, urljoin(base_url, x.getAttribute("href"))),
        non_empty_links,
    )
    return list(link_map)
