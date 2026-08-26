<VIDEO_WIDGET>

<VIDEO_ID>972</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Brute Force

When we first encounter a problem, the most direct approach is often to explore every possible candidate and check which candidates satisfy the required conditions.

This is the central idea of **Brute Force**.

> **Brute Force systematically explores the complete search space and checks every relevant candidate.**

A brute-force solution may not be the fastest final solution, but it is still extremely valuable. It helps us:

- understand the complete search space;
- build a correct baseline solution;
- discover which constraints are expensive;
- compare optimized solutions against a trusted implementation; and
- recognize opportunities for pruning or deriving one value from another.

---

## 1. Brute Force and Backtracking

Brute Force and Backtracking are closely related, but they are not identical.

### Brute Force

Brute Force is the **algorithmic idea** of exploring every possible candidate.

The enumeration can be implemented using:

- nested loops;
- permutations;
- bitmasks;
- recursion; or
- another systematic generation technique.

### Backtracking

Backtracking is a common **recursive implementation of a brute-force search**. It constructs a candidate one decision at a time.

The important additional ability of backtracking is that it can stop exploring a partial candidate as soon as that candidate becomes invalid.

```text
Brute Force
Generate complete candidates → Check every candidate

Backtracking
Build a partial candidate → Check early → Abandon invalid branches
```

| Brute Force | Backtracking |
|---|---|
| Describes the exhaustive-search strategy | Describes a recursive search framework |
| May use loops, permutations, bitmasks, or recursion | Usually builds a solution level by level using recursion |
| Often checks after generating a complete candidate | Can check partial candidates and prune early |
| May not modify shared state | Often makes a move and undoes it before trying the next choice |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/050f3359-d14c-488f-9774-9ce7d76686f4.png" alt="Brute Force explores complete candidates while Backtracking prunes invalid partial branches" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **Interview Insight:** Calling a solution “backtracking” only because it uses recursion is incomplete. Explain what the partial state represents, which choices are tried, which invalid branches are pruned, and which state changes are undone.

---

## 2. A Digit-Mapping Problem

Consider the ten characters:

```text
{a, b, c, d, e, f, g, h, i, j}
```

Every character must map to a unique digit from $0$ to $9$. Since there are ten characters and ten digits, every digit must be used exactly once.

For a given integer $N$, where:

$$
1 \le N \le 100
$$

we must find the number of assignments satisfying:

$$
N = \frac{abcde}{fghij}
$$

Here, `abcde` and `fghij` represent five digit positions:

$$
abcde = 10000a + 1000b + 100c + 10d + e
$$

$$
fghij = 10000f + 1000g + 100h + 10i + j
$$

A leading zero is allowed. For example, `01234` represents the integer $1234$, but the zero still occupies one of the five digit positions.

### The two constraints

Every valid answer must satisfy:

1. **Unique mapping:** Across the ten positions, every digit from $0$ to $9$ appears exactly once.
2. **Equation:** $abcde = N \times fghij$.

The challenge is deciding which constraint should be guaranteed by the generator and which should be verified by the checker.

---

## 3. Generators and Checkers

When a brute-force problem contains multiple constraints, it is useful to separate the solution into two components.

### Generator

The **generator** systematically creates candidate solutions.

Generation is usually the larger and more expensive part because it determines how many candidates the program must visit.

### Checker

The **checker** determines whether one generated candidate satisfies the remaining constraints.

A good checker should usually be much faster than generating the complete search space.

There are two natural choices for this problem.

### Option 1

- **Generate:** Every unique assignment using a permutation of the ten digits.
- **Check:** Whether the generated numerator and denominator satisfy the equation.

### Option 2

- **Generate:** Values satisfying the equation by choosing `fghij` and calculating `abcde = N × fghij`.
- **Check:** Whether the two five-position numbers use every digit exactly once.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/42e36f1a-b5f2-40c1-a041-8a5e69bca722.png" alt="Comparison of the permutation generator and equation-based generator for the digit-mapping problem" style="max-width: 100%; height: auto;" identifier="az-img-upload">

> 💡 **Interview Insight:** Before coding brute force, estimate the number of candidates produced by each possible generator. Prefer a generator that automatically satisfies the strongest constraint or lets one unknown value be derived from another.

