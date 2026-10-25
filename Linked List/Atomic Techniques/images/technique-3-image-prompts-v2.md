# Technique 3 — Diagram prompts and production QA (v2)

## Deliverables

- `cycle-structure-v2.png`: prefix 1 → 2 → 3 and cycle 4 → 5 → 6 → 7 → 8 → 9 → 4.
- `cycle-entry-reset-v2.png`: equal three-move paths from head 1 and meeting node 7 to the shared entry 4.
- `cycle-removal-v2.png`: before/after comparison; only node 9's next pointer changes to nullptr.

All outputs are 1536 × 1024 RGBA PNGs. Original images are retained for rollback.

## Production and quality checks

Generated using the built-in image-generation tool and finished deterministically with the user's approved exact-color and original-logo workflow.

- Flat cream interior: #EFEBDA.
- Node fill: #005C83; node values: #FFFFFF.
- Node outlines and connectors: #28190E.
- Annotations and thin rounded frame: #012B41.
- Transparent outer corners; opaque card interior.
- Smooth edge antialiasing intentionally uses blended boundary pixels.
- Original logo PNG composited directly, retaining its emblem, wordmark, gradient, and aspect ratio. Only fully transparent margins were trimmed for placement.
- Logo visible artwork resized proportionally to 138 pixels wide and placed at (1229, 143).
- Automated checks verified image dimensions, exact blank-background pixels, opaque interior, transparent corners, and exact blue samples in every node.
- The entire logo region was verified against the original asset's resized alpha composite.
- Visual inspection checked arrow directions, spacing, text legibility, and the expected 9, 7, and 18 displayed nodes respectively.
- The reset diagram contains two partial paths converging at one shared node 4, not a second complete cycle.
- Removal preserves all nine list nodes and changes only the closing link from 9 → 4 to 9 → nullptr.

The lesson update changes only the three image references and the first image's alt text from “highlighted” to “labeled”. Lesson explanations and code are preserved.

## Reference attachments

1. Style reference: `codex-clipboard-3c10bbbd-7908-487f-b514-5073cac05501.png`. Used for visual style, not its graph content.
2. Authoritative logo: `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png`. Used directly in the final artwork, not AI-redrawn.

## Generation prompts

### Cycle structure

```text
Use case: scientific-educational. New minimal AlgoZenith course linked-list diagram, landscape 1536x1024. Attached illustration is VISUAL STYLE ONLY, never copy its graph content.
One uniform opaque warmcream #EFEBDA card, thin3px #012B41 roundedframe 12px fromouteredge radius35px. Transparent outsidecorners only; entire interior opaquecream. Flat clean vector-like geometric rendering, no gradients/shading/texture/grain/shadows/highlights. Identical circular nodes tealblue #005C83, darkbrown #28190E outline5px, white centered24px rounded numerals. Directed next links darkbrown4px with clear arrowheads atdestinationboundary. Labels #012B41 regular24px restrained rounded handwritten-monospace/typewriter style, no bold. Allnodes samecolor, no rings, no red orcoloredhighlights. NO headline,title,panels,cards,legendbox,footerbanner. Large empty upper-leftandmiddle. Entire topband y0..320 empty exceptframe. Do NOT draw logo/wordmark: officialAlgoZenithPNG will be directlycomposited in upperright afterward for exactbranding. Only necessary diagram content below. Generous gaps, never overlap text/arrows.
Content: exactly9 distinct nodes1..9 form prefix1->2->3 and cycle4->5->6->7->8->9->4. Layout: node1 at(180,580),2(340,580),3(500,580),4(700,580); cycle nodes5(880,440),6(1100,440),7(1280,580),8(1100,760),9(880,760). Diameter64px. Draw ONLY directed edges1to2,2to3,3to4,4to5,5to6,6to7,7to8,8to9,9to4. The closing9to4 link points up-left into4; never4to9. A single six-node loop, no extra arrows/no nullptr. Label "head" above1, shortdownpointer. Label "cycle entry" above4 around(680,470), shortdownpointer; position notcolliding4to5. Label "x = 3" below prefixaround(340,690), label "y = 6" in emptycyclecenteraround(1000,610). No othertext. All ninevalues exactlyonce, cycleentry4 NOT duplicated.
```

### Entry reset

