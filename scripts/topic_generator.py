import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = """
You are a viral Instagram finance creator.

Return ONLY valid JSON.

{
  "title":"",
  "hook":"",
  "script":"",
  "keyword":""
}

Rules:
- Finance topic only
- Script should be 30-45 seconds
- No markdown
- No emojis
- No extra explanation
- Return only JSON
"""

response = model.generate_content(prompt)

text = response.text.strip()

# Remove code blocks if Gemini adds them
text = text.replace("```json", "")
text = text.replace("```", "")

data = json.loads(text)

# Create unique run folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

run_folder = os.path.join("output", timestamp)

os.makedirs(run_folder, exist_ok=True)

# Save current run path
with open("temp/current_run.txt", "w", encoding="utf-8") as f:
    f.write(run_folder)

# Save JSON
with open(
    os.path.join(run_folder, "topic.json"),
    "w",
    encoding="utf-8"
) as f:
    json.dump(data, f, indent=4)

print(f"Topic saved successfully: {run_folder}")
print(json.dumps(data, indent=4))