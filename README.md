# Senate Estimates Scraper

Python module that can scrape upcoming hearings for Australian Senate Estimates.

## Setup

Install `poetry`

```sh
pip3 install poetry
```

Update dependencies:

```sh
poetry update
```

## Usage

### Run as script

The module can be run to display a JSON output of the hearings like this:

```sh
poetry run py -m estimates_scraper
```

### Import module

Alternatively, you can import the module for use in scripts like this:

```py
import estimates_scraper

# Examples:
print(estimates_scraper.scrape_committees()[0]['title'])
```