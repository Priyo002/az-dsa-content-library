# Multisource BFS image correction

Authoring reference only; not part of the student lesson.

- Original URL: https://d3pdqc0wehtytt.cloudfront.net/media/reading-images/996edbe3-d9f1-48bb-a4a5-d24b99865558.png
- Archived original: `reference/multisource-monster-distances-original.png`.
- Final asset: `multisource-monster-distances-corrected.png`.
- Error: zero-based cell `(3,6)` said 1; its earliest monster-arrival time is 2.
- Built-in image generation was attempted but returned a usage-limit error; no generated output was used.
- The user then explicitly approved correcting the digit directly with a local image-editing script.
- Final method: copy the existing numeral 2 from cell `(1,6)` into cell `(3,6)` with Pillow. The source box was `(790,442,850,514)` and the target box was `(790,615,850,687)` in the original 1285-by-1085 raster. No resizing, restyling, or logo regeneration was performed.
- Pixel verification: changed pixels are confined to bounding box `(810,632,830,662)`. Every pixel outside this single digit's region is identical to the original, including all grid lines, other numbers, caption, rounded border, and AlgoZenith logo and wordmark.
- Visual verification: all 35 grid entries match the tested monster-distance matrix below. The two other supplied grid illustrations are correct and retain their original hosted URLs.

```text
2 1 0 1 1 2 3
2 # # 1 0 1 2
1 # 5 # # # #
0 # 4 # # 1 2
1 2 3 2 1 0 1
```
