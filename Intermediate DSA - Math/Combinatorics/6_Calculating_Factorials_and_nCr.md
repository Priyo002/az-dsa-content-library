<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Calculating Factorials and nCr in Code

In Competitive Programming, answering combinatorial questions usually isn't just about figuring out the math on paper—you also have to write code to calculate the massive numbers without overflowing integer limits or Timing Out (TLE). 

Because $N!$ grows extremely fast, almost every combinatorial problem requires you to calculate the answer **modulo** $10^9 + 7$.

---

## 1. Factorial ($N!$)

The factorial of a number tells us how many ways there are to arrange $N$ items in an ordered manner.
$$N! = N \times (N-1) \times (N-2) \times \dots \times 1$$

### Program for Calculating Factorial with Modulo
Calculate the factorial of a number and print the answer modulo $10^9 + 7$.

```cpp
#include<bits/stdc++.h>
using namespace std;

#define int long long 
int mod = 1e9 + 7;

int fact(int x) {
    int ans = 1;
    for(int i = 2; i <= x; i++) {
        ans = (ans * i) % mod;
    }
    return ans;
}

signed main() {
    int x;
    cin >> x;
    cout << fact(x) << '\n';
    return 0;
}
```

> 💡 **Note:** There is no need to apply the modulo to `ans` at the very end of the function, because at each iteration inside the loop, the number is securely getting modded!

---

## 2. Combination ($^nC_r$)

$n$ Choose $r$ represents the number of ways to combinatorially select $r$ items out of a total of $n$ items (where order does not matter).
$$^nC_r = \frac{n!}{r! \times (n-r)!}$$

### Reason behind $^nC_r$ always being an integer
The number of ways to physically select something can never be a fraction—it must be a whole integer. Therefore, we know mathematically that:
$$\frac{n!}{r! \times (n-r)!} \in \mathbb{I}$$

If we expand the factorial in the numerator, we get:
$$\frac{n \times (n-1) \times \dots \times (n-r+1) \times (n-r)!}{r! \times (n-r)!} \in \mathbb{I}$$
$$\implies \frac{n \times (n-1) \times \dots \times (n-r+1)}{r!} \in \mathbb{I}$$

### Divisibility of Product of Consecutive Integers
From the mathematical proof above, we derive a powerful universal rule:
> **The product of any $r$ consecutive numbers is ALWAYS perfectly divisible by $r!$**

---

## 3. Programs for Calculating $^nC_r$

Depending on the constraints of $N$, $R$, and the number of test queries, you must choose the appropriate algorithmic approach to calculate $^nC_r$.

