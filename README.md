# Speech Surgeon

> **Edit what you said without saying it again.**

Speech Surgeon is an AI-powered audio repair tool for already-recorded videos.

Upload a video.
Get the transcript.
Change the words you want.
Speech Surgeon regenerates **only the changed speech in the original speaker's voice**, surgically replaces that section of audio, and attaches the repaired audio back to the **original video frames**.

No video regeneration.
No complete rerecording.
No rebuilding the timeline just because one sentence changed.

---

## What Is Speech Surgeon?

Imagine recording a video today and realizing tomorrow that you said:

> "Our first version launched in March."

But you actually need:

> "Our first version launched in June."

Normally, you have to reopen the project, find the right section, rerecord the sentence, clean it up, match the timing, replace the audio, and export the video again.

Speech Surgeon turns that into:

**Edit the text → generate the new sentence → splice it into the original audio → export.**

The core idea is simple:

> **Treat spoken words as an editable layer instead of treating the entire video as disposable.**

---

# The Problem

A lot of recorded video becomes outdated because of tiny changes.

The video itself may still be perfectly good.

Only a few words are wrong.

Examples:

* "March" became "June"
* "2025" became "2026"
* "three thousand users" became "five thousand users"
* "Build for India Hackathon" became "We Make Devs Hackathon"
* "Version 1.0" became "Version 2.0"
* "Friday" became "Monday"
* "Product A" became "Product B"
* an old feature name needs to be corrected
* a pricing figure changed
* a launch date moved
* a company or event name changed
* a sponsor or partner name changed
* a speaker's title changed

The visual footage may still be completely usable.

The problem is the **voice track**.

Today, fixing that small mistake often means manually editing audio or recording the whole section again.

Current product-demo and training workflows describe the same maintenance problem: products, interfaces, processes, pricing, terminology, and messaging change, while previously recorded videos remain in circulation.

Speech Surgeon is built around the opposite idea:

> **Keep everything that is still correct. Repair only what changed.**

---

# What I Actually Built

This is the most important part of the project.

The current MVP is a working local end-to-end prototype.

### Input

A short video containing speech.

Example:

```text
video.mp4
    ↓
audio extracted from the video
```

### Step 1 — Transcribe the original audio

Speech Surgeon extracts the audio using FFmpeg and sends it to Fish Audio speech-to-text.

The transcription includes timestamps.

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

---

### Step 2 — Edit the transcript

The user edits the transcript directly in the browser.

Original:

```text
We launched the first version in March,
and more than three thousand people tried it
during the first week.
```

Changed to:

```text
We launched the first version in June,
and more than five thousand people tried it
during the first week.
```

The user does **not** need to rerecord anything.

---

### Step 3 — Detect what changed

Speech Surgeon compares the original transcript with the edited transcript.

It identifies the changed sentence/region instead of regenerating the entire recording.

Conceptually:

```text
Original sentence
        ↓
"March ... three thousand"
        ↓
        DIFF
        ↓
"June ... five thousand"
```

The current MVP works at the **sentence level**.

Word-level surgery is part of the future evolution.

---

### Step 4 — Generate replacement speech

The original recording is used as a voice reference.

Fish Audio S2.1 Pro generates only the edited sentence in the same speaker identity.

Conceptually:

```text
Original voice recording
        +
New text
        ↓
Fish Audio voice cloning / TTS
        ↓
Replacement speech
```

Speech Surgeon is not generating a new video.

It is generating a new **audio patch**.

Fish Audio currently provides voice cloning from reference audio through its S2.1 Pro system, which is exactly the capability this prototype uses.

---

### Step 5 — Surgically repair the audio

The original audio is split into three pieces:

```text
┌───────────────┬──────────────────────┬───────────────┐
│ Original      │ New generated speech │ Original      │
│ audio         │                      │ audio         │
└───────────────┴──────────────────────┴───────────────┘
```

More precisely:

```text
Original audio
     │
     ├── before changed region
     │
     ├── generated replacement speech
     │
     └── after changed region
```

The three pieces are concatenated into a repaired audio track.

The MVP normalizes the generated patch to a consistent 48 kHz stereo PCM format before concatenation.

---

