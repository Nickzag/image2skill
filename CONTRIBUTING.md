# Contributing

Thanks for improving image2skill.

## Public-safety requirements

Before opening a pull request, run:

```bash
python3 scripts/audit_public_repo.py
```

Do not commit:

- API keys, tokens, passwords, cookies, auth headers, or connection strings;
- local machine paths, private cache paths, private service URLs, or private workflow logs;
- raw session transcripts or private message/channel identifiers;
- real brand logos, official signage, studio marks, trademark lockups, or watermark reproduction instructions;
- named living-artist imitation prompts;
- unsafe sexual content or sexualized minor framing.

Use generic replacements such as fictional labels, abstract emblems, non-branded stickers, and unreadable graphic marks.

## Skill format

Each skill should contain:

```text
skills/<skill-key>/
├── SKILL.md
├── examples.md
└── prompts/
    ├── base.md
    └── variants.md
```

Keep examples sanitized and reusable. Prefer visual mechanics over brand names or private provenance.

## Manifest

If you add a skill, update `manifest.json` with:

- `key`
- `title`
- `sourceSiteKey` if it maps to image2skill.com
- `path`
- `repoUrl`
- `rawUrl`
- `downloadUrl`
