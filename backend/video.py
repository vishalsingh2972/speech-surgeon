import subprocess
from pathlib import Path


def run_ffmpeg(args):
    command = [
        "ffmpeg",
        "-y",
        *args,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"FFmpeg failed:\n{result.stderr}"
        )


def extract_audio(
    video_path,
    audio_path,
):
    video_path = Path(video_path)
    audio_path = Path(audio_path)

    audio_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    run_ffmpeg([
        "-i",
        str(video_path),
        "-vn",
        "-acodec",
        "pcm_s16le",
        str(audio_path),
    ])


def replace_video_audio(
    video_path,
    audio_path,
    output_path,
):
    video_path = Path(video_path)
    audio_path = Path(audio_path)
    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    run_ffmpeg([
        "-i",
        str(video_path),
        "-i",
        str(audio_path),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        str(output_path),
    ])