<VIDEO_WIDGET>

<VIDEO_ID>3507</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Why 10^9 + 7?

If you spend any time on LeetCode, Codeforces, or HackerRank, $10^9 + 7$ (or `1,000,000,007`) will quickly become the most recognizable number in your coding career.

Problem setters use this specific number universally. But why? Why not $10^9$? Why not $1,000,000$?

The answer lies in a perfect storm of mathematics, memory limits, and algorithm design. Here are the three foundational reasons $10^9 + 7$ is the undisputed king of competitive programming moduli.

---

## 1. It is a Prime Number (The Inverse Guarantee)

The number $1,000,000,007$ is a prime number. As we learned in the **Inverse of Modulo** module, division in modular arithmetic requires finding the _Modular Multiplicative Inverse_.

This inverse only mathematically exists if the divisor and the modulus are coprime ($\text{gcd}(a, m) = 1$). Because $10^9 + 7$ is prime, **every single positive integer strictly less than it is guaranteed to be coprime to it**.
This means you can safely use Fermat's Little Theorem to "divide" by any valid intermediate number without fear of the inverse failing!

### Reducing Collisions in Hashing

Beyond division, prime numbers are heavily used in hashing algorithms (like the Rolling Hash for strings). When you use a prime modulus, the mathematical distribution of remainders becomes much more uniform, drastically reducing the chances of accidental collisions (where two different strings maliciously or accidentally produce the same hash value).

---

## 2. Avoiding Integer Overflow

The maximum value of a standard signed 32-bit integer (`int`) in C++ and Java is $2,147,483,647$.

Because $1,000,000,007$ is strictly less than $2.14 \times 10^9$, any single value modulo $10^9 + 7$ will safely fit inside a standard 32-bit integer variable.

### The 64-bit Multiplication Magic

This is the most critical programmatic insight! When we multiply two modulo-reduced numbers in a program, we temporarily create a much larger intermediate number.

If we take two numbers that are slightly less than $10^9 + 7$ and multiply them, the maximum possible intermediate value before the modulo applies is:
$$(10^9 + 7) \times (10^9 + 7) \approx 10^{18}$$

Why is $10^{18}$ so important? Because the maximum capacity of a signed 64-bit integer (`long long`) is $\approx 9.22 \times 10^{18}$.
This means you can safely multiply any two modulo-reduced numbers together, and **the intermediate result will never overflow a `long long`**.

> 🚨 **The C++ Type Promotion Trap!**
> Even though the intermediate value of $10^{18}$ safely fits in a `long long`, you **must** explicitly tell C++ to use 64-bit math before you multiply!
> If `a` and `b` are 32-bit integers, `long long ans = (a * b) % MOD;` will **overflow** because C++ evaluates `a * b` in 32-bit space first!
> **The Fix:** Always multiply by `1LL` (a 64-bit literal of 1) to force type promotion:
> `long long ans = (1LL * a * b) % MOD;`

> 💡 **CP Insight:** If problem setters had chosen $10^{10} + 7$ instead, squaring it during a multiplication step would yield $10^{20}$. This instantly overflows a standard 64-bit integer, which would force you to write tedious custom BigInt code! $10^9 + 7$ is precisely engineered to fit safely inside modern CPU architectures.

---

## 3. Global Language Compatibility

Because $10^9 + 7$ plays so nicely with standard 32-bit and 64-bit boundaries, it ensures that problems are fundamentally fair across all programming languages.

Whether a student is coding in C++, Java, Python, or JavaScript, they can handle the intermediate computations using standard, out-of-the-box data types without resorting to slow, custom-built library dependencies.

</READING_WIDGET>
