---
name: onboard
description: Use when this repo has no data/ folder yet, when the user asks to get set up, get started or import their CV, or when they bring another source document (an older CV, a LinkedIn export, a past cover letter) to add to their facts.
---

# onboard

Builds the fact base in `data/` from whatever the user already has, then shows them how the repo
works.

**Core principle:** onboarding *transcribes*. A source document says what it says; the fact base
records that, marks what is missing or contradictory, and asks. It never improves a CV on the way
in, because every later application inherits whatever is written here.

## When to use

- `data/` does not exist. This is the first run.
- The user says "set me up", "get started" or "import my CV".
- The user brings a new source document later.

Do not use for: writing an application — that is `get-cv` — or recording a single fact the user
just told you, which is `get-cv` step 6.

## Workflow

### 1. Check the state

- **No `data/` folder** → copy every file from this skill's `templates/data/` into `data/` and
  create `data/sources/`. Continue with step 2.
- **`data/` exists** → this is *add-a-source* mode. Copy only template files that are missing from
  `data/`, and do not overwrite any file that is there. Run steps 2 to 4 for the new document only,
  skip step 5 unless the document is something the user wrote in their own voice, then report what
  changed.

### 2. Collect sources

Ask once what the user has. Any mix is fine:

- **Files.** A CV as PDF or DOCX, a LinkedIn profile saved as PDF, plain text. Ask them to put
  the files in `data/sources/`; if they name files elsewhere on disk, copy them into
  `data/sources/` unchanged.
- **Pasted text.** Save it as `data/sources/<short-name>.txt` before using it, so it stays on
  record.
- **Nothing.** Interview instead: each role with employer, title, start and end month; education;
  contacts. Save the answers as `data/sources/interview-<date>.txt`.

Read every source in full. `AGENTS.md` says how to read PDFs; for DOCX use `pandoc <file> -t plain`
if pandoc is installed. If a file cannot be read — a scanned PDF, no converter available — name the
file and ask the user to paste its text. **Never fill in the content of a file you could not read.**

Sources are read-only. Never edit a file in `data/sources/`.

### 3. Extract facts

Route each fact with `.claude/skills/get-cv/references/fact-files.md`. The house style is in
`data/README.md`.

- **Copy, don't improve.** Titles, dates, team sizes, percentages and technologies go in as the
  source states them.
- **One fact per bullet, absolute dates.**
- **Record the source**, on the section heading or the bullet: `(source: cv-2024.pdf)`. A fact
  that comes from the user's own answer is `(source: user, <Month Year>)`, with today's month.
- **A writing sample is a source too.** A motivation or an anecdote in a letter the user wrote goes
  into `stories.md` with the letter as its source, as well as shaping `voice.md`.
- **Vague stays vague.** "Some Go" is recorded as "some Go", not as a number of years.
- **Adjectives are not facts.** "Results-driven leader" is dropped. "Led a team of 6" is kept.
- **Sources disagree** → write both versions under a `CONFLICT:` marker. Never choose one.
- **Something an application will need is missing** → `TODO(ask): <question>` in place: a date
  with no month, a role with no achievement, no work authorization.
- **`skills.md` categories come from the user's own field.** A nurse's headings differ from a
  developer's. A skill shown in a role goes in `skills.md` and stays in the role's bullets.
- The placeholder line at the top of `data/profile.md` is removed at the end of step 4, not here.
- In add-a-source mode, add new facts and never delete or reword existing ones. Extending a
  fact's `(source: ...)` list because the new document confirms it is fine. If the new source
  contradicts a recorded fact, put a `CONFLICT:` marker next to it — unless the fact already notes
  that this value from this kind of source was ruled wrong, in which case nothing is raised.
- **When the user resolves a conflict**, keep one line saying what the losing source said and that
  it is wrong, so a later import of the same document does not raise the conflict again.

### 4. Ask — once, in a batch, then persist

One round, containing only:

1. Contact details for the CV (email, phone, profile link) and current city and country, where the
   sources lack them.
