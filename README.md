# image2skill

Open image-generation prompt skills distilled from the image2skill gallery.

image2skill is a small public collection of reusable prompt systems for OpenAI image-generation workflows. Each skill describes a repeatable visual grammar, a prompt-building method, safe usage boundaries, and sanitized examples.

Live gallery: <https://image2skill.com/>

## What is included

The repository contains reusable **skills**, not raw private session logs:

- public-facing prompt frameworks;
- usage rules and composition systems;
- sanitized example prompts;
- safety, IP, and logo-removal checks;
- a `manifest.json` that can be consumed by the image2skill frontend.

Initial stable skills:

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
├── SECURITY_AUDIT.md
├── manifest.json
├── scripts/
│   └── audit_public_repo.py
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

1. Open the skill folder.
2. Read `SKILL.md` for the visual grammar, safety boundaries, and prompt assembly procedure.
3. Start from `prompts/base.md`.
4. Replace the bracketed variables with your subject, scene, palette, pose, and constraints.
5. Check `examples.md` for sanitized prompt examples.
6. Run a safety pass before publishing outputs or prompts publicly.

Example:

```text
Use skills/editorial-poster/SKILL.md.
Subject: community coffee-grounds recycling booth.
Output: one vertical white-paper editorial poster prompt with meaningful coffee-recycling objects only, no unrelated motifs, no real brand logos.
```

## Public-safety policy

Before a skill is published here, it must pass the public audit checklist:

- no API keys, tokens, passwords, secrets, private URLs, local paths, or machine-specific data;
- no Discord channel/message IDs, Hermes/Eagle/internal workflow traces, or private session logs;
- no third-party brand logos, studio marks, watermarks, trademark lockups, or instructions to reproduce them;
- no named living-artist imitation;
- no copyrighted franchise metadata in the reusable style instructions;
- no prompt text that asks for real brand marks or official logos;
- no unsafe sexualized minor framing or explicit sexual content.

The examples in this repository are generic and sanitized. They may describe visual mechanics such as "glossy neon poster", "loose gouache typography", or "dark rim-lit concept art", but they do not rely on third-party logos, brands, studios, or private session artifacts.

Run the local audit script before committing:

```bash
python3 scripts/audit_public_repo.py
```

## License

MIT for the text, prompt frameworks, scripts, and documentation in this repository.

Generated images shown on image2skill.com may reference general visual ideas, archetypes, or user-provided subjects. Third-party characters, trademarks, brands, logos, and original IP remain the property of their respective owners. See `NOTICE.md`.
