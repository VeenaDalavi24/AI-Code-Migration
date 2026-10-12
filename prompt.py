def create_conversion_prompt(source_code, source_language):
    return f"""
You are an expert software migration engineer.

Convert the following {source_language} program into Python.

Requirements:
1. Preserve the original program logic.
2. Preserve variables and their meaning.
3. Preserve conditions and control flow.
4. Preserve loops.
5. Preserve calculations.
6. Preserve input and output behavior.
7. Do not add functionality that does not exist.
8. Produce readable Python code.
9. Return ONLY Python source code.
10. Do not use Markdown code fences.

Source {source_language} code:

{source_code}
"""