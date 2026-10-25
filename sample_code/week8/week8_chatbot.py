import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

INSTRUCTIONS = """You are a supportive Choir Director & Vocal Coach.
- Provide practical vocal tips (e.g., breath support, resonance, articulation, diction).
- Customize warm-up routines based on vocal range (Soprano, Alto, Tenor, Bass).
- Teach music theory, sight-reading techniques, and vocal health habits.
- Maintain an encouraging, energizing tone suitable for high-school choir students.
- Do not provide medical advice for vocal cord injuries or severe pain—direct them to an ENT specialist."""

previous_response_id = None

print("=== VOCAL COACH ===")
print("Ask for warm-ups, diction tips, or music theory help!")
print("Commands: 'reset' to restart session | 'quit' to exit\n")

while True:
    user_input = input("Singer: ").strip()

    if user_input.lower() == "quit":
        print("Thanks for singing! Keep practicing!")
        break

    if user_input.lower() == "reset":
        previous_response_id = None
        print("\n[Session reset. Ready for a new topic!]\n")
        continue

    if not user_input:
        print("Please type a question or topic (e.g., 'Give me a 5-minute warm-up for Altos').")
        continue

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            instructions=INSTRUCTIONS,
            input=user_input,
            previous_response_id=previous_response_id,
        )
        print(f"\nCoach: {response.output_text}\n")
        previous_response_id = response.id

    except Exception:
        print("\nConnection error. Please check your network or API key setup.\n")