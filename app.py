import streamlit as st
import subprocess
import os

# Configure the Streamlit page
st.set_page_config(page_title="Document Format Converter", layout="centered")
st.subheader("📄 DOCUMENT FORMAT CONVERTER")

# Supported input and output formats
input_formats = [
    "azw", "azw3", "cbz", "cbr", "cbc", "chm", "docx", "epub", "fb2", "html", "htmlz",
    "lit", "lrf", "mobi", "odt", "pdf", "prc", "pdb", "pml", "rb", "rtf", "snb", "tcr",
    "txt", "txtz"
]

output_formats = [
    "azw3", "cbc", "docx", "epub", "fb2", "htmlz", "lit", "lrf", "mobi", "odt", "pdf",
    "pdb", "pml", "rb", "rtf", "snb", "tcr", "txt", "txtz", "zip"
]

# File uploader and output format selector
uploaded_file = st.file_uploader("📤 Upload your file", type=input_formats)
selected_output = st.selectbox("🎯 Select output format", output_formats)

if uploaded_file and selected_output:
    st.success(f"Ready to convert `{uploaded_file.name}` ➝ `{selected_output}`")

    # Create a temporary directory for processing files
    temp_folder = "temp"
    os.makedirs(temp_folder, exist_ok=True)
    
    # Extract the base filename (without extension)
    base_filename = uploaded_file.name.rsplit('.', 1)[0]
    input_extension = uploaded_file.name.rsplit('.', 1)[-1]

    # Prepare the file names for input and output
    input_filename = os.path.join(temp_folder, f"{base_filename}.{input_extension}")
    output_filename = os.path.join(temp_folder, f"{base_filename}.{selected_output}")

    # Save the uploaded file to disk
    with open(input_filename, "wb") as f:
        f.write(uploaded_file.read())


    if st.button("Convert File"):
        with st.spinner("Converting file, please wait..."):
            try:
                # Run the external 'ebook-convert' command
                result = subprocess.run(
                    ["ebook-convert", input_filename, output_filename],
                    check=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                st.success("✅ Conversion successful!")
                with open(output_filename, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Download {base_filename}.{selected_output}",
                        data=f,
                        file_name=f"{base_filename}.{selected_output}",
                        mime="application/octet-stream"
                    )
            except subprocess.CalledProcessError as e:
                st.error("❌ Conversion failed:")
                st.code(e.stderr)
else:
    st.info("📎 Please upload a file and select a format to convert.")
