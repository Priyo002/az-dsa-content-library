# BST insert and delete diagrams

Five 1536 × 1024 PNGs are embedded in the lesson. Matching SVG files and
`generate.py` retain editable, reproducible sources using the neighboring
lessons' deterministic drawing workflow.

| Asset | Teaching point |
| --- | --- |
| `01_insert_65` | Follow comparisons and attach a leaf satisfying every ancestor constraint |
| `02_delete_leaf` | Return null and reconnect the parent's child link |
| `03_delete_one_child` | Preserve and promote the deleted node's child |
| `04_delete_two_children` | Find successor, copy key, remove original node, preserve its child |
| `05_successor_vs_predecessor` | Different valid shapes can contain the same remaining keys |

Deletion examples are independent and begin with the lesson's eight-node tree.
Thin rings identify the node being inserted, deleted, copied, or promoted.
Arrows between trees indicate successive states; tree edges show child links.
The two-child diagram deliberately includes a temporary duplicate in its middle
state. The root object persists; only its key changes.

`algozenith-original.png` is a byte-for-byte copy of the supplied official
`BLUE AZ TEXT LOGO.png`. Its transparent background, full emblem and wordmark,
colors, and aspect ratio are preserved. SVGs embed the original bytes; PNGs
composite the original asset with proportional scaling.

Palette: cream `#EFEBDA`, annotation and frame `#012B41`, node fill `#005C83`,
node outlines and edges `#28190E`, white values. PNG outer corners remain
transparent. Andale Mono annotations and Comic Sans MS numerals match adjacent
course diagrams, without claiming an exact match to the reference's font.

Rebuild on macOS with Python 3 and Pillow:

```sh
python3 'Binary Tree/images/18_BST_Insert_and_Delete/generate.py'
```

The generator validates BST ordering, node reachability, and the exact remaining
key sets for every completed state. All five PNGs were visually checked for
label spacing, correct edges, and logo placement.
