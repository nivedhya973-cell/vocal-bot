"""
CONCEPT: HANDLING EMPTY INPUT

A user might press Enter without typing a real message.

We do not want to send an empty message to the API.

.strip()
→ removes extra spaces from the beginning and end

if not message:
→ checks whether there is anything left after removing those spaces

continue
→ skips the rest of this loop and asks the user for another message
"""


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTIONS = """
You are a friendly study coach for high school students.

Explain things clearly.
Keep answers short.
Be encouraging.

Do not complete live graded tests or quizzes.
Instead, help the student understand the concept.
"""

previous_response_id = None

while True:
    message = input("You: ").strip()

    if not message:
        print("Please enter a message")
        continue

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    if message.lower() == "reset":
        previous_response_id = None
        print("Bot: Conversation reset.")
        continue

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message,
        previous_response_id=previous_response_id
    )

    print("Bot:", response.output_text)

    previous_response_id = response.id