# 🩹 Speech Surgeon

> **Edit what you said without saying it again.**

Speech Surgeon is an AI-powered speech repair tool for existing videos.

Upload a recorded video, edit the words in its transcript, and Speech Surgeon regenerates **only the changed speech in the original speaker's voice**, surgically replaces that portion of the audio, and attaches the repaired audio back to the **original video frames**.

**No complete rerecording.  
No video regeneration.  
Just repair the words that changed.**

---

## 🎯 The Idea

Recorded video is expensive to recreate, but information changes constantly.

The video may still be good. The performance may still be good. The visuals may still be good.

**Only a few words are wrong.**

For example:

```text
"We launched the first version in March."
                    ↓
"We launched the first version in June."
```

```text
"three thousand users"
        ↓
"five thousand users"
```

```text
"Build for India Hackathon"
              ↓
"We Make Devs Hackathon"
```

Normally, fixing this means reopening the project, finding the section, recording the line again, trying to match the original voice and delivery, replacing the audio, and exporting the video again.

Speech Surgeon takes a different approach:

```text
Existing video
      ↓
Transcribe
      ↓
Edit the words
      ↓
Detect what changed
      ↓
Generate replacement speech
      ↓
Patch the original audio
      ↓
Keep the original video
```

> **The goal isn't to generate another video.  
> The goal is to repair the one you already have.**

---

## ⚡ What Speech Surgeon Does

```text
🎥 Upload video
       ↓
📝 Fish Audio transcribes the speech
       ↓
✏️ Edit the transcript
       ↓
🔍 Detect the changed sentence
       ↓
🐟 Fish Audio generates replacement speech using a voice reference
       ↓
✂️ FFmpeg replaces the affected audio region
       ↓
🎬 Preserve the original video stream
       ↓
✨ Download the repaired video
```

### One video. One small correction. No rerecording.

---

## 🎯 Who It's For

Speech Surgeon is initially built for people who maintain recorded video that becomes outdated when a few spoken details change.

### 1. Creators

YouTubers, podcasters, reviewers, influencers, and independent creators who maintain videos over time.

Useful for changing:

- Dates
- Statistics
- Prices
- Product names
- Software versions
- Sponsors and partner names
- Links or references
- Outdated facts
- Episode numbers

**Example:** A tutorial recorded in 2025 says, “This works in version 3.” The software becomes version 4. Speech Surgeon aims to make the correction a transcript edit instead of a full rerecording.

```text
Version 3 → Version 4
```

### 2. Educators & Course Creators

Online courses and educational libraries can remain useful for years, while small details constantly change.

Examples include academic years, software and API versions, course dates, syllabus details, terminology, assignment deadlines, exam information, statistics, and tool names.

**Example:** An educator has 50 existing videos containing “This course is updated for 2025.”

```text
2025 → 2026
```

The lesson may still be correct. Updating the spoken year across a library is a potential future bulk workflow; the current MVP repairs one uploaded video at a time.

### 3. Companies & Teams

Companies constantly update products, features, pricing, launch dates, customer numbers, internal processes, employee roles, product terminology, sales messaging, and training material.

Potential uses include product demos, SaaS tutorials, onboarding, internal training, sales videos, marketing videos, documentation, announcements, and customer education.

**Example:**

```text
"The Pro plan costs $29."
              ↓
"The Pro plan costs $39."
```

The product demo and visuals may remain useful even after the price changes.

---

## 🌎 Where Else It Can Be Useful

The same problem appears anywhere organizations maintain libraries of recorded speech.

### Content & Media
- YouTube videos and podcasts
- Interviews and explainers
- Documentaries and commentary
- Social media content
- Product reviews

### Education
- Online courses and university lectures
- Tutorials and certification training
- Recurring educational programs
- Yearly course updates
- Software training

### Startups & SaaS
- Launch videos and product demos
- Feature announcements
- Onboarding and documentation
- Customer education
- Release videos and company updates

