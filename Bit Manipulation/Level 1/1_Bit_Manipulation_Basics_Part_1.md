<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bit Manipulation Basics — Part 1

An integer such as `11` is convenient for us to read in decimal. Inside a computer, its value is represented using bits. Once we understand what each bit means, we can work directly with individual positions instead of treating the number as one indivisible value.

**Bit manipulation** means inspecting or changing these binary digits using operations such as AND, OR, XOR, NOT, and shifts. These operations help us represent flags, work with subsets, and recognize useful patterns in integers.

We will first understand binary representation, then follow the lecture board's operator overview: `^`, `|`, `&`, `>>`, `<<`, and `~`. We will also separate them from logical operators and arithmetic negation, and explain how complements make signed representation and subtraction work.

The code uses **C++17**. Signed-number illustrations use **two's complement**, the representation used on mainstream programming-contest systems. We will explicitly state the width of short binary examples; a four-bit drawing is not a four-bit C++ `int`.

## 1. What Is a Bit?

A **bit**, short for binary digit, can hold either `0` or `1`. A bit containing `1` is called **set**; a bit containing `0` is called **unset** or **clear**.

Decimal uses powers of ten. Binary uses powers of two. Number bit positions from the right, starting at **0**:

| Position | 3 | 2 | 1 | 0 |
| --- | --- | --- | --- | --- |
| Place value | `2^3 = 8` | `2^2 = 4` | `2^1 = 2` | `2^0 = 1` |
| Bit in `1011` | 1 | 0 | 1 | 1 |
| Contribution | 8 | 0 | 2 | 1 |

Therefore:

```text
(1011)₂ = 1 × 8 + 0 × 4 + 1 × 2 + 1 × 1 = 11
```

For a non-negative integer with bits `b₀, b₁, ...`, its value is the sum of `bᵢ × 2^i`. Leading zeros do not change that value: `1011`, `00001011`, and `0000000000001011` all represent unsigned `11`.

### Converting Decimal to Binary

Repeatedly divide by 2 and collect the remainders:

| Current value | Quotient | Remainder |
| --- | --- | --- |
| 11 | 5 | 1 |
| 5 | 2 | 1 |
| 2 | 1 | 0 |
| 1 | 0 | 1 |

Read the remainders **from bottom to top** to get `1011`. The binary representation of zero is `0`.

In C++, write binary integer literals with the `0b` prefix: `0b1011` has decimal value `11`. Writing `1011` alone means the decimal number one thousand eleven.

## 2. LSB, MSB, and the Rightmost Set Bit

For an eight-bit representation of `84`:

```text
Position:  7 6 5 4 3 2 1 0
Bits:      0 1 0 1 0 1 0 0
```

- The **least significant bit (LSB)** is bit 0, the rightmost position. Its value here is `0`.
- The **most significant bit (MSB)** of this fixed-width representation is bit 7, the leftmost position. Its value here is `0`.
- The **least significant set bit**, also called the **rightmost set bit**, is at position 2. Its place value is `2^2 = 4`.
- The **highest set bit** is at position 6. Its place value is `2^6 = 64`.

The distinction matters: **the LSB and the least significant set bit are not necessarily the same bit**. Some discussions use “MSB” to mean the highest set bit of a positive number; clarify which meaning is intended.

Zero has an LSB position in a fixed-width representation, but it has **no set bit**.

Because every power of two except `2^0` is even, the LSB tells us parity: a non-negative integer is odd exactly when bit 0 is `1`.

## 3. Bitwise AND, OR, and XOR

Bitwise operators apply their rule **independently at every corresponding bit position**. Align the operands and add leading zeros when necessary.

### Truth Table

| A | B | `A & B` — AND | `A \| B` — OR | `A ^ B` — XOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

### AND (`&`): Both Bits Must Be Set

```text
    1010   = 10
  & 1100   = 12
  ------
    1000   = 8
```

Only position 3 is set in both operands. AND is useful for selecting or checking particular bits.

### OR (`|`): At Least One Bit Must Be Set

```text
    1010   = 10
  | 1100   = 12
  ------
    1110   = 14
```

