# Vertex AI

This project demonstrates how to use Google Cloud Vertex AI with Python.

## Quickstart

1. Create a service account GCP with the following roles
    - `Vertex AI User`
2. Download the SA key as a JSON file
3. (Optional, Dockerized) Mount the key file to the container
4. Write the path to the key file in `secrets/secrets.toml` as follows:

```bash
[paths]
api_key_path = "/path/to/keyfile.json" 

[project]
project_id = "your-gcp-project-id"
location = "your-gcp-location" # e.g. us-central1, europe-west9 (paris)
```

5. Run the project ``project_xx`` of your choice:

```bash
# stay in the /vertex-ai folder
uv sync
uv run python -m project_xx.main # replace xx with the project number
```
