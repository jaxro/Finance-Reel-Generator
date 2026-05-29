import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

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

# Collect video clips
clips = []

for file in sorted(os.listdir(videos_folder)):
    if file.endswith(".mp4"):

        path = os.path.join(
            videos_folder,
            file
        )

        clip = VideoFileClip(path)

        clips.append(clip)

# Merge clips
final_video = concatenate_videoclips(
    clips,
    method="compose"
)

# Match audio duration
final_video = final_video.subclipped(
    0,
    min(
        final_video.duration,
        audio_duration
    )
)

# Add narration
final_video = final_video.with_audio(audio)

# Export
output_file = os.path.join(
    run_folder,
    "final_reel.mp4"
)

final_video.write_videofile(
    output_file,
    codec="libx264",
    audio_codec="aac",
    fps=30
)

print(
    f"Reel created: {output_file}"
)