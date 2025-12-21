from typing import Any

import vertexai
from google.cloud import aiplatform
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel

from shared.authentication import init_vertex

# https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions
MODEL_NAME = "gemini-2.5-flash-lite"
MAX_TOKENS = 100


def load_model(model_name: str):
    return GenerativeModel(model_name)


def generate(model: GenerativeModel, prompt: str, max_tokens: int = MAX_TOKENS) -> Any:
    return model.generate_content(
        prompt, generation_config={"max_output_tokens": max_tokens}
    )


def display(response: Any) -> None:
    print(response.text)


def main() -> None:
    print("Initializing Vertex AI...")
    init_vertex()
    print(f"\nLoading model '{MODEL_NAME}'...")
    model = load_model(MODEL_NAME)
    prompt: str = (
        "Say hello in one sentences (like a hobbit that warn you about the red sky)."
    )
    print(f"\nGenerating response from model '{MODEL_NAME}'...")
    response = generate(model, prompt)
    display(response)


if __name__ == "__main__":
    main()
