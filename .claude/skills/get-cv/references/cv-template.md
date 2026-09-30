# CV template

Markdown, `jobs/<company>/cv.md`. Target two pages printed. Same true history for every vacancy —
what changes is selection, order and emphasis.

## Structure

```markdown
# <Full name from data/profile.md>
<Headline chosen for this vacancy>

<City, Country> · <email> · <phone> · <profile link>

## Summary
<3–4 lines. Facts, not adjectives.>

## Skills
**<Category from data/skills.md>:** ...
**<Category>:** ...

## Experience

### <Title> — <Company>
*<Month Year> – <Month Year> · <Location>*

- <Achievement bullet>
- <Achievement bullet>

## Education

## Projects        <!-- only if it carries weight for this vacancy -->
```

The name and the contact line are copied from `data/profile.md`. Leave out any contact the profile
does not record; never write a placeholder.

## Tailoring rules

**Headline.** Pick one of the headlines listed under Positioning in `data/profile.md`. If several
are listed, take the one closest to the vacancy: a leadership vacancy takes the leadership
headline, a hands-on vacancy the hands-on one. Do not invent a new one.

**Summary.** Three or four lines, each a fact the vacancy cares about, aimed at the core problem
identified in `references/reading-the-vacancy.md`. No adjective that isn't earned by a number or a
named system.

**Their nouns, not their adjectives.** If the posting calls it a "platform", "pipeline" or "CRM",
use their word for it — a reader scanning for their own vocabulary should find it. Never reuse their
self-description: "fast-paced", "world-class", "industry-leading" say nothing about the candidate.
Mirroring never changes a recorded measurement or its name: "p95 latency" in `data/` stays "p95
latency" even when the posting says "response time".

**Skills.** Categories in order of relevance to the vacancy; within a category, relevant items
first. Only list what `data/skills.md` has. If a language is recorded as exploratory, it does not
appear among the headline skills of a vacancy built on it — it appears where it honestly sits, or
not at all.

**Experience.** Reverse chronological, always. Never reorder roles by relevance — that reads as
concealment. What *is* tailored:

- How many bullets each role gets. Recent and relevant roles get 4–6; distant roles get 1–2.
- Which bullets. Pull from `data/experience.md`; drop the ones irrelevant to this vacancy.
- Roles older than ~15 years can compress to a single line, but the dates stay.

**Gaps stay visible.** A gap or career break recorded in `data/experience.md` appears on the CV as
its own entry, with what was done in it. Hiding a gap invites the exact question it was hidden to
avoid.

**Education.** One line unless the vacancy is research-adjacent.

**Projects.** Include only when a project evidences a specific requirement. An empty projects
section is better than a padded one. The heading names what is in it: "Projects", "Talks",
"Publications", or a combination.

## Hard constraints

- Bullets start with a verb, contain no pronouns, and carry a number wherever `data/` has one.
- Every bullet traces to a line in `data/`. No exceptions, no inference, no rounding up.
- Dates and titles are copied exactly from `data/experience.md`.
- No skill bars, no percentage-of-proficiency, no "expert/advanced" self-ratings.
- No photo, no date of birth, no marital status.
- If two bullets say the same thing in different words, keep one.
- Every one of the vacancy's top three pain points is answered by a bullet here or a paragraph in
  the cover letter. Check before saving.
