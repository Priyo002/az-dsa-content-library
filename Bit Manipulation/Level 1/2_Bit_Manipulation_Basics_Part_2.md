<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bit Manipulation Basics — Part 2

We learned how integers are represented in binary and how AND, OR, XOR, NOT, and shifts operate on their bits. We can now combine those operations to change selected positions without disturbing the rest of a number.

The central tool is a **bit mask**: an integer whose set bits identify the positions we want to work with. We will use masks to set, clear, check, and flip bits, then study subtraction by one, count set bits, and reverse the bits in an inclusive range.

All code uses **C++17** and unsigned integers. Bit positions are **zero-based from the right**. Unless stated otherwise, each example starts from its own original value; the examples are not a sequence of cumulative updates.

## 1. Build a Mask for One Position

To select bit `i`, start with `1` and shift it left by `i`:

```text
i = 0: 00000001   = 1
i = 1: 00000010   = 2
i = 2: 00000100   = 4
i = 3: 00001000   = 8
```

The expression `1ULL << i` creates a mask with exactly bit `i` set. The suffix `ULL` makes the left operand an `unsigned long long`, so the shift uses that type's width.

### Shared Type and Headers

Use the following declarations with the functions throughout this lesson:

```cpp
#include <bitset>
#include <iostream>
#include <limits>
#include <stdexcept>
using namespace std;

using Bits = unsigned long long;
constexpr int W = numeric_limits<Bits>::digits;

Bits bitMask(int i) {
    if (i < 0 || i >= W) {
        throw out_of_range("Bit index is outside the integer width");
    }
    return 1ULL << i;
}
```

`W` is the number of value bits in our unsigned type, commonly 64 and guaranteed to be at least 64. Valid positions are `0` through `W - 1`. The check happens **before** shifting, so an invalid index cannot trigger an invalid shift.

The helper throws an exception for invalid input. In a contest problem, the constraints may already guarantee valid positions, but the requirement still needs to be understood.

## 2. Set a Bit: Make It `1`

To set bit `i`, OR the number with its single-bit mask:

```text
x | (1ULL << i)
```

At the selected position, OR with `1` produces `1`. Everywhere else, OR with `0` preserves the original bit.

### Example: Set Bit 2 of `17`

```text
x       = 10001   = 17
mask    = 00100   = 4
          -----
x | mask= 10101   = 21
```

```cpp
Bits setBit(Bits x, int i) {
    return x | bitMask(i);
}
```

Setting a bit that is already `1` changes nothing. This is why adding `2^i` is not a general substitute: addition may carry into other positions.

## 3. Unset a Bit: Make It `0`

To clear bit `i`, AND the number with the complement of its mask:

```text
x & ~(1ULL << i)
```

The complemented mask has a zero only at position `i`. AND with zero clears that position; AND with one preserves every other position.

### Example: Clear Bit 3 of `92`

The following drawing shows seven low bits; higher bits of the complemented mask are also ones.

```text
x        = 1011100   = 92
mask     = 0001000
~mask    = 1110111   shown in seven bits
           -------
x & ~mask= 1010100   = 84
```

```cpp
Bits unsetBit(Bits x, int i) {
    return x & ~bitMask(i);
}
```

Clearing an already clear bit leaves it unchanged. Subtracting `2^i` is not equivalent unless that bit is known to be set; otherwise, subtraction borrows from other positions.

## 4. Check a Bit

AND with a single-bit mask isolates the selected position:

```text
(x & (1ULL << i)) != 0
```

### Example: Check Bit 4 of `84`

```text
Position: 6 5 4 3 2 1 0
x:        1 0 1 0 1 0 0   = 84
mask:     0 0 1 0 0 0 0   = 16
AND:      0 0 1 0 0 0 0   = 16
```

The result is nonzero, so the bit is set.

```cpp
bool checkBit(Bits x, int i) {
    return (x & bitMask(i)) != 0;
}
```

Do not compare the masked result to `1`: checking position 4 produces `16`, not `1`. An alternative is `((x >> i) & 1ULL) != 0`, provided `i` is valid.

