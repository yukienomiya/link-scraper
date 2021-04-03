# pylint: disable=missing-module-docstring,missing-function-docstring,unused-variable,too-many-locals,too-many-statements
import io
from unittest.mock import PropertyMock

import pytest  # pylint: disable=unused-import
import requests

from link_scraper.utils import scrape_links


def describe_link_scraper():
    def should_return_empty_list_if_url_is_invalid():
        res = scrape_links("abc")
        assert len(res) == 0
        res = scrape_links("")
        assert len(res) == 0

    def should_return_empty_list_if_url_doesnt_exist(mocker):
        patched_get = mocker.patch("requests.get")
        patched_get.side_effect = requests.exceptions.RequestException()
        res = scrape_links("https://example.com")
        assert len(res) == 0

    def should_return_five_links(mocker):
        fhandle = io.open(
            "tests/unit/fixtures/example.com.html", mode="r", encoding="utf-8"
        )
        patched_get = mocker.patch("requests.get")
        type(patched_get.return_value).text = PropertyMock(return_value=fhandle.read())
        res = scrape_links("https://example.com")
        assert len(res) == 6
        assert res[0] == ("", "https://example.com/mypage1")
        assert res[1] == ("My page 2", "https://example.com/mypage2")
        assert res[2] == ("My page 3", "https://example.com/mypage3")
        assert res[3] == ("My page 4", "http://example.com/mypage4")
        assert res[4] == ("Another webpage", "http://another-example.com/home")
        assert res[5] == ("Mail to", "mailto:info@example.com")
