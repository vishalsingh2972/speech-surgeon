"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [originalVideoUrl, setOriginalVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [transcript, setTranscript] = useState("");

  const [sessionId, setSessionId] = useState("");
  const [repairing, setRepairing] = useState(false);
  const [repairedVideoUrl, setRepairedVideoUrl] = useState("");

  async function transcribeVideo() {
    if (!file) return;

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "http://127.0.0.1:8000/transcribe",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Transcription failed.");
      }

      const result = await response.json();

      setTranscript(result.text);
      setSessionId(result.session_id);
    } catch (error) {
      console.error(error);
      alert("Could not transcribe the video.");
    } finally {
      setLoading(false);
    }
  }

  async function repairVideo() {
    if (!sessionId || !transcript) return;

    setRepairing(true);

    try {
      const formData = new FormData();

      formData.append("session_id", sessionId);
      formData.append("edited_text", transcript);

      const response = await fetch(
        "http://127.0.0.1:8000/repair",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error("Repair failed.");
      }

      const videoBlob = await response.blob();

      const videoUrl = URL.createObjectURL(videoBlob);

      setRepairedVideoUrl(videoUrl);

    } catch (error) {
      console.error(error);
      alert("Could not repair the video.");
    } finally {
      setRepairing(false);
    }
  }

  return (
    <main className="min-h-screen bg-zinc-950 text-white">
      <div className="mx-auto flex min-h-screen max-w-4xl flex-col px-6 py-16">
        <header className="mb-12">
          <p className="mb-3 text-sm font-medium uppercase tracking-[0.25em] text-zinc-500">
            Speech Surgeon
          </p>

          <h1 className="max-w-2xl text-5xl font-semibold tracking-tight">
            Edit what you said
            <span className="text-zinc-500">
              {" "}
              without saying it again.
            </span>
          </h1>

          <p className="mt-5 max-w-xl text-lg leading-8 text-zinc-400">
            Upload a video, edit the words you said, and regenerate only the
            changed speech in your voice.
          </p>
        </header>

        <section className="rounded-2xl border border-zinc-800 bg-zinc-900/60 p-8">
          <h2 className="text-xl font-medium">
            Upload your video
          </h2>

          <p className="mt-2 text-sm text-zinc-500">
            MP4, MOV, or WebM
          </p>

          <label className="mt-6 flex cursor-pointer flex-col items-center justify-center rounded-xl border border-dashed border-zinc-700 bg-zinc-950 px-6 py-16 transition hover:border-zinc-500">
            <span className="text-sm font-medium">
              {file ? file.name : "Choose a video"}
            </span>

            <span className="mt-2 text-sm text-zinc-500">
              {file
                ? `${(file.size / 1024 / 1024).toFixed(2)} MB`
                : "or drag and drop it here"}
            </span>

            <input
              type="file"
              accept="video/mp4,video/quicktime,video/webm"
              className="hidden"
              onChange={(event) => {
                const selectedFile = event.target.files?.[0] ?? null;

                setFile(selectedFile);

                if (selectedFile) {
                  setOriginalVideoUrl(
                    URL.createObjectURL(selectedFile)
                  );
                }
              }}
            />
          </label>

          <button
            type="button"
            disabled={!file || loading}
            onClick={transcribeVideo}
            className="mt-6 w-full rounded-xl bg-white px-5 py-3 text-sm font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-30"
          >
            {loading ? "Transcribing..." : "Transcribe video"}
          </button>
        </section>

        {transcript && (
          <section className="mt-8 rounded-2xl border border-zinc-800 bg-zinc-900/60 p-8">
            <h2 className="text-xl font-medium">
              Transcript
            </h2>

            <textarea
              value={transcript}
              onChange={(event) => {
                setTranscript(event.target.value);
              }}
              className="mt-6 min-h-48 w-full resize-y rounded-xl border border-zinc-700 bg-zinc-950 p-5 text-sm leading-7 text-zinc-200 outline-none focus:border-zinc-500"
            />
            <button
              type="button"
              disabled={!sessionId || repairing}
              onClick={repairVideo}
              className="mt-4 w-full rounded-xl bg-white px-5 py-3 text-sm font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-30"
            >
              {repairing ? "Repairing video..." : "Repair video"}
            </button>
          </section>
        )}

        {repairedVideoUrl && (
          <section className="mt-8 rounded-2xl border border-zinc-800 bg-zinc-900/60 p-8">
            <h2 className="text-xl font-medium">
              Result
            </h2>

            <div className="mt-6 grid gap-6 md:grid-cols-2">
              {originalVideoUrl && (
                <div>
                  <p className="mb-3 text-sm font-medium text-zinc-400">
                    Original
                  </p>

                  <video
                    controls
                    src={originalVideoUrl}
                    className="w-full rounded-xl"
                  />
                </div>
              )}

              <div>
                <p className="mb-3 text-sm font-medium text-zinc-400">
                  Repaired
                </p>

                <video
                  controls
                  src={repairedVideoUrl}
                  className="w-full rounded-xl"
                />
              </div>
            </div>

            <p className="mt-6 text-sm text-zinc-500">
              Same video frames. Only the spoken audio was repaired.
            </p>
          </section>
        )}

        <footer className="mt-auto pt-12 text-sm text-zinc-600">
          Original video frames stay untouched. Only the audio changes.
        </footer>
      </div>
    </main>
  );
}