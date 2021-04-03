#!/usr/bin/env python3

from typing import *  # pylint: disable=wildcard-import,unused-wildcard-import

import argparse
import sys

from .utils import scrape_links


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract links from a list of URLs.",
    )
    parser.add_argument(
        "urls",
        nargs="+",
        type=str,
        help="A list of strings containing links to score, one per line."
        " If - is given as filename it reads from stdin instead.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="If provided it provides additional logging in case of errors.",
    )
    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    urls_stream = args.urls
    if args.urls[0] == "-":
        urls_stream = sys.stdin

    for url in urls_stream:
        # TODO add strip per gli accapo
        for name, href in scrape_links(url):
            print(name, href)
        print()


def run() -> None:
    try:
        args = parse_args()
        main(args)
    except KeyboardInterrupt:
        print("\nAborted!")
    except Exception as err:  # pylint: disable=broad-except
        if args.debug:
            raise
        print("Error: %s" % err)


if __name__ == "__main__":
    run()
