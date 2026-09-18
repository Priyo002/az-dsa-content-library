# BFS image correction

Authoring reference only; not part of the student lesson.

- Mode: built-in image generation, text edit of the supplied raster diagram.
- Original: `reference/bfs-levels-original.png`.
- Original URL: https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/f94499e2-5a6b-4bff-befd-ae29d74b442d.png
- Final asset: `bfs-levels-corrected.png`.
- Correction: label the full vertex sequence as “BFS order”, not “queue”.
- Visual checks: all ten vertices and ten undirected edges preserved; levels 0–5 and the sequence 1,10,6,5,4,7,3,2,8,9 are correct; pale ivory background, rounded border, and proper AlgoZenith logo and wordmark retained.

## Final prompt

```text
Use case: text-localization / precise educational diagram edit.
Input image 1 is the EDIT TARGET. Make one correction only: replace the label "queue =" before the traversal sequence on the right with "BFS order =". The sequence is the complete traversal order, not a simultaneous queue snapshot.
Preserve the exact graph, all vertex labels, all edges, dashed level guides and distance annotations, and preserve the pale ivory background, rounded dark-teal outer border, muted blue circular vertices with white numbers, dark outlines, handwritten lettering and AlgoZenith logo AND wordmark at upper-right. Reuse the supplied proper logo; do not redesign it. Match the original landscape aspect ratio. Make enough room for "BFS order =" by modestly adjusting only the horizontal placement of that right-hand text block if needed. Do not alter the rest of the design.
Exact preserved content: source vertex 1; undirected edges (1,10),(1,6),(10,5),(10,4),(6,7),(5,3),(4,2),(7,2),(3,8),(8,9). Exactly ten vertices labelled 1 to 10, exactly ten edges, no arrowheads. Rows from top to bottom: level 0: [1]; level 1: [10,6]; level 2: [5,4,7]; level 3: [3,2]; level 4: [8]; level 5: [9]. Right text reads "BFS order = { 1, 10, 6, 5, 4, 7, 3, 2, 8, 9 }" with the existing group annotations 0 under [1], 1 over [10,6], 2 under [5,4,7], 3 over [3,2], 4 under [8], 5 over [9]. Those 0..5 numbers are distances and must not be changed. No extra text, no error note or caption, no added nodes, no missing connections. Only correct the misleading word "queue" to "BFS order".
```

