# 🩹 Speech Surgeon

> **Edit what you said without saying it again.**

**Speech Surgeon is an AI-powered speech repair tool for existing videos.**

Upload a recorded video, edit the words in its transcript, and Speech Surgeon regenerates **only the changed speech in the original speaker's voice**, surgically replaces that portion of the audio, and attaches the repaired audio back to the **original video frames**.

**No complete rerecording.
No video regeneration.
Just repair the words that changed.**

---

## 🎯 The Idea

Recorded video is expensive to recreate, but information changes constantly.

The video may still be good.

The performance may still be good.

The visuals may still be good.

**Only a few words are wrong.**

For example:

```text
"We launched the first version in March."

                    ↓

"We launched the first version in June."
```

Or:

```text
"three thousand users"
        ↓
"five thousand users"
```

Or:

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

# ⚡ What Speech Surgeon Does

The core workflow is:

```text
🎥 Upload video
       ↓
📝 Get transcript
       ↓
✏️ Edit what was said
       ↓
🔍 Detect the changed region
       ↓
🐟 Generate replacement speech in the original voice
       ↓
✂️ Surgically replace the audio
       ↓
🎬 Keep the original video frames
       ↓
✨ Repaired video
```

### One video. One small correction. No rerecording.

---

# 🎯 Who It's For

Speech Surgeon is initially built for people who maintain recorded video that becomes outdated when a few spoken details change.

## 1. Creators

YouTubers, podcasters, reviewers, influencers, and independent creators who maintain videos over time.

Useful for changing:

* dates
* statistics
* prices
* product names
* software versions
* sponsors
* partner names
* links or references
* outdated facts
* episode numbers

### Example

A tutorial recorded in 2025 says:

> "This works in version 3."

The software becomes version 4.

Instead of rerecording the tutorial:

```text
Version 3 → Version 4
```

Repair the speech.

---

## 2. Educators & Course Creators

Online courses and educational libraries can remain useful for years, while small details constantly change.

Examples:

* academic years
* software versions
* API versions
* course dates
* syllabus details
* terminology
* assignment deadlines
* exam information
* statistics
* tool names

### Example

An educator has 50 existing videos containing:

> "This course is updated for 2025."

The next year:

```text
2025 → 2026
```

The actual lesson is still correct.

Why rerecord 50 videos for one year?

---

## 3. Companies & Teams

Companies constantly update:

* products
* features
* pricing
* launch dates
* customer numbers
* internal processes
* employee roles
* product terminology
* sales messaging
* training material

This makes Speech Surgeon useful for:

* product demos
* SaaS tutorials
* onboarding
* internal training
* sales videos
* marketing videos
* documentation
* announcements
* customer education

### Example

A product video says:

> "The Pro plan costs $29."

Pricing changes:

```text
$29 → $39
```

The product demo, presenter, screen recording, and visuals can remain unchanged.

---

# 🌎 Where Else It Can Be Useful

The same repair problem appears anywhere organizations maintain libraries of recorded speech.

### Content & Media

* YouTube videos
* podcasts
* interviews
* news commentary
* explainers
* documentaries
* social media content
* product reviews

### Education

* online courses
* university lectures
* tutorials
* certification training
* recurring educational programs
* yearly course updates
* software training

### Startups & SaaS

* launch videos
* product demos
* feature announcements
* onboarding
* documentation
* customer education
* release videos
* investor or company updates

### Marketing & Advertising

* campaigns
* promotional videos
* product messaging
* seasonal campaigns
* pricing changes
* offer changes
* sponsor or partner changes

### Sales

* reusable sales videos
* personalized introductions
* product demonstrations
* customer-specific messaging
* prospect-specific information

### Hackathons, Applications & Competitions

This is another very practical use case.

Record one polished application video once.

Then reuse it for:

* hackathons
* accelerators
* startup programs
* fellowships
* demo days
* competitions
* grants
* application videos

For example:

```text
"Build for India Hackathon"
              ↓
"We Make Devs Hackathon"
```

