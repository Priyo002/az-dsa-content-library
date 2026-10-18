# Linked-list introduction image prompts

Generated using the built-in image-generation tool. The attached AlgoZenith diagram was used as the style and logo reference. No CLI fallback was used.

## Array and linked-list memory layout

Asset: `array-vs-linked-list-memory.png`

Use case: scientific-educational. Asset type: course-reading diagram for beginner linked-list students. Input image 1 is ONLY the visual-style and AlgoZenith-logo reference, not graph content to reproduce. Match its warm pale cream background, thin rounded dark teal outer frame, deep teal-blue filled nodes, dark brown outlines, simple neat handwritten-style labels, muted red accents and ample uncluttered space. No gradients except the supplied logo, no shadows, no 3D, no decorative icons. Reproduce the supplied AlgoZenith logo faithfully in the upper-right: blue triangular A shape with rounded bottom cutout, distinctive white stylized Z, and exact blue wordmark "AlgoZenith". Keep logo modest, clear, and separate from lesson content. Large legible labels and accurate arrows.
Primary request: Create one landscape educational diagram titled "Array vs Linked List". Two stacked panels with a thin separator, approximately 1536 by 1024.
Top panel title "Array: contiguous storage". Show exactly three touching equal blue rectangular array cells with white values 10, 20, 30 from left to right. Below cells labels "index 0", "index 1", "index 2". Caption "Elements are stored next to each other".
Bottom panel title "Linked list: follow the addresses". Show exactly THREE separated two-field rectangular nodes in a spacious zigzag: node 10 upper left, node 20 upper right, node 30 lower center. Within each node the left data compartment is deep teal blue with white value and right next compartment cream with dark text. Node 10 fields "10" and "2400"; node 20 fields "20" and "1600"; node 30 fields "30" and "nullptr". Put small field headings "data" and "next" above each node. Label above each node "address 1000", "address 2400", "address 1600" respectively. A separate pointer labelled "head" points to node 10. Draw one dark directed arrow FROM the 2400 next field of node 10 TO node 20; one dark directed arrow FROM the 1600 next field of node 20 TO node 30. No outgoing arrow from node 30. All arrows avoid labels. Under bottom panel, exact small note "Illustrative addresses" and main caption "Links determine the order: 10 -> 20 -> 30". Do NOT add any extra nodes, edge weights or links. The only arrowheads are head to 10, 10 to 20, and 20 to 30. Preserve logo shape from reference.

## Linked-list types

Asset: `linked-list-types.png`

Use case: scientific-educational. Asset type: course-reading diagram for beginner linked-list students. Input image 1 is ONLY the visual-style and AlgoZenith-logo reference, not graph content to reproduce. Match its warm pale cream background, thin rounded dark teal outer frame, deep teal-blue filled nodes, dark brown outlines, simple neat handwritten-style labels, muted red accents and ample uncluttered space. No gradients except the supplied logo, no shadows, no 3D, no decorative icons. Reproduce the supplied AlgoZenith logo faithfully in the upper-right: blue triangular A shape with rounded bottom cutout, distinctive white stylized Z, and exact blue wordmark "AlgoZenith". Keep logo modest, clear, and separate from lesson content. Large legible labels and accurate arrows.
Primary request: Create one landscape-to-square beginner educational diagram titled "Following the Links", approximately 1536 by 1200. Three well-spaced horizontal rows separated by thin subtle rules. All blue node circles contain white values exactly 10, 20, 30 in each row. This is a schematic of node connections, not memory layout. Every arrow must point as specified.
ROW 1 title "Singly linked list". A small "head" label with downward arrow points to node 10. Main chain 10 -> 20 -> 30 -> nullptr, all arrows rightward. Label the forward connections "next". Short caption "Forward only".
ROW 2 title "Doubly linked list". Small "head" downward pointer to node 10. Draw exactly two separate horizontal arrows between each adjacent pair of nodes: upper arrow to the RIGHT labelled "next", lower arrow to the LEFT labelled "prev". The first node 10 has a separate outgoing left arrow labelled "prev" ending at text "nullptr" at far left. Last node 30 has an outgoing right arrow labelled "next" ending at text "nullptr" at far right. Short caption "Forward and backward".
ROW 3 title "Circular singly linked list". Small "head" downward pointer to node 10. Draw 10 -> 20 -> 30 with rightward arrows labelled "next". From 30 draw a roomy dark curved return arrow BELOW all three nodes, travelling down then left then up, with its single arrowhead entering node 10. Label this return arrow "tail->next = head". No nullptr anywhere in this third row. Short caption at bottom "Stop after returning to head".
Keep all rows independent with no arrows between them. Exactly nine blue nodes total. No additional types, code, fields, symbols, numbers or paragraphs. Do not confuse prev arrow directions. Faithfully reproduce reference logo in top-right, outside the rows.

## Visual verification

- Memory diagram: array indices 0, 1, 2 hold 10, 20, 30; linked nodes use illustrative addresses 1000, 2400, 1600; next fields point to 2400, 1600, nullptr respectively.
- Type comparison: next arrows point forward, prev arrows point backward; non-circular endpoints terminate at nullptr; circular tail points back to head.
- Both images include the reference-style AlgoZenith symbol and wordmark.
- The generated diagrams omit the requested umbrella titles but retain clear panel titles. The memory diagram repeats the logo once per panel. These cosmetic differences do not affect the teaching content.

