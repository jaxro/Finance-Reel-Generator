import json
import asyncio
import edge_tts
import os

# Read current run folder
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

# Read topic json
with open(
    os.path.join(run_folder, "topic.json"),
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

script_text = data["script"]

async def generate():
    communicate = edge_tts.Communicate(
        text=script_text,
        voice="en-US-GuyNeural"
    )

    await communicate.save(
        os.path.join(run_folder, "voice.mp3")
    )

asyncio.run(generate())

print(
    f"Voice generated successfully: {run_folder}/voice.mp3"
)