### Step 6 — Put the repaired audio back onto the original video

This is a critical design decision.

Speech Surgeon does **not** regenerate the video.

The original video stream is reused and only the audio stream is replaced.

The backend effectively does:

```text
Original video ────────────────┐
                               │
Original audio → repaired audio│
                               ↓
                        Repaired MP4
```

The video stream is copied with FFmpeg rather than re-encoded.

That means:

> **The original video frames stay untouched.**

Your screen recording, camera footage, B-roll, composition, background, and visual identity are preserved.

---

# The Demo in One Sentence

The entire product can be explained as:

> **Upload a video → edit what you said → Speech Surgeon replaces only that speech in your voice → the original video stays the same.**

---

# A Real Example

One of the prototype tests used this recording:

### Original

> "This is my application for the Build for India Hackathon. I am building Chhotu."

The transcript was edited to:

### Edited

> "This is my application for the We Make Devs Hackathon. I am building Chhotu."

Speech Surgeon then:

1. detected the changed sentence,
2. generated replacement speech,
3. surgically replaced that portion of the original audio,
4. kept the original video frames,
5. exported the repaired video.

This demonstrates the actual product idea beyond the initial scripted demo.

---

# Why This Is Useful

The interesting part is not simply "AI can clone a voice."

The interesting part is:

> **A tiny text change can produce a tiny audio change instead of forcing a complete recording workflow.**

That opens up a much larger set of practical use cases.

---

# Real-World Use Cases

## 1. YouTubers and video creators

A creator records a tutorial, review, explainer, or commentary video.

Months later, one detail becomes outdated.

Examples:

```text
"2025"
→
"2026"
```

```text
"Twitter"
→
"X"
```

```text
"Version 3"
→
"Version 4"
```

```text
"three million views"
→
"five million views"
```

Instead of recreating the video, the creator can repair the spoken line.

This is especially useful for evergreen videos, tutorials, explainers, software reviews, and educational content.

The broader creator ecosystem is already moving toward AI-assisted editing workflows because manually assembling and revising video remains a significant part of the production burden.

---

## 2. Annual / yearly videos

This is one of the simplest and strongest use cases.

Imagine an educator, creator, company, or founder has 50 videos where they say:

> "This course is updated for 2025."

Next year, they need:

> "This course is updated for 2026."

The video itself may still be completely correct.

Why rerecord 50 videos for one number?

Speech Surgeon is designed for exactly this kind of localized correction.

---

## 3. Online educators and course creators

Courses accumulate outdated references.

A teacher might say:

* "This is the 2025 version."
* "Click the old Settings button."
* "We're using Python 3.11."
* "This exam takes place in June."
* "This company is called X."
* "The current API version is v1."

A year later, much of the lesson can remain valuable while a few spoken details are no longer correct.

Training-content vendors and course workflows increasingly discuss updating only changed parts instead of reshooting entire lessons when the underlying lesson is still valid.

---

## 4. Startup founders

Founders constantly update:

* product names
* feature names
* user numbers
* launch dates
* pricing
* funding numbers
* milestones
* roadmap dates
* positioning

A founder may have a great launch video recorded last month.

Then the product changes.

Instead of:

> "We launched with 500 customers."

they need:

> "We launched with 1,200 customers."

The original recording may still be worth keeping.

Speech Surgeon repairs the sentence.

---

## 5. Product launch videos

Product marketing is an especially strong fit.

A demo may say:

> "The Pro plan costs $29."

Then pricing changes.

Or:

> "Our new AI feature is called Assist."

Then the feature gets renamed.

Or:

> "Version 1.0 launches in September."

Then launch moves to October.

Product teams already deal with the recurring problem of demos becoming outdated after product changes, which creates repeated recording, editing, approval, and publishing work.

Speech Surgeon focuses on the smallest possible repair:

```text
Same video
+
same speaker
+
same visuals
+
new words
```

---

## 6. SaaS demos

A SaaS company may have dozens of:

* onboarding videos
* feature walkthroughs
* sales demos
* launch videos
* help-center videos
* customer education videos

A product name, feature name, price, or version can change without invalidating the whole recording.

Current product-demo maintenance discussions specifically emphasize the cost of keeping existing demo libraries aligned with continuously changing products.

