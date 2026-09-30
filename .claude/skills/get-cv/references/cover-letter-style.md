# Cover letter style

Plain text, `jobs/<company>/cover_letter.txt`, in the language recorded in `data/voice.md`. Four or
five short paragraphs, 220–320 words. It is pasted into a form or an email body, so no markdown: no
`#`, no `*`, no `-` bullets, no bold.

Most cover letters are never read. The ones that are get read by a person deciding whether this
candidate understood the job. That is the only thing the letter has to prove. **Clarity beats
cleverness.**

## The voice

Read `data/voice.md` before writing. It records how the user sounds, the habits to keep, the
phrases they never use and the language they apply in. The letter should read as theirs.

`voice.md` decides how sentences sound. It never overrides the shape and the rules below, or the
rule that every claim traces to `data/`.

Where `voice.md` is silent, use these defaults:

- First person, plain words, no jargon. Short declarative sentences.
- Concrete systems instead of adjectives: "a billing service that handled 40,000 invoices a day",
  not "a robust, scalable solution".
- Says what the job actually *was*, not what the title claimed.
- Contractions are fine and preferred.
- No em dashes and no semicolons.

Samples quoted in `voice.md`, and earlier letters in `jobs/` or `data/sources/`, show **register
only** — how the sentences sound. They are not models for how a letter is built, and their
sentences are never reused: a sentence lifted from a sample turns up in every letter, which is
the interchangeable letter this method exists to prevent. Write the sample's sentences verbatim
only in `voice.md`, never in a letter. Letters written without this method usually fail in the same
ways; do not reproduce them:

| Failure | Why it fails |
|---|---|
| One letter sent to several companies with the name swapped | Interchangeable is the failure the whole method exists to prevent. |
| A paragraph that walks through past jobs | A résumé in prose. The CV already does this. |
| "I'd like to work at your company" as the opener | Does no work. Says nothing they can act on. |
| Nothing about what the job involves | The reader cannot tell the posting was understood. |
| "To be more detailed", "A bit more about me" | Filler transitions. Cut them. |
| Numbers or titles that are not in `data/`, or are marked `CONFLICT` | Unverified claims. |
| "For two years now", "recently" | Goes stale and keeps being sent. Use facts with absolute dates. |
| "I hope my experience can be useful to you." | Passive. No ask. |

## Shape

Requires the requirement map from `references/reading-the-vacancy.md`. Each paragraph has a job:

**1 — Who, and why this role.** The candidate's name, what they are, and the one or two skills that
answer pain point number one. Then the connection: how that background helps with the specific
problem the posting named.

**2 — The evidence.** The achievement that answers pain point one, in context, with a number or a
named system. Context, not a job list — the CV already lists the jobs.

**3 — The bridge.** Pain point two or three, or whatever links the candidate to *this* vacancy: a
domain overlap, a specific technology, recent work recorded in `data/`, a motivation from
`data/stories.md`. If a must-have is thin, this is where it is said honestly and framed by what is
being done about it.

**4 — Why this company.** The one specific true thing found in research. If research found nothing
real, this paragraph is about the work itself instead, and it stays short.

**5 — Close.** See below.

## The close depends on the channel

`position.md` records how the application is submitted. The rule keys off that:

- **A form that already collects name, email and phone** → close with one or two quiet lines. No
  contact block, no "Best regards". This is the default when the channel is unknown.
- **An email, or a free-text field with no contact fields** → add the explicit ask, one contact
  line, and sign off with the name. Email, phone and name are copied from `data/profile.md`:

  > I'd be glad to talk about how I could help. You can reach me at <email> or <phone>.
  >
  > Best regards,
  > <Full name>

Either way the ask is made once, plainly, without pressure.

## Rules

- **Answer their problem, not your history.** Every paragraph should survive the question "why does
  the hiring manager care?" If it doesn't, cut it.
- **Do not restate the CV.** The CV lists what the candidate did; the letter explains why it
  matters here.
- Mirror the posting's nouns, never its adjectives — see `references/reading-the-vacancy.md`.
- One motivation per letter. `data/voice.md` lists the motivations that exclude each other; never
  combine two of them.
- Never claim familiarity with a product without evidence in `data/`.
- No "I am writing to apply for the position of…". No "synergy", "passionate about excellence",
  "proven track record", "dynamic environment", "I would be a great fit", "leader in the industry".
  Everything under "Never write" in `data/voice.md` is banned as well.
- Answer the question that was asked. Do not follow a gap with a compensating paragraph about
  adjacent experience. If the posting asks about a technology, the answer is about that technology.
- Never editorialize about a gap. Banned outright: "That's a gap, not a thin match", and any
  variant that labels, grades or softens the gap after stating it. The gap is a plain fact in one
  sentence, and the sentence ends there. Commentary on a gap belongs in `notes.md`, never in text
  sent to a company.
- No throat-clearing frames before a point. Say the thing. Cut openers like "The boundary worth
  stating up front", "What is worth noting", "I should be straight about", and confiding asides
  like "I'd rather you hear it from me".
- Short sentences. If a sentence has two clauses joined by a comma and both stand alone, split it.

## Read it aloud before saving

Read the finished letter back as if explaining to a friend why this person would be good at this
job.

Three failures to listen for:

1. **Stiff or robotic** — a sentence the user would never say out loud. Rewrite it in plain words.
2. **Interchangeable** — could this letter be sent to a different company by swapping the name? Then
   paragraphs one and four aren't doing their job.
3. **A résumé in prose** — if paragraph two lists roles instead of telling one thing that happened,
   replace it with the story.

Over 320 words means a paragraph is doing the CV's job. Cut it.
