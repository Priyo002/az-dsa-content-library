<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Permutations

Now that you have mastered the foundational Counting Principles, it's time to explore specific techniques for arranging objects. The first of these techniques is called a **Permutation**. 

---

## 1. What is a Permutation?

A permutation is an arrangement of objects in a **specific order**. When the order of selection *matters*, we use permutations. 

For example, given the set $\{A, B, C\}$, different permutations of two elements are:
`AB, BA, AC, CA, BC, CB`

For Permutations, **Position is everything!**

---

## 2. Number of Permutations of {1, 2, 3, ..., N}

If we have $N$ distinct objects, the number of ways to arrange them in a sequence is given by:
$$P(N) = N!$$

Where $N!$ ($N$ factorial) represents:
$$N! = N \times (N-1) \times (N-2) \times ... \times 1$$

### Example: Arranging Numbers
How many ways can we arrange the numbers $\{1, 2, 3, 4\}$?

$$4! = 4 \times 3 \times 2 \times 1 = 24$$

So there are exactly 24 unique ways to arrange $\{1, 2, 3, 4\}$.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/3760144f-f675-4157-940b-f9bdd84ee3ec.jpg" alt="Permutations of Three Elements" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **Core Insight:** Think about the Multiplication Principle! For the first spot in the arrangement, you have 4 choices. For the second spot, you only have 3 choices left. For the third, 2 choices, and for the final spot, 1 choice. Multiplying these independent choices together ($4 \times 3 \times 2 \times 1$) naturally creates the factorial!

---

## 3. Number of 5-Digit Passwords (No Repetition)

Let's apply this logic to a real-world problem. Suppose we want to create a 5-letter password using the 26 English letters (A-Z), and **no letter can be repeated**.

- **First letter:** 26 choices
- **Second letter:** 25 choices (one is already used)
- **Third letter:** 24 choices
- **Fourth letter:** 23 choices
- **Fifth letter:** 22 choices

By the Multiplication Principle, the total possible passwords are:
$$26 \times 25 \times 24 \times 23 \times 22$$

Using formal permutation notation, this is selecting 5 items out of 26:
$$P(26, 5) = \frac{26!}{(26 - 5)!} = \frac{26!}{21!}$$

Notice how dividing by $21!$ perfectly cancels out all the factors from $21$ down to $1$, leaving just $26 \times 25 \times 24 \times 23 \times 22$.

---

## 4. The General Formula: $^nP_r$

The general mathematical formula for permutations of $N$ objects taken $R$ at a time is:

$$P(N, R) = \frac{N!}{(N - R)!}$$

- $N!$ represents the total number of ways to arrange all $N$ objects.
- Dividing by $(N - R)!$ mathematically "chops off" and removes the arrangements of the remaining unused objects that we don't care about.

### Example: Selecting Letters
How many ways can we arrange exactly 3 letters from $\{A, B, C, D\}$?

$$P(4, 3) = \frac{4!}{(4 - 3)!} = \frac{4!}{1!} = \frac{24}{1} = 24$$

This formula successfully counts all ordered sequences of length 3 using 4 distinct letters.

---

## 5. Permutations with Repeated Elements

Things get tricky when some of our elements are identical. If we use the standard factorial formula, we will severely overcount, because swapping two identical elements looks like a brand new permutation to the math formula, even though it looks exactly the same to our eyes!

To fix this, we must **divide** by the factorials of those identical elements.

### The Repetition Formula
If a set contains $N$ total objects, where:
- $A$ elements are identical,
- $B$ elements are identical,
- $C$ elements are identical,

The number of *unique* permutations is:
$$\frac{N!}{A! \times B! \times C!}$$

### Example: The Anagram Problem
How many unique ways can we arrange the letters `AAABBBBCCCCCC`?

- Total letters ($N$) = $13$ letters
- Identical `A`s ($A$) = $3$
- Identical `B`s ($B$) = $4$
- Identical `C`s ($C$) = $6$

Using the formula:
$$\frac{13!}{3! \times 4! \times 6!}$$

By dividing out the internal permutations of identical letters ($3!$, $4!$, and $6!$), we perfectly eliminate all the overcounted duplicates!

> 🚨 **CP Warning: Integer Overflow & Modulo Arithmetic!**
> Be extremely careful with factorials in Competitive Programming. The value of $13!$ is $6,227,020,800$, which instantly overflows a standard 32-bit signed integer! Because factorials grow astronomically fast, CP problems almost always ask you to output the answer **modulo $10^9 + 7$**.
> 
> Furthermore, because this repetition formula requires *division* ($\frac{N!}{A! \times B!}$), you **cannot** simply use the standard modulo operator `%`. Instead, you must multiply by the **Modular Multiplicative Inverse (MMI)** of the denominator!

> 🚀 **Next Up:** Now that we understand how to arrange items where order strictly matters (Permutations), what happens when we just want to select items and don't care about the order at all? Let's dive into **Combinations**!

</READING_WIDGET>