### Marketing & Advertising
- Campaigns and promotional videos
- Product messaging
- Seasonal campaigns
- Pricing, offer, sponsor, or partner changes

### Sales
- Reusable sales videos
- Personalized introductions
- Product demonstrations
- Customer-specific messaging

### Hackathons, Applications & Competitions

Record one polished application video, then adapt the spoken event name for different opportunities.

```text
"Build for India Hackathon"
              ↓
"We Make Devs Hackathon"
```

This is a particularly practical use case for reusing an application video without recording the entire presentation again.

### Other Potential Areas
- Internal company onboarding and training
- Event announcements, webinars, and workshops
- Real-estate listings and price updates
- Travel and hospitality information
- Financial education and recurring reports
- Healthcare and life-sciences education
- Government and public-information videos
- Manufacturing and industrial training
- Automotive demonstrations and service instructions
- Construction and engineering updates
- Sports, fitness, gaming, and esports content
- Recruitment and HR videos
- Legal and compliance training

These are potential applications of the idea, not claims that the current prototype has been validated for every industry.

---

## 🧠 The Common Pattern

```text
Most of the video is still correct
              +
A small part of the spoken content changed
              ↓
Traditional workflow: edit / rerecord / export
```

Speech Surgeon aims for:

```text
Most of the video is still correct
              +
A small part of the spoken content changed
              ↓
       Detect the change
              ↓
   Generate replacement speech
              ↓
        Patch the audio
              ↓
       Keep the video stream
```

That is the product.

---

## 🔥 Why This Is Different

Many AI video systems start with a prompt or script and generate a new video.

Speech Surgeon starts with existing footage, identifies what changed in the transcript, generates replacement speech, and patches the audio while preserving the original video stream.

> **Don't regenerate what is already right.**

---

## 💰 Cost Comparison: Manual Fix vs. Speech Surgeon

The main economic opportunity is reducing the time and coordination involved in correcting small pieces of spoken content. Exact savings depend on the length of the change, API pricing, number of attempts, editing rates, and how much review is required.

The figures below are **illustrative estimates, not guaranteed quotes or measured benchmarks**. Check provider pricing and local freelance rates before using these numbers in a business case.

### 📐 Example Scenario

```text
Video length:        5 minutes
What changed:        one short sentence
Example:             "in March" → "in June"
```

### 🧑‍🔧 Manual Workflow

| Method | Illustrative cost | Typical effort | What it involves |
|---|---:|---|---|
| Do it yourself | $0 cash, plus the value of your time | About 1–2 hours in this example | Find the section, rerecord, match tone and room sound, replace audio, export |
| Freelance editor | Highly variable; potentially tens to hundreds of dollars | Hours to days, depending on availability | Supply replacement audio, have the editor patch and export |
| Editor plus voice talent | Higher and dependent on session minimums | Hours to days | Arrange a pickup recording, then edit and export |
| Full reshoot | Can be substantially more expensive | Days or longer | Recreate the performance and any affected visuals |

Actual costs vary significantly by region, project complexity, revision policy, and whether the original speaker can record a pickup.

### ⚡ Speech Surgeon Workflow

| Step | Cost profile |
|---|---|
| Fish Audio transcription | Depends on audio duration and current ASR pricing |
| Fish Audio S2.1 Pro replacement speech | Depends on generated text, current model pricing, and number of attempts |
| FFmpeg audio surgery and video remux | No per-use AI API fee; runs locally |
| Human review | Your time to check pronunciation, timing, and quality |

**Total API cost:** Calculate using the current Fish Audio pricing page and the actual number of requests made by your workflow. The exact cost depends on current rates and retries.

**Total practical cost:** API usage plus your time reviewing and approving the repaired video.

### 📚 Updating a Video Library

For a library of 50 videos that need a small update, the potential benefit is avoiding repeated recording and editing work. The current MVP processes an uploaded video at a time; automated bulk scanning and batch repair are future possibilities.

