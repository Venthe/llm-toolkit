#!/usr/bin/env node
import * as fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

async function stat(location) {
  try {
    return await fs.lstat(location);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

async function rejectLinks(location) {
  for (let current = location; ; current = path.dirname(current)) {
    if ((await stat(current))?.isSymbolicLink())
      throw new Error(`Linked path: ${current}`);
    if (path.dirname(current) === current) break;
  }
}

async function validateTree(location) {
  const info = await stat(location);
  if (info?.isSymbolicLink()) throw new Error(`Linked path: ${location}`);
  if (info?.isDirectory()) {
    for (const name of await fs.readdir(location))
      await validateTree(path.join(location, name));
  } else if (info && !info.isFile())
    throw new Error(`Unsupported file: ${location}`);
}

function inside(parent, child) {
  const relative = path.relative(parent, child);
  return (
    relative === "" ||
    (!relative.startsWith(`..${path.sep}`) &&
      relative !== ".." &&
      !path.isAbsolute(relative))
  );
}

export async function manage(action, source, project, { link = false } = {}) {
  if (!["install", "update", "remove"].includes(action))
    throw new Error("Expected install, update, or remove");
  source = path.resolve(source);
  const target = path.resolve(project, ".agents");
  await rejectLinks(target);
  if (
    inside(target, source) ||
    ["skills", "prompts"].some((folder) =>
      inside(path.join(source, folder), target),
    )
  ) {
    throw new Error("Source and target overlap");
  }
  const entries = [];
  for (const folder of ["skills", "prompts"]) {
    const base = path.join(source, folder);
    await rejectLinks(base);
    for (const name of await fs.readdir(base)) {
      const from = path.join(base, name);
      await validateTree(from);
      const info = await stat(from);
      if (
        folder === "skills"
          ? !info.isDirectory() ||
            !(await stat(path.join(from, "SKILL.md")))?.isFile()
          : !info.isFile() || !name.endsWith(".md")
      )
        continue;
      entries.push({
        from,
        to: path.join(target, folder, name),
        skill: folder === "skills",
      });
    }
  }
  for (const name of ["LICENSE", "ATTRIBUTIONS.md"]) {
    const from = path.join(source, name);
    if (await stat(from)) {
      await validateTree(from);
      entries.push({ from, to: path.join(target, "llm-toolkit", name) });
    }
  }
  // Preflight every selected destination before replacing any matching name.
  for (const { to, skill } of entries) {
    if (!inside(target, to) || to === target)
      throw new Error(`Invalid destination: ${to}`);
    await rejectLinks(path.dirname(to));
    if (!(skill && (await stat(to))?.isSymbolicLink())) await validateTree(to);
    for (let parent = path.dirname(to); ; parent = path.dirname(parent)) {
      const info = await stat(parent);
      if (info && !info.isDirectory())
        throw new Error(`Not a directory: ${parent}`);
      if (parent === path.dirname(parent)) break;
    }
  }
  for (const { from, to, skill } of entries) {
    // Paths are absolute, confined to target, and checked for links above.
    if ((await stat(to))?.isSymbolicLink()) await fs.unlink(to);
    else await fs.rm(to, { recursive: true, force: true });
    if (action !== "remove") {
      await fs.mkdir(path.dirname(to), { recursive: true });
      if (link && skill)
        await fs.symlink(
          from,
          to,
          process.platform === "win32" ? "junction" : "dir",
        );
      else await fs.cp(from, to, { recursive: true });
    }
  }
  return entries.length;
}

async function main() {
  const { values, positionals } = parseArgs({
    options: {
      target: { type: "string" },
      link: { type: "boolean", default: false },
      help: { type: "boolean", short: "h" },
    },
    allowPositionals: true,
  });
  if (values.help) {
    console.log(
      "Usage: llm-toolkit <install|update|remove> [--target <project>] [--link]",
    );
    return;
  }
  if (positionals.length !== 1)
    throw new Error("Specify install, update, or remove; use --help for usage");
  const source = fileURLToPath(new URL("../", import.meta.url));
  const project = path.resolve(values.target ?? process.cwd());
  const count = await manage(positionals[0], source, project, {
    link: values.link,
  });
  console.log(
    `${positionals[0]}: ${count} entries in ${path.join(project, ".agents")}`,
  );
}

if (
  process.argv[1] &&
  (await fs.realpath(process.argv[1])) === fileURLToPath(import.meta.url)
) {
  main().catch((error) => {
    console.error(`Error: ${error.message}`);
    process.exitCode = 1;
  });
}