---

## 4. Option One: Generate the Unique Mapping

The unique-mapping constraint can be guaranteed by generating every permutation of the digits from $0$ to $9$.

For a permutation `arr`:

- `arr[0]` through `arr[4]` form `abcde`;
- `arr[5]` through `arr[9]` form `fghij`.

Because `arr` is a permutation, every digit is already used exactly once. The checker only needs to verify the equation.

```cpp
#include <bits/stdc++.h>
using namespace std;

int optionOne(int n) {
    int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int countSolutions = 0;

    do {
        int abcde = 10000 * arr[0]
                  +  1000 * arr[1]
                  +   100 * arr[2]
                  +    10 * arr[3]
                  +         arr[4];

        int fghij = 10000 * arr[5]
                  +  1000 * arr[6]
                  +   100 * arr[7]
                  +    10 * arr[8]
                  +         arr[9];

        if (abcde == n * fghij) {
            countSolutions++;
        }
    } while (next_permutation(arr, arr + 10));

    return countSolutions;
}
```

### Why this works

`next_permutation` visits every permutation because the array begins in sorted order.

Each permutation represents exactly one assignment of the ten digits to the ten characters. Therefore:

- the unique-mapping constraint is guaranteed by construction;
- the equation is checked for every possible mapping; and
- no valid mapping is missed.

### Complexity

There are:

$$
10! = 3,628,800
$$

permutations. Forming and checking the two numbers takes constant time, so:

$$
\text{Time Complexity} = O(10!)
$$

The permutation is maintained in an array of ten digits:

$$
\text{Auxiliary Space} = O(1)
$$

> 💡 **Interview Insight:** Checking `abcde == n * fghij` is cleaner than using integer division alone. A condition such as `abcde / fghij == n` can accept a truncated quotient unless divisibility is checked separately.

---

## 5. Option Two: Generate Using the Equation

The equation gives us:

$$
abcde = N \times fghij
$$

Therefore, we do not need to generate both numbers independently.

We can:

1. choose `fghij`;
2. reject it immediately if its own five positions contain a repeated digit;
3. calculate `abcde = N × fghij` only for a valid denominator; and
4. check the five positions of `abcde` against the digits already used by `fghij`.

Because `abcde` must not exceed $98765$:

$$
fghij \le \left\lfloor\frac{98765}{N}\right\rfloor
$$

### Checking the digits with early pruning

The checker uses a 10-bit mask. Bit $d$ records whether digit $d$ has already appeared.

It extracts exactly five positions from each number. Extracting exactly five positions is important because a four-digit integer such as $1234$ represents `01234` in the problem.

```cpp
bool addFiveDistinctDigits(int value, int& usedMask) {
    for (int position = 0; position < 5; position++) {
        int digit = value % 10;

        if (usedMask & (1 << digit)) {
            return false;
        }

        usedMask |= (1 << digit);
        value /= 10;
    }

    return true;
}
```

The function returns as soon as it encounters a repeated digit. After successfully inserting ten distinct positions, all ten mask bits must be set.

> ⚡ **CP Optimization: Early Pruning:** Check the denominator before calculating and inspecting the numerator. If `fghij` already repeats a digit, it can never belong to a valid answer. Multiplication itself is inexpensive; the useful saving is that invalid denominators skip all numerator-digit processing.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/b236ad9c-c147-46e8-bbe3-c6d604fbdb61.png" alt="Option Two flowchart that rejects duplicate denominator digits before processing the numerator" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Complete equation-based approach

```cpp
int optionTwo(int n) {
    int countSolutions = 0;
    int maximumDenominator = 98765 / n;
    const int allDigitsMask = (1 << 10) - 1;

    for (int fghij = 1234;
         fghij <= maximumDenominator;
         fghij++) {

        int usedMask = 0;

        // Reject an invalid denominator immediately.
        if (!addFiveDistinctDigits(fghij, usedMask)) {
            continue;
        }

        int abcde = fghij * n;

        // The numerator must not repeat its own digits or any
        // digit that was already used by the denominator.
        if (!addFiveDistinctDigits(abcde, usedMask)) {
            continue;
        }

        if (usedMask == allDigitsMask) {
            countSolutions++;
        }
    }

    return countSolutions;
}
```

