import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = """
You are a viral Instagram finance creator.

Generate response in this format only:

TITLE:
HOOK:
SCRIPT:
KEYWORD:

Topic should be related to personal finance.
"""

response = model.generate_content(prompt)

print(response.text)