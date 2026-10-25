"""
CONCEPT: RESETTING THE CONVERSATION

Our chatbot now remembers earlier messages by storing the ID of the
previous response.

A reset should make the chatbot forget that conversation and start fresh.

Your job:
When the user types "reset":

1. remove the saved conversation state
2. print a short reset message
3. skip the API call for that turn

Hint:
What value did previous_response_id have before the conversation started?
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
    message = input("You: ")

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    if message.lower() == "reset":
        print("Memory has been reset")
        previous_response_id = None
        continue

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message,
        previous_response_id=previous_response_id
    )

    print("Bot:", response.output_text)

    previous_response_id = response.id