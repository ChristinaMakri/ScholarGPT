import streamlit as st
import os

st.title("ScholarSynth - Scientific AI Assistant")

st.write("""
Upload your PDF research papers and ask questions about their content.
""")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    os.makedirs("./data", exist_ok=True)
    for file in uploaded_files:
        with open(f"./data/{file.name}", "wb") as f:
            f.write(file.getbuffer())

    st.success("Files uploaded successfully! Now, run main.py to start the conversation.")
else:
    st.info("Please upload one or more PDF files to begin.")
