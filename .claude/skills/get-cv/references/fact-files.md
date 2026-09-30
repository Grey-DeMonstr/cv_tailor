# Where each fact goes

Routing table for step 6 of `get-cv`, and for `onboard` when it loads a source document. Each fact
goes in exactly one of these.

| Fact | File | Section |
|---|---|---|
| Contact detail, location, work authorization, spoken language | `data/profile.md` | Identity / Location / Languages |
| Positioning, headline, current status | `data/profile.md` | Positioning / Current status |
| A role, its dates, its scope, an achievement inside it | `data/experience.md` | The role's subsection |
| A technology, tool, platform, or leadership capability | `data/skills.md` | Matching category |
| A confirmed absence ("never ran X in production", "no work in domain Y") | `data/skills.md` | Matching category, as its own bullet |
| Degree, course, certification, competition | `data/education.md` | — |
| Side project, open-source repo, talk, conference, publication | `data/projects.md` | — |
| Anecdote, motivation, reason for wanting a job | `data/stories.md` | New `###` entry under the matching section |
| Target role, salary, relocation, deal-breaker, domain preference | `data/preferences.md` | — |
| How the user writes: register, habits, phrases to avoid, application language | `data/voice.md` | Matching section |

Ambiguous cases:

- An achievement **inside a job** → `experience.md`. A **standalone build** → `projects.md`.
- A skill demonstrated by a role goes in `skills.md` *and* stays in the role's bullets. Duplication
  between those two files is intended — `skills.md` is the index, `experience.md` is the evidence.
- A motivation that is really a constraint ("I want to leave advertising") → `preferences.md`.
- A motivation goes in `stories.md`. Which motivations cannot share a letter goes in `voice.md`.

## Writing the answer

Replace the marker, don't append next to it:

```diff
- - TODO(ask): Work authorization — citizen, permanent resident, or visa-dependent?
+ - Permanent resident since 2021; no sponsorship needed.
```

Resolving a `CONFLICT` means deleting the whole `CONFLICT:` block and correcting the fact it
referred to, in every file that repeats it. Conflicts about scope and titles tend to appear in both
`experience.md` and `skills.md`.

Keep the house style: one fact per bullet, absolute dates, numbers where they exist, no hedging
adverbs. If the user's answer is vague ("quite a lot of Go"), record it as vague rather than
sharpening it — `TODO(ask)` it again later if a vacancy depends on it.

## Adding a new fact with no marker

Append a bullet to the matching section. If no section fits, add a `##` heading rather than forcing
the fact somewhere wrong. If a whole new category of fact appears (patents, security clearance),
create the file and add it to the table in `data/README.md`.
