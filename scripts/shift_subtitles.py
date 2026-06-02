import os
import re

HOOK_DURATION_MS = 2000

with open(
    "temp/current_run.txt",
    "r",
    encoding="utf-8"
) as f:
    run_folder = f.read().strip()

srt_path = os.path.join(
    run_folder,
    "subtitles.srt"
)

with open(
    srt_path,
    "r",
    encoding="utf-8"
) as f:
    content = f.read()


def shift_timestamp(time_str):

    h, m, rest = time_str.split(":")
    s, ms = rest.split(",")

    total_ms = (
        int(h) * 3600000
        + int(m) * 60000
        + int(s) * 1000
        + int(ms)
    )

    total_ms += HOOK_DURATION_MS

    h = total_ms // 3600000
    total_ms %= 3600000

    m = total_ms // 60000
    total_ms %= 60000

    s = total_ms // 1000
    ms = total_ms % 1000

    return (
        f"{h:02}:{m:02}:{s:02},{ms:03}"
    )


pattern = (
    r"(\d{2}:\d{2}:\d{2},\d{3})"
    r" --> "
    r"(\d{2}:\d{2}:\d{2},\d{3})"
)


def replace(match):

    start = shift_timestamp(
        match.group(1)
    )

    end = shift_timestamp(
        match.group(2)
    )

    return (
        f"{start} --> {end}"
    )


content = re.sub(
    pattern,
    replace,
    content
)

with open(
    srt_path,
    "w",
    encoding="utf-8"
) as f:
    f.write(content)

print(
    "Subtitles shifted by 2 seconds"
)