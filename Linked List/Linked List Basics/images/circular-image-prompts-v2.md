# Circular linked-list images — v2

## Delivery

All three image references in `4_Introduction_to_Circular_Linked_List.md` now use the regenerated PNGs:

- `circular-list-boundary-cases-v2.png`
- `circular-list-insert-front-v2.png`
- `circular-list-delete-front-v2.png`

The previous PNGs are retained. Lesson prose and code are unchanged; the insertion alt text no longer claims red highlights.

## Production

Generated using the built-in image generation tool (not CLI), then the user-authorized deterministic finishing pass. Reference attachment 1 supplies the visual style; attachment 2 is the authoritative original logo. Original logo PNG: `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png`. Only transparent padding was trimmed; the emblem and wordmark were proportionally resized, not redrawn or recolored. Visible logo width is 138px, at (1229,143).

All final files are 1536 × 1024 RGBA PNGs. Flat colors: cream #EFEBDA; node fill #005C83; outline/connector #28190E; annotation/frame #012B41; values #FFFFFF. Anti-aliasing introduces transitional edge colors. The original logo retains its own gradient. Thin rounded frame, transparent exterior corners, generous whitespace, no large title or boxed panels. Generated rounded handwritten type is an approximation, not an exact original-font match.

## Quality checks

- All three finished images visually inspected after finishing.
- Pixel checks pass for exact flat background, teal node samples, transparent corners and opaque interior.
- Logo region is byte-identical to the expected resized original composited onto cream.
- Boundary cases: empty has both pointers nullptr; singleton10 has one self-link; 10→20→30→10 has head10 and tail30.
- Insertion: 10→20→30→10 becomes 5→10→20→30→5; head changes to5, tail remains30, closing link targets5.
- Deletion: 10→20→30→10 becomes 20→30→20; head changes to20, tail remains30, no dangling link. Singleton deletion explicitly resets both pointers.
- Label/edge separation and arrow directions checked. No red highlight claims remain.
- All three article image paths resolve to final workspace files.

## Prompts

### Boundary cases

```text
Use case: scientific-educational. Asset type: AlgoZenith course diagram, PNG 1536 x 1024 landscape. Create a precise flat vector-like teaching illustration with exceptionally generous whitespace. Uniform warm cream #EFEBDA interior, thin petrol #012B41 rounded border inset 12px radius35px, transparent only outside corners. No texture, grain, gradient, shadow or decorative elements. Near-circular nodes radius38px, solid #005C83 fill, 5px #28190E outlines, white centered rounded handwritten numerals size26. Connections #28190E width4 with clear consistent arrowheads touching destination boundaries, never crossing text or node interiors. External labels #012B41 size24 regular disciplined lightly handwritten rounded monospace, no bold or italics. No overall title, footer, panels, dividers or legend. Keep entire top third empty, especially upper-right rectangle x1200..1410 y100..320, reserved for original logo compositing later: DO NOT draw any logo or placeholder. All visible teaching content must stay between y390 and y890 and x100 and x1420. No red, yellow, colored highlights. Each pointer has exactly one unambiguous arrowhead. Subject: three independent circular singly linked-list boundary cases arranged horizontally with generous gaps, not connected to each other. Left group x130..400: small label "empty" at y470; below it two lines "head = nullptr" and "tail = nullptr" at y560 and y610; no nodes. Middle group x520..750: small label "one node" at y470; label "head = tail" centered x625 y530 with a short downward arrow ending at top of node10 centered(625,610). Exactly one node containing "10". Its next link leaves its right boundary, loops clockwise around below it at y720, and returns with arrowhead at its left boundary. Small "next" label below loop at y765. Right group x850..1400: small label "three nodes" centered x1120 y470. Three nodes centers(900,610),(1110,610),(1320,610), containing "10","20","30". Right-pointing straight arrows 10 to20 to30. Label "head" above first and "tail" above last, short downward pointer arrows to those nodes. Closing edge leaves bottom of30, curves gently down to y750 then left underneath all three nodes then up to bottom of10, with arrowhead pointing INTO10. Below closing edge label "tail->next = head" centered x1110 y800. No nullptr in either nonempty group. The closing edge is one directed connection, not bidirectional.
```

### Front insertion