Speech Surgeon can become the audio-maintenance layer for these assets.

---

## 7. Hackathon applications

This is a surprisingly practical use case.

Suppose you record one polished application video.

You say:

> "This is my application for the Build for India Hackathon."

Then another opportunity comes along.

Instead of recording another video, change:

```text
Build for India Hackathon
```

to:

```text
We Make Devs Hackathon
```

The rest of the video stays the same.

The same idea applies to:

* accelerator applications
* startup programs
* demo days
* fellowship applications
* competitions
* grants
* pitch submissions

---

## 8. Sales and personalized outreach

A sales representative records one strong product video.

Instead of rerecording the opening for every company:

```text
"Hi Acme..."
```

```text
"Hi Globex..."
```

```text
"Hi Stripe..."
```

the spoken variable can be replaced.

This is already an active use case for AI video systems: personalized outreach workflows commonly keep a reusable core video and change only the personalized portion.

Speech Surgeon approaches the problem from a different direction:

> Start with a real recording you already made and surgically change its spoken content.

The current MVP is a single-video workflow. Bulk CRM-driven generation is a future extension.

---

## 9. Internal company training

Companies constantly change:

* processes
* employee titles
* tools
* software interfaces
* policies
* procedures
* team names

Imagine an internal training video says:

> "Contact Sarah from the Payments team."

But Sarah moved teams.

Or:

> "Open the Legacy Dashboard."

But the company renamed it.

Replacing one sentence may be far easier than scheduling the original presenter for another recording session.

Training-content systems increasingly treat these recurring updates as a maintenance problem rather than a one-time production problem.

---

## 10. Company announcements

A company records an announcement and later needs to change:

* a date
* a number
* a person's title
* a product name
* a launch window
* an event location

Instead of throwing away an otherwise good recording, the affected sentence can become a repair candidate.

---

## 11. Event and conference videos

Promotional recordings often contain details such as:

> "Join us on September 14."

But plans change.

The event moves to September 21.

Rather than rerecording the entire announcement, only the spoken date needs to change.

The same pattern applies to:

* conferences
* webinars
* meetups
* workshops
* university events
* community events
* product launches

---

## 12. Podcasts and interview content

Long recordings often contain small verbal mistakes.

For example:

> "The company raised $2 million."

when the correct figure is:

> "$3 million."

Or a host says the wrong episode number, date, product name, or guest title.

Audio-first podcast content is an especially natural fit because visual lip-sync is less important.

Video podcasts are possible too, but visible mouth movement can make an audio-only correction noticeable.

---

## 13. News, commentary, and explainers

Recorded commentary becomes outdated when facts change.

A creator may need to update:

* a date
* a statistic
* a product name
* a release number
* a current status

Speech Surgeon could be useful for localized corrections while keeping the original footage.

The important requirement is that the creator still verifies and approves the updated statement before publishing.

---

## 14. Recruitment and job-seeking videos

Imagine creating a reusable introduction:

> "I'm applying for the XYZ Developer position."

Then needing a different version for another company.

A sentence-level voice repair can turn the same base recording into a different application.

The current MVP is not a bulk recruitment platform, but the technical primitive is directly applicable.

---

# The Common Pattern Behind All of These

All of the use cases have the same structure:

```text
90–99% of the video is still correct
             +
1–10% of the spoken content changed
             ↓
       Traditional workflow
             ↓
     edit / rerecord / export
             ↓
         wasted effort
```

Speech Surgeon aims for:

```text
90–99% of the video is still correct
             +
1–10% of spoken content changed
             ↓
       detect the change
             ↓
     regenerate only that part
             ↓
        splice it back
             ↓
       keep everything else
```

That is the product.

---

# Why Audio Surgery Instead of Video Generation?

Generative video is powerful, but it is often solving a much larger problem than necessary.

If the only thing that changed is:

> "March"

becoming:

> "June"

there is no reason to regenerate:

* the person's face
* their background
* their screen recording
* their camera framing
* their gestures
* their B-roll
* the entire video timeline

Speech Surgeon treats the video as already-correct media.

The repair happens at the smallest practical layer:

> **speech → audio**

This gives the product a very specific philosophy:

> **Don't regenerate what is already right.**

---

# Current MVP

## Implemented

* Video upload in the web UI
* MP4 / MOV / WebM input flow
* Audio extraction with FFmpeg
* Fish Audio speech-to-text
* Timestamped transcript segments
* Editable transcript
* Sentence-level change detection
* Fish Audio S2.1 Pro voice-preserving speech generation
* Reference-audio based voice cloning
* Original-audio segmentation
* Replacement audio insertion
* Audio format normalization for the generated patch
* Reassembled repaired audio
* Original video stream preserved
* Repaired MP4 export
* Original vs repaired video comparison
* Download repaired video
* In-memory session handling
* FastAPI backend
* Next.js frontend

---

# What Is Not Implemented Yet

These were part of the larger product vision, but they are **not** claims about the current MVP:

* word-level surgical editing
* waveform-based visual editing
* WaveSurfer.js integration
* drag-to-adjust boundaries
* automatic duration matching
* advanced crossfades
* automatic loudness matching
* phoneme-aware boundary refinement
* full multi-speaker editing
* bulk personalized video generation
* persistent cloud sessions
* authentication
* production database
* background job infrastructure
* cloud object storage
* production monitoring
* automatic caption regeneration
* lip-sync correction
* visual replacement
* full video regeneration
* enterprise audit/versioning

These belong to the future product.

The current MVP deliberately proves the smaller and more fundamental idea first.

---

# Current Architecture

```text
                    ┌──────────────────────┐
                    │      Next.js UI      │
                    │                      │
                    │ Upload → Edit →      │
                    │ Repair → Result      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌─────────────┐   ┌─────────────┐
       │   FFmpeg   │   │ Fish Audio  │   │   Session   │
       │            │   │             │   │   Storage   │
       │ Extract    │   │ ASR         │   │             │
       │ audio      │   │ Voice clone │   │ In-memory   │
       │ splice     │   │ TTS         │   │ sessions    │
       │ remux      │   │             │   │             │
       └─────┬──────┘   └──────┬──────┘   └─────────────┘
             │                 │
             └────────┬────────┘
                      ▼
               ┌───────────────┐
               │ Repaired MP4  │
               │ original video│
               │ + repaired    │
               │ audio         │
               └───────────────┘
```

---

# End-to-End Flow

```text
Video Upload
     ↓
Extract Audio
     ↓
Fish ASR
     ↓
Timestamped Transcript
     ↓
User Edits Text
     ↓
Detect Changed Sentence
     ↓
Locate Original Time Region
     ↓
Fish S2.1 Pro Voice Generation
     ↓
Split Original Audio
     ↓
Insert Generated Audio Patch
     ↓
Reassemble Repaired Audio
     ↓
Attach Audio to Original Video
     ↓
Export Repaired MP4
```

---

# Backend

The backend is built with FastAPI.

### Main endpoints

```text
GET /
```

Health/root endpoint.

```text
POST /transcribe
```

Accepts the uploaded video, extracts audio, runs transcription, stores the session, and returns:

* session ID
* transcript
* timestamped segments
* speaker turns when available

```text
POST /repair
```

Accepts the session and edited transcript, determines what changed, generates the replacement speech, repairs the audio, attaches it to the original video, and returns the repaired MP4.

---

# Audio Surgery

The MVP surgery engine uses a deliberately simple and understandable pipeline.

Given:

```text
target_start = 4.32s
target_end   = 10.08s
```

the original audio is split into:

```text
0.00s ───────── 4.32s
                 │
                 ▼
          original region removed
                 │
                 ▼
          generated replacement
                 │
                 ▼
10.08s ───────── end
```

The final audio becomes:

```text
before + replacement + after
```

The generated replacement is normalized before concatenation so that the patch has a consistent sample rate/channel layout.

This is intentionally a first surgical implementation.

More sophisticated synchronization and mixing can be added later.

---

# Video Handling

Speech Surgeon intentionally does not regenerate the video.

The repair step maps:

```text
Original video stream
+
Repaired audio stream
```

and uses:

```text
-c:v copy
```

for the video stream.

Conceptually:

```text
Original MP4

VIDEO ───────────────────────────► unchanged

AUDIO ──► repair ──► new AUDIO ─► final MP4
```