**CP insight:** `(x & 1ULL) != 0` checks whether an unsigned integer is odd. It inspects position 0 directly.

## 5. Flip a Bit: Toggle `0` and `1`

XOR with `1` flips a bit, and XOR with `0` preserves it. Therefore:

```text
x ^ (1ULL << i)
```

### Example: Flip Bit 1 of `84`

```text
x        = 1010100   = 84
mask     = 0000010   = 2
           -------
x ^ mask = 1010110   = 86
```

With zero-based indexing, bit 1 is the **second bit from the right**. The result `1010101 = 85` would come from flipping bit **0**, not bit 1.

```cpp
Bits flipBit(Bits x, int i) {
    return x ^ bitMask(i);
}
```

Flipping the same position twice restores the original number because `(x ^ mask) ^ mask = x`.

### The Four Operations Together

For a valid single-bit mask `m = 1ULL << i`:

| Operation | Expression | Effect at bit `i` |
| --- | --- | --- |
| Set | `x \| m` | Becomes `1` |
| Unset | `x & ~m` | Becomes `0` |
| Check | `(x & m) != 0` | Reports whether it is `1` |
| Flip | `x ^ m` | Changes to the opposite value |

The functions return a result; they do not modify the caller's variable. To keep a change, assign it: `x = setBit(x, 2)`. Compound assignments such as `x |= mask`, `x &= ~mask`, and `x ^= mask` also update `x` directly.

## 6. What Exactly Does `x - 1` Do?

For a **positive** integer `x`, identify its rightmost set bit. All positions to its right must be zeros. Subtracting one borrows through those zeros until it reaches that set bit.

As a result:

1. The rightmost set bit changes from `1` to `0`.
2. Every lower bit changes from `0` to `1`.
3. Every higher bit remains unchanged.

### Example: `84 - 1 = 83`

```text
Position: 6 5 4 3 2 1 0
x:        1 0 1 0 1 0 0   = 84
x - 1:    1 0 1 0 0 1 1   = 83
                  ^ ^ ^
                  changed positions
```

The rightmost set bit was at position 2. The suffix `100` becomes `011`, while the prefix `1010` stays unchanged.

In general, if `x` ends with a `1` followed by `k` zeros:

```text
x     = [unchanged prefix] 1 000...000
x - 1 = [unchanged prefix] 0 111...111
                            k positions
```

An odd number has `k = 0`, so only its final `1` changes to `0`. For example, `1011 - 1 = 1010`.

Zero is a separate case: it has no rightmost set bit. For our unsigned type, `0ULL - 1ULL` wraps to the maximum value with all `W` bits set. The positive-number borrowing explanation does not apply to zero.

## 7. Clear the Rightmost Set Bit with `x & (x - 1)`

ANDing `x` with `x - 1` clears exactly the rightmost set bit:

```text
x           = 1010100   = 84
x - 1       = 1010011   = 83
              -------
x & (x - 1) = 1010000   = 80
```

Why does this work?

- Higher bits are identical in both numbers, so AND preserves them.
- At the rightmost set position, AND combines `1` with `0`, producing `0`.
- Lower positions were zeros in `x`, so AND keeps them zero.

```cpp
Bits clearRightmostSetBit(Bits x) {
    return x & (x - 1ULL);
}
```

For `x = 0`, the unsigned subtraction wraps, but AND with zero still returns zero.

This expression does **not** generally find the largest power of two below `x`. For example, `84 & 83 = 80`, which is not a power of two. Repeatedly clearing low set bits until only one remains can isolate the highest set bit, but a single application has the narrower purpose described above.

### Check Whether a Number Is a Power of Two

A positive power of two has exactly one set bit:

```text
1 = 0001
2 = 0010
4 = 0100
8 = 1000
```

Clearing that one set bit leaves zero.

```cpp
bool isPowerOfTwo(Bits x) {
    return x != 0 && (x & (x - 1ULL)) == 0;
}
```

The zero check is essential. The expression `x & (x - 1)` alone is also zero when `x` is zero, but zero is not a power of two.

