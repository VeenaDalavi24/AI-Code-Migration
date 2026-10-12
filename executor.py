import subprocess
import sys
import tempfile
import os


def execute_python_code(code, input_data=""):
    """
    Execute Python code and return its output.
    """

    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as file:

            file.write(code)
            temp_file = file.name

        result = subprocess.run(
            [sys.executable, temp_file],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "output": "",
            "error": "Execution timed out."
        }

    except Exception as e:

        return {
            "success": False,
            "output": "",
            "error": str(e)
        }

    finally:

        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)