| Method | Main cost driver |
|---|---|
| DIY rerecording | Repeated recording and editing time |
| Freelance editor | Per-video editing and revision fees |
| Speech Surgeon prototype | Per-video AI usage plus review time |

Avoid treating projected savings as measured results until a representative batch has been tested.

### ⚠️ Honest Cost Notes

- Editor costs and operator time vary widely.
- Fish Audio pricing can change; use the provider's current pricing rather than treating any estimate as permanent.
- Generated speech may require multiple attempts.
- The MVP needs human listening and review.
- The current repair process replaces a sentence-sized region, so timing and delivery may differ from the original.
- The current project does not include automated bulk library processing.

**Pricing reference:** [Fish Audio model pricing and rate limits](https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits).

---

## 🛠️ What I Actually Built

The current MVP is a working local end-to-end prototype.

### Input

A short video containing speech.

```text
video.mp4
    ↓
FFmpeg extracts audio
    ↓
Fish Audio transcribes speech
```

### 1. Transcribe

Speech Surgeon extracts audio with FFmpeg and sends it to **Fish Audio ASR**.

The transcription response includes timestamped segments, which the frontend uses to present the transcript for editing.

Example:

```text
[00:00 → 00:04]
I built a small project called Speech Surgeon.

[00:04 → 00:10]
We launched the first version in March, and more than
three thousand people tried it during the first week.

[00:10 → 00:14]
We're now preparing the next version for September.
```

Exact segments and timestamps depend on the uploaded recording and the ASR response.

### 2. Edit

The transcript is editable in the browser.

Original:

```text
We launched the first version in March,
and more than three thousand people tried it
during the first week.
```

Edited:

```text
We launched the first version in June,
and more than five thousand people tried it
during the first week.
```

The user edits the words rather than rerecording the entire video.

### 3. Detect the Change

Speech Surgeon compares the original and edited transcript to identify differences, then locates the sentence to repair.

```text
Original: "March ... three thousand"
                   ↓
                 DIFF
                   ↓
Edited:   "June ... five thousand"
```

The current implementation focuses on sentence-level changes rather than arbitrary word- or phoneme-level replacement.

### 4. Generate Replacement Speech with Fish Audio

The original recording provides reference audio and its corresponding transcript.

**Fish Audio S2.1 Pro** generates the edited sentence using that reference.

```text
Original voice reference + edited sentence
                    ↓
               Fish Audio
                    ↓
          Replacement speech audio
```

This is replacement-audio generation, not video generation. Voice similarity and delivery can vary, so the result should be reviewed.

### 5. Surgically Repair the Audio

The original audio is split into three pieces:

```text
┌────────────────┬──────────────────────┬────────────────┐
│ Original audio │ Generated replacement│ Original audio │
│ before change  │       speech         │ after change   │
└────────────────┴──────────────────────┴────────────────┘
```

The current pipeline:

1. Keeps the original audio before the target region.
2. Inserts the generated replacement speech.
3. Keeps the original audio after the target region.
4. Normalizes the replacement to a compatible audio format.
5. Concatenates the pieces into repaired audio.

This is a straightforward first implementation. It does not yet provide advanced duration matching, phoneme-aware transitions, or automatic crossfades.

### 6. Preserve the Original Video

Speech Surgeon does **not** regenerate the video during the core repair workflow.

```text
Original video
      │
      ├── original video stream ──────────┐
      │                                   │
      └── original audio → repaired audio ┤
                                          ↓
                                    Repaired MP4
```

The video stream is copied rather than re-encoded when the repaired audio is remuxed.

The original camera footage, screen recording, B-roll, framing, lighting, gestures, and visual composition are preserved by the core workflow.

> **Only the audio track is repaired in the core pipeline.**

---

## 🎬 The Core Demo

Original:

> “We launched the first version in March, and more than three thousand people tried it during the first week.”

Edit the transcript:

```text
March           → June
three thousand → five thousand
```

Repaired result:

> “We launched the first version in June, and more than five thousand people tried it during the first week.”

