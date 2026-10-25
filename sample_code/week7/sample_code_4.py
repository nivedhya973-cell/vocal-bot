"""
CONCEPT: MAKING THE CHATBOT REPEAT

Right now, the program can only handle one message at a time.
After it prints the bot's response, the program ends.

A chatbot should keep asking the user for new messages until
the user chooses to stop.

Your job:
Add a loop so the program repeatedly:
1. asks the user for a message
2. sends that message to the model
3. prints the model's response
"""


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


# wrap this code in something to make it LOOP
while (True) :
    message = input("You: ")

    response = client.responses.create(
        model="gpt-6-luna",
        input=message
    )

    print("Bot:", response.output_text)