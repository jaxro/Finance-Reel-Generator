# Finance Reel Generator

## Overview

Finance Reel Generator is a fully automated AI-powered content creation pipeline that generates finance reels for Instagram using a single command.

The project automatically:

* Generates a finance topic using Gemini
* Creates a viral hook
* Writes a finance script
* Generates AI narration
* Creates scene plans
* Downloads relevant stock footage
* Creates a vertical reel
* Adds a hook screen
* Adds background music
* Generates subtitles
* Burns subtitles into the final video

Final output:

```bash
python run.py
```

↓

```text
final_reel_captioned.mp4
```

---

# Project Goal

The purpose of this project is to automate the entire short-form content creation workflow.

Traditional Workflow:

```text
Research Topic
↓
Write Script
↓
Record Voice
↓
Find Videos
↓
Edit Reel
↓
Add Subtitles
↓
Upload
```

Automated Workflow:

```text
python run.py
↓
Everything Automated
```

---

# Current Version

Version: V1 MVP

Status: Completed

Implemented Features:

* AI Topic Generation
* AI Script Generation
* AI Voice Generation
* Scene Planning
* Stock Footage Download
* Hook Screen
* Background Music
* Vertical Reel Creation
* Subtitle Generation
* Subtitle Timing Sync
* Subtitle Burn-In
* One-Click Automation

---

# Complete Architecture

```text
run.py
│
├── topic_generator.py
│
├── generate_voice.py
│
├── generate_scenes.py
│
├── download_videos.py
│
├── create_hook.py
│
├── create_reel.py
│
├── generate_subtitles.py
│
├── shift_subtitles.py
│
└── burn_subtitles.py
```

---

# End-To-End Flow

```text
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
```

---

# Folder Structure

```text
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
│   └── burn_subtitles.py
│
├── temp/
│
├── run.py
├── requirements.txt
├── README.md
└── .env
```

---

# File Explanations

## 1. topic_generator.py

### Purpose

Generates finance content using Gemini.

### Technology

* Gemini 2.5 Flash

### Input

None

### Process

```text
Prompt Gemini
↓
Generate:
Title
Hook
Script
Keyword
```

### Output

```text
topic.json
```

### Example

```json
{
  "title": "STOP Doing This With Money",
  "hook": "Most people lose money because of this...",
  "script": "...",
  "keyword": "Personal Finance"
}
```

### Future Improvements

* Trend detection
* Multiple topic generation
* Topic scoring

---

## 2. generate_voice.py

### Purpose

Converts script into narration.

### Technology

* Edge TTS

### Input

```text
topic.json
```

### Process

```text
Read Script
↓
Extract Script Section
↓
Convert To Speech
```

### Output

```text
voice.mp3
```

### Problem Solved

Originally voice was reading:

```text
***
TITLE
HOOK
```

Now only the script section is spoken.

---

## 3. generate_scenes.py

### Purpose

Creates scene descriptions for the reel.

### Technology

* Gemini

### Input

```text
topic.json
```

### Output

```text
scenes.json
```

### Example

```json
[
  "person checking investment app",
  "stock market chart",
  "retirement planning"
]
```

### Why Needed

Without scene planning:

```text
Random footage
```

With scene planning:

```text
Relevant footage
```

---

## 4. download_videos.py

### Purpose

Downloads stock footage.

### Technology

* Pexels API

### Input

```text
scenes.json
```

### Process

```text
Scene
↓
Search Pexels
↓
Find Vertical Video
↓
Download
```

### Output

```text
videos/
```

### Current Logic

```text
8 scenes
↓
8 searches
↓
5-15 downloaded clips
```

---

## 5. create_hook.py

### Purpose

Creates the opening hook screen.

### Input

```text
Title
```

### Output

```text
hook.png
```

### Example

```text
STOP
WASTING
MONEY
LIKE
THIS
```

### Why

The first 2 seconds determine reel retention.

---

## 6. create_reel.py

### Purpose

Creates the main reel.

### Technologies

* MoviePy

### Inputs

```text
videos/
voice.mp3
hook.png
bg.mp3
```

### Process

