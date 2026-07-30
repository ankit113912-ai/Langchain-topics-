st.set_page_config(
    page_title="Research AI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Research AI",
    page_icon="🔎",
    layout="wide"
)

# ------------------ Header ------------------
st.title("🔎 AI Research Assistant")
st.markdown("Ask anything and get AI-powered research answers.")

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.info(
        """
        **Model:** Hugging Face
        
        **Framework:** LangChain
        
        **Made with ❤️ using Streamlit**
        """
    )

# ------------------ Input ------------------
user_input = st.text_area(
    "💬 Enter your Prompt",
    placeholder="Example: Explain Prompt Engineering in simple words...",
    height=180
)

# ------------------ Button ------------------
if st.button("🚀 Generate Response", use_container_width=True):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a prompt first.")
    else:

        with st.spinner("Thinking... 🤖"):

            # ---------------- LLM ----------------
            llm = HuggingFaceEndpoint(
                repo_id="deepseek-ai/DeepSeek-V3-0324",
                task="text-generation",
                temperature=0.5,
                max_new_tokens=200
            )

            model = ChatHuggingFace(llm=llm)

            result = model.invoke(user_input)

        st.success("Response Generated ✅")

        st.subheader("📄 AI Response")
        st.write(result.content)
    




