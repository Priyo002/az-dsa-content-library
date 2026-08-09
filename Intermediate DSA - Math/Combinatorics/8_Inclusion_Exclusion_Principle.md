<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Inclusion-Exclusion Principle (IEP)

> *When counting combinations, it's easy to accidentally double-count elements that belong to multiple categories. The Inclusion-Exclusion Principle (IEP) is the mathematical ultimate weapon for perfectly balancing overlapping sets by systematically adding and subtracting intersections.*

---

## 1. What is the Inclusion-Exclusion Principle?

The Inclusion-Exclusion Principle is a fundamental counting technique used to determine the exact number of elements across overlapping sets. Instead of writing complex conditional loops to avoid double-counting, IEP allows us to adjust the total count mathematically by sequentially including and excluding specific intersection cases.

### The Formula for Two Sets
For two overlapping sets $A$ and $B$:
$$ |A \cup B| = |A| + |B| - |A \cap B| $$
*Logic: We add everything in $A$ and $B$. However, elements belonging to both were counted twice. We subtract their intersection $|A \cap B|$ once to correct the balance.*

### The Formula for Three Sets
For three overlapping sets $A$, $B$, and $C$:
$$ |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| $$
*Logic: We add all individual sets. We subtract all pair-wise intersections to fix double-counting. But wait! By subtracting all pairs, we accidentally completely removed the elements that belong to all three sets! We must add the triple intersection back at the end to restore them.*

> 💡 **Elite CP Insight: The Generalized $N$-Set Formula**
> While the 2-set and 3-set formulas are great for intuition, competitive programming problems often involve $N$ sets (e.g., *"Find the number of integers divisible by any prime in a given array of size $K$"*). 
> **The Generalized Pattern:** For *any* number of sets, the rule is always the same:
> 1. **Add** the sizes of all individual sets ($+$).
> 2. **Subtract** the sizes of all pairwise intersections ($-$).
> 3. **Add** the sizes of all 3-way intersections ($+$).
> 4. **Subtract** the sizes of all 4-way intersections ($-$).
> ...and so on, alternating signs based on whether the number of intersecting sets is **odd ($+$)** or **even ($-$)**!

<img src="images/iep_venn_diagram_architecture.jpg" alt="Inclusion Exclusion Principle 3-Set Venn Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Example Problems Using IEP

The true power of IEP is best demonstrated through real-world algorithmic problems. Let's explore three distinct applications.

### Example 1: Dice is Rolled 4 Times

**Problem:** A standard 6-sided die is rolled 4 times, and the numbers are recorded. Find the total number of different outcomes such that the largest number appearing is **not** 4.

> 💡 **Elite CP Insight: The Complementary Counting Trick**
> Trying to directly calculate "the largest number is NOT 4" is incredibly tedious. Instead, IEP teaches us to use Complementary Counting: Calculate the total possible universes, and subtract the universes where the largest number *is exactly* 4!

**Step 1: Count Total Possible Outcomes**
Each roll has $6$ choices. For $4$ rolls, the absolute total number of outcomes is:
$$ 6^4 = 1296 $$

**Step 2: Count Outcomes where the Largest is exactly 4**
To have $4$ as the absolute maximum, every roll must only use the numbers $\{1, 2, 3, 4\}$.
- Total outcomes restricted to $\{1, 2, 3, 4\}$ = $4^4$
- However, this includes outcomes where the largest number is only $3$ (e.g., rolling $\{1, 2, 3, 3\}$).
- To isolate cases where $4$ *actually* appears, we must subtract the subset of outcomes restricted strictly to $\{1, 2, 3\}$!
- Outcomes restricted to $\{1, 2, 3\}$ = $3^4$

Cases where the largest number is exactly 4: 
$$ 4^4 - 3^4 $$

**Step 3: Final IEP Calculation**
Total Outcomes $-$ (Cases where largest is exactly 4):
$$ 6^4 - (4^4 - 3^4) $$
$$ 1296 - (256 - 81) = 1296 - 175 = 1121 \text{ valid outcomes} $$

---

### Example 2: Counting Permutations Avoiding Substrings

**Problem:** Find the number of ways to arrange the 7 distinct letters `a, b, c, d, e, f, g` such that neither the substring `"cad"` nor the substring `"beg"` appear together.

**Step 1: Count the Total Unrestricted Arrangements**
Because all $7$ letters are unique, the total number of permutations is:
$$ 7! = 5040 $$

**Step 2: Treat Substrings as Single "Units"**
To count permutations containing `"cad"`, treat the three letters as one solid block. The remaining elements are `{cad, b, e, f, g}`.
- We now have $5$ distinct units to arrange.
- Arrangements containing `"cad"` = $5! = 120$

Similarly, to count permutations containing `"beg"`, treat it as a solid block. The remaining elements are `{beg, a, c, d, f}`.
- We have $5$ distinct units.
- Arrangements containing `"beg"` = $5! = 120$

**Step 3: The Intersection (Both Substrings Appear)**
If we enforce that *both* `"cad"` and `"beg"` must appear, we have the units `{cad, beg, f}`.
- We have exactly $3$ distinct units.
- Arrangements containing both = $3! = 6$

**Step 4: Apply Inclusion-Exclusion**
Valid Permutations = Total $-$ (Contains `"cad"` $\cup$ Contains `"beg"`)
$$ Valid = 7! - (|cad| + |beg| - |cad \cap beg|) $$
$$ Valid = 7! - (5! + 5! - 3!) $$
$$ Valid = 5040 - (120 + 120 - 6) = 5040 - 234 = 4806 $$

---

### Example 3: Counting Numbers Divisible by Multiple Primes

**Problem:** Find the number of integers between $1$ and $1000$ that are divisible by at least one of the primes $\{2, 3, 5\}$.

This is a classic 3-Set IEP problem! Let $A, B,$ and $C$ represent the sets of numbers divisible by $2, 3,$ and $5$ respectively.

**Step 1: Count Individual Sets (Using Floor Division)**
- $|A| = \lfloor 1000 / 2 \rfloor = 500$
- $|B| = \lfloor 1000 / 3 \rfloor = 333$
- $|C| = \lfloor 1000 / 5 \rfloor = 200$

**Step 2: Count Pairwise Intersections**
A number divisible by both $2$ and $3$ is divisible by their Least Common Multiple (LCM), which is $6$.
- $|A \cap B| = \lfloor 1000 / 6 \rfloor = 166$
- $|A \cap C| = \lfloor 1000 / 10 \rfloor = 100$
- $|B \cap C| = \lfloor 1000 / 15 \rfloor = 66$

**Step 3: Count the Triple Intersection**
A number divisible by $2, 3,$ and $5$ is divisible by their LCM, which is $30$.
- $|A \cap B \cap C| = \lfloor 1000 / 30 \rfloor = 33$

**Step 4: Execute the 3-Set IEP Formula**
$$ |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| $$
$$ |A \cup B \cup C| = 500 + 333 + 200 - 166 - 100 - 66 + 33 $$
$$ |A \cup B \cup C| = 1033 - 332 + 33 = 734 $$

Exactly $734$ numbers between $1$ and $1000$ are divisible by at least one of the primes $\{2, 3, 5\}$!

</READING_WIDGET>
