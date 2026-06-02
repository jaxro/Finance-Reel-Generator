import os
from moviepy import (
    VideoFileClip,
    AudioFileClip,
    ImageClip,
    CompositeAudioClip,
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

hook_path = os.path.join(
    run_folder,
    "hook.png"
)

# Load voice
audio = AudioFileClip(
    voice_path
)

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

        # Max 4 sec per clip
        clip = clip.subclipped(
            0,
            min(
                4,
                clip.duration
            )
        )

        # Convert to vertical format
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

        print(
            f"Loaded {file}"
        )

    except Exception as e:

        print(
            f"Failed: {file}"
        )

        print(e)

if not clips:

    raise Exception(
        "No videos found."
    )

# Repeat clips until audio duration is covered
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

# Main reel
main_video = concatenate_videoclips(
    extended_clips,
    method="compose"
)

main_video = main_video.subclipped(
    0,
    audio_duration
)

# Hook screen
hook_clip = (
    ImageClip(hook_path)
    .with_duration(2)
)

# Combine hook + reel
final_video = concatenate_videoclips(
    [
        hook_clip,
        main_video
    ],
    method="compose"
)

# ==========================
# Background Music
# ==========================

music_path = os.path.join(
    "assets",
    "music",
    "bg.mp3"
)

try:

    bg_music = AudioFileClip(
        music_path
    )

    # Reduce volume
    try:
        bg_music = bg_music.with_volume_scaled(
            0.10
        )
    except:
        pass

    # Trim music to reel length
    reel_duration = (
        audio_duration + 2
    )

    if bg_music.duration > reel_duration:

        bg_music = bg_music.subclipped(
            0,
            reel_duration
        )

    voice_audio = audio.with_start(
        2
    )

    final_audio = CompositeAudioClip(
        [
            bg_music,
            voice_audio
        ]
    )

    print(
        "Background music added."
    )

except Exception as e:

    print(
        "Background music not found."
    )

    print(e)

    final_audio = audio.with_start(
        2
    )

# Attach audio
final_video = final_video.with_audio(
    final_audio
)

output_file = os.path.join(
    run_folder,
    "final_reel_vertical.mp4"
)

print(
    "Rendering reel..."
)

final_video.write_videofile(
    output_file,
    codec="libx264",
    audio_codec="aac",
    fps=30
)

print(
    f"\nReel Created:\n{output_file}"
)