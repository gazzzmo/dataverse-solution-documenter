# Dataverse Solution Documenter

A web application that ingests a Microsoft Dataverse solution `.zip` export and generates comprehensive, structured Markdown documentation from the solution contents.

## Features

- 📦 **Upload a Dataverse solution `.zip`** via browser
- 📄 **Parses solution internals** including:
  - `solution.xml` — solution metadata, version, publisher info
  - `customizations.xml` — entities, attributes, forms, views, relationships
  - Workflows (`.xaml` / `Workflows/` folder)
  - Web Resources (JS, HTML, CSS, images)
  - Environment Variable Definitions & Values
  - Plugin assemblies & step registrations
  - Security roles
  - Connection references
  - Canvas Apps
- 📝 **Outputs structured Markdown documentation** per component type
- 🗂️ **Produces a documentation index** (`README.md`) linking all sections

## Tech Stack

- **Backend:** Python 3.11+ / FastAPI
- **Frontend:** Plain HTML + vanilla JS (no framework)
- **Parsing:** Python `xml.etree.ElementTree` + `zipfile`
- **Output:** Markdown files

## Getting Started

### Prerequisites

- Python 3.11+
- `uv` (recommended) or `pip`

### Install & Run

```bash
# Clone the repo
git clone https://github.com/gazzzmo/dataverse-solution-documenter.git
cd dataverse-solution-documenter

# Create venv and install dependencies
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
```

Then open http://localhost:8000 in your browser.

### Docker

```bash
docker build -t dv-solution-docs .
docker run -p 8000:8000 dv-solution-docs
```

## Project Structure

```
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── routers/
│   │   └── upload.py        # Upload & processing endpoint
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── solution.py      # Parses solution.xml
│   │   ├── customizations.py # Parses customizations.xml
│   │   ├── workflows.py     # Parses workflow XAML files
│   │   ├── webresources.py  # Parses web resources
│   │   ├── env_vars.py      # Parses environment variable definitions
│   │   └── plugins.py       # Parses plugin assemblies
│   ├── generators/
│   │   ├── __init__.py
│   │   └── markdown.py      # Renders parsed data to Markdown
│   └── static/
│       └── index.html       # Upload UI
├── tests/
│   └── test_parsers.py
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```

## Roadmap

- [ ] Core solution.xml parser
- [ ] Customizations.xml parser (entities, fields, forms, views)
- [ ] Workflow parser
- [ ] Web resource indexer
- [ ] Environment variable parser
- [ ] Plugin assembly parser
- [ ] Markdown generator
- [ ] Web UI (upload + download docs)
- [ ] ZIP download of full documentation set
- [ ] Docker support

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

MIT — see [LICENSE](LICENSE).
