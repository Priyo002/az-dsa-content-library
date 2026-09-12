<VIDEO_WIDGET>

<VIDEO_ID>70</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Karatsuba Multiplication — From Four Recursive Products to Three

## 1. What Are We Trying to Improve?

In merge sort, we divided an array into two halves, solved both halves, and combined their answers. Can we use the same **Divide → Conquer → Combine** approach to multiply two large numbers?

The answer is yes, but there is a catch:

> Splitting a problem into smaller problems does not automatically make the algorithm faster. The number of recursive calls matters too.

The straightforward split gives four smaller multiplications and still takes quadratic time. **Karatsuba multiplication** uses an algebraic identity to reduce those four multiplications to three.

We will follow this progression:

1. Express numbers using their base-`B` digits.
2. Understand why ordinary multiplication takes quadratic time.
3. Split each number into low and high parts.
4. Write the four-product divide-and-conquer solution.
5. Recover the middle term using only one additional product.
6. Derive the improved time complexity.

---

## 2. Representing Numbers in Base B

Our task is to compute `Z = X × Y` for two nonnegative integers represented in a fixed base `B ≥ 2`.

The lecture starts with two `(N + 1)`-digit numbers, with positions numbered from `0` to `N`. In this lesson, **`n` means the number of digits**, so positions run from `0` to `n - 1`:

$$
X = x_0 + x_1B + x_2B^2 + \cdots + x_{n-1}B^{n-1}
$$

$$
Y = y_0 + y_1B + y_2B^2 + \cdots + y_{n-1}B^{n-1}
$$

Each digit satisfies `0 ≤ xᵢ, yᵢ < B`. Position `0` is the **least significant** position.

For example, in base `10`:

```text
1234 = 4 + 3 × 10 + 2 × 10² + 1 × 10³

x₀ = 4, x₁ = 3, x₂ = 2, x₃ = 1
```

If the numbers have different lengths, let `n` be the larger length and conceptually pad the shorter number with leading zeros. Its value does not change.

### What does the complexity measure?

Here, the input size is the **digit count**, not the numeric value of `X` or `Y`.

We are studying numbers that may be too large for a built-in integer type. In the fixed-base digit-operation model:

- Adding or subtracting two `n`-digit numbers takes `O(n)` time.
- Multiplying two individual digits takes `O(1)` time.
- Multiplying two arbitrary `n`-digit numbers is the operation we want to improve.

Treating every large-number multiplication as a constant-time `*` would hide the very cost being analyzed.

---

## 3. Ordinary Multiplication: Why O(n²)?

Expanding the product gives:

$$
XY = \sum_{i=0}^{n-1}\sum_{j=0}^{n-1}x_i y_j B^{i+j}
$$

Group terms that have the same power of `B`:

$$
XY = z_0 + z_1B + z_2B^2 + \cdots + z_{2n-2}B^{2n-2}
$$

For example:

$$
z_0 = x_0y_0
$$

$$
z_1 = x_1y_0 + x_0y_1
$$

$$
z_2 = x_2y_0 + x_1y_1 + x_0y_2
$$

More generally:

$$
z_k = \sum_{j=\max(0,\,k-(n-1))}^{\min(k,\,n-1)}x_jy_{k-j}
$$

Every digit of `X` is multiplied by every digit of `Y`. There are `n²` such pairs, giving the usual schoolbook algorithm a time complexity of **Θ(n²)**.

### These coefficients are not yet the final digits

The `zₖ` values above are **uncarried coefficients**. They can be greater than or equal to `B`, so we must handle carries before treating them as base-`B` digits.

For example:

```text
99 × 99 = (9 + 9 × 10)(9 + 9 × 10)
        = 81 + 162 × 10 + 81 × 100
        = 9801
```

The coefficients `81, 162, 81` are not decimal digits. Carrying converts them into the digits of `9801`.

Although the uncarried expansion ends at power `2n - 2`, carrying can create a digit at position `2n - 1`. Therefore, multiplying two `n`-digit numbers can require **up to `2n` digits**.

---

## 4. Divide: Split Each Number into Two Parts

Let:

$$
m = \left\lfloor\frac{n}{2}\right\rfloor, \qquad q = B^m
$$

Write:

$$
X = X_L + qX_R
$$

$$
Y = Y_L + qY_R
$$

To match the lecture's notation:

- `X_L` and `Y_L` are the **low-order parts**, containing the last `m` digits.
- `X_R` and `Y_R` are the **high-order parts**, containing the remaining digits.

**Here, `L` means the low part; it does not mean the left side of the written decimal number.**

Equivalently:

$$
X_L = X \bmod q, \qquad X_R = \left\lfloor\frac{X}{q}\right\rfloor
$$

