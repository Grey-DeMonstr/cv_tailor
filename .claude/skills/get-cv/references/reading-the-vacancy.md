# Reading the vacancy

Turns `position.md` into a requirement map before a word is written. Both `cv.md` and
`cover_letter.txt` are generated against this map.

## 1. Find the pain points

Work from the **"What you'll do" / responsibilities** section, not the requirements list. The top
three items there are the company's biggest problems — they are what the application has to answer.
A requirements list describes an imaginary ideal candidate; a responsibilities list describes actual
unfinished work.

Then write the core problem in one sentence: *what is this job actually for?* A support role wants
someone who can calm angry customers. A platform role wants someone who can stop teams blocking each
other. Everything else is detail.

## 2. Build the two-column map

| Their need | Evidence in `data/` | Status |
|---|---|---|
| Improve customer retention | ... | evidenced / thin / absent |

Every one of the top three pain points gets a row, and every row must be answered somewhere in the
letter or the CV.

**Status meanings:**

- **evidenced** — a fact in `data/` directly covers it.
- **thin** — real but smaller in scale than what they asked for. Not a disqualifier. Someone who has
  run a 200-person newsletter can honestly answer "manage email campaigns"; the number goes in and
  speaks for itself.
- **absent** — nothing in `data/` touches it. Ask, then record as a gap.

## 3. The 60–70% rule

If roughly 60–70% of the must-haves are evidenced or thin, the application is worth writing.
**Never refuse to generate because of a shortfall, and never stretch a fact to close one.** A
shortfall is stated honestly and framed by what is being done about it:

> While I'm newer to X, I've spent the last N months building it through [specific thing]. For
> example, [concrete result].

That framing only works with a real activity behind it. If `data/` has none, the gap goes in
`notes.md` and the letter stays silent about it — silence beats a manufactured learning story.

## 4. Capture their vocabulary

Two lists, and they are treated in opposite ways.

**Their nouns — mirror these exactly.** If the posting says "CRM", write CRM, not "customer
database". If it says "platform", "pipeline", "incident", use their word. This is not a trick;
it is speaking their dialect, and it is how a human reader recognises that you understood the job.

**Their adjectives — never mirror these.** "Fast-paced", "world-class", "passionate", "dynamic",
"industry-leading". Echoing a company's self-description back at it conveys nothing except that the
posting was read.

The rule: **mirror the nouns, not the adjectives.**

## 5. Research the company — ten minutes, then stop

Look for exactly one specific, true thing worth reacting to. In order:

1. Links inside `position.md`.
2. The company's About page — stated values, but only where something concrete backs them up.
3. Their blog, changelog, or LinkedIn — a recent launch, a program, an engineering post.
4. The product itself.

| Bad | Good |
|---|---|
| "Your company is a leader in the industry." | "I saw your team launched a mentorship program last month." |
| "I admire your commitment to innovation." | "You partner with local schools for STEM workshops." |

**If ten minutes turns up nothing real, the posting's link is unreachable, or there is no web
access, skip it.** Fall back to saying
what about *the work* is genuinely appealing. An invented compliment is
worse than no compliment, and it is the single easiest thing for a hiring manager to spot.

**Never claim familiarity with a product unless `data/` records that the candidate has actually
used it.** Praise for a product the candidate has never opened gets caught in the first five minutes
of an interview.

## 6. Where the output goes

The map, the core-problem sentence, the vocabulary lists and the research finding all go into
`jobs/<slug>/notes.md`.

**They never go into `data/`.** `data/` holds facts about the candidate only. Company research is about a
company, and it goes stale the moment they ship something new.
