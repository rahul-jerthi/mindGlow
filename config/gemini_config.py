import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