The demo shows the central idea:

> **Change the words. Keep the recording.**

---

## 🧪 Real Prototype Example

The system has also been tested on an application video.

Original:

> “This is my application for the Build for India Hackathon. I am building Chhotu.”

Edited:

> “This is my application for the We Make Devs Hackathon. I am building Chhotu.”

The prototype transcribed the recording, allowed the text to be changed, generated replacement speech, patched the affected audio, and exported a video using the original video stream.

This demonstrates a practical scenario: reusing one polished application video for different opportunities without rerecording the full presentation.

---

## 🧩 MVP Architecture

```text
                    ┌──────────────────────┐
                    │      Next.js UI      │
                    │ Upload → Edit →      │
                    │ Repair → Result      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                 ▼             ▼             ▼
          ┌────────────┐ ┌────────────┐ ┌────────────┐
          │   FFmpeg   │ │ Fish Audio │ │  Session   │
          │            │ │            │ │  Storage   │
          │ Extract    │ │ ASR        │ │            │
          │ Splice     │ │ S2.1 Pro   │ │ In-memory  │
          │ Remux      │ │ Voice ref  │ │ sessions   │
          └─────┬──────┘ └─────┬──────┘ └────────────┘
                │              │
                └──────┬───────┘
                       ▼
                ┌──────────────┐
                │ Repaired MP4 │
                │ Original     │
                │ video stream │
                │ + repaired   │
                │ audio        │
                └──────────────┘
```

The core speech workflow uses **Fish Audio and local FFmpeg processing**. It does not depend on a second AI provider for speech repair.

---

## 🔄 End-to-End Flow

```text
Video Upload
     ↓
Extract Audio with FFmpeg
     ↓
Fish Audio ASR
     ↓
Timestamped Transcript
     ↓
User Edits Text
     ↓
Detect Changed Sentence
     ↓
Locate Original Time Region
     ↓
Fish Audio S2.1 Pro
     ↓
Generate Replacement Speech
     ↓
Split Original Audio
     ↓
Insert Audio Patch
     ↓
Reassemble Repaired Audio
     ↓
Attach Audio to Original Video
     ↓
Export Repaired MP4
```

---

## 🐟 Why Fish Audio?

Fish Audio is the speech AI provider used in the current core implementation.

### 1. Understand what was said

Fish Audio ASR converts the recording into a transcript and returns timing information that supports the editing workflow.

### 2. Generate replacement speech

Fish Audio S2.1 Pro uses reference audio and its transcript to generate replacement speech in a voice resembling the original speaker.

The product-level distinction is:

```text
Fish Audio
     ↓
Speech recognition + replacement speech generation

Speech Surgeon
     ↓
Transcript editing + diff + audio surgery
+ video-stream preservation
```

Speech Surgeon focuses on the editing and repair workflow built around those speech capabilities.

---

## ✂️ Audio Surgery

The MVP uses a deliberately simple and understandable repair pipeline.

For example, a detected target region might be:

```text
target_start = 4.32s
target_end   = 10.08s
```

The original audio is divided conceptually into:

```text
0.00s ─────── target_start
                    │
                    ▼
             changed sentence
                    │
                    ▼
0.00s ── before + replacement + after ── end
```

The generated replacement is normalized to a compatible format before concatenation.

This is the first surgical implementation. More advanced timing, mixing, and boundary refinement remain future work.

---

## 🎥 Video Handling

Speech Surgeon intentionally avoids regenerating the original footage.

```text
Original video stream
+
Repaired audio stream
        ↓
Final MP4
```

The core FFmpeg workflow copies the video stream using:

```bash
-c:v copy
```

This avoids re-encoding the video stream during the audio-repair remux. The audio is encoded for the output container.

> **Repair what was said while preserving the video that was already recorded.**

---

## 🎯 MVP Scope

### What Works Today