The same formulas apply to `Y`.

### Example: an even number of digits

For `X = 1234` in base `10`:

```text
n = 4, m = 2, q = 100

X_L = 34
X_R = 12

1234 = 34 + 100 × 12
```

Multiplication by `Bᵐ` shifts a number by `m` digit positions. It is not a general large-number multiplication: in a digit representation, it is a positional shift.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/c86aba10-996d-4d4e-b8e2-7a8694529964.png" alt="AlgoZenith diagram splitting 1234 into high part 12 and low part 34, and 5678 into high part 56 and low part 78, using a two-digit shift of 100" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Example: an odd number of digits

For the five-digit expression shown in the lecture:

$$
X = x_0 + x_1B + x_2B^2 + x_3B^3 + x_4B^4
$$

choose `m = 2`. Then:

$$
X_L = x_0 + x_1B
$$

$$
X_R = x_2 + x_3B + x_4B^2
$$

and `X = X_L + B²X_R`.

The low part has two digits and the high part has three. Perfectly equal halves are not required.

---

## 5. First Attempt: Four Recursive Multiplications

Substitute the split representations into `XY`:

$$
XY = (X_L + qX_R)(Y_L + qY_R)
$$

Expanding:

$$
XY = X_LY_L + q(X_LY_R + X_RY_L) + q^2X_RY_R
$$

Define three result blocks:

$$
Z_L = X_LY_L
$$

$$
Z_M = X_LY_R + X_RY_L
$$

$$
Z_R = X_RY_R
$$

Then combine them:

$$
\boxed{XY = Z_L + B^mZ_M + B^{2m}Z_R}
$$

There are three blocks, but how many multiplications do we need?

| Block | Products needed | Number of recursive multiplications |
| --- | --- | --- |
| `Z_L` | `X_L × Y_L` | 1 |
| `Z_M` | `X_L × Y_R` and `X_R × Y_L` | 2 |
| `Z_R` | `X_R × Y_R` | 1 |
| Total | | **4** |

For balanced halves, the recurrence is:

$$
T(n) = 4T(n/2) + O(n)
$$

The linear term accounts for splitting, additions, and positional shifts. The recurrence gives:

$$
T(n) = \Theta(n^2)
$$

So this recursive version has not improved the asymptotic time complexity of ordinary multiplication.

> **Interview Insight — Count operations, not named blocks:** `Z_M` is one expression but contains two recursive multiplications. The recurrence comes from the actual work performed, not the number of variables in the formula.

---

## 6. Karatsuba's Idea: Recover the Middle Term

We already need `Z_L = X_LY_L` and `Z_R = X_RY_R`. Can these answers help us compute `Z_M`?

Consider one new product:

$$
P = (X_L + X_R)(Y_L + Y_R)
$$

Expanding it gives:

$$
P = X_LY_L + X_LY_R + X_RY_L + X_RY_R
$$

The first and last terms are exactly the products we have already computed:

$$
P = Z_L + Z_M + Z_R
$$

Therefore:

$$
\boxed{Z_M = P - Z_L - Z_R}
$$

We no longer compute the two cross products separately. We obtain their **sum**, which is all the combine step requires.

The complete calculation is now:

$$
Z_L = \operatorname{multiply}(X_L,Y_L)
$$

$$
Z_R = \operatorname{multiply}(X_R,Y_R)
$$

$$
P = \operatorname{multiply}(X_L+X_R,\;Y_L+Y_R)
$$

$$
Z_M = P-Z_L-Z_R
$$

$$
\boxed{XY = Z_L + B^mZ_M + B^{2m}Z_R}
$$

> **Key Observation:** Replace one expensive recursive multiplication with a constant number of linear-time additions and subtractions. Apply this saving at every recursive level.

This is algebraic reuse, not memoization: we avoid computing the cross products individually rather than caching repeated calls.

---

## 7. The Recursive Algorithm

### Recursive contract

`karatsuba(X, Y)` returns the exact product of the two nonnegative integers `X` and `Y`.

The implementation follows the same three-step structure as merge sort:

1. **Divide:** Split each number into low and high parts using the same `m`.
2. **Conquer:** Compute the low product, high product, and product of sums recursively.
3. **Combine:** Recover the middle term and shift the three blocks into position.

### Pseudocode

The lecture focuses on the multiplication idea. The following is **arbitrary-precision pseudocode**, not C++ code using fixed-width integers. Addition, subtraction, splitting, and shifts must operate exactly on the digit representation.

