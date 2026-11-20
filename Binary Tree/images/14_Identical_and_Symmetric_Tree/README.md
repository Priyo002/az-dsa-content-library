# Identical and symmetric tree diagrams

Four 1536 × 1024 PNG illustrations are embedded in the lesson. Matching SVG
files retain editable shapes and text, with the supplied logo embedded as PNG.

| Asset | Teaching point |
| --- | --- |
| `01_identical_trees` | Same values and same left/right positions |
| `02_symmetric_mirror_pairs` | Compare LL with RR and LR with RL |
| `03_identical_structure_mismatch` | Moving a child breaks identity even when values match |
| `04_identical_but_not_symmetric` | Identical subtrees can fail the mirror structure check |

These exact geometric diagrams use the existing course's deterministic drawing
workflow. No image generation model or redrawn branding is involved.
`algozenith-original.png` is a byte-for-byte copy of the supplied official asset;
it is composited with its alpha channel at its original aspect ratio.

The palette is cream `#EFEBDA`, annotation/frame blue `#012B41`, node teal
`#005C83`, edge/outline brown `#28190E`, and white node values. PNG corners outside
the rounded card are transparent. Andale Mono annotations and Comic Sans MS
numerals match the neighboring lesson's chosen fonts, without claiming an exact
font match to the reference image.

To rebuild on macOS with Python 3 and Pillow:

```sh
python3 'Binary Tree/images/14_Identical_and_Symmetric_Tree/generate.py'
```

The script uses the system fonts under `/System/Library/Fonts/Supplemental`.
Tree edges are solid brown. The dotted blue line in the symmetry illustrations
denotes the reflection axis. Explicit `null` labels denote missing pointers,
not tree nodes. All other absent children are omitted for clarity.