- Video upload through the frontend
- MP4 / MOV / WebM upload flow
- Audio extraction with FFmpeg
- Fish Audio speech-to-text
- Timestamped transcript segments
- Editable transcript
- Sentence-level change detection
- Locating the changed sentence in the original recording
- Fish Audio S2.1 Pro speech generation
- Reference-audio voice generation
- Original-audio segmentation
- Replacement audio generation
- Audio format normalization
- Repaired audio reconstruction
- Original video stream preservation in the core repair path
- Repaired MP4 export
- Original and repaired video comparison
- Video download
- In-memory session handling
- FastAPI backend
- Next.js frontend

---

## 🚧 Current Limitations

Speech Surgeon is a working local MVP, not a production media platform.

### Sentence-Level Editing

The current diff and repair flow primarily operates at sentence level. It does not yet replace arbitrary individual words or phonemes.

### Timing

Generated speech may be longer or shorter than the original sentence. Advanced duration matching is not yet implemented.

### Audio Matching

The MVP does not yet perform sophisticated room-tone reconstruction, prosody matching, loudness matching, phoneme-aware transitions, automatic crossfades, or boundary refinement.

### Single-Speaker Focus

The workflow is primarily designed for short, relatively clean, single-speaker recordings.

### Temporary Sessions

Session data is stored in memory. Restarting the backend clears active sessions.

### Local Prototype

The current project does not yet include authentication, persistent databases, cloud storage, background job queues, distributed processing, production monitoring, enterprise permissions, or production-scale media processing.

---

## 🗺️ Roadmap

### Now — Sentence-Level Speech Repair

The MVP demonstrates the complete core loop:

```text
Upload → Transcribe → Edit → Detect
       → Generate → Splice → Preserve video
```

### Next — Finer-Grained Editing

Move from sentence-level repair toward:

- Phrase-level editing
- Word-level editing
- Improved timing
- Automatic duration fitting
- Better boundary detection
- Improved audio matching
- Smoother transitions

For example, changing “I launched in March” to “I launched in June” could eventually replace only the affected words rather than regenerating the full sentence.

### Later — Video Content Maintenance

The repair engine could evolve into a system for maintaining large video libraries.

Potential capabilities:

- Multi-speaker repair
- Bulk updates
- Reusable voice references
- Automatic content scanning
- Transcript-based search
- Affected-video detection
- Automatic update suggestions
- Version history
- Approval workflows

Bulk library scanning and batch repair are future ideas, not current MVP features.

### Long-Term Vision

> **Git for spoken video.**

Traditional software has source, diff, patch, version, and rollback.

Speech Surgeon could eventually bring a similar model to recorded speech:

```text
Original recording
       ↓
Transcript
       ↓
Text diff
       ↓
Audio patch
       ↓
New video version
```

Instead of thinking, “I need to make another video,” the user could think:

> **“I just need to patch the part that changed.”**

---

## 🧠 Why Sentence-Level Surgery First?

Reliable word- or phoneme-level editing requires solving difficult problems:

- Exact word timing
- Phoneme boundaries
- Coarticulation
- Silence placement
- Duration differences
- Prosody
- Transition matching
- Background sound continuity

Sentence-level surgery provides a cleaner first milestone. It proves the core loop:

> **Understand → Edit → Generate → Splice → Preserve**

Once that works reliably, the repair unit can become smaller:

```text
Sentence
   ↓
Phrase
   ↓
Word
   ↓
Phoneme
```

---

## 🏗️ Backend

The backend is built with **FastAPI**.

### `GET /`

Health/root endpoint.

### `POST /transcribe`

Accepts the uploaded video, extracts audio, runs Fish Audio transcription, creates a session, and returns the session ID, transcript, timestamped segments, and speaker information when available.

### `POST /repair`

Accepts the session and edited transcript. The endpoint detects the change, locates the affected region, generates replacement speech with Fish Audio, repairs the audio, attaches the repaired audio to the original video stream, and returns the repaired MP4.

The core `/repair` flow uses Fish Audio for speech tasks and FFmpeg for media processing.

