<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Bitset in STL

In the previous lesson, we used the bits of an integer to represent a subset. Each bit answered a simple question: is this item included or not?

**`std::bitset<N>` stores a fixed-size sequence of `N` bits**, where each bit is either `0` or `1`. It provides named operations to set, reset, flip, and test bits, along with operators to combine entire bit patterns.

Unlike a built-in integer mask, a bitset can contain more bits than fit in one integer. For example, `bitset<1000>` represents 1,000 binary flags in one object.

All code in this lesson uses **C++17**. Include `<bitset>` to use `std::bitset`; the snippets below use `using namespace std;` for readability.

## 1. Why Use a Bitset?

A bitset is useful when we know the number of binary flags in advance and want to store and process them together.

- **Compact storage:** Implementations typically pack bits into machine words, saving memory compared with storing every flag as a separate `bool`.
- **Convenient operations:** `set(i)`, `reset(i)`, and `test(i)` express common actions directly.
- **Operations on many flags:** AND, OR, XOR, and shifts process entire bit patterns. This is useful for representing sets, tracking availability, and comparing selections.

For example, if bit `i` represents whether item `i` is available, `1` means available and `0` means unavailable. The interpretation comes from the problem; the bitset only stores the flags.

The actual object size depends on the implementation and may include unused storage bits. Do not assume that `sizeof(bitset<N>)` is exactly `N / 8` bytes.

## 2. Construction and Bit Positions

```cpp
#include <bitset>
#include <iostream>
#include <string>
using namespace std;

bitset<8> empty;                // 00000000
bitset<8> fromNumber(42);       // 00101010
bitset<8> fromBinary(0b101010); // 00101010
bitset<8> fromString("1101");  // 00001101
```

The default constructor initializes every bit to zero. Integer and string initialization fill the available positions, with leading zeros when needed. Binary integer literals such as `0b101010` require **C++14 or later**; decimal initialization does not require that syntax.

### Indexing Starts from the Right

For `bitset<8> bits("10101010")`:

```text
Bit position:  7  6  5  4  3  2  1  0
Bit value:     1  0  1  0  1  0  1  0
```

Bit `0` is the **least significant bit**, shown on the right. Printing the bitset displays bit `N - 1` on the left and bit `0` on the right.

Therefore, `bits[0]` is `0`, while `bits[7]` is `1`. A string's first character is on the left, so string indexing and bitset indexing run in opposite directions for this representation.

### The Size Must Be Known at Compile Time

```cpp
constexpr int N = 1000;
bitset<N> flags; // Valid: N is a compile-time constant.
```

You cannot read `n` from input and then declare `bitset<n>`. A bitset also has no `push_back()` or `resize()` operation. If a problem gives a fixed maximum, you can use that maximum as the capacity; otherwise, consider a runtime-sized representation such as `vector<bool>`.

## 3. Setting, Resetting, Testing, and Flipping Bits

Start with an empty eight-bit bitset. The following operations happen **in sequence**:

```cpp
bitset<8> bits;

bits.set(2);       // 00000100: make bit 2 equal to 1
bits.set(5);       // 00100100: make bit 5 equal to 1
bits.reset(2);     // 00100000: make bit 2 equal to 0
bits.flip(1);      // 00100010: toggle bit 1
bits.set(5, false);// 00000010: another way to clear bit 5

bool first = bits.test(1); // true
bool second = bits[3];    // false
bits[3] = true;           // 00001010
```

**Setting is not toggling.** Setting a bit that is already `1` leaves it unchanged. Flipping changes `0` to `1` or `1` to `0`.

The versions without a position affect every bit:

```cpp
bits.set();   // 11111111: set every bit
bits.reset(); // 00000000: clear every bit
bits.flip();  // 11111111: toggle every bit
```

### Checked Access and `operator[]`

For `bitset<N>`, valid positions are `0` through `N - 1`.

- `test(pos)`, `set(pos)`, `reset(pos)`, and `flip(pos)` throw `std::out_of_range` for an invalid position.
- `bits[pos]` provides no bounds-checking guarantee in C++17. An invalid index causes undefined behavior.

