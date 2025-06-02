#import google.generativeai as genai
#import os
#from dotenv import load_dotenv

#load_dotenv()  # Load .env file

#genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
import streamlit as st
import google.generativeai as genai

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
