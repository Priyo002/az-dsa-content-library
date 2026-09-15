# Corrected graph image prompts

Mode: built-in image editing. Each source is in `reference/`; each final asset is named `<name>-corrected.png` in this directory. Originals remain archived and are not embedded in the lessons.

## sparse-dense

Use case: precise-object-edit. Correct this educational image while preserving its cream background, rounded border, handwriting, colors and exact upper-right AlgoZenith logo including wordmark. No error notes or commentary. Replace the entire horizontal scale and all its labels with a simple qualitative comparison: left heading 'Sparse' with subtitle 'Relatively few edges'; right heading 'Dense' with subtitle 'Relatively many edges'. Between them a single horizontal rightward arrow labelled 'Increasing number of edges'. Below centered 'For the same number of vertices'. No big-O symbols, no n^(3/2), no midpoint or numerical cutoff. Keep generous space and existing image style.

## paths

Use case: precise-object-edit. Correct this educational image while preserving its cream background, rounded border, handwriting, colors and exact upper-right AlgoZenith logo including wordmark. No error notes or commentary. Keep the six-vertex undirected graph exactly as drawn, edges 1-2,2-3,3-4,2-5,5-6,3-6. Replace the four red text rows with these exact strings: 'Path: 1 - 2 - 3 - 4'; 'Cycle: 2 - 3 - 6 - 5 - 2'; 'Simple Path: 1 - 2 - 3 - 6 - 5'; 'Simple Cycle: 2 - 5 - 6 - 3 - 2'. Change no other content.

## scc

Use case: precise-object-edit. Correct this educational image while preserving its cream background, rounded border, handwriting, colors and exact upper-right AlgoZenith logo including wordmark. No error notes or commentary. Make exactly ONE mathematical change: reverse the lower-left diagonal arrow INSIDE SCC1. It must point FROM the bottom blue vertex TO the left blue vertex (arrowhead near left vertex). Remove the old arrowhead near bottom vertex. SCC1 must be directed cycle left -> top -> right -> bottom -> left. Preserve all other arrows and nodes exactly. SCC2 remains singleton with incoming from SCC1 and outgoing to SCC3. SCC3 remains top -> right -> bottom -> top. Keep three enclosing ovals and labels SCC1 SCC2 SCC3. Do not add any new arrows or labels.

