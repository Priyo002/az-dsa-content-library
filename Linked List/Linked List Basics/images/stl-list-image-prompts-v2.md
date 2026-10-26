# STL linked-list diagrams — v2

## Outputs

All three images in `5_Linked_List_In_STL.md` were replaced with regenerated versions:

- [Iterator boundaries](stl-list-iterator-boundaries-v2.png)
- [Insertion before an iterator](stl-list-insert-v2.png)
- [Erasure and returned iterator](stl-list-erase-v2.png)

Original image files are retained. Only the three image sources changed in the lesson; all prose, alt text, code, and widget markup remain unchanged.

## Method and style

Built-in image generation tool, followed by the previously user-approved deterministic exact-color finishing pass. Attachment1 is the visual-style reference, not diagram content. Attachment2 is the authoritative logo: `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png`.

Final images: 1536×1024 RGBA PNG. Flat cream #EFEBDA, node fill #005C83, outlines/connectors #28190E, annotations/frame #012B41, white node values. Anti-aliased boundaries use transitional edge colors. Thin rounded frame and transparent exterior corners; interior remains opaque. Rounded handwritten monospace appearance is approximate, with no claim of an exact source font match. No large title, shadow, texture, colored panel, or red highlight.

The original logo is composited directly, with transparent padding trimmed and proportional resizing to138px visible width. Emblem, colors and wordmark are not redrawn. Its existing gradient is retained. Placement: (1229,143).

## Reader-focused checks

- Iterator boundaries: forward increment visits1,2,3,4,5 then end; reverse increment visits5,4,3,2,1 then rend. Dashed, unfilled stopping markers are explicitly not elements. No wraparound links. Labels distinguish `++it` from `++rit`.
- Insertion: original list1,2,3,4,5 becomes1,10,2,3,4,5. The original `it` still identifies2; returned `inserted` identifies10. Before/after states remain separate.
- Erasure: independent original list1,2,3,4,5 becomes1,3,4,5. Assignment uses the returned iterator to3. The old iterator to2 is explicitly invalid; erased2 is absent from the after state.
- Every final PNG visually inspected for legibility, edge directions, order, values, collisions, and uncluttered spacing.
- Pixel checks pass for dimensions, exact flat cream, teal samples, opaque interior, and transparent corners. The logo region matches the expected original-asset composite byte-for-byte.
- All3 lesson references resolve to the final versioned PNGs. Full-file comparison verifies only those3 sources changed. Whitespace diff validation passes.

## Prompt set

### Iterator boundaries

```text
Use case: scientific-educational. Asset type: AlgoZenith C++ course illustration, PNG exactly 1536x1024 landscape. Minimal flat vector-like geometry, spacious teaching diagram. Uniform cream #EFEBDA card, thin 3px #012B41 rounded outer frame inset12 radius35, transparent only outside rounded corners. No texture, grain, shadows, glow or gradients. Solid teal #005C83 near-circular nodes with dark brown #28190E outline5px, white rounded handwritten numerals centered inside. External annotations #012B41, regular24-26px disciplined rounded handwritten monospace, no bold or italics. Connectors brown #28190E width4 with consistent clear arrowheads, touch boundaries not interiors, never cross text. Node diameter76px. Keep top third empty, and reserve upper-right x1200..1410 y100..320 for later compositing of original logo; DO NOT draw a logo or placeholder. No overall title, panels, dividers, callout boxes, large captions, red, extra accent colors or decoration. Diagram in middle/lower canvas with roomy margins. Only text specified below. Each row is a separate state or view, not connected to another row. Subject: std::list iterator endpoints and movement, two rows. Upper row y500: five filled nodes values1,2,3,4,5 centered x350,540,730,920,1110; then EMPTY DASHED BROWN CIRCLE centered1300,500 with cream interior, no value. Straight right-pointing arrows between successive circles, showing 1→2→3→4→5→end marker. Label "begin()" above node1 at y410 with short downward arrow to1. Label "end()" above dashed circle y410 with downward arrow. Under empty dashed circle y570 text "not an element". Small text "forward: ++it" at x240,y355 (not bold). Lower row y760: empty dashed stopping circle centered160,760; five filled nodes1,2,3,4,5 centered350,540,730,920,1110. All straight arrows point LEFT, showing5→4→3→2→1→left stopping marker. Label "rend()" above dashed circle y670 with short downward arrow. Label "rbegin()" above5 y670 with downward arrow. Under empty dashed circle y830 text "not an element", keep within margins. Small label "reverse: ++rit" at x250,y625. No circular or wraparound arrows. These arrows represent iterator movement, not memory pointers. Reverse increment moves LEFT, not right. Each row has exactly five numbered elements and exactly one empty dashed circle.
```