### Isolate the Rightmost Set Bit

A related operation keeps just the rightmost set bit:

```cpp
Bits lowestSetBitValue(Bits x) {
    return x & (0ULL - x);
}
```

`0ULL - x` is unsigned modular negation, producing the two's-complement pattern. It avoids negating a potentially minimum signed integer.

For illustration, retain eight bits:

```text
x              = 01010100   = 84
~x             = 10101011
~x + 1         = 10101100
x & (~x + 1)   = 00000100   = 4
```

Complementing turns the trailing zeros into ones. Adding one turns them back into zeros and sets the position of the original rightmost `1`. Higher bits remain complementary, so their AND is zero.

The result is the bit's **value**, `4`, not its index, `2`. For zero, the function returns zero. This operation is often called `lowbit` and later appears in Fenwick trees.

## 8. Count the Set Bits

The number of ones in a bit pattern is its **population count** or **popcount**.

For `84 = 1010100`, the set positions are 6, 4, and 2, so the count is `3`.

### Approach 1: Inspect Bits from Right to Left

Read the LSB using `x & 1`, then shift right to examine the next position.

```cpp
int countSetBitsByShift(Bits x) {
    int count = 0;
    while (x != 0) {
        count += static_cast<int>(x & 1ULL);
        x >>= 1;
    }
    return count;
}
```

For positive `x`, this takes one iteration per position in its binary representation: `O(log x)` time, or `O(W)` in the worst case. For zero, the loop takes no iterations and returns zero. Auxiliary space is `O(1)`.

Unsigned right shift fills with zeros, so the loop reaches zero. A similar loop over a negative signed value may not terminate on systems that preserve the sign bit during right shift.

### Approach 2: Clear One Set Bit per Iteration

Brian Kernighan's algorithm repeatedly applies `x &= x - 1`:

```cpp
int countSetBits(Bits x) {
    int count = 0;
    while (x != 0) {
        x &= x - 1ULL;
        ++count;
    }
    return count;
}
```

### Dry Run for `84`

| Iteration | Value before clearing | Value afterward | Count so far |
| --- | --- | --- | --- |
| 1 | `1010100` = 84 | `1010000` = 80 | 1 |
| 2 | `1010000` = 80 | `1000000` = 64 | 2 |
| 3 | `1000000` = 64 | `0000000` = 0 | 3 |

Each iteration removes exactly one set bit, so the number of iterations equals the original number of ones. If that number is `k`, the algorithm takes **`O(k)` time** for positive inputs and **`O(1)` auxiliary space**; zero takes constant time without entering the loop.

**Interview insight:** Explain the borrowing effect of `x - 1` before presenting this loop. That gives both its correctness and its iteration count, rather than relying on a memorized formula.

## 9. Flip Every Bit in an Inclusive Range

“Flip” and “reverse” can mean different things in a problem statement. **Flipping** changes bit values at their existing positions; **reversing** changes their order. We will implement both.

First, build a mask containing ones at positions `a` through `b`, inclusive, with `0 <= a <= b < W`.

For a range of length `len`, `(1ULL << len) - 1` creates `len` low ones. However, `len = W` needs separate handling because shifting by `W` is invalid.

```cpp
Bits rangeMask(int a, int b) {
    if (a < 0 || a > b || b >= W) {
        throw out_of_range("Invalid inclusive bit range");
    }

    int len = b - a + 1;
    Bits lowOnes = (len == W) ? ~0ULL : ((1ULL << len) - 1ULL);
    return lowOnes << a;
}

Bits flipRange(Bits x, int a, int b) {
    return x ^ rangeMask(a, b);
}
```

Only the selected branch of `?:` is evaluated, so the `len == W` case does not execute `1ULL << W`. A valid full-width range necessarily starts at `a = 0`.

### Example: Flip Positions 1 Through 3 of `84`

```text
x        = 1010100   = 84
mask     = 0001110   = 14
           -------
x ^ mask = 1011010   = 90
```

