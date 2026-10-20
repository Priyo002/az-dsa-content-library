# XOR Linked List — Image Prompts

Generated with the built-in image generation tool using the imagegen skill.

Style and logo reference: the user's attached cream-and-teal AlgoZenith illustration, `codex-clipboard-ebf32c37-9a7f-4890-855d-90171bf753e2.png`. The reference supplies styling and branding only, not lesson content.

Final lesson assets:

- `xor-neighbour-recovery.png`: encoded link storage and bidirectional neighbour recovery, section 3.
- `xor-insertion-update.png`: before/after insertion and the three affected link fields, section 7.
- `xor-section-reversal.png`: logical reversal of addresses 300 through 500 and boundary-only changes, section 10.

All node numbers denote illustrative addresses. Double-headed connectors show logical adjacency, not two stored pointer fields. Each node stores only one XOR link field.

All three images were visually checked for legible text, correct XOR expressions, exact node order, endpoint and boundary labels, connector directions, spacious layout, and AlgoZenith branding. No generated revisions were needed. The lesson's C++ implementations are unchanged.

## xor-neighbour-recovery.png

Use case: scientific-educational.
Asset type: embedded illustration for an AlgoZenith XOR linked list lesson.
Input image 1 is a STYLE AND BRAND REFERENCE ONLY. Create a new diagram; do not reproduce its graph content.
Style: match the supplied reference's warm ivory cream background (#efecda), slim dark teal rounded outer border, deep teal circular nodes, black/dark brown outlines, white node labels, muted red highlights, dark navy type and green-teal accents. Flat, exceptionally clean, premium and spacious. Crisp geometric lines and readable professional rounded sans-serif typography, with monospace for code/formulas. No shadows, textures, gradients in the diagram, or extraneous decorations.
Canvas: landscape 1536x1024. Generous margins, generous empty space, clear hierarchy. Use the large page area effectively without crowding. Keep text large enough to read in a lesson.
Brand: faithfully reproduce the reference's AlgoZenith blue triangular emblem with the white stylized Z and the exact wordmark "AlgoZenith" once at the top right. Keep a clear exclusion area around the logo. Title top left, no overlap.
Mathematical conventions: all numbers in nodes denote illustrative decimal ADDRESSES, not payload values. Use ^ for bitwise XOR, not an arithmetic plus. All connectors between adjacent nodes are single clean double-headed lines, denoting logical adjacency; not two separately stored pointer fields. Do not invent any extra edges.
Title: "Recover the Other Neighbour"
Subtitle: "One XOR field + one known neighbour"
Composition: one large horizontal three-node chain in the upper-middle, then two spacious calculation panels below.
The three nodes left to right are A, B, C. White identity letters inside teal circles. Small labels above A and C read "head" and "tail". Directly under each circle, label its address: "address 100", "address 200", "address 300". Highlight current node B with a thin gold outer ring; place the label "current" above B.
Under each address, a distinct cream field box showing these EXACT two-line labels:
under A: "link = 0 ^ 200" then "= 200";
under B: "link = 100 ^ 300" then "= 328";
under C: "link = 200 ^ 0" then "= 200".
The two lower calculation panels sit side by side, with very generous padding:
Left heading "Arrive from A"; main formula "328 ^ 100 = 300"; smaller result "Recover C".
Right heading "Arrive from C"; main formula "328 ^ 300 = 100"; smaller result "Recover A".
Make recovered result numbers in muted red. No arrows connecting the panels or crossing the formulas.
Footer exactly: "0 represents a missing neighbour. ^ means bitwise XOR."
Technical requirements: 100 XOR 300 equals 328. The field 328 is an encoding, not a neighbour address. Keep all text exact and all three field labels visibly separate. No extra nodes, no fabricated pointer fields.

## xor-insertion-update.png

