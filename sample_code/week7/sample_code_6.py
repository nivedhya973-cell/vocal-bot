"""
CONCEPT: GIVING THE CHATBOT INSTRUCTIONS

So far, the chatbot can answer questions, but it does not have a specific role.

We can give the model instructions that describe:
1. who the chatbot should act like
2. how it should respond
3. what rules or boundaries it should follow

Your job:
Change the INSTRUCTIONS so your chatbot has its own persona.

Your instructions should include:
- a purpose
- an audience
- a tone
- at least one boundary

Then test your chatbot and see how its responses change.
"""


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTIONS = """
You are a friendly science tutor.

Explain things clearly.
Keep answers short.
Be encouraging.

Give short answers with analogies.
At the end of every answer, give the user a short quiz about the question.
"""

while True:
    message = input("You: ")

    if message.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-6-luna",
        instructions=INSTRUCTIONS,
        input=message
    )

    print("Bot:", response.output_text)