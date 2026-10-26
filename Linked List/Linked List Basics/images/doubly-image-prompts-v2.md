# Doubly linked list — image prompt and QA (v2)

## Output

`doubly-linked-list-structure-v2.png` — 1536 × 1024 RGBA PNG.

Created with the built-in image-generation tool and the approved deterministic finishing workflow. Original image retained.

## Production

- Flat #EFEBDA card interior, thin rounded #012B41 frame, transparent outer corners.
- Teal #005C83 data fields, white values, cream pointer fields, brown #28190E outlines and links, petrol #012B41 annotations.
- Normalized generated colors, removed background artifacts and flattened the data fields. Antialiased boundaries retain blended edge pixels.
- Original `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png` composited directly with its emblem, wordmark, colors and gradient preserved. Only transparent margins trimmed; visible artwork resized proportionally to 138 pixels wide, placed at (1229, 143).
- Supplied course reference used for its visual style, not graph content.

## QA

- Exactly three nodes: 10, 20, 30; each has prev, data, next fields.
- Forward links: 10 → 20 → 30 → nullptr.
- Backward links: 30 → 20 → 10 → nullptr.
- Both neighboring links agree, arrows do not pass through values or labels, and no circular connection is implied.
- Head and tail identify the first and last nodes.
- Visually inspected final spacing, text, arrows, node colors and logo.
- Automated checks verified dimensions, transparent corners, opaque card interior, exact cream/teal samples and the entire logo region against the resized original composite.
- Only the image source was changed in the current lesson; existing code, prose and alt text were preserved.

## Generation prompt

```text
Use case: scientific-educational. Generate a clean spacious AlgoZenith doubly linked list diagram, 1536x1024 landscape PNG. Uniform opaque cream #EFEBDA card, thin 3px rounded petrol-blue #012B41 frame inset12 corner35, transparent outside corners ONLY. Flat smooth vector-like illustration. No shadows, noise, gradients, textures, panels, oversized titles, legends or paragraphs. Top area y<390 entirely blank cream including upperright reserved for official logo to be composited later: do not draw logo or wordmark. Colors: data fields #005C83 with white values, pointer fields cream, all node outlines/dividers and arrows #28190E, external text #012B41. Annotation typography restrained regular rounded handwritten-monospace around25px; values32px; clear baseline. 
Content: exactly three rectangular nodes in one row centered around y620. Each has THREE fields left "prev", middle "data", right "next". Draw field names just above respective fields. Node1 spans x240..490, node2 x650..900, node3 x1060..1310. Node height100, y570..670. Each prev field75px, data100px teal, next75px. Middle values10,20,30 respectively. Pointer fields cream, show one small brown pointer dot in each. All prev dots at y640, all next dots at y600. Links: from first next dot to second node LEFT outer boundary at y600, arrow pointing RIGHT. From second next dot to third node LEFT boundary at y600, arrow RIGHT. From second prev dot to first node RIGHT outer boundary at y640, arrow LEFT. From third prev dot to second node RIGHT boundary at y640, arrow LEFT. Separate horizontal parallel opposite arrows in each gap, label "next" above forward gap arrows, "prev" below backward gap arrows at y710. First prev dot points left to text "nullptr" at x130 y640. Last next dot points right to text "nullptr" at x1420 y600. Null labels fit within frame with at least45px margin. No circular connection, no extra nodes, no links through data fields. Head label at x240 y440 with downward arrow to first node top-left corner, away from prev/data/next text at y540. Small "tail" label centered below last node at y770. Substantial white space above and below; clear arrows 4px, node outlines5px. Precise educational structure: nullptr ← 10 ⇄ 20 ⇄ 30 → nullptr, each next connects to subsequent node and each prev connects to previous node. No other text.
```

