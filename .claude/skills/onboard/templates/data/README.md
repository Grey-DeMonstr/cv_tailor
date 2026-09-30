# data/ — the single source of truth

Everything in `jobs/*/cv.md` and `jobs/*/cover_letter.txt` must trace back to a line in this
folder. Nothing gets written into an application that is not first written down here.

Facts are written in the third person as a file convention. They describe the owner of this repo.

## Files

| File | Holds |
|---|---|
| `profile.md` | Identity, contacts, location, work authorization, languages, positioning |
| `experience.md` | Employment history: roles, dates, scope, achievements, gaps |
| `skills.md` | Skills by category, including leadership skills |
| `education.md` | Degrees, courses, certifications |
| `projects.md` | Side projects, open source, talks, publications |
| `stories.md` | Reusable anecdotes and motivations for cover letters |
| `preferences.md` | What is wanted from the next job, and what is refused |
| `voice.md` | How the owner writes: register, habits, phrases to avoid, application language |
| `sources/` | Original documents. Read-only inputs, never edited |
| `recommendations/` | Optional. Recommendations received, `<company>/<author> - <position>.txt` |

## Markers

Three markers make the state of a fact machine-readable. `get-cv` looks for them.

- `TODO(ask): <question>` — unknown fact. `get-cv` asks this when a vacancy needs it, then
  replaces the marker with the answer.
- `CONFLICT: <description>` — two sources disagree. Never use either version in an application
  until resolved. Ask, pick one, delete the marker.
- `STALE(<date>): <note>` — was true when written, may not be now. Verify before reuse.

## Writing facts

- One fact per bullet. A bullet that needs "and" twice is two facts.
- Absolute dates only — "June 2012", not "three years ago".
- Numbers where they exist: team sizes, percentages, durations, counts.
- Record the source in the section heading or a trailing `(source: ...)` when it is not obvious.
  A fact from the owner's own answer is `(source: user, <Month Year>)`, with the month it was given.
- Never soften or inflate a fact to make it fit a vacancy. Tailoring happens at generation time
  by *selecting* facts, never by *editing* them.