OR combines the set positions of both operands. It is useful when we want to turn selected bits on.

### XOR (`^`): The Bits Must Be Different

```text
    1010   = 10
  ^ 1100   = 12
  ------
    0110   = 6
```

The lecture's `5 ^ 6` example uses the same rule:

```text
    101   = 5
  ^ 110   = 6
  -----
    011   = 3
```

At the leftmost position, `1 ^ 1 = 0`. At the other two positions, the bits differ, so both results are `1`.

**XOR is not exponentiation in C++.** The expression `5 ^ 6` produces `3`, not five raised to the sixth power. XOR also does not carry between positions: `1 ^ 1 = 0`, while binary addition gives `1 + 1 = 10`.

### Useful Identities

| AND | OR | XOR |
| --- | --- | --- |
| `x & 0 = 0` | `x \| 0 = x` | `x ^ 0 = x` |
| `x & x = x` | `x \| x = x` | `x ^ x = 0` |

AND, OR, and XOR are each commutative and associative. For example, `(a ^ b) ^ c = a ^ (b ^ c)`.

**Interview insight:** If every value appears exactly twice except one value that appears once, XORing all values leaves the single value. Equal pairs cancel because `x ^ x = 0`. The assumption about frequencies is essential.

## 4. NOT, NOR, NAND, and XNOR

### NOT (`~`): Flip Every Bit

Bitwise NOT changes `0` to `1` and `1` to `0`.

| A | NOT A |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

In a **four-bit model**:

```text
 A = 1010   = 10
~A = 0101   = 5, when only four bits are retained
```

The width is part of this result. In an eight-bit unsigned model, complementing `00001010` gives `11110101`, or `245`.

C++ `~` operates on the promoted operand's full width. On a two's-complement system, `~10` with type `int` is `-11`; it is not `5`. To retain just four result bits, use a mask:

```cpp
unsigned int a = 0b1010U;
unsigned int flippedLowFour = (~a) & 0b1111U; // 5
```

