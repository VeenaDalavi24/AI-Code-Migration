import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured.")


client = OpenAI(api_key=api_key)


def generate_test_cases(python_code):
    """
    Generate test cases for the converted Python program.
    """

    prompt = f"""
You are a software testing expert.

Analyze the following Python program and generate suitable
test cases for verifying its behavior.

Requirements:
1. Understand what the program does.
2. Generate up to 5 representative test cases.
3. Include normal cases.
4. Include boundary cases when applicable.
5. Each test case must contain:
   - test_id
   - input
   - expected_output
6. If the program does not require input, use an empty string for input.
7. Expected output must represent what the Python program should print.
8. Return ONLY valid JSON.
9. Do not use Markdown code fences.

Python program:

{python_code}

Return JSON in exactly this format:

{{
    "test_cases": [
        {{
            "test_id": "TC01",
            "input": "",
            "expected_output": "..."
        }}
    ]
}}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result = response.output_text.strip()

    # Remove accidental Markdown code fences
    if result.startswith("```"):
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

    return json.loads(result)