<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Derangement (No Fixed Point Permutations)

> *Imagine you write 5 letters and address 5 envelopes. If you randomly stuff the letters into the envelopes, what are the odds that **none** of the letters end up in their correct envelope? This specific constraint—where absolutely no element is allowed to remain in its original position—is called a **Derangement**.*

---

## 1. What is a Derangement?

A **Derangement** is a permutation of elements where no element appears in its original position. It is commonly referred to in competitive programming as a *"no fixed point permutation"*.

Let's look at the permutations of the word **"ABC"** (where A is in position 1, B in 2, C in 3):
- `ABC` ❌ (A, B, and C are all in their original positions)
- `ACB` ❌ (A is in its original position)
- `BAC` ❌ (C is in its original position)
- `BCA` ✅ (B is in 1, C is in 2, A is in 3. **Valid!**)
- `CAB` ✅ (C is in 1, A is in 2, B is in 3. **Valid!**)
- `CBA` ❌ (B is in its original position)

Out of 6 possible permutations, only **2** are valid derangements!

<img src="images/derangement_architecture.jpg" alt="Derangement Combinatorics Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Deriving the Formula using IEP

How do we count derangements for $N$ objects? We can leverage the **Inclusion-Exclusion Principle (IEP)**! 
Let $D_n$ (or $!n$) denote the number of derangements of $n$ objects.

The logic is exactly the same as our generalized IEP module:
1. Start with the total unrestricted permutations: $n!$
2. Subtract all permutations where at least $1$ element is fixed.
3. Add back permutations where at least $2$ elements are fixed (since we subtracted them twice).
4. Subtract permutations where at least $3$ elements are fixed.
...and so on!

### The Math Breakdown

Let $A_i$ be the set of permutations where the $i$-th element is fixed in its original position.
- **Single Fixed Position ($|A_i|$):** If 1 element is fixed, the remaining $(n-1)$ elements can be arranged freely. Since there are $\binom{n}{1}$ choices for the fixed element, the total is: $\binom{n}{1} \times (n-1)! = \frac{n!}{1!}$
- **Two Fixed Positions ($|A_i \cap A_j|$):** If 2 elements are fixed, the remaining $(n-2)$ elements can be arranged freely. There are $\binom{n}{2}$ choices. Total: $\binom{n}{2} \times (n-2)! = \frac{n!}{2!}$
- **$k$ Fixed Positions:** $\binom{n}{k} \times (n-k)! = \frac{n!}{k!}$

If we plug this directly into our alternating IEP formula, we get the master Derangement formula:
$$ D_n = n! - \frac{n!}{1!} + \frac{n!}{2!} - \frac{n!}{3!} + \dots + (-1)^n \frac{n!}{n!} $$

Factoring out $n!$, we get:
$$ D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!} \right) $$

> 💡 **Elite CP Insight: Euler's Number ($e$) Approximation**
> If you look closely at the infinite Taylor series for $e^x$, specifically for $e^{-1}$, it evaluates to:
> $$ e^{-1} = \frac{1}{e} = 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots $$
> Because this series converges incredibly fast, for any $n \ge 1$, the number of derangements is simply the nearest integer to:
> $$ D_n \approx \frac{n!}{e} \quad (\text{where } e \approx 2.718) $$

### The Base Cases
You should memorize the first few values of $D_n$ for fast CP debugging:
- $!1 = 0$
- $!2 = 1$
- $!3 = 2$
- $!4 = 9$
- $!5 = 44$
- $!6 = 265$

---

## 3. Real-World Algorithmic Examples

### Example 1: Arranging Letters ("SWORD")
**Problem:** Find the number of ways to rearrange the letters of "SWORD" such that no letter remains in its original position.
**Solution:**
We have 5 distinct letters, and no letter can stay in its original position. This is the exact definition of $D_5$.
$$ D_5 = 5! \left( 1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} \right) $$
$$ D_5 = 120 \times \left( \frac{1}{2} - \frac{1}{6} + \frac{1}{24} - \frac{1}{120} \right) = 44 $$
There are **44** valid derangements.

### Example 2: Colored Balls and Boxes
**Problem:** There are 5 balls, each colored differently, and 5 boxes of the same colors. Find the number of ways to place the balls such that no ball is placed in the box of its own color.
**Solution:** 
This problem is a pure mathematical reskin of Example 1!
- Each ball acts as a "Letter".
- Each colored box acts as an "Original Position".
Because no object is allowed in its matching position, this is simply $D_5 = 44$.

### Example 3: Enforcing a Specific Constraint
**Problem:** We have 6 numbered cards and 6 numbered envelopes, labeled 1 to 6. Find the number of ways to place the cards such that no card is placed in the envelope with the same number, **AND** Card 1 must absolutely go into Envelope 2.

**Solution:**
If there were no extra restrictions, the total number of valid derangements would just be $D_6 = 265$.

Now, let's analyze the restriction. In a standard unrestricted derangement of 6 items, Card 1 cannot go into Envelope 1. This leaves exactly **5** valid envelopes for Card 1: `{2, 3, 4, 5, 6}`. 
By symmetry, an equal number of derangements exist where Card 1 goes into Envelope 2, as where it goes into Envelope 3, etc.
Therefore, forcing Card 1 into Envelope 2 isolates exactly one-fifth of the total derangements!
$$ \text{Valid Arrangements} = \frac{D_6}{5} = \frac{265}{5} = 53 $$

</READING_WIDGET>
