<VIDEO_WIDGET>

<VIDEO_ID>365</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Product of Last K in Stream

> *Processing data streams requires a shift in mindset. You don't have a static array; you have a continuous flow of numbers. Designing a structure that can instantly return mathematical properties of the recent past is a staple in Financial Tech (FinTech) and Data Analytics interviews.*

---

## 1. The Challenge

Design a Data Structure that supports a continuous stream of numbers with two methods:
1. `void add(int x)`: Appends the number `x` to the stream.
2. `int getProduct(int k)`: Returns the product of the last `k` numbers added to the stream.

**The Constraints:** Both operations must run in **$O(1)$ Time Complexity**.

> 🚨 **The Hidden Constraint: Integer Overflow**
> In the standard LeetCode version of this problem (LC 1352), there is a crucial hidden constraint: *"It is guaranteed that the product of any prefix fits into a standard 32-bit integer."* Without this guarantee, multiplying `10` just ten times equals $10^{10}$, which permanently overflows a standard 32-bit `int` and destroys your data! You must always clarify this constraint with your interviewer before using this architecture in a production system.

### The Naive $O(K)$ Approach
The beginner approach is to simply store every incoming number in a `std::vector<int>`. When `getProduct(k)` is called, they run a `for` loop backwards from the end of the vector, multiplying the last $k$ elements together.
If $K$ is 100,000, and this function is called repeatedly, the system will instantly bottleneck. We need a mathematical shortcut.

---

## 2. The Mathematical Shortcut: Prefix Products

If you have an array `[A, B, C, D]` and you want the product of the last 2 elements (`C * D`), you can use a **Prefix Product Array**.

A Prefix Product array stores the cumulative product at each step:
`[A,  A*B,  A*B*C,  A*B*C*D]`

If you take the final element (`A*B*C*D`) and **divide** it by the element exactly $K$ steps behind it (`A*B`), you mathematically cancel out the early elements, leaving exactly the product you want:
`(A * B * C * D) / (A * B) = C * D`

Thus, `getProduct(K)` becomes a simple $O(1)$ division operation:
`prefix.back() / prefix[prefix.size() - k - 1]`

---

## 3. The Fatal Flaw: The "Zero" Trap

The prefix product logic is brilliant until someone adds a `0` to the stream.
If the stream is `[3, 2, 0, 4]`, the Prefix Product array becomes:
`[3, 6, 0, 0]`

If you try to use the division formula now, you will encounter a **Divide by Zero** exception, which instantly crashes your entire server!

### The Golden Architecture: The Zero Reset
Think about the mathematics of zero. If a `0` enters the stream, *any* future `getProduct(K)` request that includes that zero in its $K$-window will inherently evaluate to `0`! 
The numbers that came *before* the zero are now completely useless because they will always be multiplied by zero anyway.

**The Strategy:**
- We initialize our prefix array with a dummy `1` to handle math cleanly.
- If `x > 0`, we multiply it by our `prefix.back()` and push it.
- **If `x == 0`**, we completely **clear** the prefix array and reset it back to just `[1]`!
- When `getProduct(K)` is called, we check if $K$ is greater than or equal to our current `prefix.size()`. If it is, it means a `0` was added within the last $K$ elements, so we instantly return `0`. Otherwise, we perform the $O(1)$ division.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/5e91f792-7345-4b14-8012-a9c2a74b89b1.jpg" alt="Prefix Product Stream Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. The Code Implementation

```cpp
#include <vector>
using namespace std;

class ProductOfNumbers {
private:
    vector<int> prefix;

public:
    ProductOfNumbers() {
        // Initialize with a dummy 1 to make the division math work seamlessly
        prefix.push_back(1);
    }
    
    // Time Complexity: O(1)
    void add(int num) {
        if (num == 0) {
            // 🚨 SRE Defense: A zero annihilates everything before it.
            // Reset the stream completely!
            prefix.clear();
            prefix.push_back(1);
        } else {
            // Multiply the new number by the previous cumulative product
            prefix.push_back(prefix.back() * num);
        }
    }
    
    // Time Complexity: O(1)
    int getProduct(int k) {
        int n = prefix.size();
        
        if (k >= n) {
            // If K is larger than our current prefix array, it means
            // a 0 was encountered within the last K steps.
            return 0;
        }
        
        // O(1) Mathematical cancellation
        return prefix.back() / prefix[n - k - 1];
    }
};
```

### Complexity Breakdown
*   **Time Complexity:** $O(1)$ for both `add()` and `getProduct()`. Clearing a vector or pushing to it is amortized $O(1)$. The division is strict $O(1)$.
*   **Space Complexity:** $O(N)$ where $N$ is the number of elements added to the stream *since the last zero*.

> **Elite CP Insight: Modular Multiplicative Inverse**
> What if the problem does *not* guarantee the product fits in a 32-bit integer? In advanced Competitive Programming (like Codeforces), you will be asked to return the answer **Modulo $10^9 + 7$**.
> Beginners often try to do: `(prefix.back() / prefix[n - k - 1]) % MOD`. 
> **This is mathematically illegal!** You cannot distribute a modulo across division. To perform division under a modulo, you must multiply by the **Modular Multiplicative Inverse** using Fermat's Little Theorem: 
> `Answer = (prefix.back() * modInverse(prefix[n - k - 1], MOD)) % MOD`.

## 5. Module Summary
- Naive reverse iteration is $O(K)$ and cannot scale for massive stream queries.
- We use a **Prefix Product** array to reduce range multiplication to a single $O(1)$ division operation.
- A `0` in the stream destroys data continuity and will trigger a Divide-By-Zero crash if not handled.
- By intelligently resetting the prefix array upon seeing a `0`, we can answer queries instantly by checking if $K$ exceeds our current active array size.

</READING_WIDGET>