The same mask also supports `x | mask` to set the range and `x & ~mask` to clear it. Each operation takes `O(1)` time for a machine-word integer.

## 10. Reverse the Bits from Position `a` to Position `b`

Here, **reverse** means reversing the order of the bits in the inclusive range `[a, b]`. Bits outside the range remain unchanged.

For example, reversing the sequence `1100` gives `0011`. Reversing `101` leaves it unchanged, while flipping `101` gives `010`.

### Example: Reverse Positions 1 Through 4 of `22`

Write `22` in eight bits and mark the selected positions:

```text
Position:  7 6 5 | 4 3 2 1 | 0
Before:    0 0 0 | 1 0 1 1 | 0   = 22
After:     0 0 0 | 1 1 0 1 | 0   = 26
```

Reading the selected range from high to low, `1011` becomes `1101`.

We can reverse it with two indices:

1. Compare the bits at `a` and `b`.
2. If they differ, flip both. This exchanges `0` and `1`.
3. If they match, leave them unchanged.
4. Move `a` rightward in index order and `b` leftward: increment `a`, decrement `b`.
5. Stop when the indices meet or cross.

### C++ Implementation

```cpp
Bits reverseBitsInRange(Bits x, int a, int b) {
    if (a < 0 || a > b || b >= W) {
        throw out_of_range("Invalid inclusive bit range");
    }

    while (a < b) {
        Bits leftBit = (x >> a) & 1ULL;
        Bits rightBit = (x >> b) & 1ULL;

        if (leftBit != rightBit) {
            x ^= (1ULL << a) | (1ULL << b);
        }

        ++a;
        --b;
    }
    return x;
}
```

The two masks identify distinct positions because `a < b`. OR combines those positions, and XOR flips both bits when they differ.

### Dry Run

| Compared positions | Values before the step | Action | Number afterward |
| --- | --- | --- | --- |
| 1 and 4 | `1` and `1` | No change | `00010110` = 22 |
| 2 and 3 | `1` and `0` | Flip both positions | `00011010` = 26 |

The indices then cross, so the function returns `26`.

### Why Does This Work?

At every step, the two outermost unfinished positions receive their correct reversed values. The next step works strictly inside them, so completed pairs never change again. If the range has odd length, its middle bit stays in place.

Only positions inside `[a, b]` appear in the masks; therefore, bits outside the range remain unchanged.

For `L = b - a + 1`, the function processes `floor(L / 2)` pairs. It uses **`O(L)` time** and **`O(1)` auxiliary space**. Reversing twice restores the original value, and reversal preserves the number of set bits.

### Reversing a Whole Representation

The width must be specified:

```text
Reverse 1101 within 4 bits:      1101 -> 1011     = 11
Reverse 00001101 within 8 bits:  00001101 -> 10110000 = 176
```

Use `reverseBitsInRange(x, 0, 7)` to reverse the low eight bits, or `reverseBitsInRange(x, 0, W - 1)` to reverse the entire unsigned word. Leading zeros participate in the reversal.

## 11. Putting the Functions Together

Combine the shared headers and declarations with all function definitions above, then append this `main` to form a complete program:

```cpp
int main() {
    cout << "Set bit 2 of 17: " << setBit(17, 2) << '\n';
    cout << "Unset bit 3 of 92: " << unsetBit(92, 3) << '\n';
    cout << boolalpha;
    cout << "Check bit 4 of 84: " << checkBit(84, 4) << '\n';
    cout << "Flip bit 1 of 84: " << flipBit(84, 1) << '\n';
    cout << "Count by shifting: " << countSetBitsByShift(84) << '\n';
    cout << "Count by clearing: " << countSetBits(84) << '\n';
    cout << "Clear rightmost set bit: " << clearRightmostSetBit(84) << '\n';
    cout << "Rightmost set bit value: " << lowestSetBitValue(84) << '\n';
    cout << "Is 64 a power of two? " << isPowerOfTwo(64) << '\n';
    cout << "Is 0 a power of two? " << isPowerOfTwo(0) << '\n';
    cout << "Flip range [1, 3] of 84: " << flipRange(84, 1, 3) << '\n';

    Bits reversed = reverseBitsInRange(22, 1, 4);
    cout << "Reverse range [1, 4] of 22: " << reversed << '\n';
    cout << "Result in eight bits: " << bitset<8>(reversed) << '\n';
}
```

