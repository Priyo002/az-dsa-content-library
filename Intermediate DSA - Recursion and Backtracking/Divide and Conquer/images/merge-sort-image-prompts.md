# Merge Sort image-generation prompts

Created using the built-in image-generation tool. Style and logo reference: the branded ABC Puzzle row-bucket illustration.

## merge-sort-three-steps

Use case: scientific-educational. Create landscape 1536x1024 educational bitmap. Reference is STYLE/LOGO ONLY. Match cream background, navy handwritten lettering, pale-blue array cells, pale-yellow callouts, red arrows and complete thick navy rounded outer border on all four sides with safe margins. Copy same AlgoZenith triangular blue A with white Z logo upper right. Large precise labels, no clutter, no ABC content. Title "Merge Sort: Divide → Conquer → Combine". Three vertically stacked stages. DIVIDE: array [5,1,4,2,3,2] splits via arrows into [5,1,4] and [2,3,2]. CONQUER: show arrows labeled "Sort each half recursively" leading to [1,4,5] and [2,2,3]. COMBINE: arrows from both sorted halves merge into [1,2,2,3,4,5]. Label "Merge the sorted halves". Bottom banner "Sorted halves still need a merge." Exactly correct array cells; input contains six values, output contains six including two 2s. This is a high-level three-stage overview, not a full recursion tree.

## merge-sort-three-pointers

Use case: scientific-educational. Create landscape 1536x1024 educational bitmap. Reference is STYLE/LOGO ONLY. Match cream background, navy handwritten lettering, pale-blue array cells, pale-yellow callouts, red arrows and complete thick navy rounded outer border on all four sides with safe margins. Copy same AlgoZenith triangular blue A with white Z logo upper right. Large precise labels, no clutter, no ABC content. Title "Merging: Compare the Two Unread Heads". Snapshot before taking next value: sorted input A=[1,4,5], B=[2,2,3]. A cell1 (value1) faded labeled "consumed"; arrow i=1 points at value4 (zero-based index1), highlight this cell. B arrow j=0 points at FIRST value2, highlight it. Output C six cells [1, blank, blank, blank, blank, blank], arrow k=1 points second empty cell. Callout "Compare 4 and 2 → take B[j]". Below a red downward arrow to after-state: output C=[1,2,blank,blank,blank,blank], labels "i = 1 (unchanged)", "j = 1", "k = 2". Bottom banner "Advance only the chosen input pointer; always advance k." Small footer "Indices are 0-based. Copy leftovers when one input ends." Use explicit empty cells not zeros. Accurately place pointer arrows.

## merge-sort-level-cost

Use case: scientific-educational. Create landscape 1536x1024 educational bitmap. Reference is STYLE/LOGO ONLY. Match cream background, navy handwritten lettering, pale-blue array cells, pale-yellow callouts, red arrows and complete thick navy rounded outer border on all four sides with safe margins. Copy same AlgoZenith triangular blue A with white Z logo upper right. Large precise labels, no clutter, no ABC content. Title "Why Merge Sort Takes Θ(n log n)". Subtitle "T(n) = 2T(n/2) + Θ(n)". A clear recursion-level diagram with three horizontal rows: depth0 one wide rectangle labeled "n"; depth1 two rectangles each "n/2"; depth2 four rectangles each "n/4". Connect parents to children with thin navy lines. At right of EVERY row a yellow callout "Total merge work: Θ(n)". Below show ellipsis then separate footer "Singleton leaves: Θ(n) total". Side bracket covering merging levels only labeled "log₂ n merging levels". Bottom large yellow banner "Θ(n) per level × log₂ n levels = Θ(n log n)". Small note "For n a power of two; the general bound is unchanged." No claim merging occurs at singleton leaves. All text readable.

## Pointer correction

Edit only the bottom-right C output array to contain exactly six cells: [1][2][empty][empty][empty][empty]. Point k=2 at the third cell. Preserve all other content, logo, colors, layout, and full outer border.