Use case: scientific-educational.
Asset type: embedded illustration for an AlgoZenith XOR linked list lesson.
Input image 1 is a STYLE AND BRAND REFERENCE ONLY. Create a new diagram; do not reproduce its graph content.
Style: match the supplied reference's warm ivory cream background (#efecda), slim dark teal rounded outer border, deep teal circular nodes, black/dark brown outlines, white node labels, muted red highlights, dark navy type and green-teal accents. Flat, exceptionally clean, premium and spacious. Crisp geometric lines and readable professional rounded sans-serif typography, with monospace for code/formulas. No shadows, textures, gradients in the diagram, or extraneous decorations.
Canvas: landscape 1536x1024. Generous margins, generous empty space, clear hierarchy. Use the large page area effectively without crowding. Keep text large enough to read in a lesson.
Brand: faithfully reproduce the reference's AlgoZenith blue triangular emblem with the white stylized Z and the exact wordmark "AlgoZenith" once at the top right. Keep a clear exclusion area around the logo. Title top left, no overlap.
Mathematical conventions: all numbers in nodes denote illustrative decimal ADDRESSES, not payload values. Use ^ for bitwise XOR, not an arithmetic plus. All connectors between adjacent nodes are single clean double-headed lines, denoting logical adjacency; not two separately stored pointer fields. Do not invent any extra edges.
Title: "Insertion: Replace a Neighbour"
Subtitle: "Insert address 400 between 100 and 200"
Composition: two generously separated horizontal rows showing before and after, then three compact equation callouts aligned across the bottom.
Upper row labelled "Before": exactly three teal circular nodes containing "100", "200", "300" from left to right, linked by double-headed dark lines. Label "head" above 100 and "tail" above 300.
Lower row labelled "After": exactly four circular nodes containing "100", "400", "200", "300" from left to right. Node 400 is pale gold with navy digits and a small label "new" above; other nodes are teal with white digits. Label "head" above 100 and "tail" above 300. Show 100 to 400 and 400 to 200 connectors in teal-green; the 200 to 300 connector remains dark. No direct connector from 100 to 200 in the After row.
Below the rows, EXACT three callouts:
"New node 400" / "link = 100 ^ 200"
"At node 100" / "link ^= 200 ^ 400"
"At node 200" / "link ^= 100 ^ 400"
Use large precise monospaced formulas; ensure the ^ and ^= symbols are printed correctly.
Footer lines exactly:
"Cancel the old address. XOR in the new address."
"Numbers are addresses; the link at 300 is unchanged."
Avoid crossed arrows, stale dotted links, duplicate nodes, or excessive annotation. All logical adjacency lines attach cleanly at circle edges.

## xor-section-reversal.png

Use case: scientific-educational.
Asset type: embedded illustration for an AlgoZenith XOR linked list lesson.
Input image 1 is a STYLE AND BRAND REFERENCE ONLY. Create a new diagram; do not reproduce its graph content.
Style: match the supplied reference's warm ivory cream background (#efecda), slim dark teal rounded outer border, deep teal circular nodes, black/dark brown outlines, white node labels, muted red highlights, dark navy type and green-teal accents. Flat, exceptionally clean, premium and spacious. Crisp geometric lines and readable professional rounded sans-serif typography, with monospace for code/formulas. No shadows, textures, gradients in the diagram, or extraneous decorations.
Canvas: landscape 1536x1024. Generous margins, generous empty space, clear hierarchy. Use the large page area effectively without crowding. Keep text large enough to read in a lesson.
Brand: faithfully reproduce the reference's AlgoZenith blue triangular emblem with the white stylized Z and the exact wordmark "AlgoZenith" once at the top right. Keep a clear exclusion area around the logo. Title top left, no overlap.
Mathematical conventions: all numbers in nodes denote illustrative decimal ADDRESSES, not payload values. Use ^ for bitwise XOR, not an arithmetic plus. All connectors between adjacent nodes are single clean double-headed lines, denoting logical adjacency; not two separately stored pointer fields. Do not invent any extra edges.
Title: "Section Reversal: Change Only the Boundaries"
Subtitle: "Reverse addresses 300 through 500"
Composition: two main six-node rows with large vertical separation. Under them one simple focus callout and a short complexity note. Very legible wide layout. Title may wrap to two neat lines in the left area, never crowd the logo.
Upper row label "Before": EXACT node order 100, 200, 300, 400, 500, 600, each in a teal circle with white numerals.
Lower row label "After": EXACT node order 100, 200, 500, 400, 300, 600, each in a teal circle with white numerals.
In BOTH rows, put a soft pale-gold rounded highlight behind positions 3, 4, 5 only to mark the reversed section. The highlight is behind the nodes, not a connector.
The connector between position 1 and 2 is dark; the connector between position 2 and 3 is muted red; the connectors inside the highlighted three-node section are dark; the connector between position 5 and 6 is muted red. Every connector is double-headed and meets circle outlines cleanly. No crossed mapping arrows between the rows.
Above the four relevant nodes in each row show small identity labels to retain node identity:
Before: P above 200, L above 300, R above 500, S above 600.
After: P above 200, R above 500, L above 300, S above 600.
Keep 100 and 600 at the far ends in both rows. The middle node 400 keeps the same two neighbours.
Below rows in a spacious callout, EXACT text:
"Node 400 keeps the same neighbours"
"300 ^ 500 = 500 ^ 300"
"Only the links at P, L, R and S change."
Bottom footer: "O(1) rewiring when all four boundary nodes are known."
A tiny legend next to a red line reads "Changed boundary connection".
Critical: no claim that locating positions is constant-time. Reversal changes logical order, not physical memory addresses. Do not add extra links, data values, nodes or dense tables.

