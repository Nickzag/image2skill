# Security and Desensitization Audit

Every skill must pass this checklist before it is published or linked from image2skill.com.

## Required checks

### 1. Secrets and private infrastructure

Reject content containing:

- API keys, tokens, passwords, cookies, auth headers, private connection strings;
- local filesystem paths such as `/Users/`, `.hermes`, `.eagle`, cache directories, or build paths;
- localhost services, private ports, LAN addresses, private URLs, or deployment credentials;
- internal agent names or private workflow logs unless intentionally documented as public project metadata.

### 2. Source and session traces

Reject content containing:

- Discord channel IDs, message IDs, thread IDs, CDN cache URLs, or `discord://` links;
- raw Hermes session fragments;
- Eagle item IDs, folder IDs, local library paths, or unpublished metadata;
- "metadata pending", "prompt unavailable", "mapping pending", or similar placeholder text.

### 3. Third-party brand/logo risk

Reject or rewrite content that asks the model to:

- reproduce a real brand logo, studio logo, watermark, product mark, team crest, or official emblem;
- imitate official merchandise packaging;
- place exact copyrighted/trademarked text unless it is user-owned or clearly generic;
- copy the visual identity of a named brand or campaign.

Safe replacement language:

```text
abstract non-branded emblem, fictional patch, invented label, unreadable graphic marks, generic warning sticker, non-branded product shape
```

### 4. Named-artist / creator imitation

Reject content that instructs direct imitation of a named living artist, creator, studio, or proprietary style label. Rewrite as visual mechanics: line quality, palette, texture, composition, material rendering, and typography behavior.

### 5. Safety and public examples

Reject content that includes explicit sexual content, sexualized minor framing, or unsafe fetish framing. Public examples should be generic, covered, non-explicit, and focused on visual craft.

## Command

Run:

```bash
python3 scripts/audit_public_repo.py
```

The script is a guardrail, not a substitute for human review. A clean script result means "no known blocked terms were found"; it does not guarantee legal clearance.
