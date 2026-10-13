# The Upwork roast skill

Clients look at your Upwork search card for a few seconds and move on, and nobody tells you why. This skill does: five
reviewers roast your profile, each one separately, quote every weak line and say why it loses the job. Then it fixes
everything in your own voice, without inventing a single number.

## The five reviewers

| # | Reviewer | Sees | Looks for |
|---|---|---|---|
| 1 | **The Client in a Hurry** | Only the search card: title, rate, badge, first ~250 characters | Would I even click? |
| 2 | **The Tech Lead** | The whole profile | Do the technical claims and the portfolio hold up? |
| 3 | **The Field Expert** | The whole profile | Real specialist, or buzzwords and a keyword list? |
| 4 | **The Upwork Talent Scout** | The whole profile, plus Upwork's 2026 rules | Search words, Uma (Upwork's AI), the dynamic profile, rule breaks |
| 5 | **The Competitor** | The whole profile | Why a client would pick them instead |

Each reviewer roasts **your title first**, then quotes the exact weak lines with one reason each: **no numbers, too
wordy, no proof, too generic, or sounds AI-written**.

## What you get

1. **The title roast**: all five verdicts side by side.
2. **Each reviewer's opinion**, and what they all agree on, red flags first (contact details, misstated badges, photo rules).
3. **Fixes**, each in a copy-ready block with character counts:
   - 3 new titles, service keyword first
   - a rewritten overview whose first 200 characters hook the client
   - portfolio descriptions as problem → what I built → result
   - 15 ranked skills, plus 5 more if your editor allows 20
   - a short proposal template that matches the new profile
4. **`[ADD: ...]` questions** for every fact it needs from you. It never invents numbers, results or clients.

It talks to you in your language and writes all profile copy in English. Everything is saved to
`.upwork-roast/<date>-<name>/ROAST.md` where you run it.

## Built on research, not vibes

The rules come from a sourced research report ([research/upwork-roast-research-2026.md](research/upwork-roast-research-2026.md),
October 2026) that draws on Upwork's own Help Center and resources pages, academic studies of online hiring, and
labelled third-party data. The short version: **proof, not polish.**

- Clients judge your search card, which shows only about the first 250 characters of your overview, before anything else.
- Since AI made fluent writing free, tailored-sounding copy stopped predicting who gets hired. Clients now look for proof
  that is hard to fake: named results, linked contracts, review quotes.
- Upwork itself now names AI-sounding proposals as a growing reason clients discard applications. So the skill flags
  AI-sounding patterns and makes copy human through specifics, not fake chattiness.
- Simple, clear editing of profile text raised hires about 8% in a study of ~500,000 jobseekers. So the skill **edits your
  own words instead of replacing them**.
- Since May 28, 2026 Upwork has one dynamic profile that pulls your most relevant work forward for each client. So every
  service needs real, described portfolio items.

Upwork's own pages disagree on some limits (skills 15 vs 20, title length, portfolio 40/300 vs 70/600 characters). The
skill tells you when a limit is disputed. Your profile editor always wins.

## Install

Paste this into Claude Code:

```
https://github.com/aaksa/upwork-roast-skill
Install this skill, then confirm /upwork-roast works.
```

Or as a plugin:

```
/plugin marketplace add aaksa/upwork-roast-skill
/plugin install upwork-roast-skill@upwork-roast-skill
```

Or copy `skills/upwork-roast` into `~/.claude/skills/`. Open a new Claude Code session afterwards.

## Use

Export your profile as a PDF (open your profile in the browser and print it to PDF) and run:

```
/upwork-roast ~/Downloads/my-upwork-profile.pdf
```

Or type `/upwork-roast` and paste your profile text: title, rate, overview, skills, portfolio items with descriptions,
and work history with reviews. Try it on the example first:

```
/upwork-roast examples/sample-profile.md
```

One run is five sub-agent calls and counts toward your Claude plan's usage. Fill in every `[ADD: ...]` before you
publish anything: those gaps are where your real proof goes.

## Layout

```
skills/upwork-roast/
  SKILL.md                          the workflow
  references/reviewers.md           the five reviewer briefs, passed to each sub-agent word for word
  references/fix-rules.md           rules for every fix, voice rules, AI-sounding words and patterns
  references/upwork-facts-2026.md   how clients decide, field limits, platform rules, with sources
research/upwork-roast-research-2026.md   the full sourced research report
examples/sample-profile.md         a weak generalist profile to try it on
tests/test_skill.py
```

Change a reviewer by editing `reviewers.md`; change what a good fix looks like by editing `fix-rules.md`. Upwork
changes often: re-check `upwork-facts-2026.md` every few months.

## Good to know

- It roasts the profile, never the person, and judges a photo only on clarity and Upwork's photo rules.
- It flags contact details and anything that moves clients or payment off Upwork, since that breaks Upwork's terms.
- It's an opinion from language models, not a guarantee of invites or hires.
- Not affiliated with Upwork or Anthropic.

Run the tests with `python3 -m unittest discover -s tests`.

## Credit

Part of a set with [upwork-hiring-panel-skill](https://github.com/aaksa/upwork-hiring-panel-skill), which runs a review
panel on proposals. The multi-reviewer idea was first adapted from
[hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill) by Alex Chen (MIT).
