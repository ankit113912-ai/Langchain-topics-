# ==========================================
# IMPORTS
# ==========================================

import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint
)

# ==========================================
# LOAD ENV VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Research AI",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Hide Streamlit default menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Main background */

.stApp{

background:#0E1117;

}

/* Main Title */

.title{

font-size:48px;

font-weight:700;

color:white;

text-align:center;

margin-top:10px;

}

/* Subtitle */

.subtitle{

text-align:center;

color:#B0B3B8;

font-size:18px;

margin-bottom:30px;

}

/* Card */

.card{

background:#161B22;

padding:22px;

border-radius:15px;

border:1px solid #2D333B;

margin-top:15px;

}

</style>

""",unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown(
"""
<div class="title">

🔎 AI Research Assistant

</div>

<div class="subtitle">

Powered by LangChain + HuggingFace + Streamlit

</div>

""",
unsafe_allow_html=True
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.divider()

    temperature = st.slider(

        "Temperature",

        min_value=0.0,

        max_value=1.0,

        value=0.5,

        step=0.1

    )

    max_tokens = st.slider(

        "Max New Tokens",

        min_value=50,

        max_value=1000,

        value=300,

        step=50

    )

    st.divider()

    st.success("🟢 Model Ready")

    st.info("""

Framework : LangChain

Model Provider : HuggingFace

UI : Streamlit

""")

# ==========================================
# MAIN CARD
# ==========================================

st.markdown(
'<div class="card">',
unsafe_allow_html=True
)

st.subheader("💬 Ask Anything")

user_input = st.text_area(

    "",

    height=180,

    placeholder="Ask any research question..."

)

col1,col2=st.columns(2)

generate=col1.button(

    "🚀 Generate",

    use_container_width=True

)

clear=col2.button(

    "🗑️ New Chat",

    use_container_width=True

)

st.markdown("</div>",unsafe_allow_html=True)


# ==========================================
# CREATE LLM
# ==========================================

@st.cache_resource
def load_model(temp, tokens):

    llm = HuggingFaceEndpoint(

        repo_id="deepseek-ai/DeepSeek-V3-0324",

        task="text-generation",

        temperature=temp,

        max_new_tokens=tokens

    )

    model = ChatHuggingFace(llm=llm)

    return model


# ==========================================
# GENERATE RESPONSE
# ==========================================

if generate:

    if user_input.strip() == "":

        st.warning("⚠️ Please enter a prompt.")

        st.stop()

    try:

        model = load_model(

            temperature,

            max_tokens

        )

        with st.spinner("🤖 AI is Thinking..."):

            result = model.invoke(user_input)

        response = result.content

        st.session_state.last_response = response

        st.session_state.messages.append({

            "role":"user",

            "content":user_input

        })

        st.session_state.messages.append({

            "role":"assistant",

            "content":response

        })

    except Exception as e:

        st.error("❌ Error while generating response.")

        st.exception(e)


# ==========================================
# CLEAR CHAT
# ==========================================

if clear:

    st.session_state.messages=[]

    st.session_state.last_response=""

    st.rerun()


    # ==========================================
# CHAT WINDOW
# ==========================================

st.divider()

st.subheader("💬 Conversation")

chat_container = st.container(border=True)

with chat_container:

    if len(st.session_state.messages) == 0:

        st.info(
            """
👋 Welcome!

Ask anything related to AI, Programming,
Machine Learning, Research or any topic.

Your conversation will appear here.
            """
        )

    else:

        for message in st.session_state.messages:

            if message["role"] == "user":

                with st.chat_message("user", avatar="👨‍💻"):

                    st.markdown(message["content"])

            else:

                with st.chat_message("assistant", avatar="🤖"):

                    st.markdown(message["content"])

# ==========================================
# RESPONSE INFORMATION
# ==========================================

if st.session_state.last_response != "":

    st.divider()

    with st.expander("📊 Response Information", expanded=False):

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Characters",

                len(st.session_state.last_response)

            )

        with col2:

            st.metric(

                "Words",

                len(
                    st.session_state.last_response.split()
                )

            )

# ==========================================
# DOWNLOAD RESPONSE
# ==========================================

if st.session_state.last_response != "":

    st.download_button(

        label="📥 Download Response",

        data=st.session_state.last_response,

        file_name="AI_Response.txt",

        mime="text/plain",

        use_container_width=True

    )

# ==========================================
# SIDEBAR HISTORY
# ==========================================

with st.sidebar:

    st.divider()

    st.subheader("📜 Chat Statistics")

    total_messages = len(st.session_state.messages)

    total_questions = total_messages // 2

    st.metric(

        "Questions",

        total_questions

    )

    st.metric(

        "Messages",

        total_messages

    )

    st.divider()

    st.caption("🚀 Version 1.0")


    # ==========================================
# PREMIUM HEADER
# ==========================================

st.markdown("""
<style>

/* ---------- Gradient Header ---------- */

.gradient-title{

    font-size:55px;
    font-weight:800;

    background:linear-gradient(
        90deg,
        #4F46E5,
        #06B6D4,
        #22C55E
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

}

/* ---------- Buttons ---------- */

div.stButton > button{

    border-radius:12px;

    height:52px;

    font-size:18px;

    font-weight:600;

    transition:0.3s;

}

div.stButton > button:hover{

    transform:scale(1.03);

}

/* ---------- Chat Container ---------- */

[data-testid="stChatMessage"]{

    border-radius:15px;

    padding:10px;

    margin-bottom:15px;

}

/* ---------- Text Area ---------- */

textarea{

    border-radius:12px !important;

}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"]{

    border-right:1px solid #2D333B;

}

/* ---------- Scroll Bar ---------- */

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-thumb{

background:#555;

border-radius:20px;

}

</style>
""",unsafe_allow_html=True)

# ==========================================
# HEADER CARD
# ==========================================

st.markdown("""

<div style="text-align:center">

<div class="gradient-title">

🚀 AI Research Assistant

</div>

<p style="font-size:18px;color:gray;">

Professional AI Assistant powered by
LangChain + Hugging Face

</p>

</div>

""",unsafe_allow_html=True)

# ==========================================
# RESPONSE STATUS
# ==========================================

if st.session_state.last_response!="":

    st.success("✅ Response Generated Successfully")

# ==========================================
# COPY RESPONSE
# ==========================================

if st.session_state.last_response!="":

    st.code(
        st.session_state.last_response,
        language=None
    )

# ==========================================
# SIDEBAR FOOTER
# ==========================================

with st.sidebar:

    st.divider()

    st.markdown("### 🚀 Quick Actions")

    if st.button("🧹 Reset Everything"):

        st.session_state.messages=[]

        st.session_state.last_response=""

        st.rerun()

    st.divider()

    st.markdown(
        """
### 💡 Tips

- Ask detailed questions.
- Keep prompts specific.
- Adjust Temperature.
- Increase Tokens for long answers.
"""
    )

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Made with ❤️ using Streamlit • LangChain • Hugging Face"
)



