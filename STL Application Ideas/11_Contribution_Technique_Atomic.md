<VIDEO_WIDGET>

<VIDEO_ID>3601</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Contribution Technique: Atomic Item Contribution

> *Beginners write code that asks, "What elements are inside this structure?" Elite programmers invert the paradigm and ask, "How many structures contain this specific element?" This mindset shift is known as the **Contribution Technique**.*

---

## 1. Problem 1: Sum of Subarrays

**Problem Statement:** 
Given an array `arr[]` of size `N`, find the sum of *all possible subarrays* of the given array.

### The Naive $O(N^2)$ Trap
The beginner's instinct is to generate every single subarray. You run an outer loop `L` for the start index, an inner loop `R` for the end index, and keep a running sum.
While this works for $N = 1000$, the problem constraints state $N = 10^5$. An $O(N^2)$ algorithm will attempt $10^{10}$ operations and trigger a catastrophic **Time Limit Exceeded (TLE)**.

We need a strictly $O(N)$ solution.

---

## 2. The $O(N)$ Architecture: Atomic Contribution

Instead of building subarrays and summing their contents, let's zoom in on a single, atomic element at index `i`. 
**Question:** Out of all possible subarrays, how many of them actually contain `arr[i]`?

If a subarray `[L, R]` contains `arr[i]`, it must satisfy one absolute rule: 
The start index $L$ must be on or before $i$, and the end index $R$ must be on or after $i$.
$$L \le i \le R$$

### The Combinatorial Math
Let's count the choices:
1. **Choices for $L$:** The start index can be anything from $0$ up to $i$. That is exactly **$(i + 1)$** choices.
2. **Choices for $R$:** The end index can be anything from $i$ up to $N - 1$. That is exactly **$(N - i)$** choices.

Because the choice of $L$ and $R$ are completely independent, we multiply them to find the total combinations!
**Total subarrays containing `arr[i]` = $(i + 1) \times (N - i)$**

> 📝 **Dry Run: `arr = [1, 2, 3]` (N = 3)**
> - For **`1`** (at index `0`): $L$ choices = $(0+1)=1$. $R$ choices = $(3-0)=3$. Total = $1 \times 3 = \mathbf{3}$ subarrays: `[1]`, `[1,2]`, `[1,2,3]`. Contribution: $1 \times 3 = 3$.
> - For **`2`** (at index `1`): $L$ choices = $(1+1)=2$. $R$ choices = $(3-1)=2$. Total = $2 \times 2 = \mathbf{4}$ subarrays: `[2]`, `[1,2]`, `[2,3]`, `[1,2,3]`. Contribution: $2 \times 4 = 8$.
> - For **`3`** (at index `2`): $L$ choices = $(2+1)=3$. $R$ choices = $(3-2)=1$. Total = $3 \times 1 = \mathbf{3}$ subarrays: `[3]`, `[2,3]`, `[1,2,3]`. Contribution: $3 \times 3 = 9$.
> - **Total Expected Sum:** $3 + 8 + 9 = \mathbf{20}$. This exactly mathematically maps to the brute-force output!

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/d40b8b61-6d66-4d2d-ba2a-a0e619846b17.png" alt="Contribution Technique Combinatorics Architecture" style="max-width: 100%; height: auto;" identifier="az-img-upload">

If `arr[i]` appears in exactly that many subarrays, its total **contribution** to the final answer is simply:
`arr[i] * (i + 1) * (N - i)`

By looping through the array once and summing the contribution of each atomic element, we instantly solve the problem in $O(N)$!

### The Code Implementation

> 🚨 **The FAANG Overflow Trap**
> Even if the final answer fits in a 32-bit integer, the intermediate multiplication `(i + 1) * (N - i)` can easily exceed $2 \times 10^9$ for large $N$. If you don't cast these to `long long` *before* multiplying, the math will silently overflow and you will fail hidden test cases!

```cpp
#include <iostream>
#include <vector>

using namespace std;

long long subarraySum(const vector<int>& arr) {
    long long total_sum = 0;
    long long n = arr.size();
    
    for (long long i = 0; i < n; ++i) {
        // Combinatorics: Choices for Left boundary * Choices for Right boundary
        long long occurrences = (i + 1) * (n - i);
        
        // Calculate total atomic contribution
        long long contribution = arr[i] * occurrences;
        
        total_sum += contribution;
    }
    
    return total_sum;
}

int main() {
    vector<int> arr = {1, 2, 3};
    // Expected Output: 20
    cout << "Total Sum of all Subarrays: " << subarraySum(arr) << "\n";
    return 0;
}
```

---

## 3. Problem 2: Sum of All Triplets

**Problem Statement:**
Given an array `arr[]` of size `N`, find the sum of all elements across all possible triplets in the array. 

### The Triplet Combinatorics
A triplet is formed by choosing exactly 3 distinct elements from the array. 
If we use the Contribution Technique, we ask: **"How many triplets contain the specific element `arr[i]`?"**

If we lock `arr[i]` as one of the elements, we must choose exactly $2$ more elements from the remaining $(N - 1)$ elements in the array to complete the triplet.
This is basic combinations: **Choose 2 from (N - 1)**.
Mathematically, this is written as $\binom{N-1}{2}$, which evaluates to:
$$ \frac{(N - 1) \times (N - 2)}{2} $$

This means *every single element* in the array appears in exactly that many triplets!

> 📝 **Dry Run: `arr = [1, 2, 3, 4]` (N = 4)**
> - Triplet formula multiplier: $\frac{(4-1) \times (4-2)}{2} = \frac{3 \times 2}{2} = \mathbf{3}$.
> - Every element appears in exactly **3** triplets!
> - Let's verify for **`1`**: It appears in `{1,2,3}`, `{1,2,4}`, `{1,3,4}`. Exactly 3 times!
> - Total sum calculation: $(1 \times 3) + (2 \times 3) + (3 \times 3) + (4 \times 3) = 3 + 6 + 9 + 12 = \mathbf{30}$.

### The $O(N)$ Code Implementation

```cpp
#include <iostream>
#include <vector>

using namespace std;

long long tripletSum(const vector<int>& arr) {
    long long total_sum = 0;
    long long n = arr.size();
    
    // Edge case: You can't form a triplet with less than 3 elements!
    if (n < 3) return 0;
    
    // Calculate how many triplets a single element appears in
    long long occurrences = ((n - 1) * (n - 2)) / 2;
    
    for (int i = 0; i < n; ++i) {
        total_sum += (long long)arr[i] * occurrences;
    }
    
    return total_sum;
}

int main() {
    vector<int> arr = {1, 2, 3, 4};
    
    // The triplets are:
    // {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}
    // Sum = 6 + 7 + 8 + 9 = 30
    cout << "Total Sum of all Triplets: " << tripletSum(arr) << "\n";
    
    return 0;
}
```
*(💡 **Elite CP Insight:** Because the `occurrences` multiplier is identical for every element, you can optimize this even further by calculating the total sum of the array first, and just multiplying it by `occurrences` once at the very end!)*

## 4. Module Summary
- The **Contribution Technique** is a mathematical paradigm shift. Instead of looping to build structures (subarrays, subsets, combinations), you mathematically calculate how many times a single element *contributes* to those structures.
- For **Subarrays**, an element at index `i` contributes $(i + 1) \times (N - i)$ times.
- For **Combinations/Triplets**, if you lock one element, it contributes $\binom{N-1}{K-1}$ times (where $K$ is the size of the group).
- Always use `long long` for intermediate combinatorial math to prevent silent 32-bit integer overflows!

</READING_WIDGET>