---

## 🖥️ Frontend

The frontend is built around a simple workflow:

```text
UPLOAD
   ↓
EDIT
   ↓
REPAIRING
   ↓
RESULT
```

The result experience provides:

- Original video preview
- Repaired video preview
- Original-versus-repaired comparison
- Download of the repaired video
- Start-another-video flow

The UI is designed around the main product moment:

> **“I changed the words, and the recording fixed itself.”**

---

## 📁 Project Structure

```text
speech-surgeon/
│
├── backend/
│   ├── diff.py
│   ├── main.py
│   ├── session.py
│   ├── surgery.py
│   └── video.py
│
├── frontend/
│   ├── app/
│   │   ├── favicon.ico
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   │
│   ├── components/
│   │   └── ui/
│   │       └── button.tsx
│   │
│   ├── lib/
│   │   └── utils.ts
│   ├── public/
│   ├── package.json
│   └── ...
│
├── scripts/
│   ├── detect_changes.py
│   ├── find_target.py
│   ├── generate_replacement.py
│   ├── plan_surgery.py
│   ├── run_surgery.py
│   ├── surgery.py
│   ├── test_transcribe.py
│   └── test_voice_clone.py
│
├── samples/
│   ├── original.wav
│   └── test-video.mp4
│
├── .gitignore
└── README.md
```

The `scripts/` directory contains development and experimentation utilities created while building the prototype. Keep personal recordings and generated samples out of a public repository unless you intentionally want to publish them.

---

## 🧰 Technology Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- Motion
- Lucide React
- Sonner
- canvas-confetti

### Backend
- Python
- FastAPI
- Uvicorn
- Requests
- python-dotenv

### Speech AI
- **Fish Audio ASR** — transcription
- **Fish Audio S2.1 Pro** — replacement speech generation
- **Reference-audio voice generation** — conditioning generated speech on a voice sample and transcript

### Media Processing
- FFmpeg
- WAV / PCM intermediate audio
- MP4 output

---

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd speech-surgeon
```

### 2. Create the Python environment

On Windows Git Bash:

```bash
python -m venv backend/.venv
source backend/.venv/Scripts/activate
```

Install backend dependencies:

```bash
python -m pip install -U pip
pip install fastapi uvicorn python-multipart requests python-dotenv fish-audio-sdk
```

Make sure FFmpeg is installed and available on your `PATH`.

### 3. Add the Fish Audio API key

Create a `.env` file in the project root:

```env
FISH_API_KEY=your_fish_audio_api_key
```

Keep your API key private and never commit `.env` to the repository.

### 4. Start the backend

From the repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

Backend:

```text
http://127.0.0.1:8000
```

### 5. Start the frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:3000
```

---

## 🎬 Demo Walkthrough

The strongest demo is deliberately simple.

### 1. Record

Record a short video containing a date, number, product name, event name, or another detail that can change.

For example:

> “We launched the first version in March and more than three thousand people tried it.”

### 2. Upload

Speech Surgeon extracts the audio and transcribes the video using Fish Audio.

### 3. Edit

Change:

```text
March → June
three thousand → five thousand
```

### 4. Repair

Speech Surgeon detects the change, finds the affected sentence, generates replacement speech using Fish Audio, splices it into the original audio, and attaches the repaired audio to the original video stream.

### 5. Compare

Play the original and repaired videos side by side. The visual footage is preserved in the core workflow, while the spoken content changes.

---

## 🔬 What This Project Is Trying to Prove

Speech Surgeon isn't primarily trying to prove that AI can generate a video.

The interesting question is:

> **Can AI understand an existing recording well enough to make a small spoken correction without rebuilding everything around it?**

The prototype demonstrates that loop:

```text
Human recording
      ↓
Speech recognition
      ↓
Editable transcript
      ↓
Human text correction
      ↓
Changed-region detection
      ↓
Voice-preserving speech generation
      ↓
Audio patch
      ↓
Original video stream preserved
```

