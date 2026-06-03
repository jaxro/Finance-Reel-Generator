import os
import time
import requests

from dotenv import load_dotenv

from upload_to_cloudinary import upload_video
from utils import get_latest_video

load_dotenv()

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
INSTAGRAM_BUSINESS_ID = os.getenv("INSTAGRAM_BUSINESS_ID")


def create_container(video_url, caption):

    url = (
        f"https://graph.facebook.com/v25.0/"
        f"{INSTAGRAM_BUSINESS_ID}/media"
    )

    payload = {
        "media_type": "REELS",
        "video_url": video_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(
        url,
        data=payload
    )

    print("\nContainer Response:")
    print(response.status_code)
    print(response.text)

    if response.status_code != 200:
        raise Exception(
            f"Container creation failed:\n{response.text}"
        )

    return response.json()["id"]


def wait_until_ready(creation_id):

    print(
        "\nWaiting for Instagram "
        "to process the reel..."
    )

    while True:

        url = (
            f"https://graph.facebook.com/v25.0/"
            f"{creation_id}"
        )

        params = {
            "fields": "status_code",
            "access_token": ACCESS_TOKEN
        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        status = data.get(
            "status_code",
            "UNKNOWN"
        )

        print(
            f"Current Status: {status}"
        )

        if status == "FINISHED":

            print(
                "\nInstagram processing completed."
            )

            return

        if status == "ERROR":

            raise Exception(
                "Instagram processing failed."
            )

        time.sleep(10)


def publish_container(creation_id):

    url = (
        f"https://graph.facebook.com/v25.0/"
        f"{INSTAGRAM_BUSINESS_ID}/media_publish"
    )

    payload = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN
    }

    response = requests.post(
        url,
        data=payload
    )

    print("\nPublish Response:")
    print(response.status_code)
    print(response.text)

    if response.status_code != 200:
        raise Exception(
            f"Publish failed:\n{response.text}"
        )

    return response.json()


def publish_reel():

    print("\n==============================")
    print("INSTAGRAM PUBLISH STARTED")
    print("==============================")

    latest_video = get_latest_video()

    print("\nLatest Video:")
    print(latest_video)

    print("\nUploading to Cloudinary...")

    video_url = upload_video(
        latest_video
    )

    print("\nCloudinary URL:")
    print(video_url)

    caption = """
💰 Daily Finance Tip

Follow @fintechbot.daily for more.

#finance
#investing
#money
#stockmarket
#personalfinance
"""

    print("\nCreating Instagram Container...")

    creation_id = create_container(
        video_url,
        caption
    )

    print("\nCreation ID:")
    print(creation_id)

    wait_until_ready(
        creation_id
    )

    print("\nPublishing Reel...")

    result = publish_container(
        creation_id
    )

    print(
        "\nInstagram Reel Published Successfully"
    )

    print("\nPublish Result:")
    print(result)

    return result


if __name__ == "__main__":
    publish_reel()