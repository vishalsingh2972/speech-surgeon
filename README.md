# Speech Surgeon

> **Edit what you said without saying it again.**

Speech Surgeon is an AI-powered spoken-content editing tool designed to repair small mistakes or changes in an existing recording without requiring the speaker to record the changed part again.

The core idea is simple:

1. Upload a video or audio recording.
2. Speech Surgeon extracts/normalizes the audio when necessary.
3. Fish Audio transcribes the speech into an editable, timestamped transcript.
4. Select the sentence or phrase that needs to change.
5. Replace the text.
6. Reconstruct the edited speech using the original speaker's voice.
7. Surgically fit the generated speech into the original audio.
8. Compare the original and repaired versions.
9. Export the repaired audio or repaired video.

Speech Surgeon is **not another text-to-speech wrapper**. The goal is to make recorded speech behave more like an editable digital medium: instead of rerecording an entire take because of one small mistake or post-recording change, a user can modify the local spoken content while preserving the rest of the original performance.

---

## The Problem

Spoken content is often almost impossible to revise cleanly after recording.

A creator, podcaster, teacher, developer advocate, marketing team, narrator, or production team may finish a recording and discover that one sentence contains:

- an incorrect date
- the wrong product name
- an outdated price
- a factual correction
- a changed URL or promo code
- a pronunciation mistake
- a version number that has changed
- a missed phrase
- a wording change requested after recording

With a traditional workflow, the options are usually:

- record the sentence again
- schedule another recording session
- cut around the mistake
- accept an obvious audio patch
- regenerate an entire voiceover and lose the original performance

Speech Surgeon explores a different workflow:

```text
Record once
    ↓
Find the mistake or outdated line
    ↓
Edit the words
    ↓
Reconstruct only the affected speech
    ↓
Blend it back into the original
    ↓
Keep everything else untouched
```

### Example

Original:

> “We launched the product in **March**.”

Edited:

> “We launched the product in **September**.”

The user should not need to record the sentence again.

---

# Why This Matters

Speech Surgeon is based on a simple observation:

> **Digital content is increasingly editable after capture, but spoken recordings are still treated as largely fixed artifacts.**

Text can be edited after writing.

Code can be patched after being written.

Images and video can be retouched after capture.

Spoken recordings still commonly require a new take when one local part changes.

Speech Surgeon explores a new editing primitive:

```text
record → transcribe → edit → reconstruct → patch
```

The product starts with small phrase/sentence repairs and can eventually grow into a broader system for maintaining, versioning, localizing, and creatively directing spoken media.

---

# Real-World Use Cases

Speech Surgeon is intentionally useful beyond a single generic “change a word” demo. The underlying engine can support many practical workflows where recorded speech becomes outdated or needs correction.

## Creator & Sponsored Video Corrections

A creator finishes a sponsored video and the brand later changes:

- the promo code
- the discount
- the price
- a product name
- a URL

Instead of reshooting the entire video, the affected spoken line can be repaired.

**Target users:** YouTubers, influencers, creator agencies, brand marketing teams, video editors.

---

## Podcast Sponsor Read Surgery

A podcast host records a sponsor message and the advertiser later changes the offer or promo code.

Speech Surgeon can target only the sponsor section instead of requiring another recording session.

**Target users:** podcasters, podcast networks, advertisers, podcast production agencies.

---

## Developer Tutorial & DevRel Updates

A software tutorial can become outdated when a company changes:

- product names
- UI labels
- API versions
- commands
- pricing
- feature names

Speech Surgeon can repair the spoken references without rebuilding the entire recording.

**Target users:** developer-relations teams, SaaS companies, technical educators, course creators.

---

## Online Course & EdTech Maintenance

A teacher records hundreds of lessons and later needs to update a batch year, version number, policy, product name, or other small spoken reference.

For example:

> “This lesson is for the **2026 batch**.”

can become:

> “This lesson is for the **2027 batch**.”

without forcing a complete rerecording.

**Target users:** educators, coaching institutes, online course companies, instructional-design teams.

---

## Corporate Training Updates

Internal training libraries can become stale when policies, product names, prices, or procedures change.

Speech Surgeon can explore a workflow for repairing small spoken references while leaving the rest of the presentation intact.

**Target users:** enterprise learning teams, HR/L&D teams, training agencies, internal communications teams.