That is the core technical idea.

---

## 🧩 The Core Insight

A recorded video contains valuable information:

- Facial performance
- Gestures
- Screen recordings
- B-roll
- Camera framing
- Lighting
- Background
- Editing
- Composition
- Pacing

If only one sentence changed, throwing all of that away is unnecessary.

```text
Existing video
      ↓
    AUDIO
      ↓
    repair
      ↓
Existing video + repaired speech
```

> **A video doesn't need to be regenerated just because a sentence changed.**

---

## 🔐 Safety, Consent & Voice Ownership

Voice cloning should only be used responsibly.

Speech Surgeon should be used with your own voice, a voice you have explicit permission to use, or recordings where you have the right to generate derivative speech.

It should not be used to impersonate someone without permission or create deceptive statements attributed to another person.

A production version should include stronger controls around voice ownership, consent, identity verification, generated-content disclosure, audit trails, and abuse prevention.

---

## 🔒 Privacy

The current prototype is local and intentionally simple. Session state is stored in memory by the running backend, while speech processing uses the configured Fish Audio service.

For a future hosted version, privacy should be a first-class requirement. Potential safeguards include encrypted uploads, automatic deletion, explicit retention controls, private object storage, access controls, audit logs, user-controlled voice references, and clear third-party AI processing disclosures.

Do not upload sensitive recordings unless you understand and accept the provider's processing and retention terms.

---

## 📊 Current Status

### MVP Complete — Working Prototype

Speech Surgeon demonstrates the end-to-end workflow:

```text
Upload video
     ↓
Extract audio
     ↓
Fish Audio transcription
     ↓
Edit transcript
     ↓
Detect changed sentence
     ↓
Generate replacement speech with Fish Audio
     ↓
Surgically replace audio
     ↓
Attach repaired audio to original video stream
     ↓
Compare original vs. repaired
     ↓
Download result
```

The workflow has been tested on scripted product-demo content, separate recordings with different content, and a real hackathon/application video where the event name was changed without rerecording the full video.

The project is best described as:

> **A working MVP for surgical speech editing in existing videos.**

---

## 💡 Product Philosophy

> **Keep what is correct. Repair what changed.**

```text
Don't regenerate the background.
Don't regenerate the screen recording.
Don't regenerate the entire timeline.

Repair the speech.
```

---

## 🚀 Future Product Vision

The immediate product is simple:

> **Change what you said without saying it again.**

The larger opportunity is video maintenance. Imagine an organization with thousands of recorded videos. A product changes, a price changes, a software version changes, a policy changes, or a date changes.

A future system could search a video library, find outdated information, identify affected recordings, generate speech patches, and create updated versions.

```text
Video library
      ↓
Transcripts
      ↓
Detect outdated information
      ↓
Find affected recordings
      ↓
Generate speech patches
      ↓
Create updated versions
```

Eventually, recorded video could be maintained rather than becoming permanently outdated after publication.

---

## 🧭 Roadmap at a Glance

```text
TODAY
Sentence-level speech repair
        ↓
NEXT
Phrase / word-level editing
        ↓
THEN
Better timing + audio matching
        ↓
LATER
Multi-speaker + bulk updates
        ↓
LONG TERM
Maintain entire video libraries
```

The long-term vision:

> **Git for spoken video.**

---

## ⭐ One-Line Pitch

> **Speech Surgeon lets you change what you said in an existing video without saying it again.**

## 🎤 Short Demo Pitch

> Speech Surgeon is an AI speech repair tool for existing videos. You upload a video, edit the transcript, and it detects what changed, regenerates that speech in a voice based on the original recording, surgically patches the audio, and preserves the original video stream.

---

## 🏁 Built With

- **Fish Audio** — speech recognition and replacement speech generation
- **FFmpeg** — audio extraction, normalization, audio surgery, and video remuxing
- **FastAPI** — backend API
- **Next.js** — frontend
- **React / TypeScript** — application UI

---

## 📄 License

MIT License