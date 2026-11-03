"""Behavioral regression checks using temporary skill collections."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from validate_skills import validate


class SkillValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def skill(self, name="example", frontmatter=None, body="# Example\n\nDo the requested task.\n"):
        path = self.root / name
        path.mkdir(exist_ok=True)
        metadata = frontmatter if frontmatter is not None else f"name: {name}\ndescription: Perform an example task."
        (path / "SKILL.md").write_text(f"---\n{metadata}\n---\n\n{body}", encoding="utf-8")
        return path

    def test_valid_folded_description_and_string_metadata(self):
        self.skill(frontmatter='name: example\ndescription: >-\n  Handle an example\n  task.\nmetadata:\n  version: "1.0"')
        self.assertEqual(validate(self.root), ([], [], 1))

    def test_rejects_invalid_metadata(self):
        cases = [
            "name: example\ndescription: ''",
            "name: example\ndescription: true",
            "name: different\ndescription: Task",
            "name: example\ndescription: Task\nversion: 1.0",
            "name: example\nname: example\ndescription: Task",
            "name: example\ndescription: Task\nmetadata:\n  version: 1",
            "name: example\ndescription: [unclosed",
            "name: example\ndescription: " + "a" * 1025,
            "name: example\ndescription: Task\ncompatibility: " + "a" * 501,
        ]
        for metadata in cases:
            with self.subTest(metadata=metadata[:80]):
                path = self.skill(frontmatter=metadata)
                self.assertTrue(validate(path)[0])

    def test_broken_link_is_reported(self):
        self.skill(body="Read [missing](references/missing.md).")
        errors, _, _ = validate(self.root)
        self.assertTrue(any("broken local link" in error for error in errors))

    def test_linked_asset_with_space_and_external_fragment(self):
        path = self.skill(body="[Guide](references/guide.md#section) [Web](https://example.com/a(b))")
        (path / "references").mkdir()
        (path / "assets").mkdir()
        (path / "references/guide.md").write_text("[Asset](<../assets/my template.txt>)", encoding="utf-8")
        (path / "assets/my template.txt").write_text("template", encoding="utf-8")
        self.assertEqual(validate(path), ([], [], 1))

    def test_orphan_resource_fails_even_when_present(self):
        path = self.skill()
        (path / "references").mkdir()
        (path / "references/orphan.md").write_text("Unreachable guidance", encoding="utf-8")
        self.assertTrue(any("not linked" in error for error in validate(path)[0]))

    def test_companion_skill_and_link_cycle(self):
        self.skill("first", body="[Second](../second/SKILL.md)")
        self.skill("second", body="[First](../first/SKILL.md)")
        self.assertEqual(validate(self.root), ([], [], 2))

    def test_fenced_links_are_examples(self):
        path = self.skill(body="Example:\n```markdown\n[Missing](absent.md)\n```\n\nDo the task.")
        self.assertEqual(validate(path), ([], [], 1))

    def test_reference_definition_is_checked(self):
        path = self.skill(body="[Missing][guide]\n\n[guide]: missing.md")
        self.assertTrue(validate(path)[0])

    def test_missing_entrypoint_and_empty_collection_fail(self):
        self.assertTrue(validate(self.root)[0])
        (self.root / "incomplete").mkdir()
        self.assertTrue(any("missing SKILL.md" in error for error in validate(self.root)[0]))

    def test_empty_body_and_bom_fail(self):
        path = self.skill(body="")
        self.assertTrue(validate(path)[0])
        entry = path / "SKILL.md"
        entry.write_text("\ufeff" + entry.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertTrue(validate(path)[0])

    def test_missing_document_fails(self):
        self.skill()
        self.assertTrue(validate(self.root, [self.root / "missing.md"])[0])

    def test_cli_exit_status_and_read_only_behavior(self):
        path = self.skill()
        entry = path / "SKILL.md"
        before = entry.read_bytes()
        script = Path(__file__).with_name("validate_skills.py")
        result = subprocess.run([sys.executable, "-B", str(script), str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(entry.read_bytes(), before)
        result = subprocess.run([sys.executable, "-B", str(script), str(path / "missing")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