without recording the entire video again.

### Internal Company Content

* employee onboarding
* process training
* policy explanations
* software tutorials
* department introductions
* internal announcements
* recurring training

### Events

* conference announcements
* webinars
* workshops
* meetups
* university events
* event promotions
* speaker announcements

### Real Estate

* property videos
* agent videos
* listing walkthroughs
* price updates
* availability updates
* open-house dates

### Travel & Hospitality

* hotel videos
* tourism content
* destination guides
* room pricing
* availability
* seasonal information

### Finance

* financial education
* product explanations
* recurring reports
* company updates
* numbers and figures that change

### Healthcare & Life Sciences

* educational material
* training
* procedures
* terminology updates
* administrative information

### Government & Public Information

* public-information videos
* program announcements
* deadlines
* public-service instructions
* informational updates

### Manufacturing & Industrial

* safety training
* process training
* equipment instructions
* facility procedures
* operational updates

### Automotive & Transport

* vehicle demonstrations
* service instructions
* model information
* pricing
* feature updates

### Construction & Engineering

* project updates
* technical training
* safety instructions
* specifications
* project dates

### Sports & Fitness

* recurring programs
* training videos
* coaching content
* event dates
* athlete or client information

### Gaming & Esports

* patch updates
* game version information
* tournament dates
* announcements
* tutorial narration

### Recruitment & HR

* hiring videos
* employee introductions
* company information
* role descriptions
* recurring recruitment content

### Legal & Compliance

* policy updates
* compliance training
* internal procedures
* regulatory information

---

# 🧠 The Common Pattern

All of these use cases share the same basic problem:

```text
Most of the video is still correct
              +
A small part of the spoken content changed
              ↓
       Traditional workflow
              ↓
      Edit / rerecord / export
```

Speech Surgeon aims for:

```text
Most of the video is still correct
              +
A small part of the spoken content changed
              ↓
       Detect the change
              ↓
   Generate only the replacement
              ↓
        Patch the audio
              ↓
       Keep everything else
```

That is the product.

---

# 🔥 Why This Is Different

Many AI video systems start with:

```text
Prompt / Script
      ↓
Generate video
```

Speech Surgeon starts with:

```text
Existing video
      ↓
Understand it
      ↓
Find what changed
      ↓
Repair only the changed speech
      ↓
Keep everything else
```

The difference is important.

Speech Surgeon isn't trying to replace the recording.

It treats the existing recording as valuable media that should be **preserved and patched**.

> **Don't regenerate what is already right.**

---

# 💰 Cost Comparison: Manual Fix vs Speech Surgeon

How much does a small spoken correction cost today, and how much does Speech Surgeon save?

The numbers below use **current 2026 market rates** for freelance video editors, voice-over talent, and video production, compared against the real API prices of the tools Speech Surgeon uses (Fish Audio and Sync Labs).

> **Headline:**
> One sentence fixed in a 5-minute video costs about **$35–$300** the manual way.
> With Speech Surgeon it costs about **$0.05 in API fees**, or about **$6 if you count 10 minutes of your own time**.

## 📐 The Test Case

```text
Video length:        5 minutes
What changed:        one sentence (~200 characters)
Example:             "...in March..."  →  "...in June..."
```

---

## 🧑‍🔧 Manual Workflow: What It Costs Today

Normally, fixing one sentence means reopening the project, finding the section, getting the line re-recorded, matching the original voice and delivery, replacing the audio, and exporting again.

| Method | Cash cost | Time | What it involves |
|---|---|---|---|
| **A. Do it yourself** | $0 cash (≈ $35–$70 of your time) | 1–2 hours | Re-record, match tone and room sound, reopen project, replace audio, re-export |
| **B. Freelance editor revision** | $50–$200 | 1–3 days | The speaker supplies new audio, the editor patches and re-exports |
| **C. Editor + voice talent pickup** | $75–$300 | 1–3 days | Editor revision plus a $25–$100 voice-over fee |
| **D. Full reshoot** | ~$5,000–$7,500 | Days to weeks | Only needed when on-screen content must change |