### Approach 1: Using Modular Inverses
Since we cannot perform standard division under a modulo operation, we must use **Modular Multiplicative Inverses** along with Binary Exponentiation. *(Note: Raising a number to the power of `mod - 2` works exclusively because of **Fermat's Little Theorem**, which requires `mod` to be a prime number!)*

```cpp
#include<bits/stdc++.h>
using namespace std;

#define int long long
int mod = 1e9 + 7;

int binpow(int a, int b) {
    if(b == 0) return 1;
    if(b % 2 == 1) return (a * binpow(a, b-1)) % mod;
    int x = binpow(a, b/2);
    return (x * x) % mod; 
}

int inverse(int x) {
    return binpow(x, mod-2);
}

int fact(int x) { 
    int ans = 1; 
    for(int i = 2; i <= x; i++) { 
        ans = (ans * i) % mod;
    } 
    return ans; 
}

int ncr(int n, int r) {
    if (r < 0 || r > n) return 0;
    int num = fact(n);
    int den = (fact(r) * fact(n-r)) % mod;
    return (num * inverse(den)) % mod;
}
```
**Time Complexity:** $\mathcal{O}(N + R)$

### Approach 2: Small $R$ ($N \le 10^9, R \le 20$)
If $N$ is massive but $R$ is tiny, the previous code will TLE because calculating `fact(10^9)` takes too long. Instead, we manually calculate the numerator and denominator up to $R$ terms.

```cpp
int single_ncr(int n, int r) {
    if (r < 0 || r > n) return 0;
    int num = 1, den = 1;
    for(int i = 1; i <= r; i++) {
        num = (num * (n - i + 1)) % mod;
        den = (den * i) % mod;
    }
    return (num * inverse(den)) % mod;
}
```
**Time Complexity:** $\mathcal{O}(R)$
*(Tip: You can optimize this further by looping up to $\min(r, n-r)$).*

### Approach 3: Exact Value without Modulo ($N \le 40, R \le N$)
Up to $N=40$, the exact value of $^nC_r$ fits inside a standard 64-bit `long long`. We don't need modulo inverses—we can just do raw division!

```cpp
int basic_ncr(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r); // Symmetry optimization
    
    int ans = 1;
    for(int i = 1; i <= r; i++) {
        ans = ans * (n - i + 1);
        ans = ans / i;
    }
    return ans;
}
```
> ⚠️ **Warning:** Because of the consecutive integers divisibility rule, `ans / i` will always perfectly divide without decimals. This only safely works for $N \le 40$.

### Approach 4: Non-Prime Modulo ($N \le 1000$)
What if the modulo is $10^9$ (which is NOT a prime number)? You **cannot** use Fermat's Little Theorem to find the inverse! However, addition always works regardless of the modulo. We can build **Pascal's Triangle** using dynamic programming:
$$^{n}C_{r} = ^{n-1}C_{r} + ^{n-1}C_{r-1}$$

```cpp
int mod = 1e9; // Non-prime!
int ncr[1001][1001];

int ncr_random_modulo(int n, int r) {
    if (r < 0 || r > n) return 0;
    ncr[0][0] = 1; // 1 way to choose 0 from 0

    for(int i = 1; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            if(j == 0) ncr[i][j] = ncr[i-1][j] % mod;
            else ncr[i][j] = (ncr[i-1][j-1] + ncr[i-1][j]) % mod;
        }
    }
    return ncr[n][r];
}
```

### Approach 5: Multiple Queries ($Q \le 10^6, N \le 10^6$)
If there are millions of test cases, recalculating factorials for every query will TLE. We must **precompute** all factorials globally!

```cpp
int fact[1000100];

void precompute() {
    fact[0] = 1;
    for(int i = 1; i <= 1000000; i++) {
        fact[i] = (fact[i-1] * i) % mod;
    }
}

int ncr_fact(int n, int r) {
    if (r < 0 || r > n) return 0;
    int num = fact[n];
    int den = (fact[n-r] * fact[r]) % mod;
    return (num * inverse(den)) % mod;
}
```
**Time Complexity:** $\mathcal{O}(\log(\text{mod}))$ per query due to the inverse calculation. This is the most common template used in CP!

### Approach 6: $\mathcal{O}(1)$ Queries via Precomputed Inverses
If $\mathcal{O}(\log(\text{mod}))$ per query is still too slow, we can globally precompute the inverses of the factorials as well!
Notice that: $\frac{1}{(i-1)!} = i \times \frac{1}{i!} \implies \big((i-1)!\big)^{-1} = i \times (i!)^{-1}$

```cpp
int fact[1000100];
int invfact[1000100];

void precompute_for_faster() {
    fact[0] = 1;
    for(int i = 1; i <= 1000000; i++) {
        fact[i] = (fact[i-1] * i) % mod;
    }
    
    invfact[1000000] = inverse(fact[1000000]);
    for(int i = 1000000; i >= 1; i--) {
        invfact[i-1] = (invfact[i] * i) % mod;
    }
}

int ncr_fact_faster(int n, int r) {
    if (r < 0 || r > n) return 0;
    int num = fact[n];
    int den = (invfact[n-r] * invfact[r]) % mod;
    return (num * den) % mod; // den is already inverted!
}
```
**Time Complexity:** $\mathcal{O}(1)$ per query!
*(Precomputation takes $\mathcal{O}(N + \log(\text{mod}))$).*

</READING_WIDGET>
