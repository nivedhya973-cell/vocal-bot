"""
CONCEPT: STOPPING A LOOP

Our chatbot now repeats so the user can keep sending messages.

But we also need a way for the user to end the program.

Your job:
When the user types "quit":

1. print a short goodbye message
2. stop the loop so the program ends

Hint:
Think about the Python keyword used to exit a loop.
"""


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Goodbye! See you later.")
        break

    response = client.responses.create(
        model="gpt-6-luna",
        input=message
    )

    print("Bot:", response.output_text)