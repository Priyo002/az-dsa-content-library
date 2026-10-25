# Singly linked list — image prompt and QA (v2)

## Output

`singly-linked-list-structure-v2.png` — 1536 × 1024 RGBA PNG.

Created with the built-in image-generation tool, followed by the approved deterministic finishing pass. The original asset is retained.

## Style and production

- Flat #EFEBDA card, thin #012B41 rounded frame, transparent outside corners.
- Teal #005C83 data fields, white values, brown #28190E connectors/outlines, petrol #012B41 annotations.
- Removed generated background artifacts and pointer-field halos, regularized pointer-field outlines and retained the same connections.
- Antialiased edges use blended boundary pixels.
- Composited the original `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png` directly, trimming only transparent margins and resizing proportionally to 138 pixels wide. Placement: (1229, 143). No logo redraw or recoloring.
- Supplied course illustration used as the visual style reference, not as diagram content.

## Checks

- Exactly three nodes with values 10, 20, 30 and separate data/next fields.
- Head identifies node 10; next links run forward from 10 to 20 to 30 to nullptr.
- Tail label identifies node 30, without implying a stored tail pointer.
- Checked readable labels and separation from arrows.
- Automated checks passed for dimensions, exact background and teal samples, opaque card interior, transparent corners, and a byte-identical logo region relative to the expected resized original composite.
- Only the image source was updated in the current lesson. Existing prose, code and alt text were preserved.

## Generation prompt

```text
Use case: scientific-educational. Asset: AlgoZenith course diagram explaining singly linked node structure. Create a 1536 x 1024 landscape PNG. Minimal flat vector-like geometry with uniform warm cream #EFEBDA opaque background inside one thin 3px dark petrol #012B41 rounded border inset12px radius35px; genuinely transparent outer corners. No paper texture, no grain, no gradient background, shadows, panels, huge headlines, or colored accents. Spacious and premium teaching illustration. Reserve all upper region y<370 empty cream including upper-right for the official logo to be directly composited afterwards; DO NOT draw a logo, title or watermark. Three rectangular two-field nodes in one horizontal row around y590..690. Nodes at x220..460, x650..890 and x1080..1320. Each left data field width140 solid teal #005C83 with centered white values "10","20","30" respectively; each right next field width100 cream. Rectangular outlines/dividers dark brown #28190E, 5px. Small dark brown pointer dot centered in each next field. Thin dark brown right-facing arrow from first dot to second node's left boundary, from second dot to third node's left boundary, from third dot to external dark-blue text "nullptr" at x1430. Three clearly separated nodes, exactly one forward link per next field. No backward links. Field labels "data" and "next" above each field at y550, dark petrol #012B41, 25px restrained rounded handwritten-monospace regular weight. A small "head" label at x220 y450 with a short downward brown arrow to first node top boundary, routed left of field labels. Small "tail" label below last node at y760, no extra arrow needed. Rounded handwritten numerals 32px with ample padding. Single logical sequence head→10→20→30→nullptr. Main diagram in middle-to-lower portion with ample surrounding cream, no captions or paragraphs. Text must be accurate and connectors cannot intersect labels. Use supplied course reference's quiet visual rhythm, not its graph content. Original AlgoZenith branding will be added unchanged in the finishing pass.
```

