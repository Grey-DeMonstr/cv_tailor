# CV Tailor — working rules

This repo turns incoming vacancies into tailored applications: one folder per vacancy, each holding
the position description plus a CV and cover letter written for that specific role. Everything is
generated from one verified set of facts in `data/`.

**The owner of this repo is the user you are talking to.** They run their own job search here;
there is no third party. Their name and contacts are in `data/profile.md`. `data/` is written in
the third person as a file convention only — address the user directly, in the second person.

**First run.** If `data/` does not exist, run the `onboard` skill before anything else.

## Layout

```
data/                     Facts about the user. The single source of truth. See data/README.md.
  voice.md                How the user writes. Read before writing a cover letter.
  sources/                Original CVs and exports. Read-only inputs — never edit these.
  recommendations/        Optional. Recommendations received, <company>/<author> - <position>.txt
jobs/<company-slug>/
  position.md             The vacancy, verbatim, with a link to the posting.
  cv.md                   Generated.
  cover_letter.txt        Generated.
  notes.md                Generated. Fit analysis, requirement→evidence table, remaining gaps.
.claude/skills/           The skills. See the index at the end of this file.
tools/to_pdf.py           Optional PDF export.
examples/                 A worked example with a fictional candidate. Reference only.
```

Company folder names are lowercase slugs matching the company name (`acme`, `blue-river`,
`north.studio`). File names are fixed — do not invent variants.

`data/` and `jobs/` belong to the user. Every other path belongs to the template and may change
when the template is updated, so never store the user's content outside those two folders.
`examples/` is never a source of facts and is not edited during normal work.

## The iron rule

**Every claim in a generated CV or cover letter must trace to a line in `data/`.**

- No fact in `data/` → it does not go in the application. It goes in `notes.md` as a gap.
- Tailoring means *selecting, ordering and weighting* facts. It never means editing them.
- Titles, dates, team sizes, percentages and technologies are copied, not adjusted. A manager who
  led 12 engineers does not become one who led 20 because the vacancy is bigger.
- If a vacancy requires something the user has not done, say so in `notes.md`. Do not stretch an
  adjacent fact to cover it.

Violating the letter of this rule violates the spirit of it. "Reasonable inference", "obviously
implied by their seniority" and "any recruiter would assume this" are all fabrication.

## Facts are asked once and written down

When generating an application needs a fact that `data/` does not have:

1. Ask the user.
2. Write the answer into the right `data/*.md` file.
3. Only then use it.

A fact that exists only in the conversation is lost. Answering a question and generating from the
answer without persisting it is a bug, not a shortcut.

Unknowns are marked in place with `TODO(ask): <question>`, disagreements between sources with
`CONFLICT: <description>`, and facts that have expired with `STALE(<date>): <note>`.
`CONFLICT`-marked facts are unusable until resolved — see `data/README.md`.

## Workflow

1. The user gives a vacancy: the posting text or a link. A hand-written
   `jobs/<company-slug>/position.md` works too.
2. Run the `get-cv` skill.
3. Point the user to `notes.md` first — it says what could not be evidenced.
4. Questions the user answers are written back into `data/` before they are used.

## Voice

Cover letters are plain text, first person, short paragraphs, no corporate filler and no markdown.
CVs are third-person-implied bullets with no pronouns. How the user sounds is recorded in
`data/voice.md`; the rules every letter follows are in
`.claude/skills/get-cv/references/cover-letter-style.md`.

Applications are written against the vacancy's **pain points** — the top three items in its "what
you'll do" section — not against its requirements list. Mirror the posting's nouns, never its
adjectives. Clarity beats cleverness. See
`.claude/skills/get-cv/references/reading-the-vacancy.md`.

A letter that already exists in a job folder is the user's own. Never overwrite it, and never
regenerate over it, without being asked.

## Conventions

- Absolute dates everywhere. "March 2026", never "last year".
- Reading PDFs: use your own PDF reading if you have it. Otherwise run `pdftotext -layout <file> -`
  if poppler is installed. Otherwise ask the user to paste the text. Never guess the content of a
  file you could not read.
- Writing PDFs is optional: `python tools/to_pdf.py <file>` — `.txt` for cover letters, `.md` for
  CVs. Windows only; it needs Python, pandoc (for `.md`) and Chrome or Edge. Output lands next to
  the input as `<name>.pdf`. Letter styling is a plain A4 serif page with no contact header. Check
  the page count of a CV before it is sent.
- Do not commit unless asked.

## Skills

| Skill | Path | Use when |
|---|---|---|
| `onboard` | `.claude/skills/onboard/SKILL.md` | `data/` does not exist; the user asks to get set up or import a CV; the user brings another source document. |
| `get-cv` | `.claude/skills/get-cv/SKILL.md` | The user gives a vacancy as text, a link or a `position.md`; an application needs regenerating; the user wants a fact about themselves recorded. |

If your agent does not load skills automatically, read the `SKILL.md` at that path in full and
follow it, including the files under its `references/` folder that it points to.
