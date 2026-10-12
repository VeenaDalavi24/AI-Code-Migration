from converter.converter import convert_code


cobol_code = """
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.

       PROCEDURE DIVISION.
           DISPLAY "HELLO WORLD".
           STOP RUN.
"""


print("Converting COBOL to Python...")
print()

converted_code = convert_code(
    cobol_code,
    "COBOL"
)

print("Converted Python Code:")
print("----------------------")
print(converted_code)