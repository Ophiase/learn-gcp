import json

from google.oauth2 import service_account
import vertexai
from google.cloud.aiplatform_v1.services.model_service import ModelServiceClient

from shared.secrets import PROJECT_ID, LOCATION, VERTEX_AI_API_KEY


def get_credentials() -> service_account.Credentials:
    info = json.loads(VERTEX_AI_API_KEY)
    return service_account.Credentials.from_service_account_info(info)


def init_vertex() -> None:
    credentials = get_credentials()
    vertexai.init(project=PROJECT_ID, location=LOCATION,
                  credentials=credentials)


def check_auth() -> None:
    try:
        credentials = get_credentials()
        client = ModelServiceClient(credentials=credentials)
        parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
        # Trigger an API call to verify authentication
        client.list_models(request={"parent": parent})
    except Exception as e:
        raise RuntimeError(
            "Authentication failed. Please check your Google Cloud credentials."
        ) from e
