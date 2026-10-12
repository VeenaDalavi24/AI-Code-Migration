import os

from dotenv import load_dotenv
from openai import OpenAI

from converter.prompt import create_conversion_prompt


# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured.")


# Create OpenAI client
client = OpenAI(api_key=api_key)


def convert_code(source_code, source_language):
    """
    Convert legacy source code into Python using an AI model.
    """

    prompt = create_conversion_prompt(
        source_code,
        source_language
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text.strip()