---

## Product & Marketing Video Maintenance

A company may have dozens or hundreds of product videos containing old:

- pricing
- release versions
- feature names
- campaign language
- product terminology

The long-term opportunity is to search transcripts across a content library and identify recordings that need surgical updates.

**Target users:** SaaS marketing teams, product marketing teams, agencies, content operations teams.

---

## Audiobook & Narration Corrections

Narrators and publishers sometimes discover a wrong name, date, pronunciation, or editorial change after recording.

Speech Surgeon can explore local repair without regenerating the entire chapter.

**Target users:** narrators, publishers, audiobook studios, voice-production teams.

---

## Documentary / Production ADR Patches

A documentary or production voiceover may need a small factual or script correction after the original session.

The long-term direction is to make localized ADR-style repairs faster while preserving the original performance around the edit.

**Target users:** documentary teams, production houses, editors, post-production studios.

---

# Product Vision

Speech Surgeon is based on a larger thesis:

> **Recorded speech should become an editable digital artifact.**

The initial version focuses on high-quality phrase/sentence repair in a clean, single-speaker recording.

The longer-term direction can include:

- text-level speech edits
- performance edits
- localized edits
- edit history
- versioning
- library-wide content maintenance
- video-aware repair
- eventually, broader AI-assisted audio direction

The first release intentionally solves a much narrower problem: **high-quality local reconstruction of spoken content.**

---

# What Makes Speech Surgeon Different

Speech Surgeon is deliberately positioned between a speech model and a traditional audio editor.

### Fish Audio provides the speech intelligence

Fish Audio is used for the parts that require high-quality speech understanding and synthesis:

- speech-to-text
- timestamped transcription
- speaker voice reconstruction / voice models
- expressive speech synthesis

### Speech Surgeon provides the editing layer

Speech Surgeon is responsible for:

- mapping transcript segments back to audio regions
- letting the user edit spoken content
- selecting the correct source region
- constructing contextual generation input
- preparing the surgery request
- fitting generated speech to the source timing
- handling boundaries and transitions
- matching local loudness and characteristics
- rebuilding the final recording
- visualizing exactly what changed
- preserving the original recording

The central product value therefore comes from the combination:

```text
                 FISH AUDIO
                     │
       ┌─────────────┼─────────────┐
       │             │             │
      STT       Voice Identity     TTS
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
               SPEECH SURGEON
                     │
       ┌─────────────┼─────────────┐
       │             │             │
     ALIGN         EDIT          PATCH
       │             │             │
       └─────────────┼─────────────┘
                     │
                     ▼
              REPAIRED RECORDING
```

---

# End-to-End Product Flow

```mermaid
flowchart TD
    A["User uploads video or audio"] --> B["Audio extraction / preflight / normalization"]
    B --> C["Fish Audio STT"]
    C --> D["Timestamped transcript"]
    D --> E["Waveform + transcript editor"]
    E --> F["User selects phrase / sentence"]
    F --> G["User edits replacement text"]
    G --> H["Build contextual reconstruction request"]
    H --> I["Prepare authorized speaker voice"]
    I --> J["Fish Audio S2.1 Pro TTS"]
    J --> K["Generated replacement audio"]
    K --> L["Duration analysis"]
    L --> M["Controlled time fitting"]
    M --> N["Boundary alignment"]
    N --> O["Loudness / local characteristic matching"]
    O --> P["Crossfade + composition"]
    P --> Q["Surgically repaired audio"]
    Q --> R{"Input was video?"}
    R -- "No" --> S["Original vs repaired audio"]
    R -- "Yes" --> T["Replace original video audio track"]
    T --> U["Repaired video"]
    S --> V["Export"]
    U --> V
```

---

# System Architecture

```mermaid
flowchart LR
    USER["User"] --> WEB["Next.js / React Web App"]
    WEB --> API["FastAPI Backend"]

    API --> SESSION["Session Manager"]
    API --> FISH["Fish Audio Service"]
    API --> AUDIO["Audio Surgery Engine"]
    API --> FILES["Temporary File Manager"]

    FISH --> ASR["Fish STT"]
    FISH --> VOICE["Fish Voice Model / Voice Reference"]
    FISH --> TTS["Fish S2.1 Pro TTS"]

    AUDIO --> FFMPEG["FFmpeg"]
    AUDIO --> DSP["Python Audio Processing"]

    FILES --> TMP["Temporary Session Storage"]

    AUDIO --> OUTPUT["Original + Patch + Repaired Audio"]
    OUTPUT --> VIDEO["Optional Video Remux"]
    VIDEO --> WEB
    OUTPUT --> WEB
```