Output:

```text
Set bit 2 of 17: 21
Unset bit 3 of 92: 84
Check bit 4 of 84: true
Flip bit 1 of 84: 86
Count by shifting: 3
Count by clearing: 3
Clear rightmost set bit: 80
Rightmost set bit value: 4
Is 64 a power of two? true
Is 0 a power of two? false
Flip range [1, 3] of 84: 90
Reverse range [1, 4] of 22: 26
Result in eight bits: 00011010
```

`bitset<8>` displays the low eight bits, including leading zeros. It does not change the width of `Bits` or the calculations performed by our functions.

## 12. Edge Cases and Common Mistakes

| Case | Expected behavior |
| --- | --- |
| Set an already set bit | Value unchanged |
| Unset an already clear bit | Value unchanged |
| Flip a bit twice | Original value restored |
| Count set bits of zero | `0` |
| Clear or isolate the rightmost set bit of zero | `0` in our unsigned implementations |
| Test zero for power of two | `false` |
| Operate on bit `W - 1` | Valid with `1ULL` and our chosen type |
| Reverse a one-position range | Value unchanged |
| Reverse a range of all zeros or all ones | Value unchanged |
| Reverse a range twice | Original value restored |
| Flip the full range `[0, W - 1]` | Every bit toggled; no shift by `W` |
| Index outside `[0, W - 1]` or invalid range | Our helpers throw `out_of_range` |

### Parenthesize Bit Checks

Write `(x & mask) != 0`, not `x & mask != 0`. The latter is parsed as `x & (mask != 0)`, which usually checks bit 0 instead of the intended position.

Similarly, write `(x & (x - 1ULL)) == 0` with parentheses around the AND expression.

### Match the Mask Type to the Value

For our `unsigned long long` values, use `1ULL`, not plain `1`. A wider destination variable does not make the expression that produces its value wider. Check the shift count before evaluating the shift.

### Distinguish Values, Indices, and Counts

For `84 = 1010100`:

- The rightmost set bit's **index** is `2`.
- Its **value** is `4`.
- The total **number of set bits** is `3`.

These are three different answers to three different questions. In interviews, establish which one the problem requires.

## 13. Short Practice Checks

Try each result before reading the answers.

1. What happens when bit 2 of `21 = 10101` is set again?
2. What is `40 & (40 - 1)`?
3. Is `48` a power of two?
4. What is the value of the rightmost set bit of `40`?
5. What is the result of reversing `13` within its low four bits? Within its low eight bits?
6. What is the difference between flipping and reversing the three-bit pattern `101`?

### Answers

1. `21`; bit 2 was already set.
2. `101000 & 100111 = 100000`, or `32`.
3. No. `48 = 110000` has two set bits; clearing the rightmost leaves `32`.
4. `8`, corresponding to position 3.
5. Four bits: `1101 -> 1011`, or `11`. Eight bits: `00001101 -> 10110000`, or `176`.
6. Flipping gives `010`; reversing gives `101`.

## Quick Recap

- A single-bit mask is `1ULL << i` for a valid index of our unsigned type.
- OR sets a bit, AND with a complemented mask clears it, AND checks it, and XOR flips it.
- For positive `x`, subtracting one clears the rightmost set bit and changes every lower zero into one.
- `x & (x - 1)` clears one set bit; repeated application counts the set bits.
- `x != 0 && (x & (x - 1)) == 0` checks whether an unsigned number is a power of two.
- `x & (0ULL - x)` isolates the rightmost set bit's value for our unsigned type.
- A range mask lets us set, clear, or flip several positions together.
- Reversing a range swaps symmetric bit positions; it does not complement the selected bits.
- Width, signedness, and zero-based indexing are part of the problem definition, not incidental details.

</READING_WIDGET>
