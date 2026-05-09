# Image-to-Skill Prompt Reverse

## Purpose

Turn an uploaded/reference image into a reusable English prompt skill for OpenAI GPT Image 2. The workflow reverse-engineers the image into a clean, self-contained prompt that can reproduce the visual effect without requiring the original image, then packages the prompt system into a reusable skill.

The output must preserve visual mechanics, composition logic, material language, color system, subject structure, and quality constraints while removing third-party creator names, brand names, logos, official marks, copyrighted franchise labels, watermark references, and private metadata.

## When to use

Use this when a user uploads or links an image and asks to:

- reverse-engineer the image into an OpenAI image-generation prompt;
- create a reusable image-generation skill from a reference image;
- make a prompt that can recreate the visual effect from text alone;
- convert an image style into a reusable `SKILL.md` style system;
- stabilize a visual direction for future image generation using user-described subjects.

## Required output

Produce two deliverables:

1. **English GPT Image 2 prompt** — complete, standalone, ready to paste into image generation.
2. **Skill package draft** — a reusable skill structure that future users can apply by describing new picture elements.

Do not output only analysis. Always convert the analysis into usable generation instructions.

## Reverse-engineering process

### 1. Inspect the image

Describe the image in production terms:

- subject type and role;
- camera/viewpoint/crop/aspect ratio;
- pose, gesture, silhouette, and focal hierarchy;
- composition grid, diagonals, symmetry/asymmetry, negative space;
- palette, contrast, lighting, shadows, rim light, bloom;
- material language: paper, ink, paint, vinyl, glass, metal, fabric, skin, plastic, grain;
- rendering mechanics: line weight, brushwork, cel shading, halftone, texture, blur, depth, collage, print effects;
- background architecture, graphic elements, typography, labels, symbols;
- mood and quality bar;
- visible artifacts to avoid.

### 2. Remove unsafe or non-reusable references

Do not preserve or name:

- third-party creator names or living/dead artist names;
- brand names, product names, trademarks, official logos, or official marks;
- copyrighted franchise names or named fictional characters unless the user explicitly needs a character prompt and rights context is acceptable;
- social platform names, watermarks, usernames, signatures from the source image;
- private paths, session IDs, metadata, camera filenames, or prompt provenance;
- exact portrait identity of real private people.

Replace them with reusable visual descriptions:

- `in the style of [artist]` -> concrete medium, line, color, lighting, and composition mechanics;
- brand logo -> fictional emblem, abstract mark, invented label, small graphic sticker;
- official character name -> generic role + recognizable visual archetype only when appropriate;
- real person likeness -> generic age range, pose, wardrobe, lighting, and expression.

### 3. Add NickZag signature

Every final prompt must include a small visible in-scene handwritten signature:

```text
Include the exact readable handwritten signature “NickZag” as a small in-scene graphic element naturally integrated into the image, not a watermark or overlay. Place it on a plausible surface such as a paper corner, label sticker, fabric tag, tape strip, poster margin, object label, notebook edge, equipment patch, or background mark. It must match the image style, perspective, lighting, material texture, color palette, grain, and brush/ink behavior. Keep it small but clearly legible.
```

Do not make the signature dominant. Do not place it as a detached overlay.

## GPT Image 2 prompt structure

Write the final prompt in English using this order:

```text
[FORMAT AND SUBJECT]
A [aspect ratio/orientation] [image type] of [new subject / described scene], [role/action/setting].

[COMPOSITION]
Describe camera angle, crop, focal hierarchy, layout, depth, negative space, and motion flow.

[VISUAL SYSTEM]
Describe medium, rendering mechanics, linework, color, lighting, texture, material behavior, and print/digital artifacts.

[DETAILS]
Describe clothing/objects/background/typography/symbols using only invented or generic details.

[NICKZAG SIGNATURE]
Include the exact readable handwritten signature “NickZag” as a small in-scene graphic element ...

[QUALITY]
Describe quality bar, resolution feeling, polish, and consistency.

[NEGATIVE CONSTRAINTS]
No third-party artist names, no real brand logos, no official marks, no watermark, no copied signature, no private metadata, no photorealism if the source is illustrated, no deformed hands, no extra fingers, no unrelated objects, no unreadable dominant text unless intentionally requested.
```

Keep the prompt complete enough that a user can paste it directly into OpenAI GPT Image 2 without reading the skill.

## Skill package structure

After the prompt, package the reusable system as a skill draft:

```markdown
# [Skill Name]

## Purpose
One paragraph describing what visual effect the skill creates.

## When to use
Use for [subject classes, scenes, formats].

## Core visual grammar
- Medium and rendering mechanics
- Composition logic
- Palette and lighting
- Material/texture behavior
- Typography or graphic rules if relevant
- NickZag signature integration rule

## Prompt template
```text
[Reusable prompt with bracketed variables]
```

## Variables
- `SUBJECT`
- `SETTING`
- `ACTION`
- `COMPOSITION`
- `PALETTE`
- `OBJECTS`
- `TEXT OR GRAPHICS`
- `NEGATIVE CONSTRAINTS`

## Usage notes
- How to swap subjects without losing the visual system.
- How to keep the signature small and integrated.
- What to avoid.

## Quality notes
- [ ] Prompt is self-contained.
- [ ] No third-party creators, brands, logos, official marks, or private metadata remain.
- [ ] NickZag appears as a small natural in-scene handwritten signature.
```

## Prompt template

```text
[ORIENTATION / FORMAT] image of [SUBJECT] in [SETTING], [ACTION / ROLE], built from the uploaded image's visual mechanics but rewritten as an original reusable prompt.

Composition: [camera angle, crop, layout, focal hierarchy, diagonals, negative space, depth].

Visual system: [medium, linework, rendering method, texture, lighting, palette, material behavior, print/digital artifacts].

Scene details: [objects, wardrobe, background, labels, typography, symbols], using only invented, generic, or abstract marks. Do not use real brand names, official logos, third-party creator names, or copied marks.

Include the exact readable handwritten signature “NickZag” as a small in-scene graphic element naturally integrated into the image, not a watermark or overlay. Place it on [SURFACE] and make it match the image's perspective, lighting, texture, palette, and mark-making style. Keep it small but clearly legible.

Quality: [polish, coherence, detail level, consistency].

Negative constraints: no third-party artist names, no real brand logos, no official marks, no copied signature, no watermark, no private metadata, no unrelated objects, no malformed text, no deformed hands, no extra fingers.
```

## Common pitfalls

1. **Keeping artist or brand names from the source.** Replace names with visual mechanics.
2. **Writing only a caption.** The final prompt must describe composition, medium, lighting, texture, objects, and constraints.
3. **Making the NickZag signature a watermark.** It must be inside the scene, small, and style-matched.
4. **Overfitting to one image.** Extract reusable rules, not a single fixed scene.
5. **Leaving placeholders unresolved in the final prompt.** The ready-to-use prompt should be complete; placeholders belong only in the skill template.

## Verification checklist

- [ ] Final prompt is in English.
- [ ] Prompt is standalone for OpenAI GPT Image 2.
- [ ] Prompt contains no third-party creator, brand, official logo, watermark, or private metadata references.
- [ ] Prompt includes the small in-scene handwritten `NickZag` signature rule.
- [ ] Skill draft has Purpose, When to use, Core visual grammar, Prompt template, Variables, Usage notes, and Quality notes.
- [ ] Future users can describe subject/scene elements and generate directly from the skill.