For a modifiable bitset, `bits[pos]` returns a small **proxy object** that acts like a reference to a bit. It supports assignment, but it is not an ordinary `bool&`. Use `bool value = bits[pos];` when you want to copy the current value.

## 4. Querying the Bitset

Consider `bitset<8> bits("10111110")`:

| Expression | Meaning | Result |
| --- | --- | --- |
| `bits.any()` | Is at least one bit set? | `true` |
| `bits.none()` | Are all bits zero? | `false` |
| `bits.all()` | Are all bits one? | `false` |
| `bits.count()` | How many bits are set? | `6` |
| `bits.size()` | How many bit positions exist? | `8` |

**`count()` measures the number of ones; `size()` gives the fixed capacity.** Both return `size_t`.

If each bit represents membership in a set, `count()` gives the number of selected items, while `none()` tells us whether the represented set is empty.

## 5. Bitwise Operations and Shifts

Bitsets of the **same size** can be combined using the familiar bitwise operators.

```cpp
bitset<8> a("10101010");
bitset<8> b("11001010");

cout << (a & b) << '\n';  // 10001010
cout << (a | b) << '\n';  // 11101010
cout << (a ^ b) << '\n';  // 01100000
cout << (~a) << '\n';     // 01010101
cout << (a & ~b) << '\n'; // 00100000
```

These expressions produce new bitsets and leave `a` and `b` unchanged. To update `a`, use assignment forms such as `a &= b`, `a |= b`, or `a ^= b`. The expression `a &= ~b` removes every bit that is set in `b`.

When bits represent set membership:

| Expression | Set interpretation |
| --- | --- |
| `a & b` | Intersection: items in both sets |
| `a \| b` | Union: items in either set |
| `a ^ b` | Items in exactly one set |
| `a & ~b` | Items in `a` but not in `b` |
| `~a` | Complement within the bitset's `N` positions |

Unlike complementing an integer mask for a smaller universe, `~a` already stays within the bitset's declared width. If only some positions represent actual items, however, you must still ignore or clear the unused positions.

### Left and Right Shifts

```cpp
bitset<8> bits("00101101");

cout << (bits << 2) << '\n'; // 10110100
cout << (bits >> 2) << '\n'; // 00001011
cout << bits << '\n';        // 00101101: unchanged

bits <<= 2;                  // bits becomes 10110100
```

A left shift moves bits toward higher positions; a right shift moves them toward lower positions. Vacated positions become zero, and bits shifted beyond the fixed width are discarded. These are **shifts, not rotations**.

For a bitset, shifting by `N` or more produces all zeros. This differs from built-in integer shifts, where a shift count at least as large as the promoted left operand's width is invalid. See the [C++ bitset shift specification](https://eel.is/c++draft/bitset.members#7).

## 6. Converting to Strings and Integers

```cpp
bitset<8> bits("10111110");

string text = bits.to_string();              // "10111110"
unsigned long value = bits.to_ulong();       // 190
unsigned long long wide = bits.to_ullong();  // 190
```

`to_string()` returns exactly `N` characters, including leading zeros. You can also print a bitset directly using `cout << bits`.

### Overflow Depends on the Value

