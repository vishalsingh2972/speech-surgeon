"use client";

import { useEffect, useState } from "react";
import confetti from "canvas-confetti";
import {
  ArrowLeft,
  Check,
  Download,
  FileVideo,
  Loader2,
  Pencil,
  Sparkles,
  Upload,
  WandSparkles,
} from "lucide-react";
import { motion, AnimatePresence } from "motion/react";
import { toast } from "sonner";

type Step = "upload" | "edit" | "repairing" | "result";

export default function Home() {
  const [step, setStep] = useState<Step>("upload");

  const [file, setFile] = useState<File | null>(null);
  const [originalVideoUrl, setOriginalVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [transcript, setTranscript] = useState("");

  const [sessionId, setSessionId] = useState("");
  const [repairedVideoUrl, setRepairedVideoUrl] = useState("");

  /*
   * Keep the original video URL alive until it is replaced
   * or the component actually unmounts.
   */
  useEffect(() => {
    return () => {
      if (originalVideoUrl) {
        URL.revokeObjectURL(originalVideoUrl);
      }
    };
  }, [originalVideoUrl]);

  /*
   * Keep the repaired video URL separate.
   * Changing the repaired URL must NOT revoke the original URL.
   */
  useEffect(() => {
    return () => {
      if (repairedVideoUrl) {
        URL.revokeObjectURL(repairedVideoUrl);
      }
    };
  }, [repairedVideoUrl]);

  function handleFileChange(
    event: React.ChangeEvent<HTMLInputElement>
  ) {
    const selectedFile = event.target.files?.[0] ?? null;

    if (!selectedFile) {
      return;
    }

    /*
     * Create the new preview URL first.
     */
    const newOriginalVideoUrl =
      URL.createObjectURL(selectedFile);

    /*
     * Revoke the old original URL.
     */
    if (originalVideoUrl) {
      URL.revokeObjectURL(originalVideoUrl);
    }

    /*
     * Revoke any previous repaired video URL.
     */
    if (repairedVideoUrl) {
      URL.revokeObjectURL(repairedVideoUrl);
    }

    setFile(selectedFile);
    setOriginalVideoUrl(newOriginalVideoUrl);

    setTranscript("");
    setSessionId("");
    setRepairedVideoUrl("");
    setLoading(false);
    setStep("upload");
  }

  async function transcribeVideo() {
    if (!file) {
      return;
    }

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
      setStep("edit");
    } catch (error) {
      console.error(error);

      toast.error("Could not transcribe the video.");
    } finally {
      setLoading(false);
    }
  }

  async function repairVideo() {
    if (!sessionId || !transcript) {
      return;
    }

    setStep("repairing");

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

      const videoUrl =
        URL.createObjectURL(videoBlob);

      setRepairedVideoUrl(videoUrl);
      setStep("result");

      confetti({
        particleCount: 140,
        spread: 90,
        origin: {
          y: 0.6,
        },
      });

      toast.success(
        "Your video has been repaired."
      );
    } catch (error) {
      console.error(error);

      toast.error(
        "Could not repair the video."
      );

      setStep("edit");
    }
  }

  function startOver() {
    if (originalVideoUrl) {
      URL.revokeObjectURL(originalVideoUrl);
    }

    if (repairedVideoUrl) {
      URL.revokeObjectURL(repairedVideoUrl);
    }

    setFile(null);
    setOriginalVideoUrl("");
    setTranscript("");
    setSessionId("");
    setRepairedVideoUrl("");
    setLoading(false);
    setStep("upload");
  }

  function downloadVideo() {
    if (!repairedVideoUrl) {
      return;
    }

    const link =
      document.createElement("a");

    link.href = repairedVideoUrl;
    link.download =
      "speech-surgeon-repaired.mp4";

    document.body.appendChild(link);

    link.click();

    link.remove();
  }

  const stepNumber =
    step === "upload"
      ? 1
      : step === "edit"
        ? 2
        : step === "repairing"
          ? 3
          : 4;

  return (
    <main className="min-h-screen overflow-hidden bg-zinc-950 text-white">
      <div className="relative mx-auto flex min-h-screen max-w-5xl flex-col px-6 py-10 sm:px-8 sm:py-14">

        <div className="pointer-events-none absolute left-1/2 top-0 -z-0 h-96 w-96 -translate-x-1/2 rounded-full bg-white/[0.035] blur-3xl" />

        {/* HEADER */}

        <header className="relative z-10 mb-10 text-center">

          <div className="mx-auto mb-5 flex w-fit items-center gap-2 rounded-full border border-zinc-800 bg-zinc-900/70 px-4 py-2 text-xs font-medium text-zinc-400">
            <Sparkles className="h-3.5 w-3.5" />
            Speech Surgeon
          </div>

          <h1 className="mx-auto max-w-3xl text-4xl font-semibold tracking-tight sm:text-6xl">
            Edit what you said

            <span className="block text-zinc-500">
              without saying it again.
            </span>
          </h1>

          <p className="mx-auto mt-5 max-w-2xl text-base leading-7 text-zinc-400 sm:text-lg">
            Change the words. Keep your voice. Keep your video.
          </p>

        </header>

        {/* PROGRESS */}

        <div className="relative z-10 mx-auto mb-10 flex w-full max-w-xl items-center justify-center">

          {[
            ["Upload", 1],
            ["Edit", 2],
            ["Repair", 3],
            ["Result", 4],
          ].map(([label, number], index) => {

            const active =
              stepNumber >= Number(number);

            return (
              <div
                key={label}
                className="flex flex-1 items-center"
              >

                <div className="flex flex-col items-center gap-2">

                  <div
                    className={[
                      "flex h-8 w-8 items-center justify-center rounded-full border text-xs font-semibold transition-all",
                      active
                        ? "border-white bg-white text-black"
                        : "border-zinc-800 bg-zinc-900 text-zinc-600",
                    ].join(" ")}
                  >
                    {stepNumber >
                    Number(number) ? (
                      <Check className="h-4 w-4" />
                    ) : (
                      number
                    )}
                  </div>

                  <span
                    className={[
                      "text-[11px] font-medium",
                      active
                        ? "text-zinc-300"
                        : "text-zinc-700",
                    ].join(" ")}
                  >
                    {label}
                  </span>

                </div>

                {index < 3 && (
                  <div
                    className={[
                      "mx-3 mb-5 h-px flex-1 transition-colors",
                      stepNumber >
                      Number(number)
                        ? "bg-zinc-500"
                        : "bg-zinc-800",
                    ].join(" ")}
                  />
                )}

              </div>
            );
          })}

        </div>

        {/* MAIN STEP CONTENT */}

        <div className="relative z-10 mx-auto w-full max-w-3xl">

          <AnimatePresence mode="wait">

            {/* STEP 1 */}

            {step === "upload" && (
              <motion.section
                key="upload"
                initial={{
                  opacity: 0,
                  y: 12,
                }}
                animate={{
                  opacity: 1,
                  y: 0,
                }}
                exit={{
                  opacity: 0,
                  y: -12,
                }}
                transition={{
                  duration: 0.25,
                }}
                className="rounded-3xl border border-zinc-800 bg-zinc-900/60 p-6 shadow-2xl shadow-black/20 sm:p-10"
              >

                <div className="mb-8">

                  <div className="mb-3 flex items-center gap-2 text-zinc-500">

                    <Upload className="h-4 w-4" />

                    <span className="text-xs font-medium uppercase tracking-[0.2em]">
                      Step 1
                    </span>

                  </div>

                  <h2 className="text-2xl font-semibold">
                    Upload your video
                  </h2>

                  <p className="mt-2 text-sm text-zinc-500">
                    MP4, MOV, or WebM
                  </p>

                </div>

                {!originalVideoUrl ? (

                  /* EMPTY UPLOAD STATE */

                  <label className="group flex min-h-72 cursor-pointer flex-col items-center justify-center rounded-2xl border border-dashed border-zinc-700 bg-zinc-950/70 px-6 transition-all hover:border-zinc-500 hover:bg-zinc-950">

                    <div className="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl border border-zinc-800 bg-zinc-900 transition-transform group-hover:scale-105">

                      <Upload className="h-6 w-6 text-zinc-500" />

                    </div>

                    <span className="text-sm font-medium text-zinc-200">
                      Choose a video
                    </span>

                    <span className="mt-2 text-sm text-zinc-600">
                      Click to browse your files
                    </span>

                    <input
                      type="file"
                      accept="video/mp4,video/quicktime,video/webm"
                      className="hidden"
                      onChange={handleFileChange}
                    />

                  </label>

                ) : (

                  /* VIDEO PREVIEW STATE */

                  <div className="overflow-hidden rounded-2xl border border-zinc-800 bg-zinc-950">

                    <div className="aspect-video bg-black">

                      <video
                        controls
                        playsInline
                        preload="metadata"
                        src={originalVideoUrl}
                        className="h-full w-full object-contain"
                      />

                    </div>

                    <div className="flex items-center justify-between gap-4 border-t border-zinc-800 px-4 py-3">

                      <div className="flex min-w-0 items-center gap-3">

                        <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg border border-zinc-800 bg-zinc-900">

                          <FileVideo className="h-4 w-4 text-zinc-400" />

                        </div>

                        <div className="min-w-0">

                          <p className="truncate text-sm font-medium text-zinc-200">
                            {file?.name}
                          </p>

                          <p className="mt-0.5 text-xs text-zinc-600">
                            {file
                              ? `${(
                                  file.size /
                                  1024 /
                                  1024
                                ).toFixed(2)} MB`
                              : "Original video"}
                          </p>

                        </div>

                      </div>

                      <label className="shrink-0 cursor-pointer rounded-lg border border-zinc-800 px-3 py-2 text-xs font-medium text-zinc-400 transition hover:border-zinc-600 hover:text-zinc-200">

                        Change video

                        <input
                          type="file"
                          accept="video/mp4,video/quicktime,video/webm"
                          className="hidden"
                          onChange={handleFileChange}
                        />

                      </label>

                    </div>

                  </div>

                )}

                <button
                  type="button"
                  disabled={!file || loading}
                  onClick={transcribeVideo}
                  className="mt-6 flex w-full items-center justify-center gap-2 rounded-xl bg-white px-5 py-3.5 text-sm font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-30"
                >

                  {loading ? (
                    <>
                      <Loader2 className="h-4 w-4 animate-spin" />
                      Transcribing...
                    </>
                  ) : (
                    <>
                      Transcribe video
                      <ArrowLeft className="h-4 w-4 rotate-180" />
                    </>
                  )}

                </button>

              </motion.section>
            )}

            {/* STEP 2 */}

            {step === "edit" && (
              <motion.section
                key="edit"
                initial={{
                  opacity: 0,
                  x: 20,
                }}
                animate={{
                  opacity: 1,
                  x: 0,
                }}
                exit={{
                  opacity: 0,
                  x: -20,
                }}
                transition={{
                  duration: 0.25,
                }}
                className="rounded-3xl border border-zinc-800 bg-zinc-900/60 p-6 shadow-2xl shadow-black/20 sm:p-10"
              >

                <div className="mb-8 flex items-start justify-between gap-6">

                  <div>

                    <div className="mb-3 flex items-center gap-2 text-zinc-500">

                      <Pencil className="h-4 w-4" />

                      <span className="text-xs font-medium uppercase tracking-[0.2em]">
                        Step 2
                      </span>

                    </div>

                    <h2 className="text-2xl font-semibold">
                      Edit what you said
                    </h2>

                    <p className="mt-2 text-sm text-zinc-500">
                      Change only the words you want repaired.
                    </p>

                  </div>

                  <button
                    type="button"
                    onClick={startOver}
                    className="flex shrink-0 items-center gap-2 rounded-lg border border-zinc-800 px-3 py-2 text-xs font-medium text-zinc-500 transition hover:border-zinc-600 hover:text-zinc-300"
                  >
                    <ArrowLeft className="h-3.5 w-3.5" />
                    Back
                  </button>

                </div>

                <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-2">

                  <textarea
                    value={transcript}
                    onChange={(event) => {
                      setTranscript(
                        event.target.value
                      );
                    }}
                    className="min-h-56 w-full resize-y rounded-xl bg-transparent p-5 text-sm leading-8 text-zinc-200 outline-none placeholder:text-zinc-700"
                    placeholder="Your transcript will appear here..."
                  />

                </div>

                <div className="mt-5 flex items-center gap-2 text-xs text-zinc-600">

                  <WandSparkles className="h-3.5 w-3.5" />

                  Your original video frames will stay untouched.

                </div>

                <button
                  type="button"
                  disabled={
                    !sessionId ||
                    !transcript
                  }
                  onClick={repairVideo}
                  className="mt-6 flex w-full items-center justify-center gap-2 rounded-xl bg-white px-5 py-3.5 text-sm font-semibold text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-30"
                >

                  <WandSparkles className="h-4 w-4" />

                  Repair video

                </button>

              </motion.section>
            )}

            {/* STEP 3 */}

            {step === "repairing" && (
              <motion.section
                key="repairing"
                initial={{
                  opacity: 0,
                  scale: 0.98,
                }}
                animate={{
                  opacity: 1,
                  scale: 1,
                }}
                exit={{
                  opacity: 0,
                  scale: 0.98,
                }}
                className="rounded-3xl border border-zinc-800 bg-zinc-900/60 px-6 py-20 text-center shadow-2xl shadow-black/20 sm:px-10"
              >

                <motion.div
                  animate={{
                    rotate: 360,
                  }}
                  transition={{
                    duration: 2,
                    repeat: Infinity,
                    ease: "linear",
                  }}
                  className="mx-auto flex h-16 w-16 items-center justify-center rounded-2xl border border-zinc-700 bg-zinc-950"
                >

                  <WandSparkles className="h-7 w-7 text-zinc-300" />

                </motion.div>

                <h2 className="mt-7 text-2xl font-semibold">
                  Repairing your speech
                </h2>

                <p className="mx-auto mt-3 max-w-md text-sm leading-6 text-zinc-500">
                  Generating the changed words in your voice and surgically
                  placing them back into the original audio.
                </p>

                <div className="mx-auto mt-8 h-1.5 max-w-xs overflow-hidden rounded-full bg-zinc-800">

                  <motion.div
                    className="h-full w-1/2 rounded-full bg-white"
                    animate={{
                      x: [
                        "-100%",
                        "200%",
                      ],
                    }}
                    transition={{
                      duration: 1.2,
                      repeat: Infinity,
                      ease: "easeInOut",
                    }}
                  />

                </div>

              </motion.section>
            )}

            {/* STEP 4 */}

            {step === "result" && (
              <motion.section
                key="result"
                initial={{
                  opacity: 0,
                  y: 20,
                }}
                animate={{
                  opacity: 1,
                  y: 0,
                }}
                transition={{
                  duration: 0.35,
                }}
                className="rounded-3xl border border-zinc-800 bg-zinc-900/60 p-6 shadow-2xl shadow-black/20 sm:p-10"
              >

                <div className="text-center">

                  <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-full border border-zinc-700 bg-white text-black">

                    <Check className="h-6 w-6" />

                  </div>

                  <h2 className="mt-5 text-2xl font-semibold">
                    Speech repaired
                  </h2>

                  <p className="mt-2 text-sm text-zinc-500">
                    Same video. New words. Your voice.
                  </p>

                </div>

                {/* VIDEO COMPARISON */}

                <div className="mt-8 grid gap-5 md:grid-cols-2">

                  {originalVideoUrl && (
                    <div className="rounded-2xl border border-zinc-800 bg-zinc-950 p-3">

                      <div className="mb-3 flex items-center justify-between px-1">

                        <span className="text-sm font-medium">
                          Original
                        </span>

                        <span className="text-xs text-zinc-600">
                          Before
                        </span>

                      </div>

                      <video
                        controls
                        preload="metadata"
                        playsInline
                        src={originalVideoUrl}
                        className="w-full rounded-xl"
                      />

                    </div>
                  )}

                  <div className="rounded-2xl border border-zinc-700 bg-zinc-950 p-3">

                    <div className="mb-3 flex items-center justify-between px-1">

                      <span className="text-sm font-medium">
                        Repaired
                      </span>

                      <span className="text-xs text-zinc-400">
                        After
                      </span>

                    </div>

                    <video
                      controls
                      preload="metadata"
                      playsInline
                      src={repairedVideoUrl}
                      className="w-full rounded-xl"
                    />

                  </div>

                </div>

                {/* EXPLANATION */}

                <div className="mt-6 rounded-xl border border-zinc-800 bg-zinc-950/60 p-4 text-center">

                  <p className="text-xs text-zinc-500">
                    Original video frames stay untouched.
                  </p>

                  <p className="mt-1 text-xs text-zinc-600">
                    Only the spoken audio was surgically repaired.
                  </p>

                </div>

                {/* ACTIONS */}

                <div className="mt-6 grid gap-3 sm:grid-cols-2">

                  <button
                    type="button"
                    onClick={downloadVideo}
                    className="flex items-center justify-center gap-2 rounded-xl bg-white px-5 py-3.5 text-sm font-semibold text-black transition hover:bg-zinc-200"
                  >

                    <Download className="h-4 w-4" />

                    Download repaired video

                  </button>

                  <button
                    type="button"
                    onClick={startOver}
                    className="flex items-center justify-center gap-2 rounded-xl border border-zinc-700 px-5 py-3.5 text-sm font-semibold text-zinc-200 transition hover:border-zinc-500 hover:bg-zinc-900"
                  >

                    <ArrowLeft className="h-4 w-4" />

                    Start another video

                  </button>

                </div>

              </motion.section>
            )}

          </AnimatePresence>

        </div>

        <footer className="relative z-10 mt-auto pt-10 text-center text-xs text-zinc-700">
          Speech Surgeon · Edit what you said without saying it again.
        </footer>

      </div>
    </main>
  );
}