The loop starts at $1234$, which represents `01234`. Any smaller integer written using five positions would contain the leading zero and at least one additional zero, so it could not satisfy the unique-digit constraint.

> 🚨 **C++ Trap: `01234` is not decimal 1234.** An integer literal beginning with `0` is interpreted as octal in C++. The literal `01234` has decimal value $668$. Use `1234` as the integer value and let the checker process exactly five digit positions, including the leading zero position.

### Complexity

At most roughly $10^5$ denominator values are examined. A candidate processes no more than ten digit positions, and invalid candidates may stop earlier.

Every bitmask operation takes constant time, giving:

$$
O\left(10^5 \times 10\right)
$$

Since the number of processed digits is fixed, this is usually described as approximately:

$$
O(10^5)
$$

The checker stores one integer mask:

$$
\text{Auxiliary Space} = O(1)
$$

> 💡 **Interview Insight:** A bitmask is a natural representation when the universe is small and fixed. Here, ten boolean facts fit inside one integer, and membership, insertion, and duplicate detection all become constant-time bit operations.

---

## 6. Comparing the Two Generators

| Property | Option One: Permutations | Option Two: Equation |
|---|---|---|
| Generated constraint | Unique mapping | Equation |
| Checked constraint | Equation | Unique mapping |
| Number of candidates | $10! = 3,628,800$ | At most about $10^5$ |
| Checker cost | Constant-time arithmetic | Inspect at most ten digit positions; stop on the first duplicate |
| Leading-zero handling | Naturally stored in the permutation | Must process exactly five positions |
| Overall preference | Correct and useful as a baseline | Smaller search space and generally preferable |

Option Two is better because the equation determines `abcde` completely once `fghij` is chosen. There is no reason to generate millions of unrelated pairs when one value can be derived directly from the other.

> 💡 **Interview Insight:** A common optimization technique is to reduce the number of independently generated variables. If an equation uniquely determines one variable from another, generate only the free variable and derive the dependent one.

---

## 7. Correctness of Option Two

To argue that the equation-based approach is correct, prove two things.

### Every counted answer is valid

For every counted pair:

- `abcde` is calculated as `n * fghij`, so the equation holds;
- the checker processes exactly ten digit positions; and
- all ten bits are set without encountering a duplicate, so every digit from $0$ to $9$ appears exactly once.

Therefore, every counted pair is valid.

### Every valid answer is found

For any valid answer, its denominator lies between `01234` and $\lfloor 98765/N \rfloor$. The loop visits that denominator, calculates its unique corresponding numerator, and the digit checker accepts it.

Therefore, no valid answer is missed.

---

## 8. Common Mistakes

### 1. Using a leading-zero integer literal

```cpp
int value = 01234; // Octal, not decimal 1234
```

Use `1234` as the integer value. The fixed five-iteration checker is responsible for including the leading-zero position.

### 2. Extracting digits until the value becomes zero

```cpp
while (value > 0) {
    // A leading zero is never processed.
}
```

Process exactly five positions instead.

### 3. Generating numerator and denominator independently

The equation already determines the numerator after choosing the denominator. Generating both values creates unnecessary work.

### 4. Forgetting the numerator bound

If `abcde > 98765`, it cannot be represented using the required five positions. Restrict the denominator to `98765 / n`.

### 5. Using division without checking divisibility

Integer division discards the remainder. Prefer multiplication or check the remainder before comparing the quotient.

---

## 9. The Brute-Force Design Checklist

Before implementing an exhaustive search, ask:

1. What are all the constraints?
2. Which constraint should the generator satisfy automatically?
3. Which remaining constraints can be checked quickly?
4. How many candidates will the generator produce?
5. Can one unknown be calculated from another?
6. Can an invalid candidate be rejected before it is fully generated?
7. Are leading zeros, duplicate values, or representation details important?
8. What is the simplest correct baseline?
9. What optimization reduces the search space rather than merely speeding up the checker?

The most important lesson is:

> **A good brute-force solution is designed around the smallest useful search space. Generate candidates using one constraint, then check the remaining constraints as cheaply as possible.**

This generator–checker mindset will lead naturally into Backtracking, where partial candidates are checked during generation and invalid branches are abandoned early.

</READING_WIDGET>
