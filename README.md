# image2skill

Prompt skills for stable GPT image generation.

This repository turns working prompts into reusable skills. A skill captures the subject structure, visual grammar, composition rules, and prompt patterns that make an image style repeatable across new subjects. The main generation target is OpenAI's GPT Image 2 model.

image2skill.com is the gallery for the generated results: <https://image2skill.com/>

## Skills

| Skill | Preview | Folder |
|---|---|---|
| Neon Stickerbomb Character Posters | <img src="skills/neon-stickerbomb-character-posters/images/sample-1.jpg" width="160" alt="Neon Stickerbomb Character Posters sample"> | [`skills/neon-stickerbomb-character-posters`](skills/neon-stickerbomb-character-posters/) |
| nezha-cute-muscle | <img src="skills/nezha-cute-muscle/images/sample-1.jpg" width="160" alt="nezha-cute-muscle sample"> | [`skills/nezha-cute-muscle`](skills/nezha-cute-muscle/) |
| Glossy Character Fashion Poster | <img src="skills/glossy-character-fashion-poster/images/sample-1.jpg" width="160" alt="Glossy Character Fashion Poster sample"> | [`skills/glossy-character-fashion-poster`](skills/glossy-character-fashion-poster/) |
| Editorial Poster | <img src="skills/editorial-poster/images/sample-1.jpg" width="160" alt="Editorial Poster sample"> | [`skills/editorial-poster`](skills/editorial-poster/) |

## Gallery examples

### Neon Stickerbomb Character Posters

<p>
  <a href="https://image2skill.com/tsunade-medical-seal-apad0.html"><img src="skills/neon-stickerbomb-character-posters/images/sample-1.jpg" width="220" alt="Neon Stickerbomb sample 1"></a>
  <a href="https://image2skill.com/sailor-moon-moon-hggpf.html"><img src="skills/neon-stickerbomb-character-posters/images/sample-2.jpg" width="220" alt="Neon Stickerbomb sample 2"></a>
  <a href="https://image2skill.com/bulma-capsule-gadget-q823f.html"><img src="skills/neon-stickerbomb-character-posters/images/sample-3.jpg" width="220" alt="Neon Stickerbomb sample 3"></a>
</p>

### nezha-cute-muscle

<p>
  <a href="https://image2skill.com/nezha-red-gold-0c2vx.html"><img src="skills/nezha-cute-muscle/images/sample-1.jpg" width="220" alt="nezha-cute-muscle sample 1"></a>
  <a href="https://image2skill.com/nezha-bikini-beach-wcsjg.html"><img src="skills/nezha-cute-muscle/images/sample-2.jpg" width="220" alt="nezha-cute-muscle sample 2"></a>
  <a href="https://image2skill.com/nezha-celestial-lotus-4b6t6.html"><img src="skills/nezha-cute-muscle/images/sample-3.jpg" width="220" alt="nezha-cute-muscle sample 3"></a>
</p>

### Glossy Character Fashion Poster

<p>
  <img src="skills/glossy-character-fashion-poster/images/sample-1.jpg" width="220" alt="Glossy Character Fashion Poster sample 1">
  <img src="skills/glossy-character-fashion-poster/images/sample-2.jpg" width="220" alt="Glossy Character Fashion Poster sample 2">
  <img src="skills/glossy-character-fashion-poster/images/sample-3.jpg" width="220" alt="Glossy Character Fashion Poster sample 3">
</p>

### Editorial Poster

<p>
  <img src="skills/editorial-poster/images/sample-1.jpg" width="220" alt="Editorial Poster sample 1">
  <img src="skills/editorial-poster/images/sample-2.jpg" width="220" alt="Editorial Poster sample 2">
  <img src="skills/editorial-poster/images/sample-3.jpg" width="220" alt="Editorial Poster sample 3">
</p>

## Repository layout

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
└── skills/
    ├── neon-stickerbomb-character-posters/
    │   ├── SKILL.md
    │   ├── examples.md
    │   ├── sample-images.md
    │   ├── images/
    │   │   ├── sample-1.jpg
    │   │   ├── sample-2.jpg
    │   │   └── sample-3.jpg
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
5. Use `examples.md`, `prompts/variants.md`, and `sample-images.md` as starting points for variations.

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
- `sample-images.md`: image examples from the gallery.
- `images/`: small gallery preview images.
- `prompts/base.md`: a reusable base prompt.
- `prompts/variants.md`: optional prompt variations.

## License

MIT for the text, prompt frameworks, and documentation in this repository.

Sample images are included as visual references for the skills. The full generated-image gallery lives at image2skill.com.
