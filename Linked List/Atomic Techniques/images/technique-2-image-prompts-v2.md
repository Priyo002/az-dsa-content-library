# Technique 2 — Course Diagram Regeneration

## Production and QA

Generated with the built-in image-generation tool, then deterministically finished to match the user's exact palette and original-logo requirements.

- Outputs: `middle-node-conventions-v2.png` and `middle-node-slow-fast-v2.png`.
- Both PNGs are 1536 × 1024 RGBA, with a flat #EFEBDA opaque card, a thin #012B41 rounded border, and transparent exterior corners.
- Solid node fills are #005C83; outlines and list connectors use #28190E; annotations use #012B41; node values are white. Anti-aliased boundary pixels intentionally use intermediate colors.
- The first generated draft's transparent interior and the second draft's partial-alpha background/shadow artifacts were flattened onto the exact cream palette. Background artifacts were removed while retaining the diagram labels and relationships.
- The original `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png` was composited directly, honoring its alpha channel. Only transparent outer margins were trimmed, then the visible artwork was resized proportionally to 138 pixels wide and placed at (1229, 143). No emblem, lettering, or logo gradient was redrawn or recolored.
- Automated checks verified canvas dimensions, opaque interior, transparent corners, exact background samples, exact fill samples in all 29 nodes, and pixel equality of the logo regions with the expected original-asset composite.
- Visual checks: comparison has five nodes and six nodes, with 30 as the unique/first middle and 40 as the second middle. Walkthrough has three six-node snapshots with slow/fast pairs (10,20), (20,40), (30,60); every list ends at nullptr. There are no cross-row links.
- The lesson changes only two image filenames. Text, code, alt text, and placement remain unchanged. Earlier assets are retained for rollback.

## Reference roles

The user-supplied `codex-clipboard-3c10bbbd-7908-487f-b514-5073cac05501.png` provides visual style only. Its graph content is not copied. The official logo PNG is the authoritative brand asset and is applied during finishing, not generated.

## Prompt: middle-node-conventions-v2.png

```text
Use case: scientific-educational. Create a new minimal AlgoZenith course linked-list diagram, landscape 1536x1024. Attached image is STYLE REFERENCE ONLY; do not copy its graph content.
Uniform solid opaque warm cream #EFEBDA inside one thin 3px #012B41 rounded frame 12px from canvas boundary, radius35px. Actual transparent outer corners. No texture, noise, paper grain, shading, gradients, shadows or highlights anywhere. Simple flat vector-like shapes with anti-aliased edges. All nodes identical deep teal-blue #005C83 fill with dark brown #28190E 5px outline, white centered 24px numerals. Next arrows #28190E 4px straight rightward, clear arrowhead at destination boundary. Labels #012B41 in regular restrained rounded handwritten-monospace/typewriter lettering at24px, disciplined and legible, never bold. No red, no alternate node colors, no decorative rings, no cards or panels, no headline/title/footer. Generous empty upper-left and upper-middle canvas. IMPORTANT leave entire upper region y0..320 EMPTY except rounded frame: official AlgoZenith logo will be directly composited afterward from the original asset for exact branding; DO NOT DRAW any logo or wordmark. Preserve whitespace. Only diagram content below.
Content: odd and even middle-node conventions in two separated horizontal rows, all arrows rightward. Top row at y500: five circular nodes 10,20,30,40,50 then plain text nullptr. Bottom row at y740: six circular nodes 10,20,30,40,50,60 then plain text nullptr. Node diameter64px. Align firstfive columns vertically with centers around x300,465,630,795,960; sixth at1125; nullptr at1320. Toprow nullptr may be at1125 with arrow after50. Small row labels "5 nodes" atx130,y500 and "6 nodes" atx130,y740. Label "only middle" above top30 at y405, short vertical arrow down into30. Label "first middle" above bottom30 at y645, short down arrow; label "second middle" below bottom40 at y845, short up arrow ending at40 lower boundary. All three annotation arrows petrol #012B41. Exactly eleven circular nodes total. Keep labels well apart and no connector crosses any text. No additional text. 30 is the third node in both lists. 40 is fourthnode in six-node list.
```

## Prompt: middle-node-slow-fast-v2.png

```text
Use case: scientific-educational. Create a new minimal AlgoZenith course linked-list diagram, landscape 1536x1024. Attached image is STYLE REFERENCE ONLY; do not copy its graph content.
Uniform solid opaque warm cream #EFEBDA inside one thin 3px #012B41 rounded frame 12px from canvas boundary, radius35px. Actual transparent outer corners. No texture, noise, paper grain, shading, gradients, shadows or highlights anywhere. Simple flat vector-like shapes with anti-aliased edges. All nodes identical deep teal-blue #005C83 fill with dark brown #28190E 5px outline, white centered 24px numerals. Next arrows #28190E 4px straight rightward, clear arrowhead at destination boundary. Labels #012B41 in regular restrained rounded handwritten-monospace/typewriter lettering at24px, disciplined and legible, never bold. No red, no alternate node colors, no decorative rings, no cards or panels, no headline/title/footer. Generous empty upper-left and upper-middle canvas. IMPORTANT leave entire upper region y0..320 EMPTY except rounded frame: official AlgoZenith logo will be directly composited afterward from the original asset for exact branding; DO NOT DRAW any logo or wordmark. Preserve whitespace. Only diagram content below.
Content: three independent snapshots of SAME six-node acyclic linked list. No inter-row connectors. Eachrow exactly 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> nullptr. Exactly eighteen circular nodes total, node diameter58px. Nodes centered x350,515,680,845,1010,1175; nullptr at1350. Rowcenters y435,625,815. Leftrow labels regular22px "start" atx125,y435, "1 iteration" atx125,y625, "2 iterations" atx125,y815. Slow/fast labels regular24px, darkpetrol, with short pointerarrows: each slow label 78px above its node with downward arrow to node top; each fast label 78px below its node with upward arrow to nodebottom. Row1: slow at10, fast at20. Row2: slow at20, fast at40. Row3: slow at30, fast at60. No ringorcolorhighlight on30. Quiet small annotation centered atx770,y955: "fast->next = nullptr; return slow (30)". Use exact spelling, no extra text. ALL list arrows point right, none left. Clean spacing between rows so adjacent pointer labels never overlap. Upperthird remains empty for logo and whitespace.
```