---

# User Experience

Speech Surgeon intentionally keeps the product surface small.

The primary experience is composed of three major states.

## 1. Upload

The user can upload a video or audio recording.

Conceptually:

```text
┌────────────────────────────────────────────┐
│                                            │
│          Drop video or audio here         │
│                                            │
│             MP4 · MOV · WAV               │
│             MP3 · M4A                     │
│                                            │
│              [ Analyze ]                  │
│                                            │
└────────────────────────────────────────────┘
```

Internally, the application becomes audio-first even when the source is a video:

```text
Video
  ↓
Extract audio
  ↓
Speech Surgeon audio pipeline
```

The MVP should favor short, clean, single-speaker recordings so the reconstruction problem remains well controlled.

---

## 2. Edit

After transcription, the application presents:

- waveform
- playback controls
- timestamped transcript
- selectable segments
- editable replacement text
- surgery controls

Conceptually:

```text
┌────────────────────────────────────────────────────┐
│ SPEECH SURGEON                                     │
│                                                    │
│  ▶ ───────────────●───────────────────────        │
│    00:04                              00:12        │
│                                                    │
│  We launched the product in March.                 │
│                                 ^^^^^              │
│                                                    │
│  Replace with                                      │
│  [ We launched the product in September. ]         │
│                                                    │
│                 [ SURGERIZE ]                      │
└────────────────────────────────────────────────────┘
```

The user should not need to understand the underlying AI workflow.

They are simply editing what they want the recording to say.

---

## 3. Result

After the surgery is complete, the user receives a focused A/B comparison:

```text
┌──────────────────────────────────┐
│ ORIGINAL                         │
│ ▶ “We launched in March.”        │
└──────────────────────────────────┘

                VS

┌──────────────────────────────────┐
│ SURGICALLY REPAIRED              │
│ ▶ “We launched in September.”   │
└──────────────────────────────────┘

Changed: 1 segment

[ PLAY ORIGINAL ]   [ PLAY REPAIRED ]

               [ EXPORT ]
```

For video input, the repaired audio can be remuxed back into the original video container so the user receives a repaired video as well.

The interface should clearly show that the rest of the recording was preserved.

---

# Why Phrase / Sentence Surgery Comes First

The first release intentionally focuses on phrase or sentence replacement rather than promising arbitrary word-level editing.

A user might visually change:

```text
March → September
```

but the underlying system can regenerate the surrounding phrase or sentence:

```text
“We launched the product in September.”
```

This provides the speech model with linguistic context and gives the audio pipeline a more coherent unit to reconstruct.

True word-level surgery is a harder problem because the replacement may differ substantially in:

- duration
- phonetic context
- stress
- coarticulation
- sentence rhythm
- prosody

Word-level surgery is therefore considered a future alignment and reconstruction enhancement rather than a requirement for the first release.

---

# Technical Architecture

## Frontend

### Next.js

The web application is planned with:

- Next.js
- React
- TypeScript

Responsibilities:

- upload interface
- waveform rendering
- transcript rendering
- transcript editing
- segment selection
- surgery controls
- processing status
- audio/video comparison
- export

### Tailwind CSS

Used for application styling and responsive layout.

### shadcn/ui

Used for reusable interface components such as:

- buttons
- inputs
- dialogs
- tabs
- tooltips
- status indicators
- progress states

### wavesurfer.js

Used for:

- waveform visualization
- playback
- seeking
- region selection
- changed-region highlighting

---

# Backend

## Python + FastAPI

FastAPI acts as the orchestration layer between the browser, Fish Audio, and the audio-processing system.

The browser must not receive the Fish API key.

```text
Browser
   ↓
Speech Surgeon API
   ↓
Fish Audio
```

Backend responsibilities include:

- session management
- upload handling
- audio extraction
- audio preflight
- audio normalization
- Fish API calls
- transcript normalization
- voice-model preparation
- surgery orchestration
- audio rendering
- optional video remuxing
- file cleanup
- error handling

---

