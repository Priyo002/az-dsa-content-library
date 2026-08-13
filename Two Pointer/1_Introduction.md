<VIDEO_WIDGET>

<VIDEO_ID>2936</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to Two Pointers

Suppose you are given an array and asked to examine many pairs, subarrays, or positions. The first solution that comes to mind often checks every possible combination. This repeated work can take $O(N^2)$ time. For an array of size $10^5$, that may mean roughly $10^{10}$ operations—far too slow.

But many problems do not require us to reconsider every possible pair independently. If we process the array in a careful order, information from the current state can tell us where to move next.

That is the central idea behind **Two Pointers**.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/9f5e54dc-502a-48bd-a558-a32f8c104df6.png" alt="Two Pointers move through a sequence without repeating work" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. What Is the Two Pointer Technique?

The Two Pointer technique uses two indices, iterators, or positions to explore one or more sequences in a controlled manner.

In this course, we use `tail` for the **left pointer** and `head` for the **right pointer**. Depending on the form, they may represent:

- the beginning and end of the same array,
- the boundaries of a window,
- the current positions in two different arrays, or
- two positions moving at different times according to a condition.

Not every form needs both pointers. In Form 0, only `head` moves; the other boundary of the fixed window is derived from its size.

> 💡 **Important:** These are usually not C++ memory pointers such as `int*`. In this technique, the word **pointer** normally means an array index or iterator that points to a position.

The power of the technique comes from two rules:

1. Each pointer moves according to a clear condition.
2. A pointer usually moves in only one direction and does not revisit old positions.

When each pointer crosses an array at most once, the total work is often $O(N)$, even if one loop is written inside another.

---

## 2. The Real Idea: Maintain an Invariant

Two Pointer problems are not solved merely by declaring two variables. We must decide what those variables **mean** throughout the algorithm.

That meaning is called an **invariant**—a condition that remains true while the algorithm runs.

For example, in a window problem, our invariant could be:

> `sum` is always the sum of the elements in the current window `[tail, head]`.

Whenever `head` moves forward, the new element enters the maintained range. Whenever `tail` moves forward, the old element leaves it. The information describing the range must be updated with both movements.

Instead of calculating the entire window again, we update only what changed. This reuse of previous work is what makes the technique efficient.

For every Two Pointer problem, ask these three questions:

1. **What does each pointer represent?**
2. **When should each pointer move?**
3. **What information must remain correct after a pointer moves?**

If these answers are clear, the implementation usually becomes much easier.

---

## 3. The Four Forms of Two Pointers

In this course, we will study Two Pointers through four reusable forms. Each form has a different pointer movement pattern.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/512e280c-2dbf-40e6-bd1c-37d9093a244f.png" alt="The four forms of the Two Pointer technique" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Form 0: Sliding Window or Fixed Window

In a fixed-size window, we use only one moving pointer: `head`. It visits every element from left to right and represents the end of the current window.

For a window of size $K$ ending at `head`, the starting position is derived automatically:

$$\text{start} = \text{head} - K + 1$$

As `head` moves, the new element is added and the element that is now $K$ positions behind it is removed. The algorithm never needs a separately moving `tail`. This reduces many solutions from $O(NK)$ to $O(N)$.

---

### Form 1: Variable Size Window

In a variable-size window, `head` is the right pointer and expands the current range. The `tail` pointer is the left pointer and shrinks the range whenever the maintained condition requires an adjustment. Because the pointers can move independently, the window grows and contracts as the algorithm progresses.

> 🚨 **The Monotonicity Requirement:** A variable-size window does not work for every subarray problem. Moving a boundary must change validity in a predictable direction. For example, with non-negative numbers, expanding a window never decreases its sum. With arbitrary negative numbers, that property disappears, so a standard sliding window may produce the wrong answer.

---

### Form 2: Divergence Type

In the Divergence form, `tail` begins at the left end and `head` begins at the right end. They move toward each other.

The comparison at the current positions tells us which pointer should move. The algorithm deliberately eliminates impossible choices without checking them again.

The sorted or ordered nature of the problem is often what makes safe elimination possible.

---

### Form 3: Multisequence Type

In the Multisequence form, `tail` and `head` belong to different sequences. Each pointer tracks how much of its own sequence has already been processed. A comparison between the current elements determines whether one pointer or both pointers should advance.

