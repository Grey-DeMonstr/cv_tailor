---
name: get-cv
description: Use when the user gives a vacancy (pasted text, a link, or a jobs/<company>/position.md) and needs a tailored CV and cover letter, when an existing application needs regenerating or refreshing, or when the user wants a new fact about themselves recorded.
---

# get-cv

Generates `cv.md`, `cover_letter.txt` and `notes.md` for one vacancy, from the facts in `data/`.

**Core principle:** the application is a *selection* from `data/` aimed at the problems the vacancy
actually describes. If a requirement has no backing fact, the answer is to ask, or to record a gap —
never to write something plausible.

## When to use

- The user gives a vacancy: pasted text, a link, or an existing `jobs/<company>/position.md`.
- An existing application needs regenerating after facts changed.
- The user wants a fact recorded about themselves (step 6 applies on its own, with
  `references/fact-files.md`).

Do not use for: first-time setup or importing a CV — that is the `onboard` skill — or for editing
letters the user wrote by hand.

## Before you start

If `data/` does not exist, or `data/profile.md` still contains the line
`TEMPLATE: not filled in yet`, stop and run the `onboard` skill
(`.claude/skills/onboard/SKILL.md`). There are no facts to select from yet, and drafting from the
conversation instead breaks the core principle.

## Workflow

### 1. Take in the vacancy

The vacancy arrives in one of three forms:

- **Pasted text.** Work out the company, create `jobs/<slug>/` and write `position.md` in the
  format below.
- **A link.** Fetch the page and write `position.md` from it. If the fetch fails, there is no web
  access, or what comes back lacks the responsibilities and requirements (a login wall, a cookie
  page, a truncated preview), ask the user to paste the text. Never rebuild a posting from a search
  snippet.
- **An existing `jobs/<slug>/position.md`.** Use it as it is.

The slug is the company name in lowercase with spaces as hyphens (`acme`, `blue-river`,
`north.studio`). If that folder already holds a *different* role at the same company, use
`<company>-<role>` (`acme-backend`). Never overwrite an existing `position.md` without asking.

```markdown
# <Role title> — <Company>

- Link: <URL, or "none given">
- Captured: <today's date, e.g. 30 September 2026>
- Apply via: <form | email | unknown>

## Posting

<the posting text, verbatim>
```

The posting text is copied verbatim. Never summarize, translate or tidy it: step 2 depends on its
exact nouns.

If all you have is a job title or a company name, **stop and ask for the vacancy text.** Do not
generate against a job title alone — a title is not a position description, and guessing the
requirements produces the generic application this whole repo exists to avoid.

### 2. Read the vacancy

Follow `references/reading-the-vacancy.md` sections 1–4. Produce: the top three pain points from the
"what you'll do" section, the core-problem sentence, the full requirement list, and the two
vocabulary lists (their nouns to mirror, their adjectives to avoid).

### 3. Research the company

Follow `references/reading-the-vacancy.md` section 5. Ten minutes, looking for one specific true
thing. Finding nothing is an acceptable outcome and is recorded as such — an invented compliment is
worse than none.

### 4. Load facts

Read `data/README.md`, then the fact files, including `data/voice.md`. Note every `TODO(ask)`, `CONFLICT` and `STALE` marker
relevant to this vacancy.

### 5. Map requirements to evidence

Build the two-column map: each requirement marked **evidenced**, **thin**, or **absent**. A
`CONFLICT`-marked fact counts as unknown until resolved — never silently pick the more flattering
version.

Apply the 60–70% rule: a shortfall against the must-haves does not stop the application, and does
not license stretching a fact to cover it.

### 6. Ask — once, in a batch, then persist

Collect every unknown and ask them **in a single round**, not one at a time across the generation.
Ask only what this vacancy needs; unrelated `TODO(ask)` markers stay where they are.

If the posting is written in a different language from the one recorded in `data/voice.md`, add one
question to the batch: which language should this application be in? That answer is written to
`position.md` as a `- Language:` line and used for this application only; `data/voice.md` keeps
the usual language. If `voice.md` has no language recorded yet, ask for the usual one as well and
write it there.

Then, before generating anything: write each answer into the correct `data/*.md` file, replacing the
marker it resolves. See `references/fact-files.md` for routing.

**The write to `data/` happens before the write to `jobs/`.** An answer used in a CV but not saved
is lost, and the next vacancy asks the same question again.

If the user declines to answer, leave the marker — or add a `TODO(ask)` with the question where
none existed — and treat the requirement as a gap in step 10. Facts the user volunteers without
being asked are written to `data/` too.

### 7. Generate `cv.md`

