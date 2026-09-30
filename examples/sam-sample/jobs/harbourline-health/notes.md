# Notes — Senior Backend Engineer, Harbourline Health

Generated 30 September 2026. Read this before the CV or the letter: it says what could not be
evidenced.

## Core problem

A booking API and its appointments table have outgrown their design. The job is to make them fast
and reliable again for 300 clinics, run them properly on call, and bring two engineers along while
doing it.

## Pain points (top three of "What you'll do")

1. Own the appointment-booking API used by 300 clinics and bring its p95 response time under 200 ms.
2. Fix the scheduling database: the appointments table has outgrown its design and reports time out.
3. Run on-call for services on Kubernetes and improve how we handle incidents.

(4. Mentor two mid-level engineers — kept in the map below, outside the top three.)

## Requirement → evidence map

| Their need | Evidence in `data/` | Status |
|---|---|---|
| Booking API p95 under 200 ms | Rate-calculation service rewritten PHP to Python, p95 900 ms to 120 ms (experience.md, Larkfield). Different service, real number. | evidenced |
| Appointments table outgrown; reports time out | Monthly partitioning of a 400-million-row PostgreSQL events table; nightly report 50 min to 4 (experience.md). Talk on partitioning large PostgreSQL tables, October 2023 (projects.md). | evidenced |
| On-call for services on Kubernetes; improve incident handling | Set up the team's first on-call rotation and incident review process, 2022; on the rotation one week in six since (experience.md). Kubernetes: none in production, all container work on AWS ECS (skills.md). | thin — incidents evidenced, Kubernetes absent |
| Mentor two mid-level engineers | Leads a team of 6 at Larkfield; mentored 3 junior engineers at Pennine (experience.md). Levels of the 6 unknown (TODO(ask) in experience.md). | thin — juniors, not mid-level; leading 6 is real |
| 5+ years backend services in Python or Go | Python continuously June 2017 – present, both roles, about 9 years (experience.md, skills.md). Go: one internal CLI tool, 2023, about 800 lines, none in production. | evidenced (Python) |
| Deep PostgreSQL experience with large tables | 400-million-row partitioning; meetup talk October 2023 (skills.md, projects.md). | evidenced |
| Kubernetes in production | None. All container work on AWS ECS (skills.md, user answer September 2026). | absent |
| Experience leading a small team | Leads 6 engineers, March 2021 – present (experience.md, skills.md). | evidenced |
| Nice to have: healthcare data or clinical systems | None (experience.md, user answer September 2026). | absent |
| Remote (UK) | Preferences: remote within the UK; British citizen, no sponsorship needed (preferences.md, profile.md). | evidenced |

Must-haves: 3 of 4 evidenced (Python years, PostgreSQL, team lead); Kubernetes absent. 75%, above
the 60–70% threshold. Application written; shortfall stated plainly in the letter.

## Vocabulary

Their nouns, mirrored: appointment-booking API, clinics, p95, appointments table, scheduling
database, reports, on-call, incidents, Kubernetes, PostgreSQL, mentor, booking software,
independent clinics.

Their adjectives, avoided: fast-paced, world-class.

## Company research

Nothing found. The only link in the posting is on `harbourline.example`, a reserved example domain
that does not resolve, and no other company page was available. Paragraph four of the letter is
about the work instead, as the style reference requires. Nothing about the company or its product
appears in the letter or the CV.

## Fit assessment

Strong on the two biggest problems. Both pain points have a directly comparable, measured result
in `data/`: a service brought from 900 ms to 120 ms at p95, and a 400-million-row table partitioned
so a 50-minute report runs in 4. The talk on partitioning large PostgreSQL tables backs the
"deep PostgreSQL" requirement with something public. Team leadership and on-call are real and
recent. Domain preference (reliability that matters to real people, health named explicitly in
preferences.md) matches; remote UK matches.

Weak points, in order of how much they matter:

1. **Kubernetes.** A stated must-have and the platform for pain point three. Sam has none in
   production. The letter says so in one sentence. Expect this to be the first question in an
   interview; the honest answer is ECS since March 2021, containers throughout, Kubernetes not yet.
2. **Mentoring mid-level engineers.** The evidence is mentoring juniors (Pennine) and leading 6
   (Larkfield). The levels of the 6 are unknown. If any are mid-level, that is a stronger fact and
   should be recorded (marker left in experience.md).
3. **Healthcare.** Nice to have, absent. Left out of the letter and CV entirely.
4. **Scale comparison.** The posting gives 300 clinics; there is no recorded number for how many
   customers or requests the shipment-tracking API serves, so the letter cannot compare scale.
   Marker left in experience.md.
5. **Different service, same measure.** The 900 ms to 120 ms result is on the rate-calculation
   service, not the tracking API Sam leads. The letter says exactly which service; do not let it
   drift into "the API" in conversation.

## What was emphasised, what was left out

Emphasised: the p95 rewrite, the partitioning result, the on-call and incident review process, the
team of 6, the PostgreSQL talk. Summary and skills order lead with Python and PostgreSQL.

Left out: Redis and RabbitMQ stay in the skills line only (listed in the source CV, no role
evidence). The second motivation in stories.md (Larkfield freezing its platform) was not used; one
motivation per letter. Go is on the CV at its honest size (one 800-line internal tool) since the
posting says "Python or Go" and Python carries the requirement on its own.

## Gaps that survived step 6

- Kubernetes in production: user confirmed none. Recorded in skills.md and experience.md as a fact.
- Healthcare or clinical systems: user confirmed none. Recorded in experience.md.
- Scale of the shipment-tracking API: not answered ("I'd rather not say right now"). TODO(ask)
  left in experience.md.
- Levels of the 6 engineers and whether Sam mentors them directly: not answered. TODO(ask) left in
  experience.md.
- A measurable result from the incident process since 2022: not answered beyond the rotation
  cadence. Used the fact as it stands.

## Facts added to `data/` during this run (source: user, September 2026)

- `skills.md`: Go refined to one internal command-line tool in 2023, about 800 lines, none in
  production services.
- `skills.md`: Kubernetes, no production experience; all container work on AWS ECS.
- `skills.md`: on the Larkfield on-call rotation since setting it up in 2022, one week in six.
- `experience.md`: same on-call fact under the Larkfield role.
- `experience.md`: cross-cutting facts, no healthcare or clinical systems work; no production
  Kubernetes; Python since June 2017 confirmed.
- `experience.md`: two new `TODO(ask)` markers (tracking API scale; levels of the 6 engineers).

## Submission

Apply via the careers-page form: name, email, phone, CV, short cover letter. The form collects the
contacts, so the letter has no contact block. CV should be checked for page count before sending
(`python tools/to_pdf.py jobs/harbourline-health/cv.md`), though at this length it is one page.
