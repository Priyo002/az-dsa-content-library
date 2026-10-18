# Technique 2 Image Prompts

Generated using the built-in image-generation tool. The user-provided AlgoZenith image is a style and logo reference only.

## middle-node-conventions.png

Use case: scientific-educational.
Asset: professional raster teaching diagram for AlgoZenith linked-list course.
Input image 1 is STYLE AND LOGO reference only, not content. Match cream backdrop, rounded dark teal border fully inside canvas, teal-blue circular nodes with white numerals, dark brown outlines and right-facing arrow links, muted-red annotations. Clean flat aesthetic, crisp large type, generous whitespace. Landscape 1536x1024. Faithfully reproduce reference AlgoZenith logo at upper right, blue triangular A with semicircular bottom notch, white stylized Z, wordmark "AlgoZenith". Keep logo/title separate. All text and borders fully visible, minimum 45px safe margins, no cropping. No unnecessary artwork, shadows or clutter. Singly linked lists have only rightward arrows between adjacent nodes and finish at literal text "nullptr" (not a node).
Title: "Which Middle Should We Return?"
Two spacious horizontal panels.
Upper panel heading "Odd length: 5 nodes". Draw exact sequence 10 -> 20 -> 30 -> 40 -> 50 -> nullptr. Red ring around30. Pointer labelled "Only middle" goes precisely to30.
Lower panel heading "Even length: 6 nodes". Draw exact sequence 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> nullptr. Red ring around30. Pointer above30 labelled "First middle". Separate pointer below40 labelled "Second middle". Keep labels separate with no overlap. The pointer for40 must point40, not30. Other nodes unhighlighted except outlined teal ring if needed around40.
Footer in two short lines: "This lesson returns the first middle." and "For both examples, the answer is the node containing 30."
No slow or fast pointers here. All node values exact, no duplicates. Head at left optional but omit if clutter.

## middle-node-slow-fast.png

Use case: scientific-educational.
Asset: professional raster teaching diagram for AlgoZenith linked-list course.
Input image 1 is STYLE AND LOGO reference only, not content. Match cream backdrop, rounded dark teal border fully inside canvas, teal-blue circular nodes with white numerals, dark brown outlines and right-facing arrow links, muted-red annotations. Clean flat aesthetic, crisp large type, generous whitespace. Landscape 1536x1024. Faithfully reproduce reference AlgoZenith logo at upper right, blue triangular A with semicircular bottom notch, white stylized Z, wordmark "AlgoZenith". Keep logo/title separate. All text and borders fully visible, minimum 45px safe margins, no cropping. No unnecessary artwork, shadows or clutter. Singly linked lists have only rightward arrows between adjacent nodes and finish at literal text "nullptr" (not a node).
Title: "Slow and Fast: First Middle"
Subtitle: "slow moves 1 link; fast moves 2 links"
Three horizontal snapshot rows of the SAME six-node list. Row labels small on left, all numeric nodes align in vertical columns across snapshots. Each row exactly: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> nullptr.
Row1 label "Start": red downward arrow labelled "slow" points10; blue upward arrow labelled "fast" points20.
Row2 label "After 1 iteration": red downward arrow labelled "slow" points20; blue upward arrow labelled "fast" points40.
Row3 label "After 2 iterations": red downward arrow labelled "slow" points30; blue upward arrow labelled "fast" points60. Highlight30 with red ring. 
Footer exact on separate readable lines:
"Stop: fast->next is nullptr."
"Return slow: 30, the first middle."
Technical invariant: these snapshots use initialization slow=head, fast=head->next and loop condition fast != nullptr && fast->next != nullptr. Fast ends at60, NOT nullptr. No additional movement arcs or code blocks. Arrange in generous stacked rows below header while preserving full footer and bottom border within image. No label overlap.

## Slow/fast image layout refinement

Edit this image ONLY for layout: the rounded dark teal outer border must be fully visible at the bottom with a 30 pixel cream gap between the footer text and border. Fit all existing content within the landscape canvas, making vertical spacing slightly more compact as necessary. Preserve all text verbatim, all node values, pointers, arrows, colors and the proper AlgoZenith logo. Three snapshots must remain: slow10 fast20; slow20 fast40; slow30 fast60. Each row has 10 20 30 40 50 60 nullptr. Keep both footer lines exactly. No new content, no changes to algorithm. Clean professional composition with no cropping on any edge.

## Verification

- Odd-length sequence has five nodes; the unique middle is 30.
- Even-length sequence has six nodes; first middle is 30 and second middle is 40.
- Compact-loop snapshots show slow/fast at 10/20, 20/40, then 30/60.
- Fast stops at the tail because fast->next is null; no extra slow movement occurs.
- Both final images were visually checked for node values, pointer placement, arrow direction, readable captions, full borders and AlgoZenith branding.

