from faster_whisper import WhisperModel
import os

# Read current run folder
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

audio_path = os.path.join(
    run_folder,
    "voice.mp3"
)

# Load model
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

segments, info = model.transcribe(audio_path)

srt_path = os.path.join(
    run_folder,
    "subtitles.srt"
)

with open(
    srt_path,
    "w",
    encoding="utf-8"
) as srt_file:

    for i, segment in enumerate(segments, start=1):

        start = segment.start
        end = segment.end
        text = segment.text.strip()

        def format_time(seconds):
            hrs = int(seconds // 3600)
            mins = int((seconds % 3600) // 60)
            secs = int(seconds % 60)
            ms = int((seconds - int(seconds)) * 1000)

            return f"{hrs:02}:{mins:02}:{secs:02},{ms:03}"

        srt_file.write(f"{i}\n")
        srt_file.write(
            f"{format_time(start)} --> {format_time(end)}\n"
        )
        srt_file.write(f"{text}\n\n")

print(f"Subtitles saved: {srt_path}")