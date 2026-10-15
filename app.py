import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="PDF Chatbot LLM")
st.title("PDF Chatbot - LLM + RAG")
st.caption("AI Generalist Project | Bonface | B.Tech | Ex-G42 UAE")

pdf = st.file_uploader("Upload your PDF", type="pdf")
question = st.text_input("Ask a question")

if pdf and question:
    reader = PdfReader(pdf)
    text = "".join([p.extract_text() for p in reader.pages])
    st.success(f"PDF loaded with {len(text)} characters")
    st.write("Next: Connect OpenAI embeddings + FAISS for real RAG")
