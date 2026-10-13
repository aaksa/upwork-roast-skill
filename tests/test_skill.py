import json
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SKILL_DIR = os.path.join(ROOT, "skills", "upwork-roast")

REVIEWERS = ("The Client in a Hurry", "The Tech Lead", "The Field Expert", "The Upwork Talent Scout", "The Competitor")
REASONS = ("no numbers", "too wordy", "no proof", "too generic")


def read(*parts):
    with open(os.path.join(SKILL_DIR, *parts)) as f:
        return f.read()


class RoastSkillTest(unittest.TestCase):
    def setUp(self):
        self.skill = read("SKILL.md")
        self.reviewers = read("references", "reviewers.md")
        self.rules = read("references", "fix-rules.md")

    def test_frontmatter(self):
        self.assertTrue(self.skill.startswith("---\nname: upwork-roast\n"))
        front = self.skill.split("---")[1]
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, front)

    def test_five_reviewers(self):
        for i, who in enumerate(REVIEWERS, 1):
            self.assertIn(who, self.skill)
            self.assertIn("## %d. %s" % (i, who), self.reviewers)
        self.assertIn("Start five sub-agents at once", self.skill)

    def test_title_first(self):
        self.assertIn("**3a. The title, first.**", self.skill)
        self.assertIn("TITLE ROAST:", self.reviewers)
        self.assertLess(self.reviewers.index("TITLE ROAST:"), self.reviewers.index("WEAK LINES:"))

    def test_weak_line_reasons(self):
        for reason in REASONS:
            self.assertIn(reason, self.skill)
            self.assertIn(reason, self.reviewers)

    def test_fixes(self):
        for part in ("3 new titles", "first 200 characters", "problem → what I built → result",
                     "15 ranked core skills", "proposal template"):
            self.assertIn(part, self.skill)
        self.assertIn("never over 70", self.rules)
        self.assertIn("Service noun first", self.rules)
        self.assertIn("add if your editor allows 20", self.rules)
        self.assertIn("40 characters or fewer", self.rules)

    def test_never_invent(self):
        self.assertIn("Never invent numbers or results", self.skill)
        self.assertIn("fact sheet", self.skill)
        self.assertIn("zero placeholders", self.skill)
        self.assertIn("Make it stronger", self.rules)
        self.assertIn("Keep the user's audience", self.rules)
        self.assertIn("Test the hook blind", self.skill)

    def test_language(self):
        self.assertIn("language they write to you in", self.skill)
        self.assertIn("ALL profile copy in English", self.skill)

    def test_research_grounding(self):
        facts = read("references", "upwork-facts-2026.md")
        self.assertIn("references/upwork-facts-2026.md", self.skill)
        self.assertIn("2026-10-13", facts)
        for tag in ("[Upwork]", "[Academic]", "[Third-party]"):
            self.assertIn(tag, facts)
        self.assertIn("sounds AI-written", self.skill)
        self.assertIn("sounds AI-written", self.reviewers)
        self.assertIn("Self-check before showing the fixes", self.skill)
        self.assertIn("**Facts to pass:**", self.reviewers)

    def test_example_and_research(self):
        with open(os.path.join(ROOT, "examples", "sample-profile.md")) as f:
            self.assertIn("**Overview:**", f.read())
        self.assertTrue(os.path.exists(os.path.join(ROOT, "research", "upwork-roast-research-2026.md")))
        self.assertIn("research/upwork-roast-research-2026.md", read("references", "upwork-facts-2026.md"))

    def test_manifests_are_valid_json(self):
        for name in ("plugin.json", "marketplace.json"):
            with open(os.path.join(ROOT, ".claude-plugin", name)) as f:
                self.assertEqual(json.load(f)["name"], "upwork-roast-skill")

    def test_blind_hook_test(self):
        hook = read("references", "hook-test.md")
        self.assertIn("references/hook-test.md", self.skill)
        self.assertIn("Never tell a judge which card is the freelancer's", hook)
        self.assertIn("different slot in every lineup", hook)
        self.assertIn("synthetic competitor cards", hook)
        self.assertIn("after 3 rounds", hook)
        self.assertIn("CARDS I'D OPEN", hook)

    def test_voice(self):
        self.assertIn("Edit, don't replace.", self.rules)
        self.assertIn("Business first.", self.rules)


if __name__ == "__main__":
    unittest.main()
