# Introduction to Linked List — image prompts and QA (v2)

## Outputs

- `array-vs-linked-list-memory-v2.png`
- `linked-list-types-v2.png`

Both files are 1536 × 1024 RGBA PNGs, generated with the built-in image-generation tool and finished deterministically using the approved exact-color/original-logo workflow.

## References and finishing

The supplied course diagram is the style reference, not a source of lesson content. The original `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png` is the authoritative branding asset. Its transparent margins were trimmed, and its visible artwork was resized proportionally to 138 pixels wide and composited at (1229, 143). The emblem, gradient, wordmark and colors were not redrawn.

The finishing pass rebuilt the flat #EFEBDA card with a thin #012B41 rounded frame, preserved transparent outside corners, normalized foreground colors to #005C83, #28190E, #012B41 and #FFFFFF, and removed generated background artifacts. Antialiased boundary pixels intentionally blend adjacent colors.

## QA

- Verified dimensions, opaque interior, transparent corners, exact cream background samples and exact teal samples in all data-field groups/nodes.
- Verified the entire logo region against the resized original asset composited on cream.
- Visually checked spacing, label readability, pointer direction, and absence of overlapping labels.
- Memory comparison: contiguous array cells 10, 20, 30; separate linked nodes at illustrative addresses 1000, 2400, 1600 with next fields 2400, 1600, nullptr.
- Types comparison: three nodes per row; singly linked forward chain; separate forward and backward doubly linked arrows with null endpoints; circular return arrow from 30 to the same node 10 and no null endpoint.
- Only the two image sources in the lesson were changed. Original assets, alt text, explanations, and code were retained.

## Prompts

### Array versus linked storage

```text
Use case: scientific-educational. Create a premium AlgoZenith course diagram as a 1536 x 1024 landscape PNG. Flat vector-like precise geometry and clean anti-aliased strokes. Uniform opaque warm cream #EFEBDA inside a thin 3px #012B41 rounded rectangular border inset 12px, corner radius35px. Outside corners genuinely transparent. No texture, noise, shadows, gradient background, panels, dividers, big titles, decorative elements or red accents. Solid teal #005C83 node data fields with white numbers, brown #28190E outlines 5px and arrows 4px. All external annotations #012B41. Restrained rounded lightly handwritten monospace text, regular weight, 23-26px, controlled baseline. Lots of whitespace. Reserve the upper region y<310 entirely empty cream, including upper-right: the original AlgoZenith logo will be composited directly later, so DO NOT generate any logo or wordmark. Content in middle/lower region, generous breathing room. Use rectangular node shapes when representing fields. Keep arrowheads clear, links away from labels. No extra prose. Subject: compare contiguous array storage versus non-contiguous linked storage, using values10,20,30. Upper example at y400-520: small label "array" at x160 y420. Three touching teal rectangular cells of equal width160 at x480..960, y415..485, values "10","20","30" in white; indexes "0","1","2" underneath centered. Small label "index" left of index labels. NO arrows between array cells. Lower example small label "linked list" near x160 y630. Exactly three separated two-field rectangular nodes, at x360..610, x760..1010, x1130..1380 all y700..775. Each has data left field width80 teal with white value, next right field cream with dark-blue pointer value. Above each node put address label "address 1000", "address 2400", "address 1600" at y630. Put small field names "data" and "next" over their fields at y675. Node1 fields "10" and "2400", node2 "20" and "1600", node3 "30" and "nullptr". Head at x220 y735 with right arrow to first node. A right arrow from first node's next field to second node, and from second next field to third node. No outgoing arrow from third because nullptr is inside its next field. Physical gaps show separate allocations; addresses need not increase. At y870 small annotation "illustrative addresses". Everything accurately spelled and spacious. Labels not collide.
```

### Linked-list types

```text
Use case: scientific-educational. Create a premium AlgoZenith course diagram as a 1536 x 1024 landscape PNG. Flat vector-like precise geometry and clean anti-aliased strokes. Uniform opaque warm cream #EFEBDA inside a thin 3px #012B41 rounded rectangular border inset 12px, corner radius35px. Outside corners genuinely transparent. No texture, noise, shadows, gradient background, panels, dividers, big titles, decorative elements or red accents. Solid teal #005C83 node data fields with white numbers, brown #28190E outlines 5px and arrows 4px. All external annotations #012B41. Restrained rounded lightly handwritten monospace text, regular weight, 23-26px, controlled baseline. Lots of whitespace. Reserve the upper region y<310 entirely empty cream, including upper-right: the original AlgoZenith logo will be composited directly later, so DO NOT generate any logo or wordmark. Content in middle/lower region, generous breathing room. Use rectangular node shapes when representing fields. Keep arrowheads clear, links away from labels. No extra prose. Subject: three linked-list types, each sequence values10,20,30. Exactly nine teal circular nodes radius32 (three per row), with white numerals; all arrows brown and annotations darkblue. Node centers at x560,850,1140. Row1 y440, row2 y640, row3 y825. Small row names on left x120: "singly", "doubly", and two lines "circular" / "singly". No titles or panels. Singly: head label above node10 with short downward arrow. next arrows 10→20 and20→30, next labels above each; node30 points right to "nullptr" atx1380. Doubly: head above10 with downward arrow. Two separate parallel opposite arrows for each adjacent pair: top next arrows10→20 and20→30, bottom prev arrows20→10 and30→20; label next above top arrows, prev below bottom arrows. First10 points LEFT to nullptr atx390 (prev end); last30 points RIGHT to nullptr atx1380 (next end). Circular singly: head above10 with downward arrow; forward next arrows10→20 and20→30; one smooth return arrow from bottom of30 curves below row to bottom of10, arrowhead ONLY at10. Small text "tail->next = head" centered beneath return curve at y945. Circular row has NO nullptr. Use one consistent color for every node and no highlighted rings. Arrows must not intersect any label. Every null label comfortably within frame.
```