This matters because the product promise is not:

> "Make me another version of this video."

It is:

> **"Repair what I said while keeping the video I already made."**

---

# Voice Generation

Speech Surgeon uses Fish Audio for the speech layer.

### Speech-to-text

The MVP uses Fish Audio transcription with timestamps.

### Voice generation

The MVP uses:

```text
Fish Audio S2.1 Pro
```

with reference audio from the original speaker.

That means the system does not create a generic narrator.

It tries to generate the replacement in the voice identity present in the source recording.

Fish Audio's current developer materials describe S2.1 Pro as supporting reference-audio voice cloning, which is the underlying capability used here.

---

# Why Sentence-Level Surgery First?

The long-term vision is much finer-grained editing.

For example:

```text
I launched the product in March
```

could eventually become:

```text
I launched the product in June
```

without regenerating the rest of the sentence.

But reliable word-level surgery requires solving additional problems:

* exact word timing
* phoneme boundaries
* coarticulation
* silence placement
* transition matching
* duration changes
* boundary artifacts

Sentence-level surgery provides a much cleaner first milestone.

It proves the core loop:

> **understand → edit → regenerate → splice**

Once that is reliable, smaller editing units can be introduced.

---

# The Key Technical Constraint

There is one important limitation to understand.

Speech Surgeon currently changes **audio**, not the speaker's mouth movement.

So if a person is visibly talking directly to the camera, changing the spoken sentence may create a noticeable lip-sync mismatch.

The current MVP is therefore especially well suited to:

* voiceovers
* screen recordings
* demos
* tutorials
* educational recordings
* slides + narration
* off-camera speech
* podcasts
* presentation footage
* videos where the spoken change is small

A future version can combine audio repair with visual/lip-sync correction where necessary.

---

# Example Transformation

### Original transcript

```text
I built a small project called Speech Surgeon.
We launched the first version in March,
and more than three thousand people tried it
during the first week.
We're now preparing the next version for September.
```

### User edit

```text
I built a small project called Speech Surgeon.
We launched the first version in June,
and more than five thousand people tried it
during the first week.
We're now preparing the next version for September.
```

### Speech Surgeon detects

```diff
- March
+ June

- three thousand
+ five thousand
```

### Generated audio

Only the affected sentence is synthesized.

### Final video

```text
Original frames
+
original audio
+
replacement speech
```

Result:

> **Same video. New words. Your voice.**

---

# Product UX

The current frontend intentionally stays simple.

```text
UPLOAD
   ↓
EDIT
   ↓
REPAIRING
   ↓
RESULT
```

The result screen provides:

* original video
* repaired video
* side-by-side comparison
* download action
* option to start another video

The UI deliberately focuses on the magic moment:

> **"I changed the words, and the video fixed itself."**

---

# Project Structure

This is the current repository structure, not the future architecture:

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
│   │
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

The `scripts/` directory contains development and experimentation utilities used while building the prototype.

---

# Technology Stack

## Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* Motion
* Lucide React
* Sonner
* canvas-confetti

## Backend

* Python
* FastAPI
* Uvicorn
* Requests
* python-dotenv

## AI

* Fish Audio ASR
* Fish Audio S2.1 Pro
* Reference-audio voice cloning

## Media

* FFmpeg
* WAV / PCM intermediate audio
* MP4 output

---

# Running Locally

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd speech-surgeon
```

## 2. Create the Python environment

On Windows Git Bash:

```bash
python -m venv backend/.venv
source backend/.venv/Scripts/activate
```

Install the backend dependencies:

```bash
python -m pip install -U pip
pip install fastapi uvicorn python-multipart requests python-dotenv fish-audio-sdk
```

## 3. Add the Fish Audio API key

Create:

```text
.env
```

in the project root.

Add:

```env
FISH_API_KEY=your_api_key_here
```

Never commit the key.

## 4. Start the backend

From the repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

The API should be available at:

```text
http://127.0.0.1:8000
```

## 5. Start the frontend

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

# Demo Walkthrough

The simplest way to demonstrate Speech Surgeon is:

### 1. Record a short video

Say something with a date, number, name, or product reference.

Example:

> "We launched the first version in March and more than three thousand people tried it."

### 2. Upload it

Speech Surgeon extracts the audio and transcribes the recording.

### 3. Change only the words

For example:

```text
March
→
June
```

and:

```text
three thousand
→
five thousand
```

### 4. Press Repair

The system:

```text
detects the change
      ↓