# Fish Audio Integration

Speech Surgeon is built around three primary Fish capabilities for the MVP.

## 1. Fish Speech-to-Text

The recording is sent through Fish's speech recognition API to obtain transcript content and timing information.

The application uses timestamped transcript segments as the editing map between text and audio.

Conceptually:

```json
{
  "text": "We launched the product in March.",
  "start": 4.21,
  "end": 7.34
}
```

Fish API documentation:

- https://docs.fish.audio/api-reference/endpoint/openapi-v1/speech-to-text

The application converts the provider response into its own normalized transcript representation rather than coupling the frontend directly to the provider response format.

---

## 2. Fish Voice Model / Voice Reference

Speech Surgeon needs a way to reconstruct changed speech while preserving the identity of the original speaker.

The planned approach is to create or use a private speaker voice model/reference from authorized source audio.

Fish API documentation:

- https://docs.fish.audio/api-reference/endpoint/model/create-model

Voice assets should be treated as session-scoped material in the MVP.

The product should make this process invisible to the user where possible:

> **Use the voice from this recording.**

---

## 3. Fish S2.1 Pro TTS

Fish S2.1 Pro is used to synthesize the edited phrase using the prepared speaker voice.

Fish's current product positioning emphasizes expressive speech and natural-language voice direction, which provides a path for future “performance surgery” features in addition to simple text replacement.

Fish API documentation:

- https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech

Model documentation:

- https://docs.fish.audio/developer-guide/models-pricing/models-overview

---

# Fish Audio Responsibilities vs Speech Surgeon Responsibilities

| Stage | Speech Surgeon | Fish Audio |
|---|---:|---:|
| Video/audio upload | ✅ | |
| File validation | ✅ | |
| Audio extraction | ✅ | |
| Audio normalization | ✅ | |
| Speech recognition | | ✅ |
| Timestamped transcript | | ✅ |
| Transcript editor | ✅ | |
| User edit | ✅ | |
| Voice preparation | | ✅ |
| Speaker voice reconstruction | | ✅ |
| TTS generation | | ✅ |
| Duration analysis | ✅ | |
| Timing fit | ✅ | |
| Boundary handling | ✅ | |
| Crossfade | ✅ | |
| Loudness matching | ✅ | |
| Final audio composition | ✅ | |
| Video audio-track replacement | ✅ | |
| Original/repaired comparison | ✅ | |
| Export | ✅ | |

The boundary is intentional: **Fish provides speech intelligence; Speech Surgeon provides the surgical editing workflow.**

---

# Audio Surgery Engine

The surgery engine is the central application-specific component.

Conceptually:

```text
SurgeryRequest
    │
    ├── session
    ├── source segment
    ├── original text
    ├── replacement text
    └── speaker voice
          │
          ▼
    validate request
          │
          ▼
    extract target region
          │
          ▼
    construct TTS context
          │
          ▼
    generate replacement
          │
          ▼
    analyze duration
          │
          ▼
    fit timing
          │
          ▼
    align boundaries
          │
          ▼
    match loudness / local characteristics
          │
          ▼
    crossfade
          │
          ▼
    assemble final audio
```

This layer is deliberately kept separate from the Fish client.

That means:

- Fish integration can change independently.
- Audio processing can improve independently.
- The frontend does not need to know how either implementation works.

---

# Audio Pipeline

```mermaid
flowchart TD
    A["Original Audio"] --> B["Normalize input"]
    B --> C["Transcribe with Fish"]
    C --> D["Identify target segment"]
    D --> E["Extract local context"]
    E --> F["Prepare authorized speaker voice"]
    F --> G["Generate replacement with Fish S2.1 Pro"]
    G --> H["Measure generated duration"]
    H --> I["Controlled time fitting"]
    I --> J["Refine boundaries"]
    J --> K["Match loudness / local characteristics"]
    K --> L["Crossfade replacement"]
    L --> M["Reassemble original + patch"]
    M --> N["Render final audio"]
    N --> O{"Source was video?"}
    O -- "No" --> P["Audio export"]
    O -- "Yes" --> Q["Replace original video audio track"]
    Q --> R["Video export"]
```

---

# Audio Preflight

Before sending the recording into the core pipeline, Speech Surgeon should inspect:

- duration
- sample rate
- number of channels
- file format
- basic silence profile
- rough speech/noise characteristics

