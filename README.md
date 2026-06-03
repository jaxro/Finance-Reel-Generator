# Finance Reel Generator

## Overview
## Project Goal
## Current Version

Version: V1.1

Status: Production Ready

---

## Features

### V1.0 Features
- AI Topic Generation
- AI Script Generation
- AI Voice Generation
- Scene Planning
- Pexels Footage Download
- Hook Screen
- Background Music
- Vertical Reel Creation
- Subtitle Generation
- Subtitle Timing Sync
- Subtitle Burn-In

### V1.1 Features
- Cloudinary Upload
- Instagram Graph API Integration
- Facebook Page Integration
- Instagram Business Account Integration
- Automatic Reel Publishing
- Dynamic Reel Detection
- Dynamic Creation ID Handling
- Instagram Processing Polling
- One Command Publishing

---

## Complete Architecture

run.py
│
├── topic_generator.py
├── generate_voice.py
├── generate_scenes.py
├── download_videos.py
├── create_hook.py
├── create_reel.py
├── generate_subtitles.py
├── shift_subtitles.py
├── burn_subtitles.py
│
├── utils.py
├── upload_to_cloudinary.py
└── instagram_publisher.py

---

## Complete End-To-End Flow

Gemini
│
├── Title
├── Hook
├── Script
└── Keyword
│
▼

topic.json
│
▼

Edge TTS
│
▼

voice.mp3
│
▼

Gemini Scene Planner
│
▼

scenes.json
│
▼

Pexels API
│
▼

videos/
│
▼

Hook Generator
│
▼

hook.png
│
▼

MoviePy
│
▼

final_reel_vertical.mp4
│
▼

Faster Whisper
│
▼

subtitles.srt
│
▼

Subtitle Sync
│
▼

shifted subtitles
│
▼

FFmpeg
│
▼

final_reel_captioned.mp4
│
▼

Cloudinary Upload
│
▼

Public URL
│
▼

Instagram Container
│
▼

Instagram Processing
│
▼

Instagram Publish
│
▼

LIVE REEL

---

## Folder Structure

FinanceAgent/

├── assets/
│   └── music/
│       └── bg.mp3
│
├── output/
│
├── scripts/
│   ├── topic_generator.py
│   ├── generate_voice.py
│   ├── generate_scenes.py
│   ├── download_videos.py
│   ├── create_hook.py
│   ├── create_reel.py
│   ├── generate_subtitles.py
│   ├── shift_subtitles.py
│   ├── burn_subtitles.py
│   ├── utils.py
│   ├── upload_to_cloudinary.py
│   └── instagram_publisher.py
│
├── temp/
│
├── run.py
├── requirements.txt
├── README.md
└── .env

---

# File Explanations

## 1. topic_generator.py

Purpose:
Generate title, hook, script and keyword using Gemini.

Input:
None

Output:
topic.json

Future:
- Trend detection
- Topic scoring
- Multiple topic generation

---

## 2. generate_voice.py

Purpose:
Convert script to narration using Edge TTS.

Input:
topic.json

Output:
voice.mp3

---

## 3. generate_scenes.py

Purpose:
Generate scene descriptions from script.

Input:
topic.json

Output:
scenes.json

---

## 4. download_videos.py

Purpose:
Download relevant stock footage using Pexels.

Input:
scenes.json

Output:
videos/

---

## 5. create_hook.py

Purpose:
Generate first 2-second hook screen.

Output:
hook.png

---

## 6. create_reel.py

Purpose:
Create vertical reel.

Inputs:
- Videos
- Voice
- Hook
- Background Music

Output:
final_reel_vertical.mp4

Features:
- Vertical crop
- Auto looping
- Audio sync
- Background music
- Hook screen

---

## 7. generate_subtitles.py

Purpose:
Generate subtitles using Faster Whisper.

Output:
subtitles.srt

---

## 8. shift_subtitles.py

Purpose:
Shift subtitles by 2 seconds because narration starts after hook screen.

Output:
Updated subtitles.srt

---

## 9. burn_subtitles.py

Purpose:
Burn subtitles permanently using FFmpeg.

Output:
final_reel_captioned.mp4

---

## 10. utils.py

Purpose:
Automatically locate latest generated reel.

Example:

get_latest_video()

Returns:

output/<latest_timestamp>/final_reel_captioned.mp4

Problem Solved:

No hardcoded folder names.

---

## 11. upload_to_cloudinary.py

Purpose:
Upload final reel to Cloudinary.

Input:
final_reel_captioned.mp4

Output:
Public video URL

Why Needed:

Instagram requires a publicly accessible video URL.

---

## 12. instagram_publisher.py

Purpose:
Publish reel to Instagram automatically.

Flow:

Latest Reel
↓
Upload To Cloudinary
↓
Create Instagram Container
↓
Wait Until Processing Complete
↓
Publish Reel

Problems Solved:

- Dynamic Creation IDs
- Dynamic Video URLs
- Instagram Processing Delay
- No Manual Publishing

---

## 13. run.py

Purpose:
Master pipeline controller.

Command:

python run.py

Flow:

Topic Generation
↓
Voice Generation
↓
Scene Generation
↓
Video Download
↓
Hook Creation
↓
Reel Creation
↓
Subtitle Generation
↓
Subtitle Sync
↓
Subtitle Burn-In
↓
Cloudinary Upload
↓
Instagram Publishing

---

## Meta Infrastructure

Meta App:
Finance Reel Generator

Facebook Page:
FintechBot Daily

Facebook Page ID:
1144735958728121

Instagram Username:
fintechbot.daily

Instagram Business Account ID:
17841424535685192

Status:
Working

---

## Common Issues Solved

### Voice reading Gemini formatting
Fixed by extracting only script section.

### Video shorter than narration
Fixed using automatic clip looping.

### Subtitles appearing on hook screen
Fixed using subtitle shifting.

### Hardcoded output folders
Fixed using utils.py.

### Hardcoded Creation IDs
Fixed using dynamic container creation.

### Instagram publishing before processing
Fixed using status polling.

### Cloudinary upload automation
Implemented.

---

## Version History

### Version 1.0
AI Reel Generator

Status:
Completed

### Version 1.1
Instagram Auto Publishing

Status:
Completed

Achievements:
- Cloudinary Integration
- Instagram Graph API Integration
- Automated Publishing
- One Command Publishing

### Version 2.0 (Planned)

Goal:
Replace stock footage with AI-generated visuals.

Tools:
- Flux
- Stable Diffusion
- Kling
- Runway

Expected Quality:
8.5/10

---

### Version 3.0 (Planned)

Goal:
Autonomous Content Agent

Pipeline:

Scheduler
↓
Generate Topic
↓
Generate Reel
↓
Publish Reel
↓
Collect Analytics
↓
Store Metrics
↓
Improve Future Content

Features:
- Auto Posting
- Auto Captions
- Auto Hashtags
- Analytics Tracking
- Performance Monitoring

---

## Installation

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

---

## Environment Variables

GEMINI_API_KEY=

PEXELS_API_KEY=

META_ACCESS_TOKEN=

INSTAGRAM_BUSINESS_ID=

CLOUDINARY_CLOUD_NAME=

CLOUDINARY_API_KEY=

CLOUDINARY_API_SECRET=

---

## Usage

python run.py

Output:

Instagram Reel Published Automatically

---

## Current Status

Version: V1.1

Status: COMPLETE

Result:

python run.py

↓

Generate Reel

↓

Upload To Instagram

↓

Instagram Reel Live