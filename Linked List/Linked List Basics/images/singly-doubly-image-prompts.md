# Singly and Doubly Linked List — Image Prompts

Generated with the built-in image generation tool (not the CLI/API fallback).

## Visual reference

- Style and logo reference: `../../Advanced Techniques/images/xor-neighbour-recovery.png`.
- Match the established cream background, thin rounded teal border, navy typography, deep-blue nodes and AlgoZenith logo.
- The reference provides styling and branding only; the diagrams use the introductory lessons' values 10, 20 and 30.

## Assets and placement

| Asset | Lesson placement | Learning purpose |
| --- | --- | --- |
| `singly-linked-list-structure.png` | After the node/head explanation in `../2_Introduction_to_Singly_Linked_List.md` | Data and next fields, forward traversal, final null pointer. |
| `doubly-linked-list-structure.png` | After the three node fields in `../3_Introduction_to_doubtly_Linked_List.md` | Data, prev and next fields, separate pointer directions, null endpoints. |

The lessons reference these local PNGs instead of the previous CloudFront-hosted images. No lesson prose or code was changed.

## Validation

- Both final PNGs are 1536 × 1024 and were visually inspected.
- Singly: three data nodes, forward next links, head at 10, final next set to nullptr.
- Doubly: three data nodes, distinct next/prev directions, first prev and last next set to nullptr.
- Labels, values, AlgoZenith branding and reference-style layout were checked.
- Both local image paths resolve, and neither lesson retains a remote image URL.
- Comparing the lessons before and after while ignoring image tags confirms all other content is unchanged.

## 1. singly-linked-list-structure.png

```text
Use case: infographic-diagram.
Asset type: a polished educational PNG diagram embedded in an AlgoZenith linked-list lesson.
Input image role: the supplied image is ONLY a style and AlgoZenith logo reference. Create entirely new linked-list content; do not reproduce its XOR topic, addresses or equations.
Style: match the reference's warm ivory/cream background, thin dark-teal rounded outer border, rich navy rounded sans-serif headings, teal accents, restrained muted-red annotations, deep-blue node fills and clean dark outlines. Spacious, premium, professional, crisp and flat, with generous margins and excellent readable typography. Landscape 1536 by 1024, 3:2 composition.
Branding: reproduce the reference's blue triangular AlgoZenith emblem with its white stylized Z and exact wordmark "AlgoZenith" once in the upper-right corner, small and unobtrusive. No other logo.
Layout: title at top left; large structural diagram through the middle; a small explanatory strip below. No code, no textures, no hand-drawn scribbles, no screenshot UI, no tiny text. Pointer labels are field names, not data values. All arrowheads and labels must be unambiguous, separated, unobstructed.
Primary request: explain the structure of a singly linked list with three nodes holding exactly 10, 20, 30, in that order.
Exact title: "Singly Linked List"
Subtitle: "Each node stores data and one next pointer"
Main diagram: three large horizontal rectangular nodes, evenly spaced. Each node has TWO compartments: a wide deep-blue data compartment containing its white value (10, 20 or 30), and a narrower pale-teal next-pointer compartment containing a small dark pointer dot. Small clear field headers "data" and "next" appear above the corresponding compartments. The next dot is a pointer symbol, not a numeric data value.
Draw ONE right-pointing teal arrow from node 10's next compartment to node 20, then ONE right-pointing teal arrow from node 20's next compartment to node 30, then ONE right-pointing teal arrow from node 30's next compartment ending at the text "nullptr". Connect each arrow visibly to its pointer dot. There are NO backward arrows or prev fields.
A green-teal label "head" with a downward arrow points to the first node (10). A small muted label "last node" identifies node 30 without an extra pointer arrow.
Bottom explanatory strip in two spacious side-by-side lightly outlined cards:
Left card heading "data"; body "Stores the node's value".
Right card heading "next"; body "Points to the following node".
Below the two cards, one concise muted-red takeaway: "The last node's next pointer is nullptr."
Accuracy: head is a pointer to node 10, not an extra node. Exactly three nodes, exactly three next arrows including the null terminator. nullptr is not a node. No addresses or bidirectional links. Make the three nodes, arrows and final nullptr the visual focus.
```

## 2. doubly-linked-list-structure.png

```text
Use case: infographic-diagram.
Asset type: a polished educational PNG diagram embedded in an AlgoZenith linked-list lesson.
Input image role: the supplied image is ONLY a style and AlgoZenith logo reference. Create entirely new linked-list content; do not reproduce its XOR topic, addresses or equations.
Style: match the reference's warm ivory/cream background, thin dark-teal rounded outer border, rich navy rounded sans-serif headings, teal accents, restrained muted-red annotations, deep-blue node fills and clean dark outlines. Spacious, premium, professional, crisp and flat, with generous margins and excellent readable typography. Landscape 1536 by 1024, 3:2 composition.
Branding: reproduce the reference's blue triangular AlgoZenith emblem with its white stylized Z and exact wordmark "AlgoZenith" once in the upper-right corner, small and unobtrusive. No other logo.
Layout: title at top left; large structural diagram through the middle; a small explanatory strip below. No code, no textures, no hand-drawn scribbles, no screenshot UI, no tiny text. Pointer labels are field names, not data values. All arrowheads and labels must be unambiguous, separated, unobstructed.
Primary request: explain the structure of a doubly linked list with three nodes holding exactly 10, 20, 30, in that order.
Exact title: "Doubly Linked List"
Subtitle: "Each node stores data, prev and next pointers"
Main diagram: three large horizontal rectangular nodes, evenly spaced. Each node has THREE compartments: a narrow pale-teal prev field on the LEFT, a wide deep-blue data field in the CENTER containing its white value (10, 20 or 30), and a narrow pale-teal next field on the RIGHT. Small clear field headers "prev", "data", "next" sit above their respective compartments. Pointer compartments contain small dark dots, not numeric data values.
In each gap between adjacent nodes, draw two well-separated horizontal links:
UPPER teal arrow pointing RIGHT, labelled "next": node 10 to node 20; node 20 to node 30.
LOWER muted-red arrow pointing LEFT, labelled "prev": node 20 to node 10; node 30 to node 20.
Keep the two arrows parallel and visibly distinct, with ample vertical space for their labels, never crossed. Connect next arrows to right-hand next compartments, and prev arrows to left-hand prev compartments; opposing arrows must not merge into one double-headed line.
At far LEFT, a muted-red left-pointing arrow from the first node's prev compartment ends at "nullptr".
At far RIGHT, a teal right-pointing arrow from the last node's next compartment ends at "nullptr".
A teal label "head" with a downward arrow points to the first node (10). A small muted label "last node" identifies node 30.
Bottom explanatory strip: three spacious lightly outlined cards in a row, containing the exact headings and bodies:
"prev" / "Previous node"
"data" / "Stored value"
"next" / "Following node"
Under the cards, one concise muted-red takeaway: "First prev = nullptr     Last next = nullptr"
Accuracy: exactly three data nodes, two next links between nodes, two reverse prev links between nodes, two null endpoint arrows. nullptr labels are not nodes. Head is not a node. Do not imply prev or next store the values 10/20/30 themselves. Keep the diagram uncluttered and arrows anatomically correct.
```

