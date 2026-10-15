
# nlp-01-getting-started

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/denisecase/nlp-01-getting-started/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/denisecase/nlp-01-getting-started/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/nlp-01-getting-started/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Retrieve, process, and visualize text from the web using Python.

## Project Overview

Author: Denise Case

Date: 2026 October

First project in the Web Mining and Applied NLP course.

Web Mining and Applied Natural Language Processing (NLP)
focus on retrieving, processing, and analyzing text
from the web and other digital sources.

The goal is to establish a working Python environment,
explore a professional project structure,
run a Python text analysis script,
and verify that the project works.

The project is configured in
[pyproject.toml](pyproject.toml).

## Data

The example retrieves HTML from a public web page
using the Requests library.

BeautifulSoup parses the HTML and extracts text
for analysis.

No local input dataset is required.

The example uses the Wikipedia article on
[Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing).

## Approach

The project uses Python to retrieve and analyze web text.

The example demonstrates:

- Retrieving HTML using HTTP requests.
- Parsing HTML and extracting text with BeautifulSoup.
- Cleaning and normalizing text.
- Counting word frequencies using Polars.
- Visualizing frequent words using Matplotlib.
- Creating word clouds to explore vocabulary patterns.

Explore these important project components:

- [pyproject.toml](pyproject.toml) - project identity, dependencies, and tool configuration.
- [src/nlp/web_words.py](src/nlp/web_words.py) - executable Python analysis.
- [notebooks/web_words.ipynb](notebooks/web_words.ipynb) - interactive Jupyter notebook example.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated testing and documentation deployment.
- [docs/](docs/) - project documentation.
- [zensical.toml](zensical.toml) - documentation configuration.

The goal is to get the project running,
inspect the results, and understand the basic workflow
for acquiring and analyzing text.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m nlp.web_words
```

Close each visualization window after viewing
so the script can continue executing.

The Jupyter notebook provides an additional
interactive version of the analysis.

## Results

The example retrieves web text,
computes word frequencies,
and displays a frequency bar chart and word cloud.

Successful execution produces:

```shell
========================
Pipeline executed successfully!
========================
```

A `project.log` file is created in the project root.

This confirms that the Python analysis executes
and the logging system works.

### Example Visualization

![Word Cloud Example](docs/images/word_cloud_example.png)

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

## Project Documentation

The [hosted documentation site](https://denisecase.github.io/nlp-01-getting-started/)
is published using Zensical and GitHub Pages.

The documentation site is used to present the project report,
covering such sections as data, methods, results, visualizations,
interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD)
to check project files and publish the docs.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/denisecase/nlp-01-getting-started/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/denisecase/nlp-01-getting-started/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uv run prek install --force
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://denisecase.github.io/nlp-01-getting-started/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
