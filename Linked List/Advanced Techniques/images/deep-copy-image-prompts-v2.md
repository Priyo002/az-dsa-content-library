# Deep-copy lesson image regeneration

Mode: built-in image generation (scientific-educational), with deterministic palette, frame, transparency and original-logo finishing.

## Outputs

- [Interleaving](deep-copy-interleaving-v2.png)
- [Random-pointer lookup](deep-copy-random-lookup-v2.png)
- [Separation](deep-copy-separation-v2.png)

All three original image references in `2_Deep_Copy_Technique.md` were replaced. Previous image assets were retained. Only image paths and the obsolete gold-node alt-text description changed; lesson code and prose were preserved.

## Finishing and verification

- 1536 × 1024 RGBA; flat #EFEBDA interior; #012B41 thin rounded frame; transparent exterior corners.
- Solid #005C83 nodes; #28190E outlines/arrows; white node labels; #012B41 external annotations. Generated halos removed.
- Official supplied logo's visible artwork preserved, proportionally resized and composited at upper right. Only transparent padding was trimmed. Final logo region checked byte-for-byte against resized source composited over cream.
- Node letters identify objects, not values. Primes identify distinct copies without introducing category colors.
- Interleaving: five original nodes, then ten alternating original/copy nodes in A, A', B, B', C, C', D, D', E, E' order; both chains terminate at plain nullptr labels.
- Lookup: B → D and B' → D' are random links; B → B' and D → D' are temporary next links. Formula and arrow directions checked. This selected-link close-up does not imply the complete next chain.
- Separation: ten interleaved nodes, followed by separate five-node original and copied chains. No cross-list pointers; all three chains terminate at plain nullptr labels. Random links intentionally omitted as described by article alt text.
- Separation draft was regenerated because its nullptr labels were incorrectly enclosed as nodes; rejected draft was not used.
- All three final images visually inspected for labels, arrowheads, collisions and legibility; palette samples, blank cream area, alpha and logo checks passed.

## Final prompts

### Image 1

```text
Use case: scientific-educational. Generate a clean educational linked-list diagram bitmap, 1536 x 1024 landscape. Flat uniform warm cream #EFEBDA, all nodes deep teal #005C83 with dark brown #28190E outlines 5 px and white labels. All arrows dark brown 4 px, clear modest arrowheads. External annotations dark petrol #012B41, disciplined lightly handwritten rounded monospace regular 26 px. Smooth geometrically controlled vector-like artwork. Preserve generous whitespace, no texture, gradients, shadows, halos, bold headlines, boxes, panels, decorations or additional colors. No logo or frame in this draft: reserve upper third entirely blank, including upper right for original logo to be composited later. Entire content within x70..1460 y390..940. Circular nodes with uniform 36 px radius. Prime labels identify copies, never different colors. These labels denote node identity, not data. Do not introduce numeric values. Two separated horizontal rows. First row caption "Before" at x90 y420, chain centered at y510: A -> B -> C -> D -> E -> nullptr. Five equally spaced nodes. Second row caption "After interleaving" x90 y635, chain at y730: A -> A' -> B -> B' -> C -> C' -> D -> D' -> E -> E' -> nullptr. Exactly ten nodes in this order, all teal, positions x110,235,360,485,610,735,860,985,1110,1235 and nullptr x1390. Each next arrow connects adjacent node boundaries left to right. Bottom centered annotation at y870 "X->next = X'". No random arrows, no other text.
```

### Image 2

```text
Use case: scientific-educational. Generate a clean educational linked-list diagram bitmap, 1536 x 1024 landscape. Flat uniform warm cream #EFEBDA, all nodes deep teal #005C83 with dark brown #28190E outlines 5 px and white labels. All arrows dark brown 4 px, clear modest arrowheads. External annotations dark petrol #012B41, disciplined lightly handwritten rounded monospace regular 26 px. Smooth geometrically controlled vector-like artwork. Preserve generous whitespace, no texture, gradients, shadows, halos, bold headlines, boxes, panels, decorations or additional colors. No logo or frame in this draft: reserve upper third entirely blank, including upper right for original logo to be composited later. Entire content within x70..1460 y390..940. Circular nodes with uniform 36 px radius. Prime labels identify copies, never different colors. These labels denote node identity, not data. Do not introduce numeric values. Only four nodes in a spacious square, centers B=(490,470), D=(1030,470), B'=(490,730), D'=(1030,730), radius48. White B,D,B',D' labels. Top horizontal arrow B -> D labeled "random" above midpoint. Bottom horizontal arrow B' -> D' labeled "random" above midpoint. Left vertical arrow B -> B' labeled "next" to its left. Right vertical arrow D -> D' labeled "next" to its right. All four arrows have ONLY destination arrowhead, no doubleheaded arrows. At y850 centered formula "copy->random = cur->random->next". At y920 centered small note "Selected links after interleaving". No other edges or text.
```

### Image 3

```text
Use case: scientific-educational. Generate a clean educational linked-list diagram bitmap, 1536 x 1024 landscape. Flat uniform warm cream #EFEBDA, all nodes deep teal #005C83 with dark brown #28190E outlines 5 px and white labels. All arrows dark brown 4 px, clear modest arrowheads. External annotations dark petrol #012B41, disciplined lightly handwritten rounded monospace regular 26 px. Smooth geometrically controlled vector-like artwork. Preserve generous whitespace, no texture, gradients, shadows, halos, bold headlines, boxes, panels, decorations or additional colors. No logo or frame in this draft: reserve upper third entirely blank, including upper right for original logo to be composited later. Entire content within x70..1460 y390..940. Circular nodes with uniform 36 px radius. Prime labels identify copies, never different colors. These labels denote node identity, not data. Do not introduce numeric values. Three separated horizontal rows, all arrows go right and all chains terminate at nullptr. Top small row caption "Interleaved" at x90 y390 and chain at y465: A -> A' -> B -> B' -> C -> C' -> D -> D' -> E -> E' -> nullptr. Exactly ten nodes at x110,235,360,485,610,735,860,985,1110,1235, then nullptr x1390. Second small caption "Original restored" x90 y590, chain at y665: A -> B -> C -> D -> E -> nullptr. Third small caption "Independent copy" x90 y790, chain at y865: A' -> B' -> C' -> D' -> E' -> nullptr. Five-node rows at centers x310,510,710,910,1110, then nullptr x1330. No arrows between rows. All nodes same teal, copies distinguished only by prime labels. Exactly20 nodes overall. No other annotations or random links.
CRITICAL endpoint correction: nullptr is NOT a node. Render each occurrence of nullptr as plain dark petrol text on cream, with no circle, rectangle, fill or enclosure. Exactly20 teal circles:10 in first row,5 in second,5 in third. Make every annotation solid-filled dark petrol ink, never outlined lettering.
```
