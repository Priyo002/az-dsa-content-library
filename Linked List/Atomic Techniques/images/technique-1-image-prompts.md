# Technique 1 Image Prompts

Created with the built-in image-generation tool. The user-provided AlgoZenith image was used as a styling and branding reference only.

## intersection-shared-suffix.png

Use case: scientific-educational.
Asset type: clean professional raster diagram for an AlgoZenith linked-list lesson.
Input image 1: reference for STYLE AND BRAND ONLY, not the graph content to reproduce.
Match cream background, rounded dark teal border, teal-blue circular nodes with white labels, dark brown outlines and single directed connectors, muted red highlights. Landscape 1536x1024. Clear large typography and generous whitespace. Reproduce the proper reference AlgoZenith logo faithfully at upper right: blue triangular A, semicircular notch at bottom, white stylized Z and exact wordmark "AlgoZenith". Keep it separate from title/diagram. No visual clutter, shadows, texture, gradients except within brand if needed.
Graph invariants: a singly linked Y-shaped graph of exactly 10 unique nodes. Upper branch A1 -> A2 -> A3 -> A4 -> A5. Lower branch B1 -> B2. BOTH A5 and B2 have single arrows into ONE shared node C1. Shared suffix C1 -> C2 -> C3 -> nullptr. Each node label appears once. No reverse arrows, cycles, duplicated common suffix or accidental links. Draw A1..A5 on upper horizontal row left-to-right; B1,B2 on lower horizontal row aligned under A4,A5; C1 to right of A5 at middle vertical height, followed by C2,C3 to right. Keep all nodes/readable null text inside margins.
Title: "Two Lists, One Shared Suffix"
Above upper branch small label "List 1: 8 nodes". Below lower branch "List 2: 5 nodes".
Small "head1" pointer identifies A1 and "head2" pointer identifies B1.
Highlight C1 with thin outer muted-red ring and pointer labelled "First shared node". Put a bracket under C1,C2,C3 labelled "Shared suffix: 3 nodes".
Footer exactly: "Intersection means the same node in memory, not the same value."
Under footer or a small secondary line: "A1, B1 and C1 are node identities."
No other text. Prioritize Y topology and clear arrows. Branch lengths five and two; suffix length three.

## intersection-length-alignment.png

Use case: scientific-educational.
Asset type: clean professional raster diagram for an AlgoZenith linked-list lesson.
Input image 1: reference for STYLE AND BRAND ONLY, not the graph content to reproduce.
Match cream background, rounded dark teal border, teal-blue circular nodes with white labels, dark brown outlines and single directed connectors, muted red highlights. Landscape 1536x1024. Clear large typography and generous whitespace. Reproduce the proper reference AlgoZenith logo faithfully at upper right: blue triangular A, semicircular notch at bottom, white stylized Z and exact wordmark "AlgoZenith". Keep it separate from title/diagram. No visual clutter, shadows, texture, gradients except within brand if needed.
Graph invariants: a singly linked Y-shaped graph of exactly 10 unique nodes. Upper branch A1 -> A2 -> A3 -> A4 -> A5. Lower branch B1 -> B2. BOTH A5 and B2 have single arrows into ONE shared node C1. Shared suffix C1 -> C2 -> C3 -> nullptr. Each node label appears once. No reverse arrows, cycles, duplicated common suffix or accidental links. Draw A1..A5 on upper horizontal row left-to-right; B1,B2 on lower horizontal row aligned under A4,A5; C1 to right of A5 at middle vertical height, followed by C2,C3 to right. Keep all nodes/readable null text inside margins.
Title: "Align Before Moving Together"
Subtitle exactly: "Length difference: 8 - 5 = 3"
Use the specified single Y graph as main diagram, filling middle area. Fade only A1,A2,A3 to pale blue, with dark readable labels. A4,A5,B1,B2,C1,C2,C3 remain teal. Bracket above A1,A2,A3 labelled "Skip 3 nodes". Downward red pointer labelled "p" points precisely to A4. Upward red pointer labelled "q" points precisely to B1. Highlight C1 with red outline.
Below main graph, a neat three-column table, large enough to read:
Column headings "Paired moves" | "p" | "q"
Rows "0" | "A4" | "B1"
"1" | "A5" | "B2"
"2" | "C1" | "C1"
Emphasize last row red.
Footer exactly: "After alignment, both pointers have 5 nodes remaining."
No head pointers needed in this diagram; no movement arrows that could be confused with new next links. Table is a trace, not extra graph nodes.

## Alignment image refinement

Edit this image only to fix the clipped bottom footer and missing bottom border. Preserve all diagram topology, exact labels A1 A2 A3 A4 A5 B1 B2 C1 C2 C3, arrows, p and q positions, table values, colors, title and AlgoZenith logo unchanged. Recompose the content vertically slightly smaller or shift table upward so the entire footer 'After alignment, both pointers have 5 nodes remaining.' is fully visible with at least 40 pixels bottom padding inside a COMPLETE rounded dark teal outer border. No cropping on any side. Use a landscape 1536x1024 canvas, professional readable layout. Do not change the educational content.

## Verification

- Each diagram contains ten distinct graph nodes: five A nodes, two B nodes, and one shared three-node C suffix.
- Both incoming branches point to the same C1; the suffix ends at nullptr.
- List lengths are 8 and 5. Skipping three nodes places p at A4 while q remains at B1.
- The paired trace is A4/B1, A5/B2, C1/C1.
- Final images were visually inspected for labels, arrow directions, logo, and clipping. The alignment footer was repaired before insertion.

