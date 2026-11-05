# BST and Balanced BST image prompts

Regenerated on 2026-11-01 using built-in image generation. All seven diagrams retain their existing asset paths in `../5_BST_and_Balanced_BST.md`.

## Shared generation prompt

Use case: scientific-educational. Regenerate this educational tree diagram from scratch with clean flat vector-like geometric artwork, as a 1536x1024 landscape PNG. Render a solid OPAQUE cream #EFEBDA rounded card with thin #012B41 frame inset12px radius36px stroke2.5px. For this intermediate artwork, make the entire image opaque cream including the exterior corners; final rounded-corner export will be applied separately. All interior pixels must be fully opaque: NO translucent/cloudy patches, texture, grain, shading, gradient, shadows, or lighting. Uniform cream everywhere inside except diagram ink. Near-circular nodes radius32, solid teal #005C83, brown #28190E outline5px; centered white readable 26px values. Straight brown edges3.5px behind nodes, no arrows unless specified. All annotations darkpetrol #012B41, clean rounded lightly handwritten monospace24px. Generous empty space at top, no large title. Blank cream upper-right x1216..1380 y140..304 reserved for original logo to be composited afterwards: do NOT draw any logo. Keep specified content, exact edges and spelling; never invent connections. No extra decoration. 

## Final export

Generated opaque artwork was finished using Node.js and Sharp. Palette normalization removed background variation, with white and teal restricted to node interiors. Diagram edges were antialiased before compositing on a fresh 1536 × 1024 cream card. The frame has a 12-pixel inset, 36-pixel corner radius, and 2.5-pixel petrol border. Exterior corners are transparent.

The complete original `BLUE AZ TEXT LOGO.png` was composited with its original alpha and aspect ratio, resized to 150 × 150 at (1240, 95), without redrawing or recoloring it.

Palette: cream `#EFEBDA`, node fill `#005C83`, outlines and edges `#28190E`, annotations and frame `#012B41`, node values `#FFFFFF`. Antialiased boundaries blend neighboring colors.

## Review

Visual review covered tree links, search direction, subtree ranges, heights, label spacing, and branding. The lesson text and image references remain unchanged.

## 1. bst-subtree-ordering.png

Exact twelve-node lecture tree, each value appears once: 5 at(750,350); its left child4 at(430,460), right child7 at(1000,460). 4 has ONLY left child0 at(310,580). 0 has left child -5 at(190,710), right child2 at(430,710). 2 has ONLY left child1 at(350,840). 7 has left child6 at(860,580), right child10 at(1150,580). 10 has left child9 at(1040,710), right child100 at(1280,710). 9 has ONLY left child8 at(960,840). Exactly eleven edges, no additional edges, no null nodes. All circles diameter64px; fit100 with26px lettering. Add small text above left subtree at(360,350) "all values < 5"; above right subtree at(1050,350) "all values > 5", safely clear of root and logo. Under diagram centered y945 exact text "Inorder: -5 0 1 2 4 5 6 7 8 9 10 100". No traversal arrows. This diagram shows the full tree and its sorted inorder sequence.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-fd007b8a-d629-423f-ae9a-88a9cf553ec6.png`

Final asset: `bst-subtree-ordering.png`

## 2. bst-ancestor-constraint.png

Draw ONLY four nodes in left half: root5 at(510,420), left child4 at(320,590), right child7 at(700,590); 7 has ONLY left child3 at(580,760). Exactly three tree edges. At right x900 y490 text "3 < 7"; next line y545 "Parent check passes". At right x900 y665 text "Required: 5 < value < 7"; next line y720 "Ancestor check fails". Below node3 centered x580 y855 label "allowed interval: (5, 7)". Keep all text away from tree edges and border. No red marks, no extra boxes, no title. Demonstrate that node3 is smaller than7 but incorrectly sits in5's right subtree.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-2b69e69a-731e-499b-920d-e40db2d403df.png`

Final asset: `bst-ancestor-constraint.png`

## 3. bst-search-path.png

