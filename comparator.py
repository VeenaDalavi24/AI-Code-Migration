def normalize_output(output):
    """
    Normalize output before comparison.
    """

    return output.strip()


def compare_outputs(expected_output, actual_output):
    """
    Compare expected and actual program outputs.
    """

    expected = normalize_output(expected_output)
    actual = normalize_output(actual_output)

    if expected == actual:

        return {
            "match": True,
            "message": "Outputs match."
        }

    return {
        "match": False,
        "message": "Outputs do not match.",
        "expected": expected,
        "actual": actual
    }