**`to_ulong()` throws `std::overflow_error` only if the represented value cannot fit in `unsigned long`.** A bitset wider than the integer type can still convert successfully when its higher bits are zero. `to_ullong()` follows the same rule for `unsigned long long`; it is not guaranteed to be wider than `unsigned long` on every platform. See the [C++ integer conversion specification](https://eel.is/c++draft/bitset.members#38).

```cpp
bitset<1000> smallValue(5);
cout << smallValue.to_ulong() << '\n'; // 5: the value fits
```

For a large pattern that does not fit either integer type, keep using bitset operations or obtain its binary string.

### Construction Can Discard Input Bits

Integer construction keeps the lowest `N` bits when the integer contains more than `N` bits. String construction uses the first `N` characters when the supplied string is longer than the bitset.

```cpp
bitset<4> fromInteger(0b110101); // 0101: lowest four integer bits
bitset<4> fromText("110101");   // 1101: first four string characters
```

With the default character mapping, a string containing characters other than `'0'` and `'1'` causes `std::invalid_argument`.

## 7. Complete Example and Dry Run

We begin with `10101010`, set bit `2`, and then flip bit `4`.

| Step | Operation | Bitset |
| --- | --- | --- |
| Initial state | Construct from `0b10101010` | `10101010` |
| Set bit `2` | `bits.set(2)` | `10101110` |
| Toggle bit `4` | `bits.flip(4)` | `10111110` |

Bit `4` was zero, so flipping it makes it one. Bit `5` was already one; flipping bit `5` instead would produce `10001110`.

```cpp
#include <bitset>
#include <iostream>
#include <string>
using namespace std;

int main() {
    bitset<8> bits(0b10101010);

    bits.set(2);
    bits.flip(4);

    cout << "Bitset: " << bits << '\n';
    cout << "Bit at pos 3: " << bits.test(3) << '\n';
    cout << "Any set? " << bits.any() << '\n';
    cout << "All set? " << bits.all() << '\n';
    cout << "None set? " << bits.none() << '\n';
    cout << "Count set: " << bits.count() << '\n';
    cout << "Size: " << bits.size() << '\n';

    unsigned long value = bits.to_ulong();
    string text = bits.to_string();
    cout << "As ulong: " << value << '\n';
    cout << "As string: " << text << '\n';

    return 0;
}
```

Output:

```text
Bitset: 10111110
Bit at pos 3: 1
Any set? 1
All set? 0
None set? 0
Count set: 6
Size: 8
As ulong: 190
As string: 10111110
```

The integer value is `128 + 32 + 16 + 8 + 4 + 2 = 190`. Without `boolalpha`, `cout` prints Boolean results as `1` and `0`.

## 8. Useful CP and Interview Insights

### Count Common or Different Elements

Suppose two people select items from a universe numbered `0` through `7`. Store their selections in two bitsets:

```cpp
bitset<8> alice;
bitset<8> bob;

alice.set(1).set(3).set(5); // {1, 3, 5}
bob.set(3).set(4).set(5);   // {3, 4, 5}

cout << (alice & bob).count() << '\n'; // 2: common items {3, 5}
cout << (alice ^ bob).count() << '\n'; // 2: different items {1, 4}
cout << (alice & bob).any() << '\n';   // 1: at least one common item
```

`set()` returns a reference to the bitset, which allows chained calls. The expression `(a ^ b).count()` also gives the **Hamming distance** between two bit patterns: the number of positions where they differ.

### Do Not Treat Every Operation as Constant Time

A bitset can span many machine words. Under the usual packed implementation model, let `W` be the number of bits processed per word, often 64:

| Operation | Typical cost |
| --- | --- |
| Access or modify one bit; `size()` | `O(1)` |
| Whole-bitset AND, OR, XOR, flip, or shift | `O(ceil(N / W))` |
| `count()`, `any()`, `none()`, `all()` | `O(ceil(N / W))` worst case |
| Produce a string of all bits | `O(N)` |

These are **practical estimates for common implementations**, not portable complexity guarantees from the bitset interface. Some queries can stop early. Processing a word at a time can be much faster than checking every flag individually, but it does not make arbitrarily large bitsets constant-time.

### Choose the Representation to Match the Problem

- Use an **unsigned integer mask** when the flags fit in one integer and arithmetic or numeric mask enumeration is useful.
- Use **`bitset<N>`** for a fixed number of flags and frequent operations on entire bit patterns.
- Use a **runtime-sized representation** when the required size is only known after reading input.

A bitset supports bitwise operations and equality comparisons, but it is not an arbitrary-precision integer: it does not provide arithmetic operators such as `+` or `++`. It also has no standard `begin()` and `end()` iterators; use an index loop to visit individual bits.

## Quick Recap

- `bitset<N>` stores `N` binary flags, with a size fixed at compile time.
- Bit `0` is the rightmost bit when printed.
- `set`, `reset`, `flip`, and `test` operate on individual positions; several also have whole-bitset forms.
- `count()` gives the number of ones, while `size()` gives the number of positions.
- Bitwise operators combine flags, and shifts discard bits beyond the fixed width.
- Integer conversion succeeds when the value fits, even if the bitset itself is wider.
- Combining bitwise operations with `count()` is useful for common-element counts and Hamming distance.

</READING_WIDGET>