Rush delivery typically adds another 20–50% on top of the editor's rate.

---

## ⚡ Speech Surgeon: What It Costs

| Step | Cost |
|---|---|
| Transcribe a 5-minute video (Fish Audio ASR, $0.36 per audio hour) | ≈ $0.03 |
| Generate the replacement sentence (Fish Audio S2.1 Pro, $15 per 1M UTF-8 bytes, ~200 bytes) | ≈ $0.003 per attempt |
| Audio surgery and video remux (FFmpeg, runs locally) | $0 |
| **Total API cost per fix** | **≈ $0.03–$0.06** |
| Your time: upload, edit, listen, download (~10 minutes at $35/hr) | ≈ $6 |
| **Total with your time counted** | **≈ $6** |

Retrying the generation five times still costs well under a cent.

### Optional lip-sync (talking-head videos only)

| Lip-sync scope | Cost |
|---|---|
| Patched section only (~10 seconds, lipsync-2) | ≈ $0.40–$0.50 |
| Whole 5-minute video (lipsync-2) | ≈ $12–$15 |
| Whole 5-minute video (lipsync-2-pro) | ≈ $20–$25 |

Sync Labs charges per second of video that is actually lip-synced, plus a small subscription fee, so syncing only the patched section keeps the cost close to zero.

---

## 📊 Side by Side: One Fix

```text
                         CASH COST         YOUR TIME
────────────────────────────────────────────────────────
A. Do it yourself        $0                1–2 hours
B. Editor revision       $50–$200          1–3 days
C. Editor + voice talent $75–$300          1–3 days
D. Full reshoot          ~$5,000–$7,500    days to weeks
────────────────────────────────────────────────────────
Speech Surgeon           ~$0.05            ~10 minutes
  all-in (time counted)  ~$6
```

### What you save per fix

| Compared to | You save | Cheaper by |
|---|---|---|
| A. Do it yourself | ~$29–$64 and 50–110 minutes | about 6–12× |
| B. Editor revision | ~$44–$194 and days of waiting | about 8–33× |
| C. Editor + voice talent | ~$69–$294 and days of waiting | about 12–50× |

---

## 📚 Side by Side: A Whole Library

The educator example from earlier: **50 videos**, each containing `"updated for 2025"` that must become `"updated for 2026"`.

| Method | Total cost | Total time |
|---|---|---|
| A. Do it yourself (1–2 hrs × 50) | ≈ $1,750–$3,500 of your time | 50–100 hours |
| B. Editor revision round × 50 | $2,500–$10,000 | days to weeks of back-and-forth |
| **Speech Surgeon** | **≈ $3 API + ≈ $290 of your time** | **≈ 8 hours (50 × 10 min)** |

```text
Saved on a 50-video update:

vs. doing it yourself      ≈ $1,450–$3,200   and ~40–90 hours
vs. hiring editors         ≈ $2,200–$9,700   and days of coordination
```

That is roughly **83–97% cheaper** depending on the baseline, and the saving repeats every year the information changes.

---

## 🧭 Who Saves What

| User | Typical fix | Manual | Speech Surgeon | The real saving |
|---|---|---|---|---|
| **Solo creator** | Date, version, price | Free but 1–2 hrs of re-recording | ~$0.05 | **Time**: 10 minutes instead of an afternoon |
| **Hackathon / application video** | Event name | Free but 30–60 min | ~$0.02 | **Time**, and the video stays polished |
| **Educator with a course library** | Year, tool version | $2,500–$10,000 for 50 videos | ~$290 for 50 videos | **Money and time** |
| **Company with a product demo** | Price, feature name | $75–$300 per fix, plus coordination | ~$6 per fix | **Money and turnaround** |
| **Team with hundreds of videos** | Policy, price, version | Thousands of dollars per update cycle | Mostly review time | **Makes updating practical at all** |

---

