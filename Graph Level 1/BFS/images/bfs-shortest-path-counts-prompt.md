# Shortest-path counting image

Authoring reference only; not part of the student lesson.

- Mode: built-in image generation, style-preserving edit.
- Style and logo reference: `bfs-levels-corrected.png`.
- Final asset: `bfs-shortest-path-counts.png`.
- Visual verification: exactly six vertices and eight undirected edges; levels [1], [2,3], [4,5], [6]; counts 1,1,1,2,1,3. Red edge 2-3 is a same-level edge and contributes no shortest paths. Both additions and distance 3 to vertex 6 are correct. Pale ivory background, rounded border, handwritten labels, and proper AlgoZenith logo and wordmark match the reference.

## Final prompt

```text
Use case: scientific-educational / style-transfer.
Asset: lesson diagram "Counting Shortest Paths with BFS".
Input image 1 is an EDIT TARGET used as a layout/style base. Preserve its pale ivory background, rounded dark teal border, handwritten dark teal/navy lettering, blue circular vertices with dark outlines and white numeric labels. Preserve exactly its proper AlgoZenith triangular blue A containing the stylized white Z and the AlgoZenith wordmark in the upper-right. Replace the old graph and BFS-order annotations with the following new six-vertex graph and compact explanatory panel. This is not the same graph as the input.
Landscape, generous margins, readable text, title upper-left "Counting Shortest Paths with BFS".
Left area: exactly six vertices, arranged in BFS rows:
level 0: vertex 1 centered;
level 1: vertex 2 left, vertex 3 right;
level 2: vertex 4 left, vertex 5 right;
level 3: vertex 6 centered.
Exactly eight undirected edges, no arrowheads: (1,2), (1,3), (2,3), (2,4), (3,4), (3,5), (4,6), (5,6). No other edges. The horizontal edge (2,3) is muted red, all other edges dark navy. Use thin dashed level guides clearly distinct from solid edges; label levels 0,1,2,3 at left of graph.
Below each vertex, put its exact final count in dark teal: below 1 "ways = 1"; below 2 "ways = 1"; below 3 "ways = 1"; below 4 "ways = 2"; below 5 "ways = 1"; below 6 "ways = 3". Leave room so annotations never overlap edges.
Right panel exact text, with generous spacing:
"Source: 1"
"Count only next-level edges"
"ways[4] = ways[2] + ways[3]"
"= 1 + 1 = 2"
"ways[6] = ways[4] + ways[5]"
"= 2 + 1 = 3"
In muted red: "Edge 2-3 stays at level 1:"
"no shortest-path contribution"
Footer "Distance to 6 = 3 edges; shortest paths = 3".
Ensure all text and graph topology are exact. Do not add arrows, vertices, edge weights, extra logos or decorations. Reuse the original AlgoZenith logo and wordmark without redesign.
```

