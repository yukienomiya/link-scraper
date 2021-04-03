<h1 align="center">
  <b>link-scraper</b>
</h1>
<p align="center">
  <!-- Lint -->
  <a href="https://github.com/yukienomiya/link-scraper/actions?query=workflow:lint+branch:master">
    <img src="https://github.com/yukienomiya/link-scraper/workflows/lint/badge.svg?branch=master" alt="Lint status" />
  </a>
  <!-- Test - Ubuntu -->
  <a href="https://github.com/yukienomiya/link-scraper/actions?query=workflow:test-ubuntu+branch:master">
    <img src="https://github.com/yukienomiya/link-scraper/workflows/test-ubuntu/badge.svg?branch=master" alt="Test Ubuntu status" />
  </a>
  <br />
  <!-- Code style -->
  <a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style" />
  </a>
  <!-- Linter -->
  <a href="https://github.com/PyCQA/pylint">
    <img src="https://img.shields.io/badge/linter-pylint-ce963f.svg" alt="Linter" />
  </a>
  <!-- Types checker -->
  <a href="https://github.com/PyCQA/pylint">
    <img src="https://img.shields.io/badge/types%20checker-mypy-296db2.svg" alt="Types checker" />
  </a>
  <!-- Test runner -->
  <a href="https://github.com/pytest-dev/pytest">
    <img src="https://img.shields.io/badge/test%20runner-pytest-449bd6.svg" alt="Test runner" />
  </a>
  <!-- Task runner -->
  <a href="https://github.com/illBeRoy/taskipy">
    <img src="https://img.shields.io/badge/task%20runner-taskipy-abe63e.svg" alt="Task runner" />
  </a>
  <!-- Build tool -->
  <a href="https://github.com/python-poetry/poetry">
    <img src="https://img.shields.io/badge/build%20system-poetry-4e5dc8.svg" alt="Build tool" />
  </a>
  <br />
  <!-- License -->
  <a href="https://github.com/yukienomiya/link-scraper/tree/master/license">
    <img src="https://img.shields.io/github/license/yukienomiya/link-scraper.svg" alt="Project license" />
  </a>
</p>
<p align="center">
  The most basic link scraper in the whole world.
</p>

## Synopsis


This is a simple link scraper that returns all the anchor links in a webpage.

A simple [CLI](#cli) is also available for quick prototyping.  
You can run it locally or on directly on Colab using [this notebook][colab:link-scraper].

## Install

```bash
pip install git+https://github.com/yukienomiya/link-scraper.git
```
or 
```bash
poetry add git+https://github.com/yukienomiya/link-scraper.git
```

## Usage

```python
from link_scraper.utils import scrape_links

scrape_links('https://google.it')
# => [
#     ('Immagini', 'https://www.google.it/imghp?hl=it&tab=wi'),
#     ('Maps', 'https://maps.google.it/maps?hl=it&tab=wl'),
#     ...
#    ]
```

## CLI

The pip package includes a CLI that you can use to extract links.

```
usage: link-scraper [-h] [--debug] urls [urls ...]

Extract links from a list of URLs.

positional arguments:
  urls        A list of strings containing links to score, one per line. If - is given as filename it reads from stdin
              instead.

optional arguments:
  -h, --help  show this help message and exit
  --debug     If provided it provides additional logging in case of errors.
```


## Development

You can install this library locally for development using the commands below.
If you don't have it already, you need to install [poetry](https://python-poetry.org/docs/#installation) first.

```bash
# Clone the repo
git clone https://github.com/yukienomiya/link-scraper
# CD into the created folder
cd link-scraper
# Create a virtualenv and install the required dependencies using poetry
poetry install
```

You can then run commands inside the virtualenv by using `poetry run COMMAND`.  
Alternatively, you can open a shell inside the virtualenv using `poetry shell`.


If you wish to contribute to this project, run the following commands locally before opening a PR and check that no error is reported (warnings are fine).

```bash
# Run the code formatter
poetry run task format
# Run the linter
poetry run task lint
# Run the static type checker
poetry run task types
# Run the tests
poetry run task test
```


## License

This project is licensed under the MIT License - see the [license][license] file for details.



<!-- Links -->

[start]: https://github.com/yukienomiya/link-scraper#start-of-content
[license]: https://github.com/yukienomiya/link-scraper/tree/master/license
[contributors]: https://github.com/yukienomiya/link-scraper/contributors

[colab:link-scraper]: https://colab.research.google.com/github/yukienomiya/link-scraper/blob/master/examples/link_scraper.ipynb