```text
Use case: scientific-educational. Asset type: AlgoZenith course diagram, PNG 1536 x 1024 landscape. Create a precise flat vector-like teaching illustration with exceptionally generous whitespace. Uniform warm cream #EFEBDA interior, thin petrol #012B41 rounded border inset 12px radius35px, transparent only outside corners. No texture, grain, gradient, shadow or decorative elements. Near-circular nodes radius38px, solid #005C83 fill, 5px #28190E outlines, white centered rounded handwritten numerals size26. Connections #28190E width4 with clear consistent arrowheads touching destination boundaries, never crossing text or node interiors. External labels #012B41 size24 regular disciplined lightly handwritten rounded monospace, no bold or italics. No overall title, footer, panels, dividers or legend. Keep entire top third empty, especially upper-right rectangle x1200..1410 y100..320, reserved for original logo compositing later: DO NOT draw any logo or placeholder. All visible teaching content must stay between y390 and y890 and x100 and x1420. No red, yellow, colored highlights. Each pointer has exactly one unambiguous arrowhead. Subject: circular singly linked list insertion at front, two separate aligned rows, no connecting arrows between rows. Upper row: modest label "before" at(180,440). Nodes radius38 centers(500,485),(800,485),(1100,485) with values "10","20","30". Horizontal right-directed links 10 to20 and20 to30. Head label above10 at y390 and tail label above30 at y390, short downward pointers. Closing arrow leaves bottom30 curves to y580 across underneath then up into bottom10. Lower row: modest label "after inserting 5" at(260,655). Four nodes centers(350,740),(600,740),(850,740),(1100,740), values "5","10","20","30"; horizontal right-directed links 5 to10 to20 to30. Head label directly above5 y655, tail label above30 y655, short downward pointers. Position the row caption further left at x125 y740 if needed to avoid head. Closing arrow leaves bottom30 curves down to y850, across underneath, then up into bottom5; no link to10 fromtail. No text on connecting arcs. No code block or instructions. Top has huge blank space. Avoid overlapping caption and labels: caption "after inserting 5" at x190 y635; head at x350 y675. All arrows brown, all nodes sameblue. Show only final before/after states.
```

### Front deletion

```text
Use case: scientific-educational. Asset type: AlgoZenith course diagram, PNG 1536 x 1024 landscape. Create a precise flat vector-like teaching illustration with exceptionally generous whitespace. Uniform warm cream #EFEBDA interior, thin petrol #012B41 rounded border inset 12px radius35px, transparent only outside corners. No texture, grain, gradient, shadow or decorative elements. Near-circular nodes radius38px, solid #005C83 fill, 5px #28190E outlines, white centered rounded handwritten numerals size26. Connections #28190E width4 with clear consistent arrowheads touching destination boundaries, never crossing text or node interiors. External labels #012B41 size24 regular disciplined lightly handwritten rounded monospace, no bold or italics. No overall title, footer, panels, dividers or legend. Keep entire top third empty, especially upper-right rectangle x1200..1410 y100..320, reserved for original logo compositing later: DO NOT draw any logo or placeholder. All visible teaching content must stay between y390 and y890 and x100 and x1420. No red, yellow, colored highlights. Each pointer has exactly one unambiguous arrowhead. Subject: circular singly linked-list front deletion, two separate rows with generous vertical spacing. Upper row: small label "before" left at(190,460). Three nodes centered(520,470),(800,470),(1080,470) values "10","20","30", straight rightward links 10 to20 to30. Label "head" above10 and "tail" above30 at y390, short downward pointer arrows. Closing connection leaves bottom30, runs below row at y560, then up with arrowhead into bottom10. Lower row: small label "after deleting 10" left at(270,675). Exactly two nodes centered(800,690),(1080,690) values "20","30", straight rightward connection20 to30. Label "head" above20 and "tail" above30 y610 with short downward pointer arrows. Closing connection leaves bottom30, runs below row y790, then up with arrowhead into bottom20. Old node10 is absent from lower row; no dangling connector. Near bottom, one small regular annotation centered y865: "one node: deleting it sets head = tail = nullptr". No further explanations, code, steps, headline, panels or red highlights. Before/after are separate states: no connecting arrow between rows.
```
