from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

st.title("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 Paragraphs)",
        "Medium (3-5 Paragraphs)",
        "Long (Detailed Explanation)"
    ]
)

user_input = st.text_area("Enter your question")

if st.button("Summarize"):

    prompt = f"""
    Research Paper: {paper_input}

    Explanation Style: {style_input}

    Explanation Length: {length_input}

    User Question:
    {user_input}
    """

    response = client.chat_completion(
        model="deepseek-ai/DeepSeek-V4-Pro:featherless-ai",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=700
    )

    st.write(response.choices[0].message.content)