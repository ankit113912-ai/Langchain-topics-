from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="poolside/Laguna-S-2.1",
    task="text-generation"
)

st.header("Research Tool")
paper_input  = st.selectbox ("selest Research Paper Name ",["selest...","Attention is All you Need" , "BERT: Pro-traning of deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANS on Image Synthesis"])
style_input  = st.selectbox ( " Select Explanation Style",[ "Beinner- Friendly", "Technical", "Code-orinted","Mathematical"])
lenght_input = st.selestbox ( "Select Explanation Lenght ", ["Short (1-2 Paragraphs)", "Medium (3-5 paragraph)","Long (detailed explanation)"])



if st.button("Summarize"):
    result = llm.invoke(user_input)
    st.write(result)
