from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button:('summarize')
st.write('result.content')
    