Here, AND with `1111` keeps positions 0 through 3 and clears higher positions. Small integer types such as `unsigned char` usually promote to `int` before `~`, so their storage size does not automatically limit the operation. See the [C++ unary-operator rules](https://eel.is/c++draft/expr.unary.op).

### Combining NOT with Other Operations

NOR means NOT OR, NAND means NOT AND, and XNOR means NOT XOR. C++ has no dedicated symbolic operator for these combinations.

| A | B | NOR | NAND | XNOR |
| --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |

Using `A = 1010` and `B = 1100`, and retaining four bits:

| Operation | C++ expression with a four-bit mask | Binary result | Decimal |
| --- | --- | --- | --- |
| NOR | `~(A \| B) & 0b1111U` | `0001` | 1 |
| NAND | `~(A & B) & 0b1111U` | `0111` | 7 |
| XNOR | `~(A ^ B) & 0b1111U` | `1001` | 9 |

XNOR marks positions where the two bits are equal. The mask is necessary when the intended result contains only four bits.

## 5. Bitwise Operators Versus Logical Operators

The board separates `&`, `|`, and `~` from `&&`, `||`, and `!`. These groups answer different questions.

| Purpose | Operators | What they examine | Result |
| --- | --- | --- | --- |
| Bitwise operations | `&`, `\|`, `^`, `~` | Individual bits | An integer bit pattern |
| Logical operations | `&&`, `\|\|`, `!` | Truth of whole operands | `bool`: `true` or `false` |

For conversion to `bool`, zero is false and every nonzero integer is true, including a negative integer.

```text
5 & 2    = 0       because 101 & 010 = 000
5 && 2   = true    because both numbers are nonzero

5 | 2    = 7       because 101 | 010 = 111
5 || 2   = true    because at least one operand is nonzero

!5       = false
!0       = true
```

Built-in logical operators **short-circuit**: `&&` skips the right operand when the left is false; `||` skips it when the left is true. Bitwise `&` and `|` do not provide this behavior. For example, `d != 0 && n / d > 2` safely skips the division when `d` is zero. These guarantees are specified in the [logical AND](https://eel.is/c++draft/expr.log.and) and [logical OR](https://eel.is/c++draft/expr.log.or) rules.

For Boolean values, `a != b` expresses logical XOR. Logical NOR can be written as `!(a || b)`.

## 6. Signed and Unsigned Integer Representation

Before interpreting a bit pattern, establish its **width** and whether it is **signed or unsigned**.

### Unsigned Integers

An unsigned integer with `W` value bits represents:

$$
0 \text{ through } 2^W - 1.
$$

All positions have positive weights. An eight-bit unsigned integer ranges from `0` to `255`; `11111111` means `255`.

Unsigned arithmetic wraps modulo `2^W`. In an eight-bit unsigned model, `255 + 1` becomes `0` and `0 - 1` becomes `255`. This is a property of arithmetic in the unsigned type; expressions involving narrow types may first be promoted.

### Signed Integers in Two's Complement

A `W`-bit two's-complement integer represents:

$$
-2^{W-1} \text{ through } 2^{W-1} - 1.
$$

The top bit has weight **`-2^(W-1)`**; all lower bits retain their positive weights. For eight bits:

```text
11111110 = -128 + 64 + 32 + 16 + 8 + 4 + 2 = -2
```

The top bit is the sign bit: `0` indicates a non-negative value and `1` indicates a negative value. It is not a separate minus sign followed by the magnitude.

| Eight-bit pattern | Unsigned interpretation | Signed two's-complement interpretation |
| --- | --- | --- |
| `00001010` | 10 | 10 |
| `01111111` | 127 | 127 |
| `10000000` | 128 | -128 |
| `11111110` | 254 | -2 |
| `11111111` | 255 | -1 |

### Common C++ Integer Types

The following are common platform sizes, not universal guarantees. Ranges shown assume two's complement and the stated width.

| Signed / unsigned type | Common width | Signed range | Unsigned range |
| --- | --- | --- | --- |
| `signed char` / `unsigned char` | 8 | `-128` to `127` | `0` to `255` |
| `short` / `unsigned short` | 16 | `-2^15` to `2^15 - 1` | `0` to `2^16 - 1` |
| `int` / `unsigned int` | 32 | `-2^31` to `2^31 - 1` | `0` to `2^32 - 1` |
| `long` / `unsigned long` | 32 or 64 | Depends on width | Depends on width |
| `long long` / `unsigned long long` | 64 | `-2^63` to `2^63 - 1` | `0` to `2^64 - 1` |

C++ guarantees minimum widths of 8, 16, 16, 32, and 64 bits respectively. Plain `char` has implementation-defined signedness. Two's complement is required since C++20; C++17 also permitted other signed representations. See the [current fundamental-type rules](https://eel.is/c++draft/basic.fundamental) and the [C++17 draft](https://timsong-cpp.github.io/cppwp/n4659/basic.fundamental).

Use `<limits>` to inspect actual value ranges and value-bit counts:

```cpp
#include <climits>
#include <iostream>
#include <limits>
using namespace std;

int main() {
    cout << "int storage bits: " << sizeof(int) * CHAR_BIT << '\n';
    cout << "int minimum: " << numeric_limits<int>::min() << '\n';
    cout << "int maximum: " << numeric_limits<int>::max() << '\n';
    cout << "unsigned long long value bits: "
         << numeric_limits<unsigned long long>::digits << '\n';
}
```

`sizeof` counts bytes; `CHAR_BIT` gives bits per byte. For signed integers, `numeric_limits<T>::digits` excludes the sign bit. `<cstdint>` also provides exact-width types such as `std::uint32_t` and `std::uint64_t` when supported by the implementation.

For bit masks, an unsigned type is usually the simplest choice. Ordinary signed arithmetic overflow is undefined behavior; do not assume that incrementing the largest signed integer wraps to the smallest. [C++ fundamental-type rules](https://eel.is/c++draft/basic.fundamental)

## 7. One's Complement and Two's Complement

Both operations require a chosen width. Let us use **eight bits** and start with positive `5`:

```text
Original:          00000101
One's complement:  11111010   flip every bit
Two's complement:  11111011   flip every bit, then add 1
```

### One's Complement

The one's complement of a bit pattern is obtained by inverting every bit. For an unsigned `W`-bit value `x`, its complemented pattern has value `(2^W - 1) - x`.

There was also a signed representation called **one's-complement representation**, in which the complement of positive `5` represented `-5`. It had two encodings of zero: all zeros and all ones. Do not confuse that historical representation with the complement operation we can apply to any bit pattern.

### Two's Complement

Add `1` to the one's complement, retaining the chosen width. In eight-bit two's-complement representation, `11111011` means `-5`:

```text
    00000101   = +5
  + 11111011   = -5
  ----------
  1 00000000
```

Discarding the carry beyond eight bits leaves zero. The same process maps zero back to zero; two's complement has only one zero representation.

For a nonzero unsigned value `x`, the two's-complement pattern has unsigned value `2^W - x`. For zero, it is zero after reduction modulo `2^W`.

### Three Different Meanings of Negation

| Expression | Meaning | Example for signed `x = 5` on a two's-complement system |
| --- | --- | --- |
| `!x` | Logical NOT | `false` |
| `~x` | Bitwise complement | `-6` |
| `-x` | Arithmetic negation | `-5` |

The bit-pattern identity behind arithmetic negation is “complement, then add one.” On a two's-complement system, `~x = -x - 1` mathematically. However, evaluating `-x` or `~x + 1` as signed C++ arithmetic requires the intermediate results to be representable. In particular, the minimum signed value has no representable positive counterpart. Use `-x` for ordinary arithmetic and unsigned values for modular bit-pattern calculations.

## 8. Binary Subtraction Using Two's Complement

Subtraction can be expressed as addition:

$$
A - B = A + (-B).
$$

In a fixed-width two's-complement model, obtain the pattern for `-B` by complementing `B` and adding one.

### Example: `10 - 12 = -2`

Use eight bits so that both positive operands fit in the signed range:

```text
A       = 00001010   = 10
B       = 00001100   = 12
~B      = 11110011
~B + 1  = 11110100   = -12 when interpreted as signed

          00001010
        + 11110100
        ----------
          11111110   = -2 when interpreted as signed
```

We can verify the answer using the sign-bit weight: `-128 + 126 = -2`.

In a **four-bit modular calculation**, the low four result bits would be `1110`. This pattern is unsigned `14` or signed two's-complement `-2`. But positive `10` and `12` do not fit in the four-bit signed range `[-8, 7]`, so that four-bit calculation must not be presented as signed arithmetic on positive `10` and `12`.

### Example: `12 - 10 = 2`

```text
12                 =   00001100
Two's complement
of 10              =   11110110
                      --------
Sum                = 1 00000010
Retain eight bits  =   00000010 = 2
```

This explains the representation-level connection between addition and subtraction. In normal C++ code, write `A - B`; the `-` operator is an **arithmetic operator**, not a bitwise operator.

## 9. Left Shift and Right Shift

### Left Shift (`<<`)

Left shifting by `k` moves bits `k` positions toward the more significant end. New low positions receive zeros.

```text
A      = 00001010   = 10
A << 1 = 00010100   = 20
A << 2 = 00101000   = 40
```

When the result fits, shifting a non-negative value left by `k` multiplies it by `2^k`. In an unsigned `W`-bit type, bits shifted beyond the width are discarded, so the result is multiplication modulo `2^W`.

For example, in an eight-bit model, `11000000 << 1` retains `10000000`: `192 × 2 = 384`, and `384 mod 256 = 128`. A drawing limited to eight bits does not make a C++ `unsigned int` eight bits wide.

### Right Shift (`>>`)

Right shifting moves bits toward the less significant end. Bits shifted past position 0 are lost.

```text
A      = 00001010   = 10
A >> 1 = 00000101   = 5
A >> 2 = 00000010   = 2
```

Unsigned right shift inserts zeros at the left. For non-negative values, shifting right by `k` computes `floor(A / 2^k)`. Shifts are not rotations: discarded bits do not reappear at the other end.

### Signed Shifts and Valid Shift Counts

In C++17, right shift of a negative signed integer is implementation-defined; left shift of a negative signed integer is undefined. Since C++20, signed right shift is arithmetic: it extends the sign and rounds division toward negative infinity. For example, `-5 >> 1` is `-3` under that rule, while `-5 / 2` is `-2` because integer division truncates toward zero. See the [C++17 shift rules](https://timsong-cpp.github.io/cppwp/n4659/expr.shift) and the [current shift rules](https://eel.is/c++draft/expr.shift).

For portable C++17 bit manipulation, prefer unsigned operands. A shift count must be non-negative and strictly less than the width of the **promoted left operand**. Shifting by the full width is undefined, even for zero. [C++17 shift rules](https://timsong-cpp.github.io/cppwp/n4659/expr.shift)

```cpp
unsigned long long mask = 1ULL << 40; // Valid: left operand has at least 64 bits.
```

`1ULL` is an `unsigned long long` literal. On a platform with 32-bit `int`, `1 << 40` is invalid; assigning that expression to a wider variable afterward does not fix the shift.

## 10. A Small C++ Operator Demonstration

This complete program uses unsigned operands and explicitly masks the four-bit complement examples.

```cpp
#include <iostream>
using namespace std;

int main() {
    unsigned int a = 10U;
    unsigned int b = 12U;
    unsigned int lowFour = 0b1111U;

    cout << "AND: " << (a & b) << '\n';
    cout << "OR: " << (a | b) << '\n';
    cout << "XOR: " << (a ^ b) << '\n';
    cout << "Lecture XOR: " << (5U ^ 6U) << '\n';
    cout << "NOT in four bits: " << ((~a) & lowFour) << '\n';
    cout << "NOR in four bits: " << (~(a | b) & lowFour) << '\n';
    cout << "NAND in four bits: " << (~(a & b) & lowFour) << '\n';
    cout << "XNOR in four bits: " << (~(a ^ b) & lowFour) << '\n';
    cout << "Left shift by 2: " << (a << 2) << '\n';
    cout << "Right shift by 1: " << (a >> 1) << '\n';

    int signedA = 10;
    int signedB = 12;
    cout << "Signed subtraction: " << (signedA - signedB) << '\n';
}
```

Output:

```text
AND: 8
OR: 14
XOR: 6
Lecture XOR: 3
NOT in four bits: 5
NOR in four bits: 1
NAND in four bits: 7
XNOR in four bits: 9
Left shift by 2: 40
Right shift by 1: 5
Signed subtraction: -2
```

## 11. Useful Insights and Common Mistakes

- **State the width before complementing or reversing bits.** Leading zeros can become ones under NOT and can move under reversal.
- **Separate the bit pattern from its interpretation.** `11111110` is unsigned `254` or signed eight-bit two's-complement `-2`.
- **Use `^` for XOR, not powers.** To build a single-bit mask, use an appropriate unsigned `1` shifted by the bit index.
- **Do not replace `&&` with `&`.** One checks truth and short-circuits; the other combines integer bits.
- **Avoid mixing signed and unsigned arithmetic casually.** Usual conversions can turn a negative signed operand into a large unsigned value.
- **Use parentheses around bitwise expressions in output and conditions.** For example, write `cout << (a ^ b)`.
- **Treat one machine-word operation as `O(1)`.** This model applies to fixed-width integer operations; arbitrary-length binary strings may require work proportional to their length.

## Quick Recap

- Bits are binary digits with powers-of-two place values; position 0 is the LSB.
- AND keeps common set bits, OR combines set bits, and XOR marks differing bits.
- NOT flips bits across the operation's width; NOR, NAND, and XNOR combine NOT with other operations.
- Logical operators work on truth values and are distinct from bitwise operators.
- Signed and unsigned types can interpret the same bit pattern differently.
- One's complement flips every bit; two's complement flips every bit and adds one within a fixed width.
- Subtraction can be understood as adding the two's complement of the subtrahend.
- Shifts move bits and discard those that leave the width; valid counts and operand types matter.

</READING_WIDGET>
