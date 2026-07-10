<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Combinations

In the previous module, we learned about Permutations—where the order of selection strictly matters. However, in many real-world problems, we just want to form a group or a team, and we don't care about the order in which they were selected. This is where **Combinations** come in!

---

## 1. What is a Combination?

A combination is a way of selecting objects from a set where **order does not matter**. Unlike permutations, combinations focus only on the *selection* of objects, not their *arrangement*.

For example, given the set $\{A, B, C\}$, different combinations of two elements are:
`AB, AC, BC`

In contrast, permutations would consider `AB` and `BA` as two completely different outcomes. For combinations, $\{A, B\}$ and $\{B, A\}$ are the exact same group!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d6db6340-3987-4a7d-b30c-25d2656a41a2.jpg" alt="Understanding Combinations" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Deriving the Formula Using Permutations

We can naturally derive the formula for combinations directly from what we already know about permutations!

The number of ways to arrange $R$ objects out of $N$ objects is given by permutations:
$$P(N, R) = \frac{N!}{(N - R)!}$$

However, since order does not matter in combinations, this permutation formula severely overcounts. Specifically, it counts every internal arrangement of those $R$ selected objects as a distinct outcome. 
To fix this overcounting, we must **divide by the $R!$ ways** to arrange those selected objects:

$$C(N, R) = \frac{P(N, R)}{R!} = \frac{\frac{N!}{(N - R)!}}{R!}$$

Thus, we obtain the standard formula for Combinations (often read as "$N$ choose $R$"):

$$C(N, R) = \binom{N}{R} = \frac{N!}{R!(N - R)!}$$

where:
- $N!$ represents the total arrangements of objects.
- $(N - R)!$ chops off the unselected objects.
- $R!$ divides out the redundant internal orderings of the selected objects!

### Example: Selecting Students
How many ways can we choose 3 students from a class of 10?

$$C(10, 3) = \frac{10!}{3!(10 - 3)!} = \frac{10!}{3! \times 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

So, there are exactly 120 unique groups of 3 students you can form.

> 💡 **CP Math Hack: The Symmetry Property**
> If you have 100 students and need to select 98 of them, calculating $C(100, 98)$ sounds mathematically terrifying. But think about it logically: choosing 98 students to keep is exactly the same as choosing 2 students to *leave behind*!
> 
> This gives us the Symmetry Property:
> $$\binom{N}{R} = \binom{N}{N - R}$$
> 
> Whenever $R$ is greater than half of $N$, immediately swap it to $N - R$ to make your calculations drastically smaller!

---

## 3. Committee Selection Problems

Combinations are heavily used in "Committee Selection" problems in Competitive Programming. Let's look at how to handle different mathematical conditions using the Addition and Multiplication principles.

### (a) Selecting Exactly 2 Men and 4 Women
Suppose we have a pool of 6 men and 8 women, and we need to form a 6-person committee of exactly 2 men **AND** 4 women.

- Ways to select 2 men from 6: $C(6, 2) = \frac{6!}{2!4!} = 15$
- Ways to select 4 women from 8: $C(8, 4) = \frac{8!}{4!4!} = 70$

Since we need men **AND** women to form the committee, we multiply (Multiplication Principle):
$$15 \times 70 = 1050 \text{ ways}$$

### (b) Selecting a Committee with AT LEAST 3 Women
If the committee consists of 6 people, and we must include *at least* 3 women, we must break this down into mutually exclusive cases (Addition Principle).

- **Case 1 (3W, 3M):** $C(8, 3) \times C(6, 3) = 56 \times 20 = 1120$
- **Case 2 (4W, 2M):** $C(8, 4) \times C(6, 2) = 70 \times 15 = 1050$
- **Case 3 (5W, 1M):** $C(8, 5) \times C(6, 1) = 56 \times 6 = 336$
- **Case 4 (6W, 0M):** $C(8, 6) \times C(6, 0) = 28 \times 1 = 28$

Since a committee can be Case 1 **OR** Case 2 **OR** Case 3 **OR** Case 4, we add them up:
$$1120 + 1050 + 336 + 28 = 2534 \text{ ways}$$

### (c) Selecting a Committee with AT MOST 3 Women
Similarly, we break this down into cases starting from 0 up to 3 women:

- **Case 1 (0W, 6M):** $C(8, 0) \times C(6, 6) = 1 \times 1 = 1$
- **Case 2 (1W, 5M):** $C(8, 1) \times C(6, 5) = 8 \times 6 = 48$
- **Case 3 (2W, 4M):** $C(8, 2) \times C(6, 4) = 28 \times 15 = 420$
- **Case 4 (3W, 3M):** $C(8, 3) \times C(6, 3) = 56 \times 20 = 1120$

Total ways = $1 + 48 + 420 + 1120 = 1589 \text{ ways}$

> 💡 **CP Insight:** When dealing with "At Least" or "At Most" problems, always ask yourself if calculating the *complement* (the opposite) is faster! For example, if a problem asks for "at least 1 woman", it is much faster to calculate `(Total possible committees of any gender) - (Committees with exactly 0 women)`.

---

> 🚀 **Next Up:** You have now mastered both Permutations (order matters) and Combinations (order does not matter). It's time to test your ability to distinguish between the two and apply the math in the **Combinations Quiz**!

</READING_WIDGET>