Follow `references/cv-template.md`. Same true history every time; what changes per vacancy is which
bullets appear, in what order, and which phrasing of a fact is chosen.

### 8. Generate `cover_letter.txt`

Follow `references/cover-letter-style.md`, which starts from `data/voice.md`. Plain text — no markdown, no bullet syntax, no headers.
Every one of the three pain points is answered in the letter or the CV.

### 9. Read it aloud

Run the three checks at the end of `references/cover-letter-style.md`: does it sound like a person,
could it be sent to another company unchanged, does paragraph two tell a story or list jobs. Fix
before saving, not after.

### 10. Generate `notes.md`

The requirement→evidence map covering every item from step 2, the core-problem sentence, the
research finding (or a note that there wasn't one), an honest fit assessment, the gaps that survived
step 6, and the facts added to `data/` during this run.

Company research lives here, never in `data/`.

### 11. Report

Tell the user what was emphasized, what was left out, and where the application is weak. The weak
points matter more than the strong ones — they are what the user needs to prepare for.

## Quick reference

| Situation | Action |
|---|---|
| `data/` missing or still the template | Stop. Run `onboard`. |
| Only a job title or a company name | Stop. Ask for the vacancy text. |
| Link fails, or returns a login wall or a preview | Ask the user to paste the text |
| Second role at a company already in `jobs/` | New folder `<company>-<role>` |
| Posting is all buzzwords | Work from "what you'll do", ignore the adjectives |
| Only ~65% of must-haves met | Apply anyway. State the shortfall honestly. |
| Requirement is met at smaller scale | **thin** — use it, with the real number |
| Requirement has no fact at all | Ask in the step 6 batch |
| User answers a question | Write it to `data/*.md` **before** using it |
| User declines to answer | Leave the marker; record as a gap in `notes.md` |
| Sources disagree | `CONFLICT` — unusable until the user resolves it |
| Research finds nothing real | Say nothing about the company. Write about the work. |
| Posting says "CRM" | Write CRM. Mirror their nouns. |
| Posting says "fast-paced" | Never echo it back. |
| Fact exists but is unflattering | Include or omit; never reword it |
| Vacancy wants 10y of X, the candidate has 4 | Write 4. State the gap in `notes.md`. |
| A letter already exists in the folder | Leave it. Ask before overwriting. |
| Tempted to model the letter on an existing one | Don't. Take register only — see the style reference. |

## Common mistakes

- **Skipping the pain points and working from the requirements list.** The requirements describe an
  imaginary ideal candidate; the responsibilities describe the actual unfinished work.
- **Writing a letter that restates the CV.** The CV lists what the candidate did. The letter explains why it
  matters *here*. If a paragraph survives being moved into the CV, it belongs in the CV.
- **Forgetting the "why should they care".** Every claim links to something the posting asked for.
- **Asking questions one at a time.** Batch them in step 6.
- **Using an answer without saving it.** The fact base never grows and the same questions recur.
- **Echoing the posting's adjectives.** Mirror nouns, never adjectives.
- **Generic company flattery.** "A leader in the industry" is worse than saying nothing.
- **Inflating scope to match the role.** 12 engineers is 12 engineers.
- **Copying `stories.md` entries wholesale.** They are raw material; the letter is written fresh.
- **Treating earlier letters as templates.** A letter in another job folder or in `data/sources/`
  shows register, not structure. Copying its structure produces an interchangeable letter.
- **Using mutually exclusive motivations.** `data/voice.md` lists the motivations that contradict
  each other. One per letter.
- **Silently dropping a requirement** with no matching fact. Every requirement appears in the
  `notes.md` map, including the failures.
- **Putting company research in `data/`.** `data/` is facts about the candidate. Research goes in
  `notes.md`.
- **Tidying the posting.** `position.md` holds the text verbatim; a summary loses the nouns step 2
  needs.

## Red flags — stop

- "Any senior engineer would have done this, it's safe to write."
- "The data says 12 but the vacancy is bigger, so I'll say 20+."
- "The candidate is missing three must-haves, I shouldn't generate this." — apply the 60–70% rule.
- "I'll write a learning story about the missing skill" — only if `data/` records a real activity.
- "They probably value innovation, I'll say I admire that."
- "I'll note the gap instead of asking" — asking comes first; gaps are what remains after asking.
- "I'll save the fact to `data/` after generating." No. Before.
- "The position description is thin, I'll work from the job title."
- "It reads a bit stiff but the content is right." — step 9 exists for exactly this.
- "An earlier letter does it this way." — earlier letters are register samples, not models.
- "The link didn't load, I'll work from the search snippet."
- "`data/` is empty, but I can draft from what the user just told me."

All of these mean: go back to the workflow step you skipped.
