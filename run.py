import subprocess

steps = [
    "python scripts/topic_generator.py",
    "python scripts/generate_voice.py",
    "python scripts/generate_scenes.py",
    "python scripts/download_videos.py",
    "python scripts/create_hook.py",
    "python scripts/create_reel.py",
    "python scripts/generate_subtitles.py",
    "python scripts/shift_subtitles.py",
    "python scripts/burn_subtitles.py"
]

for step in steps:

    print("\n" + "=" * 50)
    print(f"Running: {step}")
    print("=" * 50)

    result = subprocess.run(
        step,
        shell=True
    )

    if result.returncode != 0:

        print(
            f"\nFAILED: {step}"
        )

        break

print(
    "\nPipeline Complete!"
)