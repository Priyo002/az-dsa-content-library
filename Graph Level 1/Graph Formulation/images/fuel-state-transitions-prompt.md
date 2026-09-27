# Fuel-state transition diagram

- Mode: built-in image-generation tool, new diagram using a style/logo reference.
- Reference: the previous node-cost graph image, https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/6de252c3-7d06-4a32-908f-62f0168f116f.png.
- Final asset: `fuel-state-transitions.png`.
- Validation: buying adds one litre and costs P[u]; driving subtracts road length and costs zero additional money. Both feasibility conditions, empty initial tank, and any-fuel destination are correct. Rounded border, cream/teal palette, and proper AlgoZenith mark and wordmark are present.

## Final prompt

Use case: scientific-educational.
Generate a new landscape AlgoZenith course diagram explaining a fuel-constrained shortest-path state.
Input image 1: STYLE AND LOGO REFERENCE ONLY. Match the warm cream background, thin fully visible rounded navy border, teal-blue state shapes with white handwritten labels, dark handwritten captions, and restrained red accents. Preserve the proper AlgoZenith blue triangular mark with white stylized Z and AlgoZenith wordmark at top right. Do NOT copy the reference graph.
Title: "Two actions from a fuel state"
Subtitle: "State = (city, fuel)   |   Distance = money spent"
Main layout: two generous horizontal rows, each a source state box at left and destination state box at right, joined by one right-pointing arrow. No other arrows.
Top row: left box "(u, f)" and right box "(u, f + 1)". Arrow label above "Buy 1 litre"; label below "Money cost: P[u]". Small condition below the row "Allowed when f < C".
Bottom row: left box "(u, f)" and right box "(v, f - d)". Arrow label above "Drive on road u - v of length d"; label below "Money cost: 0". Small condition below the row "Allowed when f >= d".
Bottom footer in a clean outlined pale-gold band, exact text on two lines:
"Start: (A, 0), cost 0"
"Goal: any state (B, f), where 0 <= f <= C"
Constraints: exact state expressions, correct inequality signs and units. Buying increases fuel in the same city; driving changes city and decreases fuel. Do not show road length as a monetary cost. No extra graph or decoration, ample whitespace, all text clearly legible, no cropped border/logo.
