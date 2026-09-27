# DSU Path Compression Diagram

Generated with the built-in image-generation tool. Style and logo reference: `../../Graph Formulation/images/fuel-state-transitions.png`.

## Final Prompt

Use case: scientific-educational. Create one landscape DSU teaching diagram. Reference image is ONLY for visual style and AlgoZenith branding, not content. Match its cream background, handwritten navy text, blue/teal nodes with white numbers, complete rounded navy outer border and proper blue triangular AlgoZenith logo with stylized white Z and AlgoZenith wordmark at top-right.
Title: "DSU: Path Compression"
Two clearly separated panels, left "Before find_set(4)", right "After find_set(4)".
Each panel contains exactly four nodes labelled 1, 2, 3, 4, each number once per panel.
LEFT panel: node 1 at top, nodes 2 and 3 on middle row, node 4 below node 3. Exactly these parent arrows: 2 -> 1, 3 -> 1, 4 -> 3. Arrows point from child to parent, upward. Label node 1 "Root". No self-loop drawn.
RIGHT panel: node 1 at top, nodes 2, 3, 4 in a horizontal bottom row. Exactly these parent arrows: 2 -> 1, 3 -> 1, 4 -> 1. Arrows point from child to root, upward. Label node 1 "Root". No other edges, no self-loop.
Between panels, a modest transition arrow, not connected to graph nodes.
Footer in a pale yellow bordered box: "Same set: {1, 2, 3, 4}   |   Representative: 1   |   Size: 4"
Second footer line: "Only parent links change; set membership stays the same."
Small legend: "Arrows point to parents. parent[1] = 1."
Keep arrowheads unambiguous, nodes well-spaced, all text legible, border fully visible, proper reference logo. This is a mathematical parent-pointer diagram, not an original graph's edges.

## Verification

- Before: parent[1] = 1, parent[2] = 1, parent[3] = 1, parent[4] = 3.
- After find_set(4): all four parent values are 1.
- Both panels describe the same four-element set with representative 1 and size 4.
- Arrows correctly point from children to parents; the root's self-parent is stated in the legend.
- This tree is produced by union_sets(1, 2), union_sets(3, 4), union_sets(1, 3), with ties keeping the first root.
- Visually checked node labels, arrowheads, border, and reference-style AlgoZenith mark and wordmark.
