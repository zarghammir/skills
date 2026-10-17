# Skills

Agent skills I like and use, kept in one place. Each folder is one skill, copied from its author with the author's licence and credit kept next to it. Every skill links back to its original, so check there for the newest version.

## The skills

| Skill | What it does | Author | Licence |
|---|---|---|---|
| [ian-xiaohei-illustrations](ian-xiaohei-illustrations/) | Turns one idea from an article into a hand-drawn 16:9 picture that explains it, with a small black character doing the work | [Ian](https://github.com/helloianneo) ([original](https://github.com/helloianneo/ian-xiaohei-illustrations)) | MIT |

## Using a skill

Copy the skill's folder into your agent's skills folder:

- Claude Code: `~/.claude/skills/<skill-name>/`
- Codex: `~/.codex/skills/<skill-name>/`

Then ask for the skill by name. You can also just describe the task, and the agent picks the skill up from its description.

---

## ian-xiaohei-illustrations

![An idea too soft to use is pressed into a key that someone wants to try](ian-xiaohei-illustrations/assets/examples/11-idea-press.png)

*Example by Ian: an idea that is "too soft" gets pressed into a key that someone is willing to try.*

Ian wrote this skill for illustrating Chinese articles, so the skill's own text is in Chinese.

**What it makes.** Each picture explains a single idea from an article: a judgement, a process, a before-and-after, a state of mind. It is not a diagram or a slide. The look is always the same:

- a pure white background and thin, slightly wobbly black pen lines;
- lots of empty space, with the drawing taking up about half the picture;
- at most 5 to 8 short handwritten labels, in red (warnings), orange (the main flow) and blue (side notes);
- **Xiaohei (小黑)**, a small solid-black creature with white dot eyes and thin legs, who always does the main action. The skill's test: if you can remove Xiaohei and the picture still works, he is only decoration, and the picture is redone.

**How it works.**

1. It reads the article and picks the few places where a picture helps. That's usually 4 to 8 for a long article, and fewer for a short one.
2. It writes a shot list. For each picture, the list gives where it goes, the idea it shows, what Xiaohei is doing, and the labels.
3. For each picture, it invents a fresh metaphor from an everyday object (a press, a well, a drawer, a scale) instead of reusing old ones.
4. It draws each picture separately, from a fixed prompt template.
5. It checks every picture against a checklist: white background, enough empty space, Xiaohei doing the work, few and short labels, nothing that looks like a slide. It redraws or edits any picture that fails.

**What it needs.** The skill itself is free; it is only instructions. The drawing is done by an image model:

- **In Codex,** the skill uses Codex's built-in image generator.
- **In Claude Code,** which cannot draw, it plans the pictures and writes the prompts. You paste each prompt into any image tool, for example the free Gemini app or ChatGPT.

**Worth knowing.**

- Image models often misspell words inside pictures. Keep the labels short and check every picture.
- Xiaohei is part of Ian's own visual style. If you use the skill for your own brand, design your own character and credit Ian.
- This copy is unchanged from the original at commit [`4102eb8`](https://github.com/helloianneo/ian-xiaohei-illustrations/tree/4102eb807f03bcb6e538a16e8b31b41db8b5b954) (2026-09-24). See [SOURCE.md](ian-xiaohei-illustrations/SOURCE.md).