Inputs can be normalized into a predictable internal format before downstream processing.

A controlled internal representation makes the rest of the audio pipeline easier to test.

The MVP should prefer:

- one speaker
- clear speech
- limited background noise
- limited reverberation
- no overlapping speech

---

# Voice Reference Preparation

A speaker reference is needed to reconstruct the changed speech.

The target flow is:

```text
Original recording
      ↓
Find clean speech region
      ↓
Create temporary voice reference
      ↓
Create / use private Fish voice model
      ↓
Use model for replacement generation
```

The long-term UX should make this invisible to the user.

The intended interaction is simply:

> **Use the voice from this recording.**

The system handles the reference preparation internally.

---

# Contextual Reconstruction

The system should preserve enough local linguistic context when generating the replacement.

For example, instead of asking the model to generate:

```text
September
```

it may be better to reconstruct:

```text
We launched the product in September.
```

and then replace the corresponding source region.

This provides the synthesis model with more context for:

- rhythm
- pronunciation
- sentence-level prosody
- transitions
- natural phrasing

The exact context-window strategy can evolve after listening tests.

---

# Duration Matching

Generated speech will not necessarily have the same duration as the original segment.

Example:

```text
Original selected segment:   2.14 sec
Generated replacement:       2.48 sec
```

Speech Surgeon should therefore calculate a duration ratio and apply controlled timing adjustment.

A practical first approach is:

```text
ratio = target_duration / generated_duration
```

Extreme adjustments should not be forced.

If the replacement is substantially longer or shorter than the source, the UI can encourage the user to use a more compact phrase.

Example:

> **This replacement changes the rhythm substantially. Try a shorter phrase for a more natural result.**

---

# Boundary Handling

Exact ASR boundaries are useful but are not necessarily perfect splice points.

Speech Surgeon should be able to use small amounts of contextual padding around the selected segment and refine the final transition point using local audio characteristics.

The goal is to avoid an obvious:

```text
ORIGINAL → AI PATCH → ORIGINAL
```

sound.

The desired result is:

```text
ORIGINAL → seamless continuation → ORIGINAL
```

---

# Crossfading

A hard cut between original and generated speech may expose tiny differences in phase, room tone, pitch, or level.

Speech Surgeon therefore uses short crossfades when reconstructing the region.

The exact duration of the crossfade should be tuned empirically using the evaluation set.

---

# Loudness Matching

The synthesized patch may be slightly louder or quieter than the source recording.

Before insertion, the audio engine should compare local source characteristics and adjust patch gain so the transition does not create an obvious level jump.

Later iterations may also include more advanced local spectral/tone matching.

---

# Video Handling

Video support is intentionally thin in the MVP.

Speech Surgeon does not attempt to become a full video editor.

The video path is:

```text
Input MP4/MOV
     ↓
Extract audio
     ↓
Perform Speech Surgeon surgery
     ↓
Render repaired audio
     ↓
Replace original audio track
     ↓
Export repaired video
```

The visual track should remain unchanged.

The first public demonstration should favor edits whose spoken replacement is naturally compatible with the speaker's visible performance rather than making perfect audiovisual lip-sync a core engineering requirement.

Advanced audiovisual alignment can be explored later if the product requires it.

---

# Audio File Strategy

The original recording should never be overwritten.

A session may contain:

```text
session_xxx/
├── original_source
├── normalized.wav
├── transcript.json
├── reference.wav
├── patch_01.wav
└── repaired_01.wav
```

The principle is:

> **Original source is immutable; surgeries produce new versions.**

This also creates a foundation for future version history.

---

# Proposed Internal API

The browser should communicate with application-level endpoints rather than directly exposing Fish API contracts.

```text
POST   /api/sessions
POST   /api/sessions/:id/upload
POST   /api/sessions/:id/transcribe
POST   /api/sessions/:id/voice
POST   /api/sessions/:id/surgery

GET    /api/sessions/:id
GET    /api/sessions/:id/audio/original
GET    /api/sessions/:id/audio/repaired
GET    /api/sessions/:id/video/repaired

DELETE /api/sessions/:id
```

These endpoints are an architectural starting point and can evolve as implementation details become clearer.

---

# Session State

A session can progress through a controlled state machine:

```text
CREATED
   ↓
UPLOADED
   ↓
PREPROCESSED
   ↓
TRANSCRIBING
   ↓
TRANSCRIBED
   ↓
VOICE_READY
   ↓
READY_TO_EDIT
   ↓
SURGERIZING
   ↓
RENDERING
   ↓
READY
```

Failure states should be explicit:

```text
ERROR_UPLOAD
ERROR_PREPROCESSING
ERROR_TRANSCRIPTION
ERROR_VOICE
ERROR_TTS
ERROR_RENDER
```

This prevents the UI from getting stuck on generic loading states.

---

# Planned Repository Structure

```text
speech-surgeon/
├── apps/
│   └── web/
│       ├── app/
│       ├── components/
│       ├── hooks/
│       └── lib/
│
├── services/
│   └── api/
│       ├── routes/
│       ├── services/
│       │   ├── fish/
│       │   ├── audio/
│       │   └── surgery/
│       ├── models/
│       └── utils/
│
├── audio/
│   ├── preprocessing/
│   ├── alignment/
│   ├── rendering/
│   └── mixing/
│
├── tests/
│   ├── audio/
│   ├── surgery/
│   └── api/
│
├── docs/
│   └── architecture/
│
├── .env.example
├── README.md
└── LICENSE
```

The final structure may change during implementation, but the main separation should remain:

```text
Web UI
   ↓
API orchestration
   ↓
Fish integration
   +
Audio surgery engine
   ↓
Optional video remuxing
```

---

# Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Web framework | Next.js | Frontend application |
| UI | React | Interactive interface |
| Language | TypeScript | Frontend type safety |
| Styling | Tailwind CSS | UI styling |
| Components | shadcn/ui | Reusable interface primitives |
| Waveform | wavesurfer.js | Audio visualization and regions |
| Backend | Python + FastAPI | API and orchestration |
| Audio CLI | FFmpeg | Conversion, composition, export, video remuxing |
| Audio processing | Python audio tooling | Analysis and signal processing |
| Speech recognition | Fish Audio STT | Transcript generation |
| Voice reconstruction | Fish Audio Voice Models | Speaker identity |
| Speech synthesis | Fish Audio S2.1 Pro | Replacement speech generation |
| MVP storage | Temporary files | Session-scoped audio/video assets |
| Future storage | S3/R2-compatible object storage | Persistent project assets |
| Future database | PostgreSQL | Persistent projects/version history |

---

# MVP Scope

## Supported

- short video or audio recordings
- single speaker
- clean spoken content
- phrase/sentence replacement
- same-language editing
- authorized speaker voice reconstruction
- waveform + transcript editing
- original/repaired A/B comparison
- audio export
- repaired video export when the input is video

## Not part of the first version

- multiple overlapping speakers
- arbitrary noisy environments
- music-heavy recordings
- full digital audio workstation functionality
- unrestricted word-level replacement
- automatic fact checking
- automatic script correction
- advanced lip-sync correction
- automatic mass-library updating
- multilingual surgery
- public voice marketplace
- account/team management
- billing
- social sharing inside the application

These are intentionally deferred so the first version can focus on reconstruction quality and a convincing user workflow.

---

# Product Demonstration Concept

The public demonstration is designed around a very recognizable production problem.

### Setup

A creator records a short video or spoken clip.

### Mistake

A line becomes outdated or incorrect after recording.

Example scenarios:

```text
Sponsor code changed
Product name changed
Price changed
Date changed
Version changed
Course batch year changed
```

### Repair

The user opens Speech Surgeon, edits the transcript, and clicks **SURGERIZE**.

### Result

The corrected line plays in the same speaker's voice while the rest of the recording remains unchanged.

The strongest demonstration is one where the before/after difference is obvious to the viewer but the actual product interaction remains simple:

```text
Original recording
       ↓
“This offer uses code SAVE20.”
       ↓
Edit transcript
       ↓
“This offer uses code SAVE25.”
       ↓
SURGERIZE
       ↓
Repaired recording
```

The exact demonstration scenario may change, but the principle remains: **show a realistic reason someone would need a post-recording correction.**

---

# Quality Criteria

The central product question is not whether Fish can pronounce the replacement.

The question is whether the replacement **sounds like it belonged in the original recording**.

Speech Surgeon should evaluate every surgery against:

## 1. Voice Identity

Does the replacement sound like the same speaker?