finds the original time region
      ↓
generates replacement speech
      ↓
splices it into the audio
      ↓
attaches repaired audio to original video
```

### 5. Compare

Play:

```text
Original
vs.
Repaired
```

The visual footage remains the same.

The spoken content has changed.

---

# What This Project Is Trying to Prove

Speech Surgeon is not trying to prove that AI can generate a video.

There are already many systems capable of generating video.

The more interesting question is:

> **Can AI understand an existing recording well enough to make a tiny spoken correction without rebuilding everything around it?**

The prototype demonstrates that loop:

```text
Human recording
      ↓
Speech recognition
      ↓
Editable representation
      ↓
Human text correction
      ↓
Voice-preserving generation
      ↓
Precise audio replacement
      ↓
Original video preserved
```

That is the core technical idea.

---

# Why This Is Different

Many AI video systems start from:

```text
Prompt / Script
      ↓
Generate video
```

Speech Surgeon starts from:

```text
Existing video
      ↓
Understand it
      ↓
Find the mistake
      ↓
Change only the mistake
      ↓
Keep everything else
```

That difference matters.

The goal is not **generation**.

The goal is **repair**.

---

# Quality Goals

The current MVP focuses on proving five things:

### 1. Text accuracy

The intended spoken change should be correctly understood.

### 2. Speaker identity

Replacement speech should resemble the original speaker.

### 3. Correct location

The replacement should appear in the intended section of the recording.

### 4. Continuity

Everything before and after the changed region should remain original.

### 5. Video preservation

The visual stream should remain untouched.

More advanced audio quality work will eventually include:

* duration matching
* silence alignment
* boundary refinement
* loudness matching
* crossfades
* phoneme-aware transitions
* prosody preservation

---

# Current Limitations

Speech Surgeon is a working MVP, not a production-ready media platform.

### Sentence-level editing

The current change detector operates primarily at sentence level.

### Timing

Replacing a sentence with a longer or shorter generated recording can change the total audio duration.

### Lip-sync

The current version does not modify the speaker's mouth movement.

### Single-speaker focus

The MVP is primarily designed around short, relatively clean speech recordings.

### Temporary sessions

Session state is stored in memory.

Restarting the backend clears active sessions.

### Local prototype

There is currently no:

* authentication
* persistent database
* cloud storage
* job queue
* distributed processing
* production monitoring

Those are deployment concerns for a later version.

---

# Safety, Consent, and Voice Ownership

Voice cloning must be used responsibly.

Speech Surgeon should only be used with:

* your own voice
* a voice you have explicit permission to use
* recordings where you have the right to generate derivative speech

The product is intended for legitimate editing, correction, maintenance, and content-production workflows.

It should not be used to impersonate someone without permission or create deceptive statements attributed to another person.

A production version should add explicit consent controls and stronger safeguards around voice ownership.

---

# Privacy

The current prototype is local and intentionally simple.

Current session data is stored in memory by the running backend.

Uploaded media is processed during the active workflow.

For a future hosted version, privacy should be treated as a first-class product requirement:

* encrypted uploads
* automatic deletion
* explicit retention controls
* private storage
* audit logs
* user-controlled voice references
* clear third-party AI processing disclosures

---

# Future Direction

The current sentence-level prototype is the foundation.

The long-term system can evolve toward:

```text
Sentence Editing
       ↓
Phrase Editing
       ↓
Word Editing
       ↓
Phoneme-Level Repair
```

with increasing precision at each step.

Potential future capabilities include:

### Word-level surgery

Change:

```text
March
```

to:

```text
June
```

without regenerating the surrounding words.

### Smarter timing

Automatically fit replacement speech to the original timing.

### Better audio matching

Match:

* loudness
* room tone
* pauses
* cadence
* background characteristics

### Visual repair

For talking-head videos, synchronize the repaired speech with facial motion when necessary.

### Multi-speaker support

Identify which speaker owns the changed sentence and repair only that speaker.

### Bulk editing

One base video could generate many variations:

```text
Company A
Company B
Company C
Company D
```

or:

```text
2025 → 2026
```

across an entire content library.

### Content-library maintenance

Longer-term, Speech Surgeon could become a maintenance system for recorded video libraries:

```text
Old video
   ↓
