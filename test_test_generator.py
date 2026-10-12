from verifier.test_generator import generate_test_cases


python_code = '''
print("HELLO WORLD")
'''


print("Generating test cases...")
print()

test_cases = generate_test_cases(python_code)

print("Generated Test Cases:")
print("---------------------")

for test_case in test_cases["test_cases"]:
    print(test_case)