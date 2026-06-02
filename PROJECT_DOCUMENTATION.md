# PROJECT_DOCUMENTATION.md

# Finance Reel Generator - Developer Documentation

## Project Information

Project Name:

Finance Reel Generator

Author:

Abhay Negi

Current Version:

V1 MVP

Status:

Completed

Repository Purpose:

Automatically generate finance reels using AI and export ready-to-post Instagram content.

---

# Why This Project Exists

Creating short-form content manually requires:

1. Topic research
2. Script writing
3. Voice recording
4. Finding footage
5. Editing videos
6. Adding music
7. Creating subtitles
8. Exporting

This process can take:

```text
1-3 hours per reel
```

Goal of this project:

```text
One Command

↓

Generate Complete Reel

↓

Ready For Instagram
```

---

# High Level Architecture

```text
run.py

↓

Gemini

↓

Script

↓

Voice

↓

Scene Planning

↓

Video Download

↓

Hook Creation

↓

Video Editing

↓

Subtitle Generation

↓

Subtitle Sync

↓

Subtitle Burn

↓

Final Reel
```

---

# Complete System Architecture

```text
┌─────────────────────┐
│     run.py          │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ topic_generator.py  │
└──────────┬──────────┘
           │
           ▼

       topic.json

           │
           ▼

┌─────────────────────┐
│ generate_voice.py   │
└──────────┬──────────┘
           │
           ▼

        voice.mp3

           │
           ▼

┌─────────────────────┐
│ generate_scenes.py  │
└──────────┬──────────┘
           │
           ▼

       scenes.json

           │
           ▼

┌─────────────────────┐
│ download_videos.py  │
└──────────┬──────────┘
           │
           ▼

         videos/

           │
           ▼

┌─────────────────────┐
│ create_hook.py      │
└──────────┬──────────┘
           │
           ▼

        hook.png

           │
           ▼

┌─────────────────────┐
│ create_reel.py      │
└──────────┬──────────┘
           │
           ▼

final_reel_vertical.mp4

           │
           ▼

┌─────────────────────────┐
│ generate_subtitles.py   │
└──────────┬──────────────┘
           │
           ▼

       subtitles.srt

           │
           ▼

┌─────────────────────┐
│ shift_subtitles.py  │
└──────────┬──────────┘
           │
           ▼

shifted subtitles

           │
           ▼

┌─────────────────────┐
│ burn_subtitles.py   │
└──────────┬──────────┘
           │
           ▼

final_reel_captioned.mp4
```

---

# Technologies Used

## LLM

Gemini 2.5 Flash

Purpose:

* Topic generation
* Hook generation
* Script generation
* Scene planning

---

## Voice Generation

Edge TTS

Purpose:

Convert generated script into narration.

Output:

```text
voice.mp3
```

---

## Scene Planning

Gemini

Purpose:

Generate visual descriptions.

Example:

```json
[
  "person checking finances",
  "investment graph",
  "retirement planning"
]
```

---

## Stock Footage

Pexels API

Purpose:

Download videos matching scene descriptions.

---

## Video Editing

MoviePy

Purpose:

* Merge clips
* Resize clips
* Vertical formatting
* Add hook
* Add music
* Add narration

---

## Subtitle Generation

Faster Whisper

Purpose:

Generate subtitles automatically.

---

## Subtitle Burn

FFmpeg

Purpose:

Embed subtitles into final video.

---

# Folder Structure

FinanceAgent/

├── assets/
│
│   └── music/
│       └── bg.mp3
│
├── output/
│
├── scripts/
│
│   ├── topic_generator.py
│   ├── generate_voice.py
│   ├── generate_scenes.py
│   ├── download_videos.py
│   ├── create_hook.py
│   ├── create_reel.py
│   ├── generate_subtitles.py
│   ├── shift_subtitles.py
│   └── burn_subtitles.py
│
├── temp/
│
├── run.py
├── requirements.txt
├── .env

---

# Output Folder Structure

Every execution creates a new folder.

Example:

output/

└── 20260602_114141/

```
topic.json

scenes.json

voice.mp3

hook.png

subtitles.srt

final_reel_vertical.mp4

final_reel_captioned.mp4

videos/
```

---

# Detailed Script Documentation

## topic_generator.py

Purpose:

Generate content.

Input:

None

Output:

topic.json

Contains:

* title
* hook
* script
* keyword

Responsibilities:

* Ask Gemini for topic
* Create structured output
* Save topic

