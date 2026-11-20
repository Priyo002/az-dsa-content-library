# Nodes at distance K diagrams

Four 1536 × 1024 PNG illustrations are embedded in the lesson, with matching
editable SVG sources and a reproducible Python generator.

| Asset | Teaching point |
| --- | --- |
| `01_target_and_answer` | Answers can lie below the target or across an ancestor |
| `02_parent_access` | The parent map adds the missing upward move |
| `03_bfs_layers` | Process complete layers and stop before expanding distance K |
| `04_opposite_subtree_distance` | Reaching the opposite child uses two edges beyond leftDistance |

The deterministic drawing workflow follows neighboring lessons. Rings identify
answer nodes. The full tree uses undirected edges; arrows in the other diagrams
show traversal moves. The DFS local view explicitly omits target descendants.
The BFS diagram rearranges the same nodes into distance layers from target 5.

`algozenith-original.png` is a byte-for-byte copy of the supplied official
`BLUE AZ TEXT LOGO.png`, verified against the attachment. Its transparent canvas,
emblem, wordmark, colors, and proportions are preserved. SVGs embed the original
file bytes; PNGs composite that same asset with proportional scaling.

Background: `#EFEBDA`; text and frame: `#012B41`; nodes: `#005C83`;
outlines and edges: `#28190E`; values: white. PNG outer corners are transparent.
Andale Mono labels and Comic Sans MS numerals match neighboring diagrams;
these are approximations, not a claim about the reference's original fonts.

Rebuild with Python 3, Pillow, and the macOS fonts named in the generator:

```sh
python3 'Binary Tree/images/17_Nodes_at_Distance_K/generate.py'
```

Verified content: BFS layers are `[5]`, `[6, 2, 3]`, `[7, 4, 1]`, and `[0, 8]`.
For K = 2, only the third layer is returned. At cur 3, leftDistance = 0 and
the opposite-subtree remainder is `2 - 0 - 2 = 0`, so node 1 is collected.
