# DFS illustration prompts and checks

Authoring reference only; not part of the student lesson.

- Generation mode: built-in image generation, two separate assets using one shared reference.
- Style and logo reference: `reference/graph-representation-style.png`, copied from the first image in `1_Graph_Representation.md`.
- Reference source: https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/590f290a-4cfe-4642-9402-a9122944bdd6.png
- Shared style: pale ivory background, inset rounded dark-teal border, flat teal-blue nodes/frames, dark outlines, white labels, handwritten text, muted red annotations, and upper-right AlgoZenith triangular mark with white stylized Z and blue wordmark.
- Reference graph is directed; the new dry-run graph is undirected. Only styling and branding are transferred.

## dfs-components-dry-run.png

Visually checked: exactly seven vertices; undirected edges 1–2, 1–3, 2–4, 3–4, 5–6; vertex 7 isolated; no diagonal or inter-component edges. Starting calls and discovery sequences match the lesson's input order. Border and AlgoZenith logo/wordmark present.

```text
Use case: scientific-educational.
Asset type: final landscape illustration for an AlgoZenith introductory DFS lesson.
Input image 1: STYLE AND LOGO REFERENCE ONLY. Create a different teaching diagram, not a copy of its graph. Match its exact pale ivory background, inset dark teal rounded rectangular outer border, flat muted teal-blue circular nodes with dark brown outlines and centered white handwritten numbers, restrained dark handwritten text, and generous whitespace. Reuse the proper AlgoZenith logo from the reference: navy-to-blue triangular A silhouette with semicircular cutout, white stylized Z, and the blue wordmark "AlgoZenith" beneath, at upper-right inside the border. Do not invent a plain Z or omit the wordmark. Keep the logo modest and clear.
Title near top-left: "DFS: One Component at a Time"
Subtitle: "Undirected graph  |  n = 7, m = 5"
Content: Exactly SEVEN vertices and FIVE undirected edges. Three separate groups across the page, each with ample separation. The first larger group on the left is a square: vertex 1 upper-left, vertex 2 upper-right, vertex 3 lower-left, vertex 4 lower-right. Draw only the four square-side edges 1--2, 2--4, 4--3, 3--1. NO diagonals. NO arrowheads on graph edges. The middle group contains only nodes 5 and 6 with one horizontal edge between them. The right group contains isolated node 7 with NO edges. Do not connect the three groups.
Below first group, print "Start dfs(1)" and on the next line "1, 2, 4, 3". Below middle group, print "Start dfs(5)" and below it "5, 6". Below isolated node 7 print "Start dfs(7)" and below it "7". Use muted red for the discovery-order number sequences only; these are ordered lists, not graph arrows.
Bottom note in dark teal: "Restart only at an unvisited vertex."
Small second bottom note: "Discovery order: 1, 2, 4, 3, 5, 6, 7"
Use the stated ordering; it comes from neighbour lists 1:[2,3], 2:[1,4], 3:[1,4], 4:[2,3], 5:[6], 6:[5], 7:[]; these lists are metadata and MUST NOT be printed. No extra text, no extra nodes, no arrows between components, no decorative illustrations. High-resolution readable typography. Canvas approximately 3:2 landscape.
```

## dfs-call-stack-backtracking.png

Visually checked: bottom-to-top frames [1,2,4,3], [1,2,4], [1,2], [1]; each top label points to the active call. Visited remains {1,2,3,4}, and vertex 1 skips already-visited neighbour 3. Border and AlgoZenith logo/wordmark present.

```text
Use case: scientific-educational.
Asset type: final landscape call-stack illustration for an AlgoZenith introductory DFS lesson.
Input image 1: STYLE AND LOGO REFERENCE ONLY. Match its pale ivory background, dark teal inset rounded border, flat blue/teal shapes with dark brown outlines, friendly legible handwritten text, restrained muted red accents, generous whitespace. Reuse its proper AlgoZenith logo at upper-right: navy-to-blue triangular A mark with semicircular cutout, white stylized Z, and exact blue wordmark "AlgoZenith" below. Keep logo clear, not a substitute letter.
Title near upper-left: "DFS: Returning Does Not Mean Unvisiting"
Subtitle: "Call stack while returning from vertex 3"
Four side-by-side panels in chronological left-to-right order. Each contains a vertical stack of flat teal rounded rectangular blocks with white labels. All stack bases align on a shared horizontal level but do not draw a connecting baseline. Stack TOP is at the uppermost occupied block, label "top" once adjacent to each top block.
Panel A heading: "At vertex 3". Stack bottom-to-top: "dfs(1)", "dfs(2)", "dfs(4)", "dfs(3)".
Panel B heading: "Return to 4". Stack bottom-to-top: "dfs(1)", "dfs(2)", "dfs(4)".
Panel C heading: "Return to 2". Stack bottom-to-top: "dfs(1)", "dfs(2)".
Panel D heading: "Resume at 1". Stack consists ONLY of "dfs(1)".
Place one small muted-red right-pointing process arrow BETWEEN each pair of panels, not on or through stack blocks. These show returns over time, not graph edges.
Below all four panels, a simple light-cream callout with thin dark-teal outline states on two lines:
"Visited stays {1, 2, 3, 4}"
"At vertex 1: skip neighbour 3 — already visited."
Bottom caption: "Returning removes a call, not a visited mark."
This is for the exact recursive call sequence dfs(1) -> dfs(2) -> dfs(4) -> dfs(3). After 3 finishes, 4 then 2 finish; 1 resumes its loop and skips 3. Do NOT reverse stack order, do NOT duplicate frames, do NOT unmark any vertex, do NOT add a fifth panel. No graph drawing needed. All text must be accurate and large enough to read. Match the reference's educational hand-drawn style, no photorealism or 3D. Canvas approximately 3:2 landscape.
```

