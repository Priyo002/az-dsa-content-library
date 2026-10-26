# Folding and unfolding diagrams — v2

## Saved outputs

All2 images in `1_Folding_and_Unfolding_Linked_List.md` now use:

- [Folding pipeline](folding-pipeline-v2.png)
- [Unfolding pipeline](unfolding-pipeline-v2.png)

Original PNGs are retained. Code and algorithm explanations remain unchanged apart from removing outdated gold-ring descriptions in the folding alt text and adjacent sentence.

## Production

Built-in image generation tool, followed by the previously user-approved deterministic finishing pass for exact flat colors, frame/transparency, original-logo compositing and layout scaling. Attachment1 supplied visual style; attachment2 supplied the authoritative logo. No CLI generation.

Final files: 1536×1024 RGBA. Cream #EFEBDA; teal nodes #005C83; dark brown outlines and connectors #28190E; petrol annotations and thin frame #012B41; white values. Anti-aliased edges use transitional colors. No texture, shadows, large headline, boxed panels, colored rings or decoration. Rounded handwritten monospace lettering is approximate, not an exact font match.

Original logo source: `/Users/priyabratadas/Downloads/BLUE AZ TEXT LOGO.png`. Only transparent padding is trimmed. Original visible emblem and wordmark are proportionally resized to138px width and composited at(1229,143), preserving the asset's colors and gradient; neither is redrawn.

## Quality checks

- Both finished PNGs visually inspected.
- All4 stages in each figure contain exactly the same6 example values, each once per stage.
- Folding: original1→2→3→4→5→6; split1→2→3 and4→5→6; reverse only second to6→5→4; alternate merge1→6→2→5→3→4.
- Unfolding: folded1→6→2→5→3→4; position labels1..6 distinct from values; odd positions produce1→2→3 and even positions6→5→4; reverse second to4→5→6; concatenate to1→2→3→4→5→6.
- Every independent chain ends at nullptr. No arrows join the two disjoint groups during split/reversal stages. No connectors imply transitions between snapshots or introduce cycles.
- Labels, values, arrow direction and whitespace checked. All node fills share the same palette, without gold tracking rings.
- Pixel checks pass for dimensions, exact cream background, teal node samples, opaque interior and transparent corners. Logo region is byte-identical to expected resized original composited over cream.
- Both article image sources resolve to final workspace PNGs; full-file comparison confirms only intended source and gold-ring-description edits. Whitespace diff validation passes.

## Prompts

### Folding

```text
Use case: scientific-educational. Asset type: AlgoZenith linked-list teaching illustration, exactly1536x1024 landscape PNG. Uniform flat cream #EFEBDA, thin3px petrol #012B41 rounded frame inset12 radius35 with transparent outside corners. Clean anti-aliased vector-like artwork, no texture, gradient, shadow or glow. Generous whitespace occupying top third, upper-right area x1200..1410 y100..320 fully EMPTY reserved for later original-logo compositing; do not generate a logo or placeholder. No overall title, panels, dividers, colored rings, red, gold, decorative elements. All nodes same solid teal #005C83, brown #28190E outline4px; diameter60px. White centered rounded handwritten numerals24px. External labels petrol #012B41 regular22-24px restrained rounded handwritten monospace. Connectors brown width3px with clear rightward arrowheads; terminate at node boundary, no crossing text. No bidirectional links. Four horizontal rows, each a separate snapshot with no vertical connectors. Main content y360..900. Left row labels x80..290, diagrams x370..1420. Labels not bold. Every chain ends with an arrow to plain petrol text "nullptr" outside any circle. Null is never a filled node. No other prose, no footer. Layout rows carefully, avoid crowding and label collisions. Subject: folding six nodes through middle split, reversal, alternate merge. Row1 at y420: label "original" atx160; nodes centers x390,560,730,900,1070,1240 with values1,2,3,4,5,6 respectively, connected in that order by straight right-directed arrows; last6→nullptr atx1380. Row2 y570: left label "1. split"; two DISJOINT horizontal chains. First centers390,510,630 values1,2,3 then nullptr x760. Second centers960,1080,1200 values4,5,6 then nullptr x1350. Do not draw any edge between the two groups. Row3 y720: left label "2. reverse second" on two short lines if needed; first centers390,510,630 values1,2,3 then nullptr760 unchanged. Second centers960,1080,1200 values6,5,4 then nullptr1350. Row4 y870: left label "3. merge alternately" on two short lines; six centers390,560,730,900,1070,1240 values1,6,2,5,3,4, connected rightward then nullptr1380. Correct final order exactly1→6→2→5→3→4. All rows reuse same six nodes conceptually, no duplicated node values within a row, no gold rings. Diagram itself should make split/reverse/interleave evident by stable first-part placement and visibly reversed second chain.
```

### Unfolding

```text
Use case: scientific-educational. Asset type: AlgoZenith linked-list teaching illustration, exactly1536x1024 landscape PNG. Uniform flat cream #EFEBDA, thin3px petrol #012B41 rounded frame inset12 radius35 with transparent outside corners. Clean anti-aliased vector-like artwork, no texture, gradient, shadow or glow. Generous whitespace occupying top third, upper-right area x1200..1410 y100..320 fully EMPTY reserved for later original-logo compositing; do not generate a logo or placeholder. No overall title, panels, dividers, colored rings, red, gold, decorative elements. All nodes same solid teal #005C83, brown #28190E outline4px; diameter60px. White centered rounded handwritten numerals24px. External labels petrol #012B41 regular22-24px restrained rounded handwritten monospace. Connectors brown width3px with clear rightward arrowheads; terminate at node boundary, no crossing text. No bidirectional links. Four horizontal rows, each a separate snapshot with no vertical connectors. Main content y360..900. Left row labels x80..290, diagrams x370..1420. Labels not bold. Every chain ends with an arrow to plain petrol text "nullptr" outside any circle. Null is never a filled node. No other prose, no footer. Layout rows carefully, avoid crowding and label collisions. Subject: unfolding six folded nodes using CURRENT positions, not parity of values. Row1 y420: label "folded" leftx160; six centers390,560,730,900,1070,1240 values1,6,2,5,3,4 connected rightward then nullptrx1380. Above these six nodes at y365 exact labels "pos 1","pos 2","pos 3","pos 4","pos 5","pos 6" respectively in petrol, clearly distinct from white node values. Row2 y590: left label "1. separate" and below it "positions", two short lines. Two independent chains: centers390,510,630 values1,2,3 then nullptrx760; centers960,1080,1200 values6,5,4 then nullptr1350. Small group labels "odd positions" above firstchain atx510 y535 and "even positions" above secondchain atx1080 y535. No edges between groups. Row3 y735: left label "2. reverse second" on two short lines; unchanged firstchain1→2→3→nullptr at samecenters; secondchain becomes4→5→6→nullptr at samecenters. Row4 y875: left label "3. join" and "end to end" on two short lines; six centers390,560,730,900,1070,1240 values1,2,3,4,5,6 connected rightward then nullptr1380. Correct final order1→2→3→4→5→6. It is concatenation, NOT alternate merge. No coloredrings. Position labels appear ONLY above folded row and group labels only above separate row, to avoid confusion.
```