If the first sequence has length $N$ and the second has length $M$, each pointer usually moves only forward, giving a total time complexity of $O(N + M)$.

---

## 4. Comparing the Four Forms

| Form | Initial pointer positions | Movement pattern | Main recognition signal |
|---|---|---|---|
| **Form 0: Fixed Window** | Only `head` is used | `head` moves forward; the start is derived using $K$ | Every considered range has the same size |
| **Form 1: Variable Window** | `tail` and `head` usually start at the beginning | `head` expands; `tail` shrinks conditionally | The valid range can grow or shrink |
| **Form 2: Divergence** | `tail` at the left end; `head` at the right end | Move toward each other | A comparison safely eliminates one side |
| **Form 3: Multisequence** | One pointer in each sequence | Advance `tail`, `head`, or both | Two sequences must be processed together |

The problem statement may never say “use Two Pointers.” Your job is to recognize the movement pattern hidden inside it.

---

## 5. Why Can Two Pointers Be $O(N)$?

At first glance, a Two Pointer process may appear to be $O(N^2)$ because one pointer can move while the other is still progressing. But count the total movements.

- In Form 0, `head` crosses the sequence once: at most $N$ movements.
- In the other forms, `head` and `tail` each cross their relevant sequence at most once.

Therefore, the total number of pointer movements is at most about $2N$:

$$N + N = 2N = O(N)$$

This analysis is called **amortized analysis**. A pointer may move several times during one step, but its total movement across the complete algorithm remains linear.

> 💡 **Important:** Two Pointers is not automatically $O(N)$. The linear bound depends on monotonic pointer movement and constant-time work per movement. If pointers repeatedly move backward or if every movement performs another expensive operation, the complexity can be higher.

---

## 6. A Pattern-Based Problem-Solving Checklist

Before writing code, follow this process:

### Step 1: Write the brute-force idea

Understand what combinations, pairs, or ranges the direct solution checks. This reveals the repeated work that needs to be removed.

### Step 2: Identify the form

Ask whether the problem uses:

- a fixed-size range,
- a range whose size changes,
- opposite ends of one sequence, or
- positions in multiple sequences.

### Step 3: Define the pointer meanings

Write a sentence such as:

> “`tail` is the left boundary and `head` is the right boundary of the current valid window.”

### Step 4: Define the invariant

Decide what data describes the current state: sum, frequency, number of distinct values, mismatch count, or something else.

### Step 5: Write the movement rules

For every condition, decide exactly which pointer moves and why the discarded position can never be part of a better answer.

### Step 6: Prove the complexity

Count how many times each pointer can move. Do not assume that nested loops automatically mean $O(N^2)$.

---

## 7. Common Mistakes

### Mistake 1: Mixing inclusive and exclusive boundaries

If the current window is `[tail, head]`, its length is:

$$\text{length} = \text{head} - \text{tail} + 1$$

Forgetting the `+1` is one of the most common off-by-one errors.

### Mistake 2: Updating the state in the wrong order

When shrinking a window, remove the element at `tail` from the maintained state **before** moving `tail` forward. Reversing this order removes the wrong element and breaks the invariant.

### Mistake 3: Moving both pointers without proof

Sometimes only `tail` should move; sometimes only `head`; sometimes both. Form 0 uses only `head`. Moving a pointer without a clear reason can skip the correct answer.

### Mistake 4: Using a variable window when validity is not monotonic

Negative values, non-local conditions, or complex dependencies can make a normal sliding window invalid. In those cases, another technique such as prefix sums, binary search, a deque, or a map may be required.

### Mistake 5: Forgetting empty and single-element inputs

Always consider:

- `n = 0`,
- `n = 1`,
- no valid answer,
- the entire sequence being the answer, and
- duplicate values.

---

## 8. Course Roadmap

We will now study each form separately:

1. **Form 0 — Sliding Window or Fixed Window:** Maintain information for every range of an exact size.
2. **Form 1 — Variable Size Window:** Expand and shrink a range while maintaining a validity condition.
3. **Form 2 — Divergence Type:** Start from separated positions and eliminate possibilities through ordered movement.
4. **Form 3 — Multisequence Type:** Coordinate pointers across two or more sequences.

Do not try to memorize isolated solutions. Learn the invariant and movement pattern behind each form. Once you can recognize those patterns, many problems that initially look unrelated begin to feel like variations of the same idea.

</READING_WIDGET>
