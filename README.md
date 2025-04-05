# 📚 PubMed Fetcher

Pubmed-fetcher is a command-line utility and Python library designed to retrieve research articles from PubMed using a search query. It specifically filters the results to include only those associated with non-academic pharmaceutical or biotech firms, and presents the findings in a structured CSV format.



## 📁 Project Structure

```
pubmed_fetcher/
│
├── pubmed_fetcher/
│   ├── __init__.py
│   ├── command_line.py         # Core logic for fetching and parsing PubMed articles
│   └── main.py          # Command-line interface
│
├── pyproject.toml      # Poetry dependency and packaging config
├── README.md           # You're reading this!
├── LICENSE             # Project license
```

---

## 🛠️ Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/pubmed-fetcher.git
cd pubmed-fetcher
```

### 2. Install dependencies using [Poetry](https://python-poetry.org/):
```bash
poetry install
```


## 🚀 Usage

### Basic CLI usage:

```bash
poetry run get-papers-list "cancer immunotherapy"
```

### Save results to a CSV:

```bash
poetry run get-papers-list "mRNA vaccine" -f results.csv
```

### Enable debug output:

```bash
poetry run get-papers-list "covid vaccine" --debug
```

### Display help:

```bash
poetry run get-papers-list --help
```


## 🧰 Tools & Libraries Used

| Tool / Library | Purpose | Link |
|----------------|---------|------|
| [Biopython](https://biopython.org/) | Used to access NCBI's PubMed API | https://biopython.org |
| [Pandas](https://pandas.pydata.org/) | Used for formatting and saving data as CSV | https://pandas.pydata.org |
| [Poetry](https://python-poetry.org/) | Python dependency management and packaging | https://python-poetry.org |
