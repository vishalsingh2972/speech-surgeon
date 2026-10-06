import subprocess
from pathlib import Path


def run_ffmpeg(args):
    command = ["ffmpeg", "-y", *args]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"FFmpeg failed:\n{result.stderr}"
        )


def repair_audio(
    original_path,
    replacement_path,
    target_start,
    target_end,
    output_path,
):
    original_path = Path(original_path)
    replacement_path = Path(replacement_path)
    output_path = Path(output_path)

    before_path = output_path.parent / "tmp_before.wav"
    after_path = output_path.parent / "tmp_after.wav"
    replacement_normalized = (
        output_path.parent / "tmp_replacement.wav"
    )
    concat_path = output_path.parent / "concat.txt"

    try:
        run_ffmpeg([
            "-i",
            str(original_path),
            "-t",
            str(target_start),
            "-c:a",
            "pcm_s16le",
            str(before_path),
        ])

        run_ffmpeg([
            "-i",
            str(original_path),
            "-ss",
            str(target_end),
            "-c:a",
            "pcm_s16le",
            str(after_path),
        ])

        run_ffmpeg([
            "-i",
            str(replacement_path),
            "-ar",
            "48000",
            "-ac",
            "2",
            "-c:a",
            "pcm_s16le",
            str(replacement_normalized),
        ])

        with open(concat_path, "w", encoding="utf-8") as f:
            f.write(f"file '{before_path.name}'\n")
            f.write(
                f"file '{replacement_normalized.name}'\n"
            )
            f.write(f"file '{after_path.name}'\n")

        run_ffmpeg([
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_path),
            "-c:a",
            "pcm_s16le",
            str(output_path),
        ])

    finally:
        for path in [
            before_path,
            after_path,
            replacement_normalized,
            concat_path,
        ]:
            if path.exists():
                path.unlink()