```text
Use case: scientific-educational. New minimal AlgoZenith course linked-list diagram, landscape 1536x1024. Attached illustration is VISUAL STYLE ONLY, never copy its graph content.
One uniform opaque warmcream #EFEBDA card, thin3px #012B41 roundedframe 12px fromouteredge radius35px. Transparent outsidecorners only; entire interior opaquecream. Flat clean vector-like geometric rendering, no gradients/shading/texture/grain/shadows/highlights. Identical circular nodes tealblue #005C83, darkbrown #28190E outline5px, white centered24px rounded numerals. Directed next links darkbrown4px with clear arrowheads atdestinationboundary. Labels #012B41 regular24px restrained rounded handwritten-monospace/typewriter style, no bold. Allnodes samecolor, no rings, no red orcoloredhighlights. NO headline,title,panels,cards,legendbox,footerbanner. Large empty upper-leftandmiddle. Entire topband y0..320 empty exceptframe. Do NOT draw logo/wordmark: officialAlgoZenithPNG will be directlycomposited in upperright afterward for exactbranding. Only necessary diagram content below. Generous gaps, never overlap text/arrows.
Content: reset-phase partialpaths only, exactly7 distinctnodes1,2,3,7,8,9,4. Upperpath1->2->3->4. Lowerpath7->8->9->THE SAME4. Layout: uppernodes1(280,480),2(520,480),3(760,480); lowernodes7(280,740),8(520,740),9(760,740); single sharednode4 at(1090,610). Allnodes64pxdiameter. Upper3to4 slopesdownright, lower9to4 slopesupright. Short label "from head" above1 withdownarrow, "from meeting" below7 withuparrow. Label "cycle entry" rightof4 withshortleftarrow, keepwithinframe. Label each path's successive three directededges "1","2","3" in small22px annotationtext, giving movescount: firstedge1,secondedge2,diagonallastedge3. Place labels above each edge with generousclearance, never touchingline. Small quiet text "3 moves each" centeredbelow at(775,865). NO othertext. Do not draw missingcycleedges; these are thetwo resetpaths only, do notadd5or6 orduplicate4.
```

### Cycle removal

```text
Use case: scientific-educational. New minimal AlgoZenith course linked-list diagram, landscape 1536x1024. Attached illustration is VISUAL STYLE ONLY, never copy its graph content.
One uniform opaque warmcream #EFEBDA card, thin3px #012B41 roundedframe 12px fromouteredge radius35px. Transparent outsidecorners only; entire interior opaquecream. Flat clean vector-like geometric rendering, no gradients/shading/texture/grain/shadows/highlights. Identical circular nodes tealblue #005C83, darkbrown #28190E outline5px, white centered24px rounded numerals. Directed next links darkbrown4px with clear arrowheads atdestinationboundary. Labels #012B41 regular24px restrained rounded handwritten-monospace/typewriter style, no bold. Allnodes samecolor, no rings, no red orcoloredhighlights. NO headline,title,panels,cards,legendbox,footerbanner. Large empty upper-leftandmiddle. Entire topband y0..320 empty exceptframe. Do NOT draw logo/wordmark: officialAlgoZenithPNG will be directlycomposited in upperright afterward for exactbranding. Only necessary diagram content below. Generous gaps, never overlap text/arrows.
Content: two separatedhorizontal states before/after cycle removal. Toprow at y470 exactly9nodes labeled1..9 lefttoright. Bottomrow at y780 exactlysame9nodes1..9. Diameter56px. Columns centersx160,300,440,580,720,860,1000,1140,1280 inbothrows. Everyrow has rightwardedges1->2->3->4->5->6->7->8->9. BEFORE: node9 has ONLY one outgoinglink: from9bottom down toy590, leftunderrow to x580, then upwardarrow into4bottom. No arrowto nullptron top. AFTER: node9 points rightto plaintext "nullptr" atx1430; no returnlink. Rowlabels "before" at(160,375), "after" at(160,690), regular24px. A small "head" justleftofnode1 eachrow withshortrightpointer. Small annotation "9->next = nullptr" centered at(940,660), betweenstates withoutcrossingline. Exactly18nodes,9eachrow, novaluesmissingorduplicated withinrow, allnodes samecolor. Allninepreserved. NO dividerlines,panels,headline,footer.
```

