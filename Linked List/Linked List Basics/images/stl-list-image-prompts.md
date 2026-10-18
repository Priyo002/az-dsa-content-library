# STL List Image Prompts

Generated with the built-in image-generation tool. The attached AlgoZenith graph image was used only as a styling and logo reference.

## stl-list-iterator-boundaries.png

Use case: scientific-educational.
Asset type: raster educational diagram for an AlgoZenith C++ linked-list lesson.
Input image 1 is STYLE AND BRAND REFERENCE ONLY. Create a new diagram, not the pictured graph.
Match the reference's cream background, rounded dark-teal outer border, blue/teal filled nodes with white numerals, dark brown outlines and connectors, restrained muted-red annotations. Professional, clean crisp typography, generous whitespace, landscape 1536x1024 layout. Reproduce the reference's proper AlgoZenith logo faithfully at the upper right: blue triangular A with lower semicircular notch, white stylized Z, exact AlgoZenith wordmark. Keep logo clear of title and diagrams. No unrelated graph, gradients, shadows, decorative objects or long prose. Thick legible lines, explicit arrowheads, clear labels.
Title: "List Iterator Boundaries"
Two horizontal panels separated by a fine rule. Show conceptual traversal positions, not implementation internals.
Top panel heading "Forward traversal". Five blue nodes in order 1, 2, 3, 4, 5, left to right, joined with right-facing arrows. A red pointer labelled "begin()" points exactly at node1 from above. After node5, an arrow leads to a dashed unfilled marker labelled "end()" with small text "not an element". Below row: "++it moves right".
Bottom panel heading "Reverse traversal". Five blue nodes in the SAME spatial order 1, 2, 3, 4, 5 left to right, joined with left-facing arrows. A red pointer labelled "rbegin()" points exactly at node5 from above. To the LEFT of node1, an arrow leads leftward to a dashed unfilled marker labelled "rend()" and "not an element". Below row: "++it moves left".
Footer: "Stop at the end marker. Never dereference it."
Constraints: begin points1, rbegin points5; end and rend are not nodes and must not have blue fills/numbers. Reverse row arrows only face left. No wraparound. No array indices. Exactly five numbered elements in each panel.

## stl-list-insert.png

Use case: scientific-educational.
Asset type: raster educational diagram for an AlgoZenith C++ linked-list lesson.
Input image 1 is STYLE AND BRAND REFERENCE ONLY. Create a new diagram, not the pictured graph.
Match the reference's cream background, rounded dark-teal outer border, blue/teal filled nodes with white numerals, dark brown outlines and connectors, restrained muted-red annotations. Professional, clean crisp typography, generous whitespace, landscape 1536x1024 layout. Reproduce the reference's proper AlgoZenith logo faithfully at the upper right: blue triangular A with lower semicircular notch, white stylized Z, exact AlgoZenith wordmark. Keep logo clear of title and diagrams. No unrelated graph, gradients, shadows, decorative objects or long prose. Thick legible lines, explicit arrowheads, clear labels.
Title: "Insert Before an Iterator"
Code subtitle: "auto inserted = values.insert(it, 10);"
Two wide rows labelled "Before" and "After", connected by a small downward transition arrow in whitespace, not a node link.
Before: five blue nodes 1, 2, 3, 4, 5 left to right, adjacent nodes joined with bidirectional arrows. Red downward pointer labelled "it" to node2.
After: exactly six nodes 1, 10, 2, 3, 4, 5 left to right, adjacent nodes joined with bidirectional arrows. Node10 has a red outline to highlight the new element but same blue fill. Pointer labelled "inserted" goes exactly to node10. Separate pointer labelled "it" goes exactly to node2.
Below: two short lines "New element: 10" and "Existing iterator still identifies 2".
Footer: "Insertion does not invalidate existing list iterators."
Constraints: insertion before2, not after; original it does NOT move to10. No indices, no end markers. Ensure two After pointers are separated and unambiguous.

## stl-list-erase.png

Use case: scientific-educational.
Asset type: raster educational diagram for an AlgoZenith C++ linked-list lesson.
Input image 1 is STYLE AND BRAND REFERENCE ONLY. Create a new diagram, not the pictured graph.
Match the reference's cream background, rounded dark-teal outer border, blue/teal filled nodes with white numerals, dark brown outlines and connectors, restrained muted-red annotations. Professional, clean crisp typography, generous whitespace, landscape 1536x1024 layout. Reproduce the reference's proper AlgoZenith logo faithfully at the upper right: blue triangular A with lower semicircular notch, white stylized Z, exact AlgoZenith wordmark. Keep logo clear of title and diagrams. No unrelated graph, gradients, shadows, decorative objects or long prose. Thick legible lines, explicit arrowheads, clear labels.
Title: "Erase and Use the Returned Iterator"
Code subtitle: "it = values.erase(it);"
Two wide rows labelled "Before" and "After", connected by a small downward transition arrow in whitespace, not a node link.
Before: five blue nodes 1, 2, 3, 4, 5 left to right, adjacent nodes joined with bidirectional arrows. Red pointer labelled "it" points exactly to node2. Node2 outlined red to indicate deletion.
After: exactly four blue nodes 1, 3, 4, 5 left to right, adjacent nodes joined with bidirectional arrows. A red pointer labelled "it" points exactly to node3.
Below: two short lines "Old iterator to 2 is invalid" and "erase returns the next position: 3".
Footer: "Erasing the last element returns end()."
Constraints: no2 or ghost/deleted node in After row, no10 in either row. Assignment replaces old iterator with returned iterator. Do not imply erased iterator remains valid. Clear spacing.

## Erase diagram refinement

Edit this educational diagram. Change ONLY the connectors between adjacent blue nodes in both Before and After rows: replace the duplicated parallel double-headed arrows with exactly ONE horizontal double-headed dark brown arrow per adjacent pair, like 1 <-> 2. Seven adjacent pairs total: Before 1-2,2-3,3-4,4-5; After 1-3,3-4,4-5. Preserve all node values, positions, iterator arrows, labels, title, code, colors, background, border and proper AlgoZenith logo exactly. No other edits. Clean crisp professional output.

## Verification

- Iterator rows show the correct traversal directions and non-element end markers.
- Insert adds 10 before 2; the original iterator stays on 2 and the returned iterator identifies 10.
- Erase removes 2; the assigned returned iterator identifies 3.
- Final diagrams were visually checked for labels, node sequences, arrowheads, spacing and AlgoZenith branding.

