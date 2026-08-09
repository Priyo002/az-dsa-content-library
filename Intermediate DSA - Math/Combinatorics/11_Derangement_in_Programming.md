<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Derangement in Programming

> *While the Inclusion-Exclusion formula $n! \sum \frac{(-1)^k}{k!}$ is mathematically beautiful, it is computationally expensive to calculate factorials and perform large divisions in a competitive programming environment. Luckily, derangements follow an incredibly elegant **Dynamic Programming** recurrence relation!*

---

## 1. The Recursive Formula

The number of derangements of $N$ elements, denoted as $D(N)$, can be computed using the following recursive formula:
$$ D(N) = (N - 1) \times (D(N - 1) + D(N - 2)) $$

### The Logical Proof
If we have $N$ elements and want to create a derangement, consider the $1$st element. 
It must be placed in a wrong position. There are exactly **$(N - 1)$** wrong positions it could go to. 

Let's assume we place element $1$ into position $K$. What happens to element $K$? We have two choices:
1. **Swap:** Element $K$ goes directly into position $1$. The two elements have perfectly swapped. Now, we just need to derange the remaining $(N - 2)$ elements! This gives us the $D(N - 2)$ term.
2. **Displace:** Element $K$ goes anywhere *except* position $1$. This is mathematically identical to saying "derange the remaining $(N - 1)$ elements" (where element $K$ is pretending that position $1$ is its "original" restricted position). This gives us the $D(N - 1)$ term.

Since the $1$st element had $(N - 1)$ choices for $K$, we multiply the sum of these two outcomes by $(N - 1)$.

### The Base Cases
- $D(1) = 0$ (You cannot derange 1 element; it must sit in its only slot).
- $D(2) = 1$ (You just swap the two elements).

<img src="images/derangement_dp_architecture.jpg" alt="Derangement Dynamic Programming Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 2. Implementing the Formula

There are three ways to compute $D(N)$. Let's evolve from the naive approach to the FAANG-optimal approach.

### Approach 1: Naive Recursion ❌
Translating the formula directly into recursion without memoization results in massive overlapping subproblems.

```cpp
#include <iostream>
using namespace std;

long long derangement(int n) {
    if (n == 1) return 0;
    if (n == 2) return 1;
    return (n - 1) * (derangement(n - 1) + derangement(n - 2));
}
```
- **Time Complexity:** $O(2^N)$ - Exponential. This will immediately trigger a Time Limit Exceeded (TLE) for anything past $N = 30$.

### Approach 2: Dynamic Programming (Bottom-Up Array) ⚠️
Since the state only depends on the previous two states, we can build it iteratively using an array.

```cpp
#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;
long long der[1000001]; 

void compute_derangements(int N) {
    der[1] = 0;
    der[2] = 1;
    for (int i = 3; i <= N; i++) {
        // Apply modulo at the addition AND multiplication steps to prevent overflow!
        der[i] = ((i - 1) * ((der[i - 1] + der[i - 2]) % MOD)) % MOD;
    }
}
```
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ - Creating a massive array of size $10^6$ takes significant memory overhead. We can do better!

### Approach 3: Space-Optimized DP (Rolling Variables) ✅
Look closely at the formula: $D(N)$ *only* cares about $D(N-1)$ and $D(N-2)$. We don't need to store the entire array in memory! We can just use two variables to "roll" forward, exactly like generating the Fibonacci sequence.

> 💡 **Elite CP Insight: Rolling State Transition**
> Whenever a DP state only relies on a fixed window of previous states (e.g., $i-1$ and $i-2$), always drop the $O(N)$ array and use rolling variables to achieve $O(1)$ space complexity!

```cpp
#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

long long compute_derangement_optimal(int N) {
    if (N == 1) return 0;
    if (N == 2) return 1;

    long long prev2 = 0; // Represents D(i-2)
    long long prev1 = 1; // Represents D(i-1)
    long long current = 0;

    for (int i = 3; i <= N; i++) {
        current = ((i - 1) * ((prev1 + prev2) % MOD)) % MOD;
        // Roll the variables forward
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}
```
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(1)$ - The absolute optimal FAANG solution.

> 💡 **Elite CP Architecture: The 1st-Order Recurrence**
> You correctly reduced the state to two variables (`prev1` and `prev2`) using the standard DP transition. However, elite competitive programmers know a mathematical trick to reduce it to just *one* variable!
> There is a mathematically proven 1st-order recurrence relation for derangements:
> $$ D_N = N \times D_{N-1} + (-1)^N $$
> This means you don't even need `prev2`! You only need the immediate previous state. Implementing this requires careful handling of negative numbers with modulo arithmetic in C++ (e.g., `(x % MOD + MOD) % MOD`), but it represents the absolute mathematical ceiling of this problem.

---

## 3. Real-World Application: The Christmas Party

**Problem Statement:**
There are $N$ children at a Christmas party, and each of them has brought a gift. The idea is that everybody will get a gift brought by someone else (no child can receive their own gift). In how many ways can the gifts be distributed? Return the answer modulo $10^9 + 7$.

**Constraints:** $1 \le N \le 10^6$

**Analysis:**
The problem enforces that no child (element) receives their own gift (original position). This is the exact definition of a Derangement! 
Because $N$ goes up to $10^6$, we must use the $O(N)$ Dynamic Programming approach. 
Because the answers grow astronomically fast, we must enforce modulo arithmetic at every step.

**The Solution:**
```cpp
#include <iostream>
using namespace std;

const int MOD = 1e9 + 7;

long long christmas_party(int N) {
    if (N == 1) return 0;
    if (N == 2) return 1;

    long long prev2 = 0;
    long long prev1 = 1;
    long long current = 0;

    for (int i = 3; i <= N; i++) {
        current = ((i - 1) * ((prev1 + prev2) % MOD)) % MOD;
        prev2 = prev1;
        prev1 = current;
    }
    
    return current;
}

int main() {
    int N;
    // Example: N = 5 children
    cin >> N;
    cout << "Ways to distribute gifts: " << christmas_party(N) << endl;
    return 0;
}
```

By recognizing the derangement constraint and optimizing our space to $O(1)$, we solve the problem optimally, blowing past memory limits and TLEs.

</READING_WIDGET>
