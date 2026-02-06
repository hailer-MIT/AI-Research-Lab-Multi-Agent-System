import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

def list_models(api_key=None):
    load_dotenv()
    if not api_key:
        api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("Error: No API key provided and GOOGLE_API_KEY not found in .env file.")
        print("Usage: python diagnose_models.py YOUR_API_KEY")
        return

    genai.configure(api_key=api_key)
    
    print(f"Listing available models for key: {api_key[:10]}...")
    try:
        found = False
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Model ID: {m.name}, Name: {m.display_name}")
                found = True
        if not found:
            print("No models found with 'generateContent' support.")
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else None
    list_models(key)
