"""
CONCEPT: USER INPUT → API INPUT

The user types a message into the terminal.
We save that message in a Python variable called `message`.

The API needs to know what text it should send to the model.
Your job is to connect the user's message to the API request.

Fill in the blank for `input=` using the variable that stores
what the user typed.
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

message = input("You: ")

response = client.responses.create(
    model="gpt-6-luna",
    input= message
)

print("Bot:", response.output_text)