### Insertion

```text
Use case: scientific-educational. Asset type: AlgoZenith C++ course illustration, PNG exactly 1536x1024 landscape. Minimal flat vector-like geometry, spacious teaching diagram. Uniform cream #EFEBDA card, thin 3px #012B41 rounded outer frame inset12 radius35, transparent only outside rounded corners. No texture, grain, shadows, glow or gradients. Solid teal #005C83 near-circular nodes with dark brown #28190E outline5px, white rounded handwritten numerals centered inside. External annotations #012B41, regular24-26px disciplined rounded handwritten monospace, no bold or italics. Connectors brown #28190E width4 with consistent clear arrowheads, touch boundaries not interiors, never cross text. Node diameter76px. Keep top third empty, and reserve upper-right x1200..1410 y100..320 for later compositing of original logo; DO NOT draw a logo or placeholder. No overall title, panels, dividers, callout boxes, large captions, red, extra accent colors or decoration. Diagram in middle/lower canvas with roomy margins. Only text specified below. Each row is a separate state or view, not connected to another row. Subject: std::list insertion before an iterator. Two rows centered horizontally. Top row y500: five filled nodes containing1,2,3,4,5 at x350,550,750,950,1150. Adjacent nodes connected with horizontal brown double-headed links. Small row label "before" at x180,y500. Label "it" above node2 at x550,y410 with downward arrow to2. Between rows at y605, one regular code annotation "inserted = values.insert(it, 10)" centered, no box. Bottom row y760: six filled nodes containing1,10,2,3,4,5 at x300,500,700,900,1100,1300, each adjacent pair connected with horizontal double-headed links. Small row label "after" at x160,y760. Label "inserted" above10 at x500,y675 with downward arrow to10. Label "it" above2 at x700,y675 with downward arrow to2. One concise teaching annotation below bottom row at y860: "it still identifies the same element: 2". New10 inserted immediately before2; all nodes same fill and outline (no colored highlight). No arrow between rows, no giant operation title.
```

### Erasure

```text
Use case: scientific-educational. Asset type: AlgoZenith C++ course illustration, PNG exactly 1536x1024 landscape. Minimal flat vector-like geometry, spacious teaching diagram. Uniform cream #EFEBDA card, thin 3px #012B41 rounded outer frame inset12 radius35, transparent only outside rounded corners. No texture, grain, shadows, glow or gradients. Solid teal #005C83 near-circular nodes with dark brown #28190E outline5px, white rounded handwritten numerals centered inside. External annotations #012B41, regular24-26px disciplined rounded handwritten monospace, no bold or italics. Connectors brown #28190E width4 with consistent clear arrowheads, touch boundaries not interiors, never cross text. Node diameter76px. Keep top third empty, and reserve upper-right x1200..1410 y100..320 for later compositing of original logo; DO NOT draw a logo or placeholder. No overall title, panels, dividers, callout boxes, large captions, red, extra accent colors or decoration. Diagram in middle/lower canvas with roomy margins. Only text specified below. Each row is a separate state or view, not connected to another row. Subject: std::list erase and returned successor iterator. Two separate rows. Top row y500: five filled nodes containing1,2,3,4,5 centered x350,550,750,950,1150. Adjacent nodes connected with horizontal brown double-headed links. Small row label "before" at x170,y500. Label "it" above2 at x550,y410 with downward arrow to2. Between rows at y600 one regular monospace code annotation "it = values.erase(it)" centered, no box. Bottom row y755: four filled nodes containing1,3,4,5 centered x450,700,950,1200. Adjacent nodes connected with horizontal brown double-headed links. Small row label "after" x200,y755. Label "it (returned)" above3 x700,y670 with short downward arrow to3. Two small lines below bottom row centered y850 and y890: "old iterator to 2: invalid" and "returned iterator identifies 3". Do not draw deleted2 in lower row or draw dangling arrows. No colored highlight or warning panel. Preserve all other values and exact labels.
```
