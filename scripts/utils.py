from pathlib import Path

def get_latest_video():
    output_dir = Path("output")

    latest_folder = max(
        [f for f in output_dir.iterdir() if f.is_dir()],
        key=lambda x: x.name
    )

    video_path = latest_folder / "final_reel_captioned.mp4"

    return str(video_path)
if __name__ == "__main__":
    print(get_latest_video())