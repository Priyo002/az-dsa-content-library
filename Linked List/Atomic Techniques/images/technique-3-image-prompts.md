# Technique 3: Image Prompts

Generation mode: built-in image generation (not CLI).

Purpose: three focused educational diagrams for `../3_Technique_3.md`, matching the existing AlgoZenith cream, teal, brown, and red visual style.

Style and logo reference: `middle-node-conventions.png` in this folder. The earlier clipboard reference was no longer available as a local file; the existing branded lesson image supplied the style and logo reference instead.

All three outputs were visually checked for node counts, directed links, labels, logo, spacing, and text clipping. No correction passes were needed. Original generated outputs are retained under `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/`.

## 1. cycle-structure.png

Saved asset: `cycle-structure.png`.

Original output: `exec-3e9ba12e-f751-4b8c-afd7-1d8fcb50f494.png`.

Final prompt:

```text
Use case: scientific-educational. Create one polished landscape educational diagram for a linked-list lesson, about 1536x1024. The input image is ONLY a style and AlgoZenith logo reference, not an edit target; do not copy its middle-node subject. Match its cream background, rounded dark-teal outer border, teal-blue circular nodes with white numbers and dark brown outlines, dark brown directed arrows, restrained red highlights, and navy typography. Reproduce the blue triangular AlgoZenith mark with white Z and the exact wordmark "AlgoZenith", small in the upper-right corner. Premium, clean, spacious editorial design: flat even cream fill, crisp lines, modest typography, generous margins and whitespace. No shadows, no texture, no gradients except within the reference logo, no cartoon illustration. Keep all artwork and captions well inside the border, with at least 80px bottom clearance. Use arrowheads at destinations, no accidental edges, no overlapping labels. All numbers and exact text must be legible.
Title: "A Linked List with a Cycle"
Main drawing occupies the spacious central canvas: a three-node horizontal prefix 1 → 2 → 3 points to entry node 4. Draw a large six-node clockwise loop on the right: 4 is left-middle of the loop, 5 upper-left, 6 upper-right, 7 right-middle, 8 lower-right, 9 lower-left. The directed edges must be exactly 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→8, 8→9, 9→4. Nine circles total, each number 1 through 9 exactly once. No nullptr in this diagram. Space prefix nodes generously and keep the loop large, never crossed.
A small "head" label points at node 1. A red halo around node 4 and nearby red label "Cycle entry: 4" identify entry unambiguously, without covering 3→4 or 4→5. Under only nodes 1,2,3, a slim bracket labeled "Prefix: 3 nodes". Inside the open loop, center "Cycle length: 6". Footer inside generous margins: "Following next revisits the same nodes." Do not include other text or extra nodes.
```

## 2. cycle-entry-reset.png

Saved asset: `cycle-entry-reset.png`.

Original output: `exec-a4a6c420-534a-4b39-9419-3a0db3ecf50b.png`.

Final prompt:

```text
Use case: scientific-educational. Create one polished landscape educational diagram for a linked-list lesson, about 1536x1024. The input image is ONLY a style and AlgoZenith logo reference, not an edit target; do not copy its middle-node subject. Match its cream background, rounded dark-teal outer border, teal-blue circular nodes with white numbers and dark brown outlines, dark brown directed arrows, restrained red highlights, and navy typography. Reproduce the blue triangular AlgoZenith mark with white Z and the exact wordmark "AlgoZenith", small in the upper-right corner. Premium, clean, spacious editorial design: flat even cream fill, crisp lines, modest typography, generous margins and whitespace. No shadows, no texture, no gradients except within the reference logo, no cartoon illustration. Keep all artwork and captions well inside the border, with at least 80px bottom clearance. Use arrowheads at destinations, no accidental edges, no overlapping labels. All numbers and exact text must be legible.
Title: "Finding the Cycle Entry"
Subtitle: "Floyd meets at 7. Reset one pointer to head."
Show TWO PARTIAL PATHS in a large central diagram, with both paths converging on ONE shared node 4 on the right. Top path has nodes 1 → 2 → 3 → 4. Bottom path has nodes 7 → 8 → 9 → the SAME shared 4. Use exactly seven circles: 1,2,3 top row and 7,8,9 bottom row, plus shared4 vertically centered to their right. Horizontal arrows 1→2→3 and 7→8→9; two diagonal arrows 3→4 and 9→4. All arrows end at boundaries, no crossing. Do not draw any other list edges or any duplicated node4. This is a view of the two pointer paths, not the entire list.
Label above node1 "From head"; below node7 "From meeting". Put small move labels "1", "2", "3" by each path's three arrows, with a discreet key "Arrow labels = moves" safely above the footer. Highlight shared node4 with one red outline halo, label "Cycle entry" beside it. Keep all numeric move labels visually smaller than node values, no confusion.
Bottom centered takeaway: "Move both pointers one link at a time."
Second footer line: "After 3 moves each, both reach node 4."
Maintain lots of whitespace between diagram, title, and footer; no full dry-run table.
```

## 3. cycle-removal.png

Saved asset: `cycle-removal.png`.

Original output: `exec-e157a3ef-20b3-466c-957a-1148d475a624.png`.

Final prompt:

```text
Use case: scientific-educational. Create one polished landscape educational diagram for a linked-list lesson, about 1536x1024. The input image is ONLY a style and AlgoZenith logo reference, not an edit target; do not copy its middle-node subject. Match its cream background, rounded dark-teal outer border, teal-blue circular nodes with white numbers and dark brown outlines, dark brown directed arrows, restrained red highlights, and navy typography. Reproduce the blue triangular AlgoZenith mark with white Z and the exact wordmark "AlgoZenith", small in the upper-right corner. Premium, clean, spacious editorial design: flat even cream fill, crisp lines, modest typography, generous margins and whitespace. No shadows, no texture, no gradients except within the reference logo, no cartoon illustration. Keep all artwork and captions well inside the border, with at least 80px bottom clearance. Use arrowheads at destinations, no accidental edges, no overlapping labels. All numbers and exact text must be legible.
Title: "Remove the Cycle, Keep Every Node"
Use two spacious horizontal sections separated by a thin pale teal rule, not heavy boxes.
Top section heading "Before". Draw a horizontal row of nine equal circles labeled 1,2,3,4,5,6,7,8,9 left to right, connected with dark-brown arrows 1→2→3→4→5→6→7→8→9. Show a SINGLE red return arrow from node9 exiting downward, running left below the row, then upward into the bottom of node4; its arrowhead must point INTO node4. This red edge is the one to change. Center a short annotation below that edge: "Replace 9 → 4 with 9 → nullptr". Do not add a null arrow to the top row, and do not cross out node9 or node4.
Bottom section heading "After". Draw exactly the same horizontal sequence 1→2→3→4→5→6→7→8→9, followed by an arrow to text "nullptr". No return edge in this bottom section. Fit all nine circles plus nullptr with generous horizontal spacing inside margins. A small "head" label above node1 in both rows. No extra arrows from labels that can look like data links.
Bottom takeaway with large margin: "Only one next pointer changes. All 9 nodes remain."
No code blocks, no extra diagrams. The node9-to-node4 edge must be visibly the only structural difference between the two sections.
```
