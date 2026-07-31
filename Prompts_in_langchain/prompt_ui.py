from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="poolside/Laguna-S-2.1",
    task="text-generation"
)

st.header("Research Tool")
paper_input  = st.selectbox


if st.button("Summarize"):
    result = llm.invoke(user_input)
    st.write(result)
