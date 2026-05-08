# image2skill

Reusable image-generation skills from the image2skill gallery.

image2skill turns selected generated works into compact prompt skills: each skill captures the visual grammar, subject structure, composition rules, and reusable prompt templates behind a consistent image style.

Live gallery: <https://image2skill.com/>

## What is included

- reusable prompt frameworks;
- style grammar and composition systems;
- base prompts and variants;
- example prompts for common use cases;
- a `manifest.json` index for website integration.

Initial skills:

| Skill | Directory | Gallery key |
|---|---|---|
| Neon Stickerbomb Character Posters | `skills/neon-stickerbomb-character-posters` | `neon-stickerbomb-character-posters` |
| Nezha cute muscle | `skills/nezha-cute-muscle` | `nezha-style` |
| Glossy Character Fashion Poster | `skills/glossy-character-fashion-poster` | `glossy-character-fashion-poster` |
| Editorial Poster | `skills/editorial-poster` | `editorial-poster` |

## Repository layout

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── manifest.json
└── skills/
    ├── neon-stickerbomb-character-posters/
    │   ├── SKILL.md
    │   ├── examples.md
    │   └── prompts/
    │       ├── base.md
    │       └── variants.md
    ├── nezha-cute-muscle/
    ├── glossy-character-fashion-poster/
    └── editorial-poster/
```

## How to use a skill

1. Open a skill folder.
2. Read `SKILL.md` for the visual grammar and prompt assembly notes.
3. Start from `prompts/base.md`.
4. Replace the bracketed variables with your subject, scene, palette, pose, and constraints.
5. Use `examples.md` and `prompts/variants.md` as starting points for variations.

Example:

```text
Use skills/editorial-poster/SKILL.md.
Subject: community coffee-grounds recycling booth.
Output: one vertical white-paper editorial poster prompt with meaningful coffee-recycling objects only.
```

## Skill format

Each skill follows the same structure:

- `SKILL.md`: purpose, use cases, visual grammar, prompt template, variables, and quality notes.
- `examples.md`: finished prompt examples.
- `prompts/base.md`: a reusable base prompt.
- `prompts/variants.md`: optional prompt variations.

## License

MIT for the text, prompt frameworks, scripts, and documentation in this repository.

Generated images shown on image2skill.com may include user-provided subjects or visual references. Those images are separate from this repository unless explicitly included here.
