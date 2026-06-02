import json
import os
from PIL import Image, ImageDraw, ImageFont

# Current run folder
with open("temp/current_run.txt", "r", encoding="utf-8") as f:
    run_folder = f.read().strip()

# Read topic
with open(
    os.path.join(run_folder, "topic.json"),
    "r",
    encoding="utf-8"
) as f:
    topic = json.load(f)

# Use hook instead of title
hook_text = topic["hook"].upper()

# Break into multiple lines
words = hook_text.split()
hook_text = "\n".join(words)

# Create image
img = Image.new(
    "RGB",
    (1080, 1920),
    color="black"
)

draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype(
        "arial.ttf",
        120
    )
except:
    font = ImageFont.load_default()

bbox = draw.multiline_textbbox(
    (0, 0),
    hook_text,
    font=font
)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (1080 - text_width) / 2
y = (1920 - text_height) / 2

draw.multiline_text(
    (x, y),
    hook_text,
    fill="white",
    font=font,
    align="center"
)

hook_path = os.path.join(
    run_folder,
    "hook.png"
)

img.save(hook_path)

print("Hook Created:", hook_path)