Transcript
   ↓
Changed source text
   ↓
Affected region
   ↓
Automatic repair
   ↓
Updated version
```

---

# Future Product Vision

The larger vision is:

> **Git for spoken video.**

Traditional source code has:

```text
diffs
versions
patches
rollbacks
```

Speech Surgeon could eventually give recorded speech the same kind of editing model:

```text
original recording
      ↓
text diff
      ↓
audio patch
      ↓
new version
```

Instead of thinking:

> "I need to make another video."

the user could think:

> "I just need to patch three sentences."

That could make long-lived video content much easier to maintain.

---

# Example Product Evolution

### Today

```text
Upload video
↓
Edit transcript
↓
Change one sentence
↓
Generate replacement
↓
Splice audio
↓
Download repaired video
```

### Future

```text
Upload video
↓
Automatic transcript + timestamps
↓
Editable word-level timeline
↓
Detect changes automatically
↓
Generate only changed words/phrases
↓
Match timing + tone + room sound
↓
Repair lips when required
↓
Version entire video library
```

---

# Research / Market Signal

The problem Speech Surgeon targets is not hypothetical.

Current product-marketing and training workflows repeatedly describe the same pattern: software releases, pricing changes, renamed features, changed procedures, and revised messaging can make previously recorded videos stale even when most of the underlying video remains useful.

Sales teams are also already exploring reusable videos with dynamically personalized spoken sections rather than recording a completely new video for every prospect.

Community discussions around product demos show the same frustration from a builder's perspective: recording and editing even short demos can become a surprisingly large production task, especially when revisions are requested later.

Speech Surgeon takes that problem and focuses it into one primitive:

> **Change the words. Keep the recording.**

---

# Why Fish Audio?

Speech Surgeon needs two important speech capabilities:

1. Understand what was said.
2. Generate replacement speech that preserves the speaker identity.

Fish Audio provides both speech-to-text and voice-generation capabilities, including reference-audio voice cloning through its S2.1 Pro system.

That makes it a strong foundation for the speech layer while Speech Surgeon focuses on the higher-level problem:

> **How do we surgically apply the change to an existing recording?**

---

# The Core Insight

The most important idea in Speech Surgeon is surprisingly small:

> **A video does not need to be regenerated just because a sentence changed.**

The existing media already contains enormous amounts of valuable information:

* facial performance
* gestures
* screen recordings
* B-roll
* camera framing
* background
* lighting
* editing
* composition
* pacing

Throwing all of that away because of one sentence is inefficient.

Speech Surgeon keeps it.

Only the speech changes.

---

# Project Status

## MVP complete — working prototype

Speech Surgeon currently demonstrates the complete loop:

```text
Upload video
    ↓
Extract audio
    ↓
Transcribe
    ↓
Edit transcript
    ↓
Detect changed sentence
    ↓
Generate replacement speech in original voice
    ↓
Surgically replace audio
    ↓
Attach repaired audio to original video
    ↓
Compare original vs repaired
    ↓
Download repaired MP4
```

The workflow has been tested on the original scripted demo as well as a separate real-world recording with different content, including changing a hackathon name without recording the video again.

The project is now best described as:

> **A working MVP / local prototype for surgical speech editing in existing videos.**

---

# One-Line Pitch

> **Speech Surgeon lets you change what you said in an existing video without saying it again.**

---

# Demo Pitch

> **Upload a video. Edit the transcript. Speech Surgeon detects what changed, regenerates only that speech in your voice, surgically replaces it in the original audio, and keeps the original video frames untouched.**

---

# Built With

* **Fish Audio** — speech recognition and voice-preserving speech generation
* **FFmpeg** — audio extraction, surgery, normalization, and video remuxing
* **FastAPI** — backend API
* **Next.js** — frontend
* **React / TypeScript** — application UI

---

# License

MIT License