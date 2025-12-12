# Project 00

Simple verification of BigQuery setup and authentication.
- Verify that the user can authenticate and access BigQuery.
- Create a sample dataset and table.
- Load sample data into the table.
- Run a simple query to retrieve data from the table.

```bash
# To sync the project environment
uv sync 

# Authenticate with Google Cloud
gcloud auth application-default login

# Run the main script
uv run python -m main

# We recommend you to clean up resources after running the project
rm ~/.config/gcloud/application_default_credentials.json
```