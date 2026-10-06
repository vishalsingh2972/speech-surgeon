from uuid import uuid4

sessions = {}

def create_session(
    original_text,
    segments,
    audio_bytes,
    filename,
    video_bytes=None,
):
    session_id = str(uuid4())

    sessions[session_id] = {
        "original_text": original_text,
        "segments": segments,
        "audio_bytes": audio_bytes,
        "filename": filename,
        "video_bytes": video_bytes,
    }

    return session_id

def get_session(session_id):
    session = sessions.get(session_id)

    if session is None:
        raise RuntimeError(
            "Session not found."
        )

    return session