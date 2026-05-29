import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Current run folder
with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

# Read scenes
with open(
    os.path.join(run_folder, "scenes.json"),
    "r",
    encoding="utf-8"
) as f:
    search_terms = json.load(f)

PEXELS_API_KEY = os.getenv(
    "PEXELS_API_KEY"
)

headers = {
    "Authorization": PEXELS_API_KEY
}

videos_folder = os.path.join(
    run_folder,
    "videos"
)

os.makedirs(
    videos_folder,
    exist_ok=True
)

download_count = 1

for term in search_terms:

    print(f"\nSearching: {term}")

    url = (
        "https://api.pexels.com/videos/search"
        f"?query={term}"
        "&orientation=portrait"
        "&per_page=10"
    )

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        data = response.json()

        videos = data.get(
            "videos",
            []
        )

        if not videos:
            print(
                f"No videos found for {term}"
            )
            continue

        selected_video = None

        # Pick first portrait video
        for video in videos:

            width = video.get(
                "width",
                0
            )

            height = video.get(
                "height",
                0
            )

            if height > width:
                selected_video = video
                break

        if not selected_video:
            print(
                f"No portrait video found for {term}"
            )
            continue

        # Get best quality file
        video_files = selected_video.get(
            "video_files",
            []
        )

        if not video_files:
            continue

        video_url = sorted(
            video_files,
            key=lambda x: x.get(
                "height",
                0
            ),
            reverse=True
        )[0]["link"]

        print(
            f"Downloading: {term}"
        )

        video_data = requests.get(
            video_url,
            timeout=60
        )

        filename = os.path.join(
            videos_folder,
            f"scene_{download_count}.mp4"
        )

        with open(
            filename,
            "wb"
        ) as f:
            f.write(
                video_data.content
            )

        print(
            f"Saved: {filename}"
        )

        download_count += 1

    except Exception as e:

        print(
            f"Error: {e}"
        )

print(
    f"\nDownloaded {download_count - 1} scene videos."
)