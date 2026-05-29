import os
from moviepy import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips
)

# Current run folder
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

videos_folder = os.path.join(
    run_folder,
    "videos"
)

voice_path = os.path.join(
    run_folder,
    "voice.mp3"
)

# Load audio
audio = AudioFileClip(voice_path)

audio_duration = audio.duration

clips = []

print("Loading videos...")

for file in sorted(os.listdir(videos_folder)):

    if not file.endswith(".mp4"):
        continue

    path = os.path.join(
        videos_folder,
        file
    )

    try:

        clip = VideoFileClip(path)

        # Limit each clip to 4 sec max
        clip = clip.subclipped(
            0,
            min(
                4,
                clip.duration
            )
        )

        # Convert to vertical
        target_ratio = 9 / 16

        current_ratio = (
            clip.w / clip.h
        )

        if current_ratio > target_ratio:

            new_width = int(
                clip.h * target_ratio
            )

            x_center = clip.w / 2

            clip = clip.cropped(
                x1=x_center - new_width / 2,
                x2=x_center + new_width / 2
            )

        clip = clip.resized(
            height=1920
        )

        clips.append(clip)

        print(f"Loaded {file}")

    except Exception as e:

        print(
            f"Failed: {file}"
        )

        print(e)

if not clips:

    raise Exception(
        "No videos found."
    )

# Repeat clips until audio ends
extended_clips = []

total_duration = 0

while total_duration < audio_duration:

    for clip in clips:

        extended_clips.append(
            clip.copy()
        )

        total_duration += (
            clip.duration
        )

        if total_duration >= audio_duration:
            break

print(
    f"Generated timeline: {total_duration:.2f}s"
)

# Merge all clips
final_video = concatenate_videoclips(
    extended_clips,
    method="compose"
)

# Trim exactly to audio duration
final_video = final_video.subclipped(
    0,
    audio_duration
)

# Add narration
final_video = final_video.with_audio(
    audio
)

output_file = os.path.join(
    run_folder,
    "final_reel_vertical.mp4"
)

print("Rendering reel...")

final_video.write_videofile(
    output_file,
    codec="libx264",
    audio_codec="aac",
    fps=30
)

print(
    f"\nReel Created:\n{output_file}"
)