Show the exact twelve-node lecture tree on the left with compact but spacious placement: 5 at(580,350); 4 at(300,470),7 at(800,470); 0 at(210,590),6 at(680,590),10 at(930,590); -5 at(125,710),2 at(300,710),9 at(830,710),100 at(1040,710); 1 at(230,830),8 at(750,830). EXACT edges:5-left4,5-right7,4-left0,0-left(-5),0-right2,2-left1,7-left6,7-right10,10-left9,10-right100,9-left8. Exactly12 nodes and11 edges. All same fill. Make ONLY the four structural edges on the search path 5–7–10–9–8 heavier (6px brown); all other edges3px brown. Put small darkpetrol step annotations near path nodes: "1" just aboveleft5, "2" just upperright7, "3" just upperright10, "4" just left9, "5" just right8, each clearly outside circles. On right x1140 y440 text "find 8". Below at x1140 y505 "8 > 5: right"; y560 "8 > 7: right"; y615 "8 < 10: left"; y670 "8 < 9: left"; y725 "8 = 8: found". These are plain unboxed short lines, not panels. Below tree centered(600,930) text "5 → 7 → 10 → 9 → 8". No other text.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-91066d28-9d8e-4dd7-862d-f577362774bd.png`

Final asset: `bst-search-path.png`

## 4. bst-postorder-validation.png

Show the subtree rooted at10 from the lesson in center: 10 at(760,410), left9 at(490,590), right100 at(1050,590), and9 has ONLY left8 at(350,765). Exactly four circles and three structural tree edges. Above10 at(760,335) exact "isBST = true, range = [8, 100]". Left of9 around(245,510) exact "range = [8, 9]"; below100 at(1080,700) exact "range = [100, 100]"; below8 at(350,845) exact "range = [8, 8]". Show two short thin dark-petrol arrows next to but distinct from the edges9–10 and100–10, pointing UPWARD toward10 to indicate returned summaries; arrows must not touch labels or cross edges. Center beneath diagram at(800,925) exact "max(left) < 10 < min(right): 9 < 10 < 100". No title, no boxes, no other text. The extrema summarize all descendants, not only immediate children.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-e5df1dad-5144-4766-bcdb-7319f6b94f79.png`

Final asset: `bst-postorder-validation.png`

## 5. bst-height-comparison.png

Compare two separate BSTs using SAME seven keys1,2,3,4,5,6,7. Left chain has node1 at(180,380), rightchild2 at(235,460), rightchild3 at(290,540), rightchild4 at(345,620), rightchild5 at(400,700), rightchild6 at(455,780), rightchild7 at(510,860). Every link slopes down-right; exactly six links. Right balanced tree root4 at(1050,430), left2 at(880,600), right6 at(1220,600); node2 left1 at(795,770),right3 at(965,770); node6 left5 at(1135,770),right7 at(1305,770). Six links on this tree. Modest group labels "Skewed BST" centered(345,310) and "Balanced BST" centered(1050,350), both24px regular. Left below at(345,945) "h = 7"; right below at(1050,870) "h = 3"; right nextline(1050,925) "Same keys, shorter paths". No arrows between trees, no suggestion this is a single rotation, no extra nodes. Height measured in nodes.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-e15b5afe-1f85-438a-bfe1-f5fa4a98f226.png`

Final asset: `bst-height-comparison.png`

## 6. bst-balance-every-node.png

Exact twelve-node lecture tree, each value appears once: 5 at(750,350); its left child4 at(430,460), right child7 at(1000,460). 4 has ONLY left child0 at(310,580). 0 has left child -5 at(190,710), right child2 at(430,710). 2 has ONLY left child1 at(350,840). 7 has left child6 at(860,580), right child10 at(1150,580). 10 has left child9 at(1040,710), right child100 at(1280,710). 9 has ONLY left child8 at(960,840). Exactly eleven edges, no additional edges, no null nodes. All circles diameter64px; fit100 with26px lettering. Add three compact callouts in otherwise open whitespace, ALL24px regular. At(470,340) "root: |4 - 4| = 0". Left of4 in free area x115 y430 text "node 4:" and next line x115 y470 "|3 - 0| = 3"; this block must remain left of4 without touching its edge to0. At right of7 in free area x1160 y420 text "node 7:" and next line x1160 y460 "|1 - 3| = 2". Below tree at(768,945) text "The height condition must hold at every node." No extra rings or color highlights; same fill everywhere. The root passes but nodes4 and7 fail. Exactly12 nodes and11 edges remain as specified.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-a6289024-7634-432f-8aae-cf5b62b8a419.png`

Final asset: `bst-balance-every-node.png`

## 7. bst-balanced-heights.png

Draw exact nine-node balanced lecture BST with local height labels beside every node: root5 at(760,370); left child2 at(480,520), right child8 at(1040,520). 2 has left -1 at(310,680), right4 at(650,680). 8 has left7 at(900,680),right10 at(1180,680). -1 has left -3 at(205,840),right0 at(415,840). Exactly eight straight structural edges; no others. Put labels "h = 4" next to5 at(870,365); "h = 3" left of2 at(365,510); "h = 2" right of8 at(1150,510); "h = 2" left of -1 at(190,670); "h = 1" below4 at(650,750); "h = 1" below7 at(900,750); "h = 1" below10 at(1180,750); "h = 1" below -3 at(205,910); "h = 1" below0 at(415,910). Ensure height labels have noticeable gap from node outlines and no collision with diagonals. Small plain note at(1000,870) "empty subtree: h = 0"; next line at(1000,925) "h = 1 + max(left, right)". No title or footer. These are heights in nodes, returned bottom-up.

Generated intermediate: `/Users/priyabratadas/.codex/generated_images/01a08680-2c84-7422-8407-6f171aeb67e5/exec-a9f1b947-c74e-4336-9160-46699e840e0e.png`

Final asset: `bst-balanced-heights.png`

