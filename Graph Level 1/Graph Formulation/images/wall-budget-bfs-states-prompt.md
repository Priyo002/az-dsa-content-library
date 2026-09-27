# Wall-budget BFS state diagram

- Mode: built-in image-generation tool, generation with a style/logo reference.
- Reference: the preceding minimum-walls lesson's AlgoZenith grid diagram, https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/8ba414da-9edb-4ce6-b84b-350fe46c5940.png.
- Final asset: `wall-budget-bfs-states.png`.
- Validation: the two-row grid, row/column labels, both states, move counts, remaining budgets, and six-move answer match the lesson. The cream background, complete rounded navy border, teal cells, and proper AlgoZenith mark and wordmark are present.

## Final prompt

Use case: scientific-educational.
Create a new landscape AlgoZenith lesson infographic explaining BFS states for a wall-breaking budget.
Input image 1 is a STYLE AND LOGO REFERENCE ONLY, not the graph to copy. Match its warm cream background, thin rounded dark navy border on every side, teal-blue grid cells, white handwritten symbols, dark handwritten captions, restrained red accents. Faithfully reproduce its proper blue triangular AlgoZenith mark with white stylized Z and AlgoZenith wordmark at top right.
Title: "Same cell, different states"
Subtitle: "k = 1   |   State = (row, column, walls broken)"
Left panel: a clear EXACTLY 2-row 5-column grid. Column labels 1 2 3 4 5 above; row labels 1 2 at left. Row 1 symbols exactly S # . # E. Row 2 symbols exactly . . . # #. Highlight row 1 column 3 with a thin gold inner outline, preserving its dot. Caption below: "Compare arrivals at (1, 3)". Do NOT draw route arrows on the grid.
Right panel: two clean cream cards outlined navy, vertically stacked.
Top card exact text: "(1, 3, 1)" then "2 moves | 0 breaks left" then "Cannot enter the wall at (1, 4)" in muted red.
Bottom card exact text: "(1, 3, 0)" then "4 moves | 1 break left" then "Can enter the wall at (1, 4)" in dark teal.
Bottom footer exact text: "Keep both states. Minimum moves to E: 6."
Scientific constraints: The grid has only ten cells, only one S and one E. No extra symbols, no adjacency arrows, no distance matrix. Ensure all text is readable and correctly spelled, all digits exact, no cropped border or logo. This diagram shows two paths arriving at the same cell with different remaining budgets, not simultaneous physical agents. Use roomy layout and consistent hand-drawn educational style.
