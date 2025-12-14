# Big Query Demo

This project demonstrates how to use Google Cloud BigQuery with Python.

Projects
- [Project 00: BigQuery Setup Verification](./project_00)

## Quickstart

1. Create a service account on GCP with the following roles:
    - BigQuery Jobs User
    - BigQuery Data Viewer
    - BigQuery Data Editor
2. Download the service account key as a JSON file
3. (Optional, Dockerized) Mount the key file to the container
4. Write the path to the key file in `secrets/secrets.toml` as follows:

```bash
[paths]
api_key_path = "/path/to/keyfile.json" 
```

5. Run the project ``project_xx`` of your choice:

```bash
# stay in the /big-query folder
uv sync
uv run python -m project_xx.main # replace xx with the project number
```