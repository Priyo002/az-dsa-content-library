# Binary-State BFS Diagram

Generated with the built-in image-generation tool. Reference: `fuel-state-transitions.png` in this directory (visual style and AlgoZenith logo only).

## Final Prompt

Create one educational diagram matching the attached reference's visual design: warm cream background, complete rounded dark navy outer border, handwritten navy typography, teal/blue state boxes with white labels, restrained red highlights. Faithfully reproduce the proper AlgoZenith logo and wordmark from the reference in the top-right corner. This is a new diagram, not about fuel; replace all fuel content.
Title: "Avoid banned states with BFS"
Subtitle: "3-bit teaching example"
Show a spacious, mathematically exact selected-transition diagram:
Main horizontal route has three blue rounded boxes: "011", "001", "101". Put "Start" above 011 and "Target" above 101.
A directed arrow from 011 to 001 labelled "flip bit 1".
A directed arrow from 001 to 101 labelled "flip bit 2".
Below 011, show a red outlined rounded box "100" with "Banned" clearly next to it and a red cross. A directed arrow from 011 down to 100 labelled "+1"; show it is blocked. No other arrows.
Below the main route show "Minimum operations: 2".
Small footer: "Selected transitions only. Bit 0 is the rightmost bit."
Second footer: "Actual problem: 20 bits"
Ensure all strings have exactly three digits as specified, arrows point exactly as described, no extra transitions, labels never overlap arrows or nodes, and preserve the complete border. Proper reference AlgoZenith mark, not a generic A or plain Z.

## Verification

- `011 XOR 010 = 001`: flip bit 1.
- `001 XOR 100 = 101`: flip bit 2.
- `011 + 1 = 100`, which is banned.
- No allowed single operation transforms `011` into `101`; the illustrated two-operation route is optimal.
- The diagram explicitly uses a 3-bit teaching example and selected transitions, not the full 20-bit graph.
- Checked the labels, directed arrows, complete border, and reference-style AlgoZenith logo.
