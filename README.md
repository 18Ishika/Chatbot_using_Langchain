AI CHATBOT USING TINY LLAMA

This is a simple AI chatbot built using Streamlit and Hugging Face's TinyLlama model. It allows users to interact with an open-source chat model and adjust settings like temperature and max tokens.

Features

Real-time chat interface using Streamlit
Adjustable settings for temperature and token limit
Powered by TinyLlama-1.1B-Chat-v1.0 from Hugging Face

Prerequisites

Python 3.7 or above
Hugging Face API Token
Required libraries: streamlit, python-dotenv, langchain_huggingface

Installation
Clone the Repository:

        git clone <repository_url>
        cd <repository_folder>
Create a Virtual Environment:

        python -m venv venv
        source venv/bin/activate   # On macOS/Linux
        .\venv\Scripts\activate    # On Windows
        
Install Dependencies:

        pip install requirements.txt

Set up Environment Variables:

  Create a .env file in the root directory.
  Add your Hugging Face API token:
  
      HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key

Usage
Run the application with:

        streamlit run your_app.py --server.fileWatcherType none