---

## generate_voice.py

Purpose:

Convert script to speech.

Input:

topic.json

Output:

voice.mp3

Important Logic:

Only reads SCRIPT section.

Avoids reading:

TITLE
HOOK
Formatting characters

Problem Fixed:

Originally reading:

```text
***
TITLE
HOOK
```

Now reads:

```text
script only
```

---

## generate_scenes.py

Purpose:

Generate visual plan.

Input:

topic.json

Output:

scenes.json

Responsibilities:

* Read script
* Generate scenes
* Return JSON list

---

## download_videos.py

Purpose:

Download footage.

Input:

scenes.json

Output:

videos/

Process:

Scene

↓

Search Pexels

↓

Select Video

↓

Download

Current Limitation:

Sometimes only 5 videos downloaded.

Current Fix:

Loop footage until narration ends.

---

## create_hook.py

Purpose:

Create opening frame.

Input:

Title

Output:

hook.png

Purpose:

Increase retention.

Current Duration:

2 seconds

---

## create_reel.py

Most important file.

Responsibilities:

1. Load footage
2. Convert to vertical
3. Resize
4. Merge clips
5. Loop clips
6. Add hook
7. Add narration
8. Add music

Inputs:

videos/

voice.mp3

hook.png

bg.mp3

Output:

final_reel_vertical.mp4

---

## generate_subtitles.py

Purpose:

Generate subtitles.

Technology:

Faster Whisper

Input:

voice.mp3

Output:

subtitles.srt

---

## shift_subtitles.py

Purpose:

Subtitle timing correction.

Why Needed:

Hook screen occupies:

0-2 sec

Narration starts:

2 sec

Without correction:

Subtitles appear on hook screen.

Solution:

Shift all timestamps +2 sec.

---

## burn_subtitles.py

Purpose:

Hardcode subtitles.

Technology:

FFmpeg

Input:

video

*

srt

Output:

final_reel_captioned.mp4

---

## run.py

Master orchestrator.

Runs:

1. Topic Generation
2. Voice Generation
3. Scene Planning
4. Video Download
5. Hook Creation
6. Reel Creation
7. Subtitle Generation
8. Subtitle Shift
9. Subtitle Burn

Final Output:

final_reel_captioned.mp4

---

# Bugs Encountered During Development

## Bug 1

Voice reading title and formatting.

Solution:

Extract script only.

---

## Bug 2

Video shorter than narration.

Solution:

Clip looping.

---

## Bug 3

Hook screen without sync.

Solution:

Audio starts after hook.

---

## Bug 4

Subtitles appearing on hook.

Solution:

shift_subtitles.py

---

## Bug 5

FFmpeg not found.

Solution:

Install FFmpeg using winget.

---

## Bug 6

FFmpeg Windows path issue.

Cause:

Spaces in folder names.

Solution:

Use escaped paths.

---

# Current Quality Assessment

Topic Quality:

8/10

Voice Quality:

8/10

Video Quality:

6.5/10

Subtitle Quality:

7/10

Automation Quality:

9/10

Overall:

7.5/10

---

# Version 2 Roadmap

Goal:

Replace stock footage.

Current:

Gemini

↓

Scenes

↓

Pexels

↓

Videos

Future:

Gemini

↓

Scene Prompt

↓

AI Images

↓

Animation

↓

Video

Expected Improvement:

Visual Quality

6.5/10

↓

8.5/10

Potential Tools:

* Gemini Image
* Flux
* Stable Diffusion
* Kling
* Runway

---

# Version 3 Roadmap

Goal:

Fully Autonomous Content Agent

Architecture:

Scheduler

↓

Generate Reel

↓

Upload Instagram

↓

Save Analytics

↓

Track Performance

↓

Improve Content

Capabilities:

* Auto posting
* Auto hashtags
* Auto captions
* Analytics storage
* Daily posting

---

# Important Files To Never Commit

.env

output/

temp/

venv/

---

# Important Files To Always Commit

scripts/

run.py

README.md

PROJECT_DOCUMENTATION.md

requirements.txt

.gitignore

---

# Recovery Guide

If project breaks:

1. Create venv

```bash
python -m venv venv
```

2. Activate

```bash
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure .env

5. Run

```bash
python run.py
```

---

# Current Status

Version 1

Completed Successfully

Next Target:

Version 2

AI Generated Visuals

Final Target:

Version 3

Fully Autonomous Instagram Content Factory
