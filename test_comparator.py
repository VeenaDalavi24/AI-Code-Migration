from verifier.comparator import compare_outputs


expected_output = "HELLO WORLD\n"
actual_output = "HELLO WORLD\n"


result = compare_outputs(
    expected_output,
    actual_output
)


print("Output Comparison:")
print("------------------")
print("Match:", result["match"])
print("Message:", result["message"])