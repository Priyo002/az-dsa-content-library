# Maximum path sum diagrams

Five 1536 × 1024 PNG illustrations are embedded beside the corresponding lesson
explanations. Each has an editable SVG with the original logo embedded.

| Asset | Teaching point |
| --- | --- |
| `01_optimal_path_below_root` | The optimum need not contain the root |
| `02_return_gain_vs_complete_path` | Save both branches as a candidate, return one branch |
| `03_negative_nodes_can_help` | Judge full gains; a negative node can connect the optimum |
| `04_all_negative_nonempty_path` | Discard negative child gains without allowing an empty answer |
| `05_postorder_gains` | Returned gains differ from the best complete path |

The deterministic SVG/PNG workflow follows neighboring lessons. Node rings mark
the selected path; tree edges remain undirected. The only arrow on a tree diagram
represents a gain returned to a parent, not an additional tree edge.

`algozenith-original.png` is a byte-for-byte copy of the supplied official
`BLUE AZ TEXT LOGO.png`. It retains the original transparent canvas, colors,
emblem, and wordmark. It is scaled proportionally without cropping or redrawing.
The SVG embeds the source bytes; the PNG composites the same source.

The card uses cream `#EFEBDA`, annotations and frame `#012B41`, node fill
`#005C83`, edges and outlines `#28190E`, and white node values. Outer corners
are transparent. Andale Mono annotations and Comic Sans MS numerals follow
neighboring lessons; these are not claimed to be the exact reference fonts.

Rebuild with Python 3, Pillow, and the macOS fonts used in the generator:

```sh
python3 'Binary Tree/images/16_Max_Path_Sum/generate.py'
```

Content checks: running example optimum 42, gain at node 20 is 35, root
candidate 34, root gain 25; chain `2, -5, 10` has child gain 5 and optimum 10;
root -5 with two children valued 10 has optimum 15; the all-negative tree
has optimum -2.
