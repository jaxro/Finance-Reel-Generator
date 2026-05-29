import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Current run
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

# Read topic
with open(
    os.path.join(run_folder, "topic.json"),
    "r",
    encoding="utf-8"
) as f:
    topic = json.load(f)

script = topic["script"]

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

prompt = f"""
Read this finance reel script.

Create 8 visual scenes.

Return ONLY JSON.

Example:

[
  "person checking investment app",
  "stock market graph",
  "saving money jar"
]

Script:

{script}
"""

response = model.generate_content(
    prompt
)

text = response.text.strip()

text = text.replace(
    "```json",
    ""
)

text = text.replace(
    "```",
    ""
)

scenes = json.loads(text)

with open(
    os.path.join(
        run_folder,
        "scenes.json"
    ),
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        scenes,
        f,
        indent=4
    )

print("Scenes Generated")
print(scenes)