2. Work authorization: where the user can work without sponsorship.
3. Target roles and deal-breakers.
4. Each gap between roles longer than three months: what happened in it. A period covered by
   recorded full-time education is not a gap.
5. Every `CONFLICT` from step 3: which version is true.
6. Writing samples: one to three texts the user wrote themselves, such as cover letters, emails or
   posts. A letter among the source documents already counts as one. Always ask which phrases they
   would never want under their name. If they have no samples, also ask: do they write formally or
   plainly, and are they reserved or personal.
7. The language their applications are usually written in.
8. What they want from the next job, and why they are looking.

Everything else stays a `TODO(ask)`. `get-cv` asks those when a vacancy needs them; a forty-question
interview on day one is how people abandon the setup.

Write each answer into `data/` as soon as it arrives, replacing the marker it resolves. If the user
declines or does not know, leave the marker and move on. **Declined answers never block onboarding**
— a fact base with honest markers is a finished onboarding.

On a first run, when the batch is done, delete the placeholder line at the top of
`data/profile.md`, whether or not every question was answered. That line means "onboarding has not
happened"; what remains unknown is now marked with `TODO(ask)`, and `get-cv` asks for it when a
vacancy needs it.

In add-a-source mode, ask only the questions the new document raises.

### 5. Write the voice

Fill `data/voice.md` from the answers to questions 6 to 8:

- **With samples:** save them in `data/sources/`. Describe the register in three or four bullets,
  quote two short excerpts verbatim under Samples, and note habits: sentence length, contractions,
  punctuation.
- **Without samples:** record the answers. Sections the user did not address keep the template's
  defaults.
- Samples show how the user *sounds*. They are not quality models and say nothing about how a
  letter is built.
- Each motivation from question 8 becomes a `###` entry under Motivations in `data/stories.md`.
  Two motivations exclude each other when one letter could not honestly hold both: "I want a
  quieter role" and "I want to build a team from nothing", or "I want a two-person startup" and
  "I want the stability of a large employer". List each such pair in `voice.md` under "Motivations
  that exclude each other".

### 6. Report and teach

In add-a-source mode, report only what changed and which markers were added or resolved. On a
first run, in the conversation, briefly:

- What was loaded, one line per file, and how many `TODO(ask)` and `CONFLICT` markers remain.
- The rule: every line of an application must trace to `data/`. Nothing is invented, so a hole in
  `data/` stays a hole in the application until the user fills it.
- What to do next: paste a vacancy's text, or a link to it.
- Read `notes.md` first in every generated application. It says what could not be evidenced.
- To add a fact later, just say it. It is written into `data/`.
- A worked example is in `examples/`.
- Keep this repo private. It now holds personal data.

## Quick reference

| Situation | Action |
|---|---|
| `data/` already exists | Add-a-source mode. Overwrite nothing. |
| File cannot be read | Name it. Ask for a paste. Never guess. |
| A role's start or end has a year but no month | Record the year. `TODO(ask)` the month. Achievements inside a role need no month. |
| Two sources give different numbers | `CONFLICT:` with both. Ask in the batch. |
| CV says "expert in X" | Record X as a skill. Drop "expert". |
| User has no CV at all | Interview. Save the answers as a source. |
| User declines a question | Leave the marker. Carry on. |
| User has no writing samples | Three voice questions. Defaults for the rest. |
| Tempted to ask about every `TODO(ask)` | Don't. Only the eight items in step 4. |

## Red flags — stop

- "The CV says 2019–2021, so it was probably January to December."
- "'Managed a large team' — I'll write 10+."
- "The LinkedIn number is newer, so I'll use that one."
- "This summary paragraph is well written, I'll keep it as a fact."
- "`data/` exists but looks thin, I'll start again from the templates."
- "I'll ask these one at a time so it feels like a conversation."
- "They skipped the work authorization question, so I can't finish."
- "I couldn't open the PDF, but a CV like this usually says…"

All of these mean: go back to the step you skipped.
