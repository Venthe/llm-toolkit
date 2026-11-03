import { test } from "node:test";
import assert from "node:assert/strict";
import * as fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { manage } from "../bin/llm-toolkit.js";

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "toolkit-"));
  t.after(() => fs.rm(root, { recursive: true, force: true }));
  const source = path.join(root, "source");
  const target = path.join(root, "project");
  await fs.mkdir(path.join(source, "skills/example"), { recursive: true });
  await fs.mkdir(path.join(source, "prompts"), { recursive: true });
  await fs.writeFile(path.join(source, "skills/example/SKILL.md"), "original");
  await fs.writeFile(path.join(source, "prompts/example.md"), "prompt");
  await fs.writeFile(path.join(source, "LICENSE"), "license");
  return { source, target, root, installed: path.join(target, ".agents") };
}

test("install copies and replaces matching names, including local edits and extra files", async (t) => {
  const { source, target, installed } = await fixture(t);
  const skill = path.join(installed, "skills/example");
  await fs.mkdir(skill, { recursive: true });
  await fs.writeFile(path.join(skill, "SKILL.md"), "local");
  await fs.writeFile(path.join(skill, "obsolete.md"), "old");
  await manage("install", source, target);
  assert.equal(
    await fs.readFile(path.join(skill, "SKILL.md"), "utf8"),
    "original",
  );
  await assert.rejects(fs.stat(path.join(skill, "obsolete.md")), {
    code: "ENOENT",
  });
  assert.equal((await fs.lstat(skill)).isSymbolicLink(), false);
  await fs.writeFile(path.join(source, "skills/example/SKILL.md"), "new");
  assert.equal(
    await fs.readFile(path.join(skill, "SKILL.md"), "utf8"),
    "original",
  );
  await manage("update", source, target);
  assert.equal(await fs.readFile(path.join(skill, "SKILL.md"), "utf8"), "new");
});

test("update can install and removal preserves other names", async (t) => {
  const { source, target, installed } = await fixture(t);
  await manage("update", source, target);
  const other = path.join(installed, "skills/other");
  await fs.mkdir(other);
  await fs.writeFile(path.join(other, "SKILL.md"), "keep");
  await fs.writeFile(path.join(installed, "prompts/other.md"), "keep");
  await manage("remove", source, target);
  await manage("remove", source, target);
  assert.equal(await fs.readFile(path.join(other, "SKILL.md"), "utf8"), "keep");
  assert.equal(
    await fs.readFile(path.join(installed, "prompts/other.md"), "utf8"),
    "keep",
  );
  await assert.rejects(fs.stat(path.join(installed, "skills/example")), {
    code: "ENOENT",
  });
  await assert.rejects(fs.stat(path.join(installed, "prompts/example.md")), {
    code: "ENOENT",
  });
});

test("linked target fails before writes and preserves external data", async (t) => {
  const { source, target, root } = await fixture(t);
  const external = path.join(root, "external");
  await fs.mkdir(external);
  await fs.mkdir(target);
  await fs.symlink(external, path.join(target, ".agents"), "junction");
  await assert.rejects(manage("install", source, target), /link/i);
  assert.deepEqual(await fs.readdir(external), []);
});

test("source overlap is rejected", async (t) => {
  const { source } = await fixture(t);
  await assert.rejects(
    manage("install", source, path.join(source, "skills")),
    /overlap/i,
  );
});

test("link mode links each skill, copies prompts, and supports switching modes", async (t) => {
  const { source, target, installed } = await fixture(t);
  await fs.mkdir(path.join(source, "skills/second"));
  await fs.writeFile(path.join(source, "skills/second/SKILL.md"), "second");
  await manage("install", source, target, { link: true });
  assert.equal(
    (await fs.lstat(path.join(installed, "skills"))).isSymbolicLink(),
    false,
  );
  for (const name of ["example", "second"]) {
    assert.equal(
      (await fs.lstat(path.join(installed, "skills", name))).isSymbolicLink(),
      true,
    );
  }
  assert.equal(
    (
      await fs.lstat(path.join(installed, "prompts/example.md"))
    ).isSymbolicLink(),
    false,
  );
  await fs.writeFile(path.join(source, "skills/example/SKILL.md"), "changed");
  assert.equal(
    await fs.readFile(path.join(installed, "skills/example/SKILL.md"), "utf8"),
    "changed",
  );
  await manage("update", source, target, { link: true });
  await manage("update", source, target);
  assert.equal(
    (await fs.lstat(path.join(installed, "skills/example"))).isSymbolicLink(),
    false,
  );
  await manage("update", source, target, { link: true });
  await manage("remove", source, target);
  assert.equal(
    await fs.readFile(path.join(source, "skills/example/SKILL.md"), "utf8"),
    "changed",
  );
});

test("broken skill links can be replaced without touching their targets", async (t) => {
  const { source, target, installed, root } = await fixture(t);
  await fs.mkdir(path.join(installed, "skills"), { recursive: true });
  await fs.symlink(
    path.join(root, "missing"),
    path.join(installed, "skills/example"),
    "junction",
  );
  await manage("install", source, target, { link: true });
  assert.equal(
    await fs.readFile(path.join(installed, "skills/example/SKILL.md"), "utf8"),
    "original",
  );
  await assert.rejects(fs.stat(path.join(root, "missing")), { code: "ENOENT" });
});
