# XOR linked-list image regeneration

Mode: built-in image generation, scientific-educational, followed by deterministic palette and brand finishing.

## Saved images

- [Neighbour recovery](xor-neighbour-recovery-v2.png)
- [Insertion](xor-insertion-update-v2.png)
- [Section reversal](xor-section-reversal-v2.png)

All three image references in `3_XOR_Linked_List.md` now use these assets. Original assets remain available. Obsolete gold/red descriptions in alt text and one adjacent sentence were updated. All C++ and other lesson content were preserved.

## Quality checks

- All three final PNGs visually inspected for legibility, layout, labels, correct relationships and no collisions.
- 1536 × 1024 RGBA; exact #EFEBDA background; #012B41 thin rounded frame; transparent exterior corners and opaque interior.
- Solid #005C83 nodes, #28190E outlines/connectors, white internal labels and dark petrol annotations. Generated halos removed; no colored categories or panels.
- Original supplied AlgoZenith logo composited at original proportions. Only empty transparent padding trimmed. Final logo region byte-checked against proportionally resized source composited over cream.
- Recovery: A/B/C addresses100/200/300 and encoded links200/328/200. Checked 100 ^ 300 = 328, 328 ^ 100 = 300, 328 ^ 300 = 100.
- Insertion: 100,200,300 becomes100,400,200,300. Resulting fields0 ^ 400,100 ^ 200,400 ^ 300; field at300 unchanged. Number labels explicitly identified as illustrative addresses.
- Reversal: 100,200,300,400,500,600 becomes100,200,500,400,300,600. P=200,L=300,R=500,S=600 labels preserved across rows; node400 retains the same unordered neighbour pair.
- Doubleheaded connectors denote logical adjacency, not two stored pointer fields, as clarified in the lesson.

## Final prompts

### Image 1

```text
Use case: scientific-educational. Asset: linked-list course diagram. Generate 1536x1024 landscape. Flat uniform cream #EFEBDA background, no texture, halos, shadows or gradients. Deep teal #005C83 circular nodes, brown #28190E 5px outlines and 4px connectors; white internal labels. Annotations solid dark petrol #012B41 in disciplined rounded lightly handwritten monospace 26px regular. Clean vector-like geometric artwork. No large title, panels, banners, boxes, legend or decorative elements. Upper third entirely empty including upper right reserved for original logo to be composited later; no generated logo or outer frame. Content within x80..1450,y380..960. All nodes same teal. Double-headed arrows represent logical adjacency, NOT two stored pointers. Arrowheads at both ends stop at node boundaries. No red/gold/accent colors. Exactly three nodes A,B,C radius48 at centers x340,768,1196 y520. One double-headed straight brown connector A to B, one B to C. Above nodes at y420: "head", "current", "tail" respectively. Below each node at y610: "address 100", "address 200", "address 300" respectively. Beneath at y675: "link = 200", "link = 328", "link = 200" respectively. Two separate worked examples below with substantial horizontal gap: left centered x440 at y785 "Arrive from A", at y840 "328 ^ 100 = 300", at y890 "Recover C". Right centered x1100 at same y: "Arrive from C", "328 ^ 300 = 100", "Recover A". All annotations same regular weight no bold. Preserve caret ^ for bitwise XOR, exact arithmetic. No extra lines or text.
```

### Image 2

```text
Use case: scientific-educational. Asset: linked-list course diagram. Generate 1536x1024 landscape. Flat uniform cream #EFEBDA background, no texture, halos, shadows or gradients. Deep teal #005C83 circular nodes, brown #28190E 5px outlines and 4px connectors; white internal labels. Annotations solid dark petrol #012B41 in disciplined rounded lightly handwritten monospace 26px regular. Clean vector-like geometric artwork. No large title, panels, banners, boxes, legend or decorative elements. Upper third entirely empty including upper right reserved for original logo to be composited later; no generated logo or outer frame. Content within x80..1450,y380..960. All nodes same teal. Double-headed arrows represent logical adjacency, NOT two stored pointers. Arrowheads at both ends stop at node boundaries. No red/gold/accent colors. Two rows illustrate insertion of address400 between100 and200. Small label "Before" x110 y405. Top row three circles radius45 centers (370,480),(760,480),(1150,480) white internal text100,200,300; double-headed arrows between adjacentnodes. Small label "After" x110 y610. Lower row four circles radius45 centers (280,695),(605,695),(930,695),(1255,695) white text100,400,200,300. Doubleheaded arrows connect100 to400,400 to200,200 to300. Label "new" directly above400 at y620. Below lower row aligned to corresponding node centers at y810 two-line annotations: under100 "link = 0 ^ 400"; under400 "link = 100 ^ 200"; under200 "link = 400 ^ 300"; under300 "unchanged". Set each formula on one line26px and ensure enough space between columns. At bottom y920 centered smallnote "Numbers are illustrative addresses". Exactly7 nodes. No arrows between rows or other annotations.
```

### Image 3

```text
Use case: scientific-educational. Asset: linked-list course diagram. Generate 1536x1024 landscape. Flat uniform cream #EFEBDA background, no texture, halos, shadows or gradients. Deep teal #005C83 circular nodes, brown #28190E 5px outlines and 4px connectors; white internal labels. Annotations solid dark petrol #012B41 in disciplined rounded lightly handwritten monospace 26px regular. Clean vector-like geometric artwork. No large title, panels, banners, boxes, legend or decorative elements. Upper third entirely empty including upper right reserved for original logo to be composited later; no generated logo or outer frame. Content within x80..1450,y380..960. All nodes same teal. Double-headed arrows represent logical adjacency, NOT two stored pointers. Arrowheads at both ends stop at node boundaries. No red/gold/accent colors. Two rows show reversing section of addresses300 through500. Exactly12 circles radius45,6perrow, centers x310,510,710,910,1110,1310. Small "Before" at x90 y510. Top row centers y520 internal numbers100,200,300,400,500,600. Above nodes200,300,500,600 at y425 labels P,L,R,S respectively; no other top labels. Small "After" x90 y740. Bottom row centersy750 internal numbers100,200,500,400,300,600. Above bottom nodes200,500,300,600 at y655 labels P,R,L,S respectively. Each adjacentpair connected by brown doubleheaded arrow, five connectors perrow; no inter-row connectors. At y860 center "At 400: 300 ^ 500 = 500 ^ 300". At y910 center "Only links at P, L, R, S change". Bottom smallnote at y960 "Numbers are illustrative addresses". No large title, no sectioncolor, no highlighted connections, no extra nodes or text.
```
