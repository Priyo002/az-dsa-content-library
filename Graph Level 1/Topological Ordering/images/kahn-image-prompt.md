# Kahn diagram correction

- Mode: built-in image-generation tool, image edit (text-localization).
- Original reference: `reference/kahn-original.png`.
- Original URL: https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/5f38ce19-162e-41b7-a610-d4b208cc9967.png
- Final asset: `kahn-indegrees-corrected.png`.
- Validation: both first panels have two incoming edges into vertex 4, from 2 and 3. Its in-degree is 2 in both. Later, after processing 1, 3, 2, vertex 4 has in-degree 0 and vertex 5 has in-degree 1. All six original edges, the final order, the border, and the AlgoZenith mark remain represented correctly.

## Final prompt

Use case: text-localization. Edit target: supplied Kahn algorithm diagram. Correct ONLY two red indegree labels: (1) red 1 below blue vertex 4 in the upper-left initial graph must become red 2; (2) red 1 below blue vertex 4 in the upper-right graph with topo=[1] must become red 2. Both vertices 4 have incoming edges from vertices 2 and 3. Preserve EVERY other digit, node, directed edge and arrowhead, panel position, connecting arrow, topo list, cream background, rounded dark border, and the exact proper AlgoZenith triangular blue logo with white stylized Z and AlgoZenith wordmark at top right. Do not redesign, crop, add titles, or alter any other content. In particular keep the later lower-right vertex 4 indegree 0 unchanged and final order [1,3,2,4,5] unchanged. Match original handwriting font, red ink and sizing on the two changed labels.