```text
Load Videos
↓
Crop To Vertical
↓
Resize
↓
Trim
↓
Merge
↓
Loop Clips
↓
Add Hook
↓
Add Voice
↓
Add Music
```

### Output

```text
final_reel_vertical.mp4
```

### Improvements Implemented

* Vertical crop
* Hook screen
* Background music
* Audio sync
* Video looping

### Problems Solved

#### Problem

Video ended before audio.

#### Solution

Auto looping clips until narration finishes.

---

## 7. generate_subtitles.py

### Purpose

Creates subtitles.

### Technology

* Faster Whisper

### Input

```text
voice.mp3
```

### Output

```text
subtitles.srt
```

### Example

```srt
1
00:00:00,000 --> 00:00:03,280

Want your money to make money effortlessly?
```

### Why

Many Instagram users watch without sound.

---

## 8. shift_subtitles.py

### Purpose

Sync subtitles with narration.

### Why Needed

Hook screen occupies:

```text
0-2 seconds
```

Voice starts:

```text
2 seconds
```

Subtitles originally started:

```text
0 seconds
```

### Process

```text
Shift every subtitle timestamp
+2 seconds
```

### Result

Subtitles appear exactly when narration starts.

---

## 9. burn_subtitles.py

### Purpose

Burn subtitles into video permanently.

### Technology

* FFmpeg

### Input

```text
final_reel_vertical.mp4
subtitles.srt
```

### Output

```text
final_reel_captioned.mp4
```

### Why FFmpeg

* Fast
* Reliable
* Industry standard

---

## 10. run.py

### Purpose

Master controller.

### Command

```bash
python run.py
```

### Executes

```text
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
```

### Final Output

```text
final_reel_captioned.mp4
```

---

# Output Structure

Example:

```text
output/

└── 20260602_114141/

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

# Common Issues Solved

## Issue 1

Voice reading Gemini formatting.

### Fix

Extract script only.

---

## Issue 2

Video shorter than narration.

### Fix

Loop clips automatically.

---

## Issue 3

Subtitles appearing on hook screen.

### Fix

shift_subtitles.py

---

## Issue 4

FFmpeg not detected.

### Fix

Install FFmpeg and use explicit executable path.

---

## Issue 5

Stock footage ended before narration.

### Fix

Timeline extension and clip looping.

---

# Version 2 Roadmap

Goal:

Replace stock footage with AI visuals.

Current:

```text
Gemini
↓
Scenes
↓
Pexels
↓
Videos
```

Future:

```text
Gemini
↓
Scene Prompts
↓
AI Image Generation
↓
Animation
↓
Reel
```

Potential Tools:

* Gemini Image Generation
* Flux
* Stable Diffusion
* Kling
* Runway

Expected Quality:

```text
Current:
6.5/10

Version 2:
8.5/10
```

Benefits:

* Better storytelling
* Better visual consistency
* More unique content
* Higher engagement

---

# Version 3 Roadmap

Goal:

Fully Autonomous Instagram Agent

Architecture:

```text
Scheduler
↓
Generate Topic
↓
Generate Reel
↓
Upload To Instagram
↓
Collect Analytics
↓
Store Results
```

Capabilities:

* Auto posting
* Auto captions
* Auto hashtags
* Analytics tracking
* Performance monitoring

Pipeline:

```text
python run.py

↓

Create Reel

↓

Upload Reel

↓

Instagram Post

↓

Collect Analytics

↓

Improve Future Content
```

---

# Installation

Create Environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

PEXELS_API_KEY=YOUR_PEXELS_API_KEY
```

---

# Usage

Run Everything

```bash
python run.py
```

Final Output:

```text
output/<timestamp>/

final_reel_captioned.mp4
```

---

# Project Status

Version 1 MVP

Completed Successfully

Current Features:

* AI Content Generation
* AI Narration
* Scene Planning
* Stock Footage Download
* Hook Screen
* Background Music
* Subtitle Generation
* Subtitle Synchronization
* Subtitle Burn-In
* One Click Automation

Next Milestone:

Version 2
AI Generated Visuals

Future Milestone:

Version 3
Fully Autonomous Instagram Content Agent
