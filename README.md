# CV Tailor

A template repo that lets a coding agent write a tailored CV and cover letter for every vacancy you
apply to, from one verified set of facts about you.

You keep your career history as plain files in `data/`. For each vacancy the agent reads the
posting, works out what the employer actually needs, selects the facts that answer it, and writes a
CV, a cover letter and a set of notes.

**The one rule:** every claim in a generated application must trace to a line in `data/`. The agent
selects and orders your facts. It never invents or inflates them. What it cannot evidence, it asks
you about, or reports as a gap.

## Quick start

You need git and a coding agent. Claude Code is the tested one; see [Agent support](#agent-support).

1. Clone the template and, if you want a remote copy, point it at a **private** repo of your own:

   ```
   git clone <this-repo-url> my-job-search
   cd my-job-search
   git remote rename origin template
   git remote add origin <your-private-repo-url>
   git push -u origin main
   ```

   The last two lines are optional. The repo works fine as a local folder. Clone rather than using
   GitHub's "Use this template" button: a shared history is what lets you pull updates later.

2. Open the folder with your agent and say **"set me up"**. The `onboard` skill reads your existing
   CV in whatever form you have it, asks one round of questions, and builds `data/`. No CV at all?
   It interviews you instead.
3. Paste a vacancy's text, or a link to it. The `get-cv` skill writes the application into
   `jobs/<company>/`.
4. Read `notes.md` first. It says what was emphasized, what could not be evidenced and where the
   application is weak.

## Privacy

Your copy will hold your contact details, your employment history and your applications.

- Keep it private. **A GitHub fork of a public repo is public**, so clone as shown above instead of
  forking.
- `*.pdf` is ignored by git, so PDF originals and exports stay on your machine. Everything else in
  `data/` and `jobs/`, including text sources, is committed if you commit, so the repo itself must
  be private.
- Your agent sends the files it reads to its model provider. That is how agents work; check your
  provider's data policy if it matters to you.

## How it works

| Path | What it is |
|---|---|
| `data/` | Your facts: profile, experience, skills, education, projects, stories, preferences, voice. Created by `onboard`. |
| `data/sources/` | Your original documents. Never edited. |
| `jobs/<company>/position.md` | The vacancy, verbatim. |
| `jobs/<company>/cv.md` | The tailored CV. |
| `jobs/<company>/cover_letter.txt` | The cover letter, plain text, ready to paste into a form. |
| `jobs/<company>/notes.md` | What the employer needs, which facts answer it, and what is missing. |

Three markers in `data/` show the state of a fact:

- `TODO(ask): ...` — not known yet. The agent asks when a vacancy needs it, then writes your answer
  down, so no question is asked twice.
- `CONFLICT: ...` — two of your documents disagree. Unusable until you say which is right.
- `STALE(date): ...` — was true once and needs checking.

To add or correct a fact, tell the agent. It is written into `data/` and used from then on.

Cover letters follow `data/voice.md`, which records how you write. Give `onboard` a few texts you
wrote yourself and the letters will sound like you.

## Agent support

The rules live in `AGENTS.md` and the skills in `.claude/skills/`. Claude Code is the agent this
was built and exercised with. The others are expected to work from their documentation, and
reports are welcome.

| Agent | Status | Notes |
|---|---|---|
| Claude Code | Tested | `CLAUDE.md` imports `AGENTS.md`. The skills appear as `/onboard` and `/get-cv`, and were exercised in dry runs through the `AGENTS.md` index as well. |
| Cursor, GitHub Copilot, OpenCode | Untested | They read `AGENTS.md` and `.claude/skills/`. |
| Codex CLI | Untested | Reads `AGENTS.md` but not `.claude/skills/`. The skill index at the end of `AGENTS.md` tells it which file to read. |
| Gemini CLI | Untested | Does not read `AGENTS.md` by default. Add `{ "context": { "fileName": ["AGENTS.md"] } }` to `.gemini/settings.json`. |

## Getting updates

Your facts and applications live in `data/` and `jobs/`, which the template never ships, so
updating cannot overwrite them:

```
git pull template main
```

## PDF export (optional)

```
python tools/to_pdf.py jobs/<company>/cv.md
python tools/to_pdf.py jobs/<company>/cover_letter.txt
```

Windows only for now. It needs Python, pandoc (for the CV) and Chrome or Edge. Any other
markdown-to-PDF route works just as well.

## Example

`examples/` holds a complete run for a fictional candidate: the input documents, the fact base
built from them, and one finished application.

## Licence

Copyright (C) 2026 Sergei Ivanov

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License version 3 as published by the Free Software Foundation. It is distributed
without any warranty. See `LICENSE` for the full text.

The licence covers the files this template ships. Your `data/`, your `jobs/` and every document
generated from them are yours and are not covered by it.
