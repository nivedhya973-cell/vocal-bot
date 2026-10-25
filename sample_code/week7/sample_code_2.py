"""
CONCEPT: MAKING YOUR FIRST API REQUEST

This program sends one request to an AI model and prints the response.

The API request needs:
1. A model — which AI model should answer.
2. An input — what we want to ask the model.

Your job:
Replace "insert-model-name" with the model we are using in class.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hello in one short sentence."
)

print(response.output_text)