## 2. Continuity

Does it fit the surrounding speech naturally?

## 3. Timing

Does the replacement preserve the original pacing closely enough?

## 4. Boundary Quality

Can the splice be heard?

## 5. Loudness

Is the replacement noticeably louder or quieter?

## 6. Text Accuracy

Did the generated audio actually say what the user requested?

## 7. Overall Plausibility

Would a listener believe the revised sentence was part of the original take?

For video input, an additional consideration is:

## 8. Visual Compatibility

Does the replacement avoid creating an obvious audiovisual mismatch with the source footage?

Perfect lip-sync is not a first-release requirement; the product should first optimize for convincing audio reconstruction.

---

# Evaluation Examples

A small controlled evaluation set should be used during development.

### Test 1 — short substitution

```text
March → May
```

### Test 2 — date change

```text
March → September
```

### Test 3 — number change

```text
3,000 → 5,000
```

### Test 4 — product name change

```text
Product Alpha → Product Beta
```

### Test 5 — sponsor code

```text
SAVE20 → SAVE25
```

### Test 6 — version change

```text
Version 2.4 → Version 3.0
```

### Test 7 — proper noun

Replace a company, person, product, or location name.

### Test 8 — moderately longer replacement

Use a replacement that expands the phrase length but remains within a practical timing range.

### Test 9 — expressive sentence

Use an excited or emotional sentence to test performance continuity.

### Test 10 — pronunciation-sensitive text

Use words with difficult phonetic transitions.

The same source recording should be reused when comparing algorithmic improvements.

---

# Safety, Consent, and Voice Ownership

Speech Surgeon is designed around **authorized voice editing**.

Users should only process voices they own or have permission to modify.

The product should be positioned around use cases such as:

- repairing the user's own content
- correcting authorized interviews
- fixing company-owned recordings
- revising permitted voice-talent recordings

The product should not encourage unauthorized impersonation or cloning of public figures or other people without permission.

Where practical, uploaded recordings and generated voice assets should remain session-scoped and be removed after processing.

---

# Privacy Approach

The MVP can follow a temporary-processing model:

```text
Upload
  ↓
Process
  ↓
Generate
  ↓
Export
  ↓
Delete session assets
```

Persistent storage is not required for the core experience.

If persistent projects are introduced later, retention and deletion controls should be designed explicitly rather than added as an afterthought.

---

# Error Handling

The application should report problems in product language rather than exposing raw provider errors.

### Unsupported multi-speaker recording

> **This version of Speech Surgeon supports one speaker at a time.**

### Weak reference audio

> **We couldn't find a clean enough voice reference. Try a clearer recording.**

### Excessive timing change

> **This replacement changes the rhythm substantially. Try a shorter phrase.**

### Unsupported video/editing condition

> **This recording needs a simpler edit for the current version of Speech Surgeon.**

### Fish/API failure

> **The speech service could not complete this request. Please try again.**

The frontend should never expose API credentials or raw internal configuration.

---

# Design Principles

## Edit, don't regenerate

Preserve as much of the original recording as possible.

## Context matters

Give the synthesis system enough local linguistic information to produce natural speech.

## Quality beats feature count

One convincing surgery is more valuable than many unreliable editing controls.

## Original audio is immutable

Never destroy the user's source recording.

## Make the change visible

The user should always understand which portion was modified.

## Fail honestly

Not every recording or edit will be equally reconstructible.

## Video stays thin

Video support exists to deliver a practical end-to-end creator workflow; Speech Surgeon is fundamentally an audio-reconstruction product, not a general-purpose video editor.

## Voice ownership matters

Voice reconstruction should be used only with appropriate authorization.

---

# Future Direction

Speech Surgeon is intentionally designed so the MVP can grow into a broader spoken-media editing system.

## Performance Surgery

Instead of only changing what was said:

> “Keep the words, but make this sound more confident.”

The system could regenerate the local performance using expressive voice controls.

---

## Word-Level Surgery

Introduce a finer-grained alignment engine capable of isolating and reconstructing smaller units than full phrases.

---

## Multilingual Surgery

Edit one sentence in the source language and propagate the change into localized versions.

Example:

```text
English source
      ↓
edit sentence
      ↓
patch English
      ↓
patch Hindi
      ↓
patch Japanese
      ↓
patch Spanish
```

