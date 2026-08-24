# Sample Output

Generated documentation from the sample solutions in `../sample-solutions/`.

Each subfolder contains the full Markdown documentation set produced by running
the Dataverse Solution Documenter against the corresponding solution zip.

| Folder | Solution | Generated Docs |
|---|---|---|
| [`VendorIntegration/`](VendorIntegration/) | Vendor Admin Self-Service v1.1.0.0 | 12 Markdown files |

To regenerate, run the app locally and upload the corresponding zip from `sample-solutions/`,
or run the pipeline script directly:

```bash
cd /path/to/dataverse-solution-documenter
source .venv/bin/activate
python3 scripts/generate_sample_output.py
```
