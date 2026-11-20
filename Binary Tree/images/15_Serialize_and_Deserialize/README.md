# Serialization and deserialization diagrams

Four 1536 × 1024 PNG illustrations are embedded in the lesson. Matching SVG
files retain editable geometry and text with the original logo embedded.

| Asset | Teaching point |
| --- | --- |
| `01_null_markers_preserve_structure` | Null markers distinguish left and right child positions |
| `02_bfs_serialization` | Visit queued positions in level order, including nulls |
| `03_bfs_deserialization` | Assign two child tokens to each real parent in queue order |
| `04_dfs_subtree_boundaries` | Each recursive call consumes one complete subtree encoding |

These diagrams extend the neighboring lessons' deterministic drawing workflow.
No image generation model or redrawn logo is used. The logo file is a
byte-for-byte copy of the supplied `BLUE AZ TEXT LOGO.png`, composited with its
original transparency and aspect ratio. The SVG embeds those original bytes.

Colors: cream `#EFEBDA`, annotation/frame blue `#012B41`, node teal `#005C83`,
edge/outline brown `#28190E`, and white node values. Outside corners are
transparent. Andale Mono annotations and Comic Sans MS numerals match the
neighboring lessons' chosen fonts; they are not claimed to be the reference's
exact fonts. Null markers are plain text, not real nodes.

The running example has five real nodes and six null positions. Its complete
BFS encoding is `1,2,3,#,-4,2,#,#,#,#,#`; its complete DFS encoding is
`1,2,#,-4,#,#,3,2,#,#,#`. Labels `2a` and `2b` distinguish positions and are
not serialized values. DFS indices are token indices, not character offsets.

Rebuild on macOS with Python 3, Pillow, and the fonts under
`/System/Library/Fonts/Supplemental`:

```sh
python3 'Binary Tree/images/15_Serialize_and_Deserialize/generate.py'
```
