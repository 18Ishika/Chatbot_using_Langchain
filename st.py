import streamlit as st
from dotenv import load_dotenv
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Load environment variables
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="AI Chatbot using TinyLlama", page_icon="🤖", layout="wide")

st.title("AI Chatbot using Chat Model Opensource (HF)")

# Sidebar Settings
st.sidebar.header("⚙️ Chatbot Settings")
temp = st.sidebar.slider("Temperature", 0.1, 1.0, 0.7, 0.05)
max_token = st.sidebar.slider("No_of_Tokens", 16, 512, 256, 16)

# Hugging Face API Token
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_token:
    st.error("⚠️ Hugging Face API token is missing! Set it in your .env file.")
    st.stop()

@st.cache_resource
def load_model(temp,max_token):
    """Load the Hugging Face Chat Model (cached for efficiency)."""
    llm = HuggingFaceEndpoint(
        repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        huggingfacehub_api_token=api_token,
        temperature=0.7,
        max_new_tokens=max_token
    )
    return ChatHuggingFace(llm=llm)

# Load the model once and reuse it
model = load_model(temp,max_token)

# Session State for Chat Messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Handling
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Response
    with st.spinner("Thinking... 🤔"):
        response = model.invoke(user_input).content  # ✅ No extra parameters in invoke()

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
