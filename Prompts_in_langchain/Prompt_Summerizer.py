from dotenv import load_dotenv
import streamlit as st

from langchain_huggingface import ChatHuggingFace
from huggingface_hub import InferenceClient

load_dotenv()

# Hugging Face Client
client = InferenceClient()

# LangChain Chat Wrapper
llm = ChatHuggingFace(llm=client)

st.title("📄 Research Tool")

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short",
        "Medium",
        "Long"
    ],
)

user_input = st.text_area("Ask your question")

if st.button("Summarize"):

    prompt = f"""
Research Paper: {paper_input}

Explanation Style: {style_input}

Explanation Length: {length_input}

Question:
{user_input}
"""

    response = llm.invoke(prompt)

    st.write(response.content)