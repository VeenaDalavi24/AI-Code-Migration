from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY was not found.")
    exit()

print("API key found successfully.")

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-5.6-luna",
        input="Say only: API connection successful."
    )

    print("OpenAI API connection successful!")
    print("AI Response:")
    print(response.output_text)

except Exception as e:
    print("API request failed.")
    print(type(e).__name__)
    print(e)