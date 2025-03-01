from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Templates in LangChain", page_icon="🤖", layout="wide")
st.title("LANGCHAIN TEMPLATES")
st.header("Research Tool")

# Dropdowns for user input
paper_input = st.selectbox("Select the research paper name:", [
    "Attention is All You Need",
    "BERT: Pre-Training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GAN on Image Synthesis"
])

style_input = st.selectbox("Select the explanation style:", [
    "Code oriented", "Beginner Friendly", "Mathematical", "Technical"
])

length_input = st.selectbox("Select the length of output:", [
    "Short (1-2 para)", "Medium (2-3 para)", "Large (4-5 para)"
])

# Prompt template
prompt = f"""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  

1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""

# Retrieve API token from .env file
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not api_token:
    st.error("Hugging Face API token not found. Please check your .env file.")

# Initialize Falcon API Client
client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2", token=api_token)

# Generate summary on button click
if st.button("Summarize"):
    try:
        with st.spinner("Generating summary... ⏳"):
            response = client.text_generation(prompt, max_new_tokens=256)
        st.subheader("Generated Summary:")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
