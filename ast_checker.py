import ast


def validate_python_code(code):
    """
    Validate whether the generated Python code
    has valid Python syntax.
    """

    try:
        ast.parse(code)

        return True, "Python syntax is valid."

    except SyntaxError as e:

        return False, f"Syntax error at line {e.lineno}: {e.msg}"