```text
karatsuba(X, Y):
    if X == 0 or Y == 0:
        return 0

    n = max(number_of_base_B_digits(X), number_of_base_B_digits(Y))

    if n <= 3:
        return schoolbook_multiply(X, Y)

    m = floor(n / 2)
    q = B^m

    X_L = X mod q
    X_R = X div q
    Y_L = Y mod q
    Y_R = Y div q

    Z_L = karatsuba(X_L, Y_L)
    Z_R = karatsuba(X_R, Y_R)
    P   = karatsuba(X_L + X_R, Y_L + Y_R)

    Z_M = P - Z_L - Z_R

    return Z_L + shift_digits(Z_M, m) + shift_digits(Z_R, 2*m)
```

Here, `shift_digits(V, k)` means `V × Bᵏ`, and `div` means integer division. Splitting by a power of the representation base can be implemented by separating digit ranges.

### Why use a small-size cutoff?

The sums `X_L + X_R` and `Y_L + Y_R` can have one more digit than either half. For very small inputs, their digit count need not be strictly smaller than `n`.

The cutoff `n ≤ 3` makes termination straightforward: for every larger input,

$$
\left\lceil n/2\right\rceil + 1 < n
$$

so even the product-of-sums call is smaller. Any suitable fixed cutoff at least this large also works; the value `3` is a teaching choice, not a performance-tuned threshold.

---

## 8. Dry Run: 1234 × 5678

Use base `10`, so `n = 4`, `m = 2`, and `q = 100`.

### Step 1: Divide

```text
X = 1234 = 34 + 100 × 12
Y = 5678 = 78 + 100 × 56

X_L = 34, X_R = 12
Y_L = 78, Y_R = 56
```

### Step 2: Compute three smaller products

| Product | Calculation | Value |
| --- | --- | --- |
| `Z_L` | `34 × 78` | `2652` |
| `Z_R` | `12 × 56` | `672` |
| `P` | `(34 + 12) × (78 + 56) = 46 × 134` | `6164` |

Notice that `134` has three digits even though the original halves had at most two. This is the extra-digit issue discussed above. Under our pseudocode's cutoff, all three products are handled directly.

### Step 3: Recover the middle term

```text
Z_M = P - Z_L - Z_R
    = 6164 - 2652 - 672
    = 2840
```

For verification only, the original cross-product expression gives:

```text
34 × 56 + 12 × 78 = 1904 + 936 = 2840
```

Karatsuba does **not** compute these two cross products separately.

### Step 4: Combine

```text
XY = Z_L + 100 × Z_M + 10000 × Z_R
   = 2652 + 284000 + 6720000
   = 7006652
```

The result blocks can overlap after shifting because they may contain more than `m` digits. We **add** the shifted values with carries; we do not concatenate their decimal strings.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/a3754e74-8cda-454f-a2d8-8fdd166c612f.png" alt="AlgoZenith Karatsuba dry run: three products 2652, 672, and 6164 recover the middle term 2840, then shifted addition gives 1234 times 5678 equals 7006652" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 9. Why Is the Algorithm Correct?

We prove the recursive contract by induction on the maximum digit count.

### Base case

If either input is zero, returning zero is correct. For inputs within the small-size cutoff, schoolbook multiplication returns the exact product.

### Recursive step

Assume the recursive calls return correct products for smaller inputs. The split identities give:

$$
X = X_L + B^mX_R, \qquad Y = Y_L + B^mY_R
$$

By the induction hypothesis, the three calls correctly compute `Z_L`, `Z_R`, and `P`. Consequently:

$$
P-Z_L-Z_R = X_LY_R + X_RY_L
$$

Substituting this into the returned value gives:

$$
Z_L+B^m(P-Z_L-Z_R)+B^{2m}Z_R
$$

$$
=X_LY_L+B^m(X_LY_R+X_RY_L)+B^{2m}X_RY_R
$$

$$
=(X_L+B^mX_R)(Y_L+B^mY_R)=XY
$$

Thus, the current call also returns the exact product. The argument works for odd lengths and unequal input lengths because it uses the actual split width `m`.

---

## 10. Time and Space Complexity

### 10.1 The recurrence

Each non-base call performs three multiplications on approximately half-size inputs, plus linear-time digit work:

$$
T(n) = 3T(n/2) + O(n)
$$

This is the standard balanced-size recurrence used in the lecture. More precisely, the two direct products have operands of at most `⌈n/2⌉` digits, and the product of sums can have operands of at most `⌈n/2⌉ + 1` digits. A corresponding worst-case upper bound is:

$$
T(n) \le 2T(\lceil n/2\rceil)
+T(\lceil n/2\rceil+1)+O(n)
$$

The rounding and one extra digit do not change the asymptotic exponent. Along any branch, repeated halving leaves a size of `n/2ʰ + O(1)` after `h` levels; a fixed base-case cutoff absorbs the constant-size remainder.

### 10.2 Understanding the exponent

For the balanced recurrence, at recursion level `i`:

- There are `3ⁱ` subproblems.
- Each has about `n/2ⁱ` digits.
- Their total nonrecursive work is `O(n(3/2)ⁱ)`.

The depth is approximately `log₂ n`. Unlike merge sort, where every level costs `O(n)`, here the work per level grows geometrically.

At the bottom, the number of constant-size subproblems is:

$$
3^{\log_2 n}=n^{\log_2 3}
$$

Summing the geometric level costs gives the same order:

$$
\boxed{T(n)=\Theta(n^{\log_2 3})\approx\Theta(n^{1.585})}
$$

This is the standard worst-case complexity of Karatsuba multiplication under the digit-operation model. Special inputs, such as multiplication by zero, may finish earlier.

| Approach | Balanced recurrence | Time complexity |
| --- | --- | --- |
| Schoolbook multiplication | Directly considers all digit pairs | `Θ(n²)` |
| Four-product divide and conquer | `4T(n/2) + O(n)` | `Θ(n²)` |
| Karatsuba multiplication | `3T(n/2) + O(n)` | `Θ(n^log₂3) ≈ Θ(n^1.585)` |

> **Interview Insight — Saving one call changes the exponent:** This is not merely a constant-factor saving at the root. Reducing the branching factor from four to three at every level changes quadratic growth into subquadratic growth.

### 10.3 Auxiliary space

The recursion depth is `O(log n)`, but that is not the entire memory cost: the algorithm also stores multi-digit pieces, sums, and intermediate products.

With sequential recursive calls and temporary buffers released or reused after each call, the live digit storage along a branch is bounded by:

$$
O(n)+O(n/2)+O(n/4)+\cdots=O(n)
$$

Thus, a standard depth-first implementation can use **O(n) auxiliary digit storage**, plus **O(log n) call frames**. Retaining every intermediate result in the entire recursion tree would use more memory.

---

## 11. Important Implementation Details

### 11.1 Use the same split width for both numbers

Choose `m` from the maximum input length, not independently for `X` and `Y`. Both decompositions must use the same `q = Bᵐ` for the combine formula above.

### 11.2 Preserve positional width even when a part has leading zeros

For `X = 1203` and `m = 2`, the low part has value `3`, but the split is still:

```text
1203 = 3 + 100 × 12
```

Do not replace the shift by `10` just because the low part's value has one digit.

### 11.3 Use B^(2m), not always B^n

When `n` is even, `2m = n`. When `n` is odd, these differ. The universally correct high-product shift is **`B^(2m)`**.

### 11.4 Store and reuse the three products

Compute `Z_L` and `Z_R` once. Recomputing them while evaluating `P - Z_L - Z_R` would undo the intended saving.

### 11.5 Do not ignore arithmetic limits

The inputs, sums, partial products, and final result must all be representable. Replacing the pseudocode's numbers with `long long` does not create an arbitrary-precision implementation.

Likewise, mathematical `B^m` denotes exponentiation; in C++, `^` is bitwise XOR. Avoid floating-point powers when exact digit shifts are needed.

### 11.6 Test the representation as well as the identity

Useful checks include multiplication by zero, one-digit values, unequal lengths, odd lengths, low parts containing zeros, and all-`9` decimal inputs that produce many carries. For small random inputs, compare the result with ordinary multiplication.

> **CP Insight — Match the algorithm to the constraints:** For values whose product fits a built-in integer type, ordinary multiplication is the appropriate tool. Karatsuba becomes relevant when working with large digit-based representations; its recursion and temporary arithmetic also have overhead, so a practical implementation uses schoolbook multiplication below a chosen threshold.

---

## 12. Quick Recap

For `m = ⌊n/2⌋`, split:

$$
X=X_L+B^mX_R, \qquad Y=Y_L+B^mY_R
$$

Compute only three recursive products:

$$
Z_L=X_LY_L, \qquad Z_R=X_RY_R,
\qquad P=(X_L+X_R)(Y_L+Y_R)
$$

Recover the middle term and combine:

$$
Z_M=P-Z_L-Z_R
$$

$$
XY=Z_L+B^mZ_M+B^{2m}Z_R
$$

The resulting recurrence is `T(n) = 3T(n/2) + O(n)`, giving **O(n^1.585)** time, approximately, instead of **O(n²)**.

> The reusable divide-and-conquer lesson is to ask: **Do we really need every smaller answer individually, or can we reconstruct the combination we need with fewer recursive calls?**

</READING_WIDGET>