---

## Library-Wide Content Maintenance

Search transcripts across a content library and identify every recording containing an outdated term.

Example:

```text
Product name changed:
Atlas → Orbit

Video 01  → 3 matches
Video 04  → 1 match
Video 07  → 4 matches
Video 12  → 2 matches
```

A future workflow could allow approved bulk surgery across selected recordings.

---

## Video Surgery

Extend the same concept into more advanced video workflows:

```text
Video
  ↓
Extract audio
  ↓
Speech Surgeon
  ↓
Patch audio
  ↓
Replace audio track
  ↓
Export video
```

Future versions can explore stronger audiovisual alignment where needed.

---

## Surgery History / Voice Git

Every change can become a version:

```text
Original
   ↓
Surgery 01
   ↓
Surgery 02
   ↓
Surgery 03
```

This creates a foundation for a future version-control system for spoken media.

---

## AI Audio Director

A longer-term evolution could let users make high-level creative requests such as:

> “Make the scene feel more tense, but keep the narrator restrained.”

The system could eventually coordinate:

- voice performance
- pacing
- emphasis
- ambience
- sound effects
- transitions

Speech Surgeon would then become a focused first step toward a broader **AI-native audio editing environment**.

---

# Product Evolution

```text
Speech Surgeon
      │
      ├── Phrase Surgery
      │       ↓
      ├── Performance Surgery
      │       ↓
      ├── Word-Level Surgery
      │       ↓
      ├── Multilingual Surgery
      │       ↓
      ├── Library-Wide Maintenance
      │       ↓
      ├── Video Surgery
      │       ↓
      ├── Surgery History / Voice Git
      │       ↓
      └── AI Audio Director
```

This is a directional product vision rather than a promise that every future feature will be implemented.

---

# Example Architecture Walkthrough

A complete surgery for a simple recording may look like this:

```text
1. User uploads video/audio
          ↓
2. Speech Surgeon extracts/normalizes audio when needed
          ↓
3. Fish STT produces transcript + timestamps
          ↓
4. User selects the sentence
          ↓
5. User changes “March” to “September”
          ↓
6. Speech Surgeon prepares a clean speaker reference
          ↓
7. Fish voice model/reference is prepared
          ↓
8. Fish S2.1 Pro generates contextual replacement speech
          ↓
9. Speech Surgeon measures generated duration
          ↓
10. Patch is time-fitted to source region
          ↓
11. Patch boundaries are refined
          ↓
12. Loudness/local characteristics are matched
          ↓
13. Patch is crossfaded into source
          ↓
14. Repaired audio is rendered
          ↓
15. If input was video, repaired audio replaces the source audio track
          ↓
16. User compares original vs repaired
          ↓
17. User exports the repaired result
```

---

# What Speech Surgeon Is Trying to Prove

The prototype is testing one specific hypothesis:

> **A recorded voice can be treated as editable content rather than a fixed artifact.**

If that works reliably, a much larger family of capabilities becomes possible:

```text
Recorded Speech
      ↓
Understand
      ↓
Edit
      ↓
Reconstruct
      ↓
Blend
      ↓
Version
      ↓
Maintain
      ↓
Localize
      ↓
Direct
```

Speech Surgeon starts with the smallest useful version of that idea: **repair a sentence without asking the speaker to record it again.**

---

# Built With Fish Audio

Speech Surgeon uses Fish Audio as the speech intelligence layer for transcription, speaker voice reconstruction, and expressive speech synthesis.

Fish Audio:

- https://fish.audio/

Developer documentation:

- https://docs.fish.audio/

Speech-to-text API:

- https://docs.fish.audio/api-reference/endpoint/openapi-v1/speech-to-text

Voice model creation:

- https://docs.fish.audio/api-reference/endpoint/model/create-model

Text-to-speech API:

- https://docs.fish.audio/api-reference/endpoint/openapi-v1/text-to-speech

Model overview:

- https://docs.fish.audio/developer-guide/models-pricing/models-overview

---

# Project Status

**Early development / prototype**

The product direction is defined around high-quality single-speaker phrase/sentence repair with optional video input/output. The current focus is validating the reconstruction and audio-surgery pipeline before expanding into longer-form, multilingual, versioned, or performance-aware workflows.

---

# License

License information will be added when the public implementation is finalized.
