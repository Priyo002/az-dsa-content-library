# Girth illustration

Authoring reference only; not part of the student lesson.

- Mode: built-in image generation using a prior lesson image as a style template.
- Style and logo reference: `directed-dfs-edge-types-corrected.png`.
- Final asset: `girth-every-source.png`.
- Visual verification: each panel has exactly vertices 1,2,3,4 and undirected edges 1-2,2-3,2-4,3-4; no arrowheads. Source-1 distances are 0,1,2,2 and source-2 distances are 1,0,1,1. Candidate sums 5 and 3 are correct; true girth is 3 and vertex 1 lies on no cycle. Matching ivory background, rounded navy border, handwritten labels, and AlgoZenith logo and wordmark retained.

## Final prompt

```text
Use case: scientific-educational / style-transfer.
Input image 1 is an edit target used as a visual template. Preserve its ivory background, rounded navy outer border, handwritten teal/navy typography and original proper AlgoZenith blue triangular A logo with stylized white Z and AlgoZenith wordmark, upper-right. Replace the old directed graph and legend entirely with a new two-panel undirected-graph lesson diagram. Wide landscape composition, ample spacing.
Title: "Why We Run BFS from Every Vertex"
Two panels separated by a subtle vertical rule. Exactly FOUR vertices in each panel (same graph repeated), labelled 1,2,3,4 in cream circles with dark outlines. Vertex 1 at top, vertex 2 below it, vertex 3 lower-left and vertex 4 lower-right. Exactly these four UNDIRECTED edges in each graph: 1-2, 2-3, 2-4, 3-4. No arrowheads anywhere. Edge 3-4 muted red; other edges muted green.
Left title "Source s = 1". Labels beside vertices: at 1 "d = 0", at 2 "d = 1", at 3 "d = 2", at 4 "d = 2". Under graph exact text:
"Candidate from edge 3-4:"
"2 + 2 + 1 = 5"
"The shared prefix is counted twice."
Right title "Source s = 2". Labels beside vertices: at 1 "d = 1", at 2 "d = 0", at 3 "d = 1", at 4 "d = 1". Under graph exact text:
"Candidate from edge 3-4:"
"1 + 1 + 1 = 3"
"Cycle: 2 - 3 - 4 - 2"
Footer centered: "Girth = 3. Vertex 1 is not on any cycle."
The left-hand candidate 5 is NOT a simple cycle length: it represents walking down the shared edge 1-2 and back. Do not label 5 as a cycle. Match the reference handwriting, colors and proper AlgoZenith branding. All labels readable, not overlapping edges. No extra vertices, edges, arrows, formulas, logos or decorative objects.
```