## ⚠️ Honest Notes

* **These are estimates for a typical small fix.** Editor hours and the 10-minute operator time are assumptions. The hourly rates, voice-over fees, and API prices come from the sources listed below.
* **For a solo creator re-recording their own voice, the cash saving is small.** The real value is minutes instead of hours.
* **Quality still needs a human listen.** The current MVP repairs at the sentence level, so prosody and timing can differ slightly from the original. The 10-minute estimate includes that review.
* **Lip-sync is the one cost that can grow.** A manual re-record has the same mouth-mismatch problem on talking-head video unless you reshoot or lip-sync as well.
* **Freelance rates vary by region.** Offshore editors can run around $25/hr versus $100+/hr in major Western markets, which narrows the cash gap but not the time gap.
* **Fish Audio bills by UTF-8 bytes.** Non-Latin scripts cost more per sentence, but it is still a fraction of a cent.
* **Closest alternative:** Descript offers text-based editing with Overdub voice cloning for a flat $16–$50 per month. Speech Surgeon's angle is the repair-and-preserve workflow and, long term, bulk library maintenance.

---

## 🔗 Sources

Prices researched in October 2026. Check each provider for current rates.

* Video editor rates and revision costs: [Vidico](https://vidico.com/news/video-editor-cost/), [Krock.io](https://krock.io/blog/stay-creative/how-much-video-editor-should-charge/), [Ruah Creative House](https://ruahcreativehouse.org/blog/video-editing-rates/)
* Offshore editor rates: [Videotto](https://www.videotto.com/blog/how-much-does-video-editing-cost-global-2026)
* Voice-over rates and session minimums: [VoiceBros](https://voicebros.com/en/voice-over-rates), [Voices.com profile terms](https://www.voices.com/profile/jimkirkvo/engaging-sincere-voice-over-to-bring-your-brand-to-life)
* Talking-head production cost per finished minute: [Forasoft](https://www.forasoft.com/learn/elearning-video/articles-elearning/ai-avatars-video-synthesis-for-courses)
* Fish Audio API pricing: [docs.fish.audio](https://docs.fish.audio/developer-guide/models-pricing/pricing-and-rate-limits)
* Sync Labs lip-sync pricing: [sync.so billing](https://sync.so/docs/billing), [sync.so calculator](https://sync.so/calculator)
* Descript plans: [Layer3 Labs](https://www.layer3labs.io/guides/descript-pricing)

---

# 🛠️ What I Actually Built

The current MVP is a working local end-to-end prototype.

## Input

A short video containing speech.

```text
video.mp4
    ↓
audio extracted from video
```

---

## 1. Transcribe

Speech Surgeon extracts the audio with FFmpeg and sends it to **Fish Audio** speech-to-text.

The returned transcript includes timestamps.

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

## 2. Edit

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

The user doesn't rerecord anything.

---

## 3. Detect the Change

Speech Surgeon compares the original and edited transcript.

Conceptually:

```text
Original
"March ... three thousand"

          ↓

        DIFF

          ↓

Edited
"June ... five thousand"
```

The current MVP identifies the changed region at the **sentence level**.

---

## 4. Generate Replacement Speech

The original recording provides the voice reference.

Fish Audio S2.1 Pro generates the edited speech using the original speaker's voice reference.

Conceptually:

```text
Original voice
      +
New text
      ↓
Fish Audio
      ↓
Replacement speech
```

The result is an **audio patch**, not a regenerated video.

---

## 5. Surgically Repair the Audio

The original audio is split into three pieces:

```text
┌────────────────┬──────────────────────┬────────────────┐
│ Original audio │ Generated replacement│ Original audio │
│ before change  │       speech         │ after change   │
└────────────────┴──────────────────────┴────────────────┘
```

Conceptually:

```text
Original audio
      │
      ├── before changed region
      │
      ├── replacement speech
      │
      └── after changed region
```

The pieces are concatenated into the repaired audio track.

The generated patch is normalized to a consistent audio format before concatenation.

---

## 6. Preserve the Original Video

This is one of the most important design decisions.

Speech Surgeon does **not** regenerate the video.

Instead:

```text
Original video
      │
      ├── original video frames ────────────┐
      │                                     │
      └── original audio → repaired audio ──┤
                                            ↓
                                      Repaired MP4
```

The video stream is copied rather than re-encoded.

The original:

* camera footage
* screen recordings
* B-roll
* background
* framing
* lighting
* gestures
* visual composition

remain intact.

> **Only the speech changes.**

---

# 👄 Optional: Sync the Mouth After Repair

For talking-head videos, changing audio can sometimes create a visible lip-sync mismatch.

Speech Surgeon therefore has an **optional experimental lip-sync enhancement** powered by Sync Labs.

The core product does not depend on it.

The hierarchy is:

```text
CORE
Speech repair
    ↓
Audio surgery
    ↓
Original video preserved

OPTIONAL
Lip-sync
    ↓
Adjust facial movement when needed
```

This is especially useful when the speaker is directly facing the camera.

For voiceovers, screen recordings, podcasts, presentations, slides, and off-camera narration, audio repair can often be useful without visual modification.

---

# 🎬 The Core Demo

A simple demo can be explained in seconds:

```text
Original:

"We launched the first version in March
and more than three thousand people tried it."

             ↓ EDIT

"We launched the first version in June
and more than five thousand people tried it."

             ↓

Speech Surgeon

             ↓

Same video
Same speaker
Same visuals
New words
```

The demo proves the core idea:

> **Change the words. Keep the recording.**

---

# 🧪 Real Prototype Example

The system has also been tested on a real application video.

Original:

> "This is my application for the Build for India Hackathon. I am building Chhotu."

Edited:

> "This is my application for the We Make Devs Hackathon. I am building Chhotu."

Speech Surgeon:

1. transcribed the recording,
2. detected the changed content,
3. generated replacement speech,
4. surgically replaced the affected audio,
5. preserved the original video,
6. exported the repaired video.

This is a practical example of reusing one polished recording for multiple opportunities.

---

# 🧩 MVP Architecture

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
       │ audio      │   │ S2.1 Pro    │   │ In-memory   │
       │ splice     │   │ voice       │   │ sessions    │
       │ remux      │   │ generation  │   │             │
       └─────┬──────┘   └──────┬──────┘   └─────────────┘
             │                 │
             └────────┬────────┘
                      ▼
               ┌───────────────┐
               │ Repaired MP4  │
               │               │
               │ Original      │
               │ video frames  │
               │ + repaired    │
               │ audio         │
               └───────────────┘
```

Optional:

```text
Repaired video + repaired audio
              ↓
         Sync Labs
              ↓
       Lip-synced video
```

---

# 🔄 End-to-End Flow

```text
Video Upload
     ↓
Extract Audio
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
     ↓
Optional Lip-Sync
```

---

# 🐟 Why Fish Audio?

Fish Audio is the core speech layer of Speech Surgeon.

Speech Surgeon needs two major capabilities:

### 1. Understand what was said

Fish Audio provides speech-to-text transcription used to create the editable transcript and timestamped regions.

### 2. Generate replacement speech

Fish Audio S2.1 Pro is used with reference audio to generate replacement speech matching the original speaker.

This gives Speech Surgeon the speech primitives it needs while the project focuses on the higher-level problem:

> **How do we surgically repair an existing recording?**

The important distinction is:

```text
Fish Audio
     ↓
Speech intelligence + voice generation

Speech Surgeon
     ↓
Editing + diff + audio surgery + video preservation
```

---

# ✂️ Audio Surgery

The MVP uses a deliberately simple and understandable surgery pipeline.

For example:

```text
target_start = 4.32s
target_end   = 10.08s
```

The original audio becomes:

```text
0.00s ─────── 4.32s
              │
              ▼
        changed region
              │
              ▼
        replacement
              │
10.08s ─────── end
```

The final audio becomes:

```text
before + replacement + after
```

The replacement audio is normalized before being concatenated.

This is intentionally a first surgical implementation.

More sophisticated timing and mixing can be added as the editing granularity improves.

---

# 🎥 Video Handling

Speech Surgeon intentionally avoids video regeneration.

The repair operation effectively performs:

```text
Original video stream
+
Repaired audio stream
        ↓
Final video
```

The video stream is copied with FFmpeg:

```text
-c:v copy
```

Conceptually:

```text
Original MP4

VIDEO ───────────────────────────────► unchanged

AUDIO ──► repair ──► repaired AUDIO ─► final MP4
```

This is central to the product philosophy.

The promise isn't:

> "Make another version of this video."

It is:

> **"Repair what I said while keeping the video I already made."**

---

# 🎯 MVP Scope

## What Works Today

```text
VIDEO
  ↓
TRANSCRIPT
  ↓
EDIT
  ↓
DIFF
  ↓
VOICE GENERATION
  ↓
AUDIO SURGERY
  ↓
ORIGINAL VIDEO PRESERVED
  ↓
REPAIRED VIDEO
```

The current MVP supports:

* video upload
* MP4 / MOV / WebM input flow
* audio extraction with FFmpeg
* Fish Audio speech-to-text
* timestamped transcript segments
* editable transcript
* sentence-level change detection
* locating the changed sentence in the original recording
* Fish Audio S2.1 Pro speech generation
* reference-audio voice cloning
* original-audio segmentation
* replacement audio generation
* audio format normalization
* repaired audio reconstruction
* original video stream preservation
* repaired MP4 export
* original vs repaired comparison
* video download
* optional Sync Labs lip-sync enhancement
* in-memory session handling
* FastAPI backend
* Next.js frontend

---

# 🚧 Current Limitations

Speech Surgeon is a working MVP/local prototype, not a production media platform.

### Sentence-level editing

The current diff and repair flow primarily operates at the sentence level.

### Timing

A generated sentence may be longer or shorter than the original sentence.

Advanced duration matching is not yet implemented.

### Audio matching

The MVP does not yet perform sophisticated:

* room-tone reconstruction
* prosody matching
* loudness matching
* phoneme-aware transitions
* automatic crossfades
* boundary refinement

### Lip-sync

Lip-sync is an optional enhancement for talking-head footage rather than the core repair mechanism.

### Single-speaker focus

The current workflow is primarily designed for short, relatively clean single-speaker recordings.

### Temporary sessions

Session data is stored in memory.

Restarting the backend clears active sessions.

### Local prototype

The current project does not yet include:

* authentication
* persistent database
* cloud storage
* background job queue
* distributed processing
* production monitoring
* enterprise permissions
* production-scale media processing

---

# 🗺️ Roadmap

## Now

### Sentence-level speech repair

The current MVP proves the complete loop:

```text
Upload
↓
Transcribe
↓
Edit
↓
Detect
↓
Generate
↓
Surgically replace
↓
Preserve video
```

---

## Next — Finer-Grained Editing

Move from sentence-level repair toward:

* phrase-level editing
* word-level editing
* improved timing
* automatic duration fitting
* better boundary detection
* improved audio matching
* smoother transitions

For example:

```text
"I launched in March."

        ↓

"I launched in June."
```

could eventually replace only the affected words rather than regenerating the full sentence.

---

## Later — Video Content Maintenance

The repair engine could evolve into a system for maintaining large video libraries.

Potential capabilities:

* multi-speaker repair
* bulk updates
* reusable voice references
* automatic content scanning
* transcript-based search
* affected-video detection
* automatic update suggestions
* version history
* approval workflows

For example:

```text
Content library
      ↓
Find videos mentioning "2025"
      ↓
Replace with "2026"
      ↓
Generate affected speech
      ↓
Create updated versions
```

---

## Long-Term Vision

> **Git for spoken video.**

Traditional software has:

```text
source
diff
patch
version
rollback
```

Speech Surgeon could eventually provide a similar model for recorded speech:

```text
original recording
       ↓
transcript
       ↓
text diff
       ↓
audio patch
       ↓
new video version
```

Instead of thinking:

> "I need to make another video."

the user could think:

> **"I just need to patch the part that changed."**

---

# 🧠 Why Sentence-Level Surgery First?

The long-term vision is fine-grained editing.

But reliable word-level or phoneme-level editing requires solving difficult problems:

* exact word timing
* phoneme boundaries
* coarticulation
* silence placement
* duration differences
* prosody
* transition matching
* background sound continuity

Sentence-level surgery provides a cleaner first milestone.

It proves the core loop:

> **Understand → Edit → Generate → Splice → Preserve**

Once that works reliably, the repair unit can become smaller.

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

# 🏗️ Backend

The backend is built with **FastAPI**.

### Main endpoints

```text
GET /
```

Health/root endpoint.

```text
POST /transcribe
```

Accepts the uploaded video, extracts audio, runs transcription, creates a session, and returns:

* session ID
* transcript
* timestamped segments
* speaker information when available

```text
POST /repair
```

Accepts the session and edited transcript.

The endpoint:

1. determines what changed,
2. locates the affected region,
3. generates replacement speech,
4. repairs the audio,
5. attaches repaired audio to the original video,
6. returns the repaired MP4.

```text
POST /lipsync
```

Optional enhancement endpoint.

It sends the repaired video/audio through the configured Sync Labs workflow and returns the resulting lip-synced video.

---

# 🖥️ Frontend

The frontend is intentionally simple:

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

* original video
* repaired video
* original vs repaired comparison
* optional lip-sync action
* final video preview
* download
* start another video

The UI is designed around the main product moment:

> **"I changed the words, and the recording fixed itself."**

---

# 📁 Project Structure

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

The `scripts/` directory contains development and experimentation utilities created while building the prototype.

---

# 🧰 Technology Stack

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

## AI / Speech

* **Fish Audio ASR**
* **Fish Audio S2.1 Pro**
* Reference-audio voice cloning

## Optional Video Enhancement

* **Sync Labs**
* Lip-sync generation for repaired talking-head videos

## Media Processing

* FFmpeg
* WAV / PCM intermediate audio
* MP4 output

---

# 🚀 Running Locally

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd speech-surgeon
```

---

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

---

## 3. Add API Keys

Create a `.env` file in the project root:

```env
FISH_API_KEY=your_fish_audio_api_key
SYNC_API_KEY=your_sync_labs_api_key
```

The Sync Labs key is only required if you want to test the optional lip-sync workflow.

**Never commit API keys to the repository.**

---

## 4. Start the backend

From the repository root:

```bash
uvicorn backend.main:app --reload --port 8000
```

Backend:

```text
http://127.0.0.1:8000
```

---

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

# 🎬 Demo Walkthrough

The strongest demo is deliberately simple.

## 1. Record

Record a short video containing a date, number, product name, event name, or other information that can easily change.

For example:

> "We launched the first version in March and more than three thousand people tried it."

---

## 2. Upload

Speech Surgeon extracts the audio and transcribes the video.

---

## 3. Edit

Change:

```text
March
```

to:

```text
June
```

and:

```text
three thousand
```

to:

```text
five thousand
```

---

## 4. Repair

Speech Surgeon:

```text
detects the change
      ↓
finds the affected region
      ↓
generates replacement speech
      ↓
splices it into the original audio
      ↓
attaches repaired audio to original video
```

---

## 5. Compare

Play:

```text
Original
   vs.
Repaired
```

The visual footage stays the same.

The spoken content changes.

---

## 6. Optional Lip-Sync

If the recording is a talking-head video:

```text
Repaired video
      ↓
Sync Labs
      ↓
Lip-synced result
```

This demonstrates the optional visual enhancement without making it the core product.

---

# 🔬 What This Project Is Trying to Prove

Speech Surgeon isn't primarily trying to prove:

> "AI can generate a video."

The interesting question is:

> **Can AI understand an existing recording well enough to make a small spoken correction without rebuilding everything around it?**

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
Changed-region detection
      ↓
Voice-preserving generation
      ↓
Audio patch
      ↓
Original video preserved
```

That is the core technical idea.

---

# 🧩 The Core Insight

A recorded video contains a huge amount of valuable information:

* facial performance
* gestures
* screen recordings
* B-roll
* camera framing
* lighting
* background
* editing
* composition
* pacing

If only one sentence changed, throwing all of that away is unnecessary.

Speech Surgeon keeps the existing media and repairs the smallest practical layer:

```text
Existing video
      ↓
      AUDIO
        ↓
     repair
        ↓
 Existing video
 + repaired speech
```

> **A video doesn't need to be regenerated just because a sentence changed.**

---

# 🔐 Safety, Consent & Voice Ownership

Voice cloning should only be used responsibly.

Speech Surgeon should be used with:

* your own voice
* a voice you have explicit permission to use
* recordings where you have the right to generate derivative speech

The system is intended for legitimate editing, correction, maintenance, and content-production workflows.

It should not be used to impersonate someone without permission or create deceptive statements attributed to another person.

A production version should include stronger controls around:

* voice ownership
* consent
* identity verification
* generated-content disclosure
* audit trails
* abuse prevention

---

# 🔒 Privacy

The current prototype is local and intentionally simple.

Session state is stored in memory by the running backend.

For a future hosted version, privacy should be a first-class requirement.

Potential production safeguards include:

* encrypted uploads
* automatic deletion
* explicit retention controls
* private object storage
* access controls
* audit logs
* user-controlled voice references
* clear third-party AI processing disclosures

---

# 📊 Current Status

## MVP Complete — Working Prototype

Speech Surgeon currently demonstrates the complete end-to-end workflow:

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
Generate replacement speech
     ↓
Surgically replace audio
     ↓
Attach repaired audio to original video
     ↓
Compare original vs repaired
     ↓
Optional lip-sync
     ↓
Download result
```

The workflow has been tested on:

* the scripted product demo
* separate recordings with different content
* a real hackathon/application video
* changing an event/hackathon name without rerecording the video

The project is currently best described as:

> **A working MVP for surgical speech editing in existing videos.**

---

# 💡 Product Philosophy

Speech Surgeon follows one simple principle:

> **Keep what is correct. Repair what changed.**

That means:

```text
Don't regenerate the face.
Don't regenerate the background.
Don't regenerate the screen recording.
Don't regenerate the entire timeline.

Repair the speech.
```

---

# 🚀 Future Product Vision

The immediate product is simple:

> **Change what you said without saying it again.**

But the larger opportunity is video maintenance.

Imagine an organization with thousands of recorded videos.

A product changes.

A price changes.

A software version changes.

A policy changes.

A date changes.

A company name changes.

Instead of manually searching through every video and deciding what needs to be rerecorded:

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

Eventually, recorded video could become something that is **maintained**, rather than something that becomes permanently outdated after publication.

---

# 🧭 Roadmap at a Glance

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

# ⭐ One-Line Pitch

> **Speech Surgeon lets you change what you said in an existing video without saying it again.**

---

# 🎤 Short Demo Pitch

> **Speech Surgeon is an AI speech repair tool for existing videos. You upload a video, edit the transcript, and it detects what changed, regenerates only that speech in your voice, surgically patches the original audio, and keeps the original video frames untouched.**

Optional follow-up:

> **And for talking-head videos, an optional lip-sync step can update the mouth movement after the speech is repaired.**

---

# 🏁 Built With

* **Fish Audio** — speech recognition and voice-preserving speech generation
* **FFmpeg** — audio extraction, surgery, normalization, and video remuxing
* **Sync Labs** — optional lip-sync enhancement
* **FastAPI** — backend API
* **Next.js** — frontend
* **React / TypeScript** — application UI

---

# 📄 License

MIT License