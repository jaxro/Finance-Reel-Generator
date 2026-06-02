import os
import subprocess
import shutil

# Current run folder
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

video_path = os.path.abspath(
    os.path.join(
        run_folder,
        "final_reel_vertical.mp4"
    )
)

subtitle_path = os.path.abspath(
    os.path.join(
        run_folder,
        "subtitles.srt"
    )
)

output_path = os.path.abspath(
    os.path.join(
        run_folder,
        "final_reel_captioned.mp4"
    )
)

# Copy subtitle to simple filename
temp_sub = os.path.abspath(
    os.path.join(
        run_folder,
        "sub.srt"
    )
)

shutil.copy(
    subtitle_path,
    temp_sub
)

# FFmpeg-safe path
temp_sub_ffmpeg = (
    temp_sub
    .replace("\\", "/")
    .replace(":", "\\:")
)

ffmpeg_path = r"C:\Users\ABhay negi\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"

cmd = [
    ffmpeg_path,
    "-y",
    "-i",
    video_path,
    "-vf",
    f"subtitles='{temp_sub_ffmpeg}'",
    output_path
]

print("Burning subtitles...")

subprocess.run(
    cmd,
    check=True
)

print("Done!")
print(output_path)