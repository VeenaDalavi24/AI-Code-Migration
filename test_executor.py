from verifier.executor import execute_python_code


python_code = '''
print("HELLO WORLD")
'''


print("Executing Python code...")
print()

result = execute_python_code(
    python_code
)

print("Execution Result:")
print("-----------------")
print("Success:", result["success"])
print("Output:", repr(result["output"]))
print("Error:", result["error"])