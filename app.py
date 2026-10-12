import streamlit as st
from converter.converter import convert_code
from verifier.ast_checker import validate_python_code
from verifier.test_generator import generate_test_cases
from verifier.executor import execute_python_code
from verifier.comparator import compare_outputs

# Page configuration
st.set_page_config(
    page_title="AI Code Migration",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI-Based Code Migration")
st.write(
    "Convert legacy source code into modern Python "
    "with intelligent verification."
)

st.divider()

# Source code input
st.subheader("1. Source Code Input")

source_language = st.selectbox(
    "Select Source Language",
    ["COBOL"]
)

input_method = st.radio(
    "Choose Input Method",
    ["Paste Code", "Upload File"],
    horizontal=True
)

legacy_code = ""

# Paste code
if input_method == "Paste Code":

    legacy_code = st.text_area(
        "Paste your COBOL code here",
        height=300,
        placeholder="Enter COBOL code..."
    )

# Upload file
else:

    uploaded_file = st.file_uploader(
        "Upload COBOL file",
        type=["cbl", "cob", "txt"]
    )

    if uploaded_file is not None:
        legacy_code = uploaded_file.read().decode(
            "utf-8",
            errors="ignore"
        )

st.divider()

# Convert button
if st.button("Convert Code", type="primary"):
    
    if not legacy_code.strip():

        st.warning("Please enter or upload COBOL code.")

    else:

        st.subheader("Original COBOL Code")

        st.code(
            legacy_code,
            language="text"
        )

        try:

            # 1. AI CONVERSION
            with st.spinner("AI is converting COBOL to Python..."):

                converted_code = convert_code(
                    legacy_code,
                    source_language
                )

            st.success("Code conversion completed!")

            st.subheader("Converted Python Code")

            st.code(
                converted_code,
                language="python"
            )
            st.download_button(
    label="⬇️ Download Converted Python Code",
    data=converted_code,
    file_name="converted_code.py",
    mime="text/x-python"
)


            # 2. AST VALIDATION
            st.subheader("Python Syntax Verification")

            is_valid, message = validate_python_code(
                converted_code
            )

            if is_valid:

                st.success(
                    f"✅ PASS — {message}"
                )

            else:

                st.error(
                    f"❌ FAIL — {message}"
                )

                st.stop()


            # 3. TEST CASE GENERATION
            st.subheader("🧪 Automated Test Cases")

            with st.spinner("Generating test cases..."):

                test_cases = generate_test_cases(
                    converted_code
                )

            st.success("Test cases generated successfully!")

            for test_case in test_cases["test_cases"]:

                st.write(
                    f"**{test_case['test_id']}**"
                )

                st.write(
                    f"Input: `{test_case['input']}`"
                )

                st.write(
                    f"Expected Output: "
                    f"`{test_case['expected_output']}`"
                )


            # 4. EXECUTION AND COMPARISON
            st.subheader("📊 Verification Results")

            for test_case in test_cases["test_cases"]:

                execution_result = execute_python_code(
                    converted_code,
                    test_case["input"]
                )

                if not execution_result["success"]:

                    st.error(
                        f"❌ {test_case['test_id']} — "
                        "Execution failed"
                    )

                    st.code(
                        execution_result["error"]
                    )

                    continue


                comparison = compare_outputs(
                    test_case["expected_output"],
                    execution_result["output"]
                )


                if comparison["match"]:

                    st.success(
                        f"✅ {test_case['test_id']} — PASS"
                    )

                else:

                    st.error(
                        f"❌ {test_case['test_id']} — FAIL"
                    )

                    st.write(
                        f"Expected: "
                        f"`{comparison['expected']}`"
                    )

                    st.write(
                        f"Actual: "
                        f"`{comparison['actual']}`"
                    )


        except Exception as e:

            st.error(
                f"Pipeline failed: {e}"
            )