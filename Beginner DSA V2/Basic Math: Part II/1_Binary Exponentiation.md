<VIDEO_WIDGET>

<VIDEO_ID>3503</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Binary Exponentiation

Imagine you need to calculate $3^{10}$. What is it conceptually? 
It is simply $3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3$.

In many algorithms, you will need to raise a base number $a$ to a power $b$. While this seems mathematically trivial, how you write the code to compute it can mean the difference between your program finishing instantly or timing out completely.

Let's explore how to compute $a^b$ efficiently.

*(Note: We will compute raw exponentiation here. In the next module, we will introduce "modulo arithmetic" which is almost always paired with exponentiation in competitive programming!)*

---

## 1. The Naive Approach $O(b)$

The most obvious way to compute $a^b$ is to write a loop that multiplies $a$ exactly $b$ times.

```cpp
// Time Complexity: O(b)
long long power(long long a, long long b) {
    long long ans = 1;
    for (long long i = 1; i <= b; i++) {
        ans = ans * a;
    }
    return ans;
}
```

*Socratic Question:* What if $b = 10^9$? 
Your loop will run $1,000,000,000$ times, which takes about a full second in C++. What if $b = 10^{18}$? It would take years! We need a much faster way.

---

## 2. The Optimal Approach: Binary Exponentiation $O(\log b)$

Let's look closely at how we calculate $3^{16}$.
Instead of multiplying $3$ by itself 16 times, what if we use the properties of exponents?

We know that $3^{16} = (3^8) \times (3^8)$.
If we already know the value of $3^8$, we can just square it to get $3^{16}$ in exactly **one operation**!

Let's break it down further:
- $3^{16} = (3^8)^2$
- $3^8 = (3^4)^2$
- $3^4 = (3^2)^2$
- $3^2 = (3^1)^2$
- $3^1 = 3$

Instead of 16 multiplications, we only needed **4 multiplications**! This technique is called **Exponentiation by Squaring** or **Binary Exponentiation**.

What if the power is an **odd number**, like $3^{13}$?
We can't perfectly divide 13 by 2. But we can simply peel off one $3$ to make the power even!
$3^{13} = 3 \times 3^{12}$
And now we can halve $12$ exactly as we did before: $3^{12} = (3^6)^2$.

### The Core Logic
If $b = 0$, the answer is always $1$.
If $b$ is **even**, $a^b = (a^{b/2})^2$.
If $b$ is **odd**, $a^b = a \times a^{b-1}$.

---

## 3. Recursive Implementation

Since our logic naturally breaks a large problem into smaller sub-problems, it translates beautifully into a recursive function.

```cpp
// Time Complexity: O(log b)
// Space Complexity: O(log b) due to the call stack
long long powerRecursive(long long a, long long b) {
    // Base Case
    if (b == 0) return 1;
    
    // Calculate the power of half the exponent
    long long halfPower = powerRecursive(a, b / 2);
    
    // If b is even, just square the half power
    if (b % 2 == 0) {
        return halfPower * halfPower;
    } 
    // If b is odd, square it and multiply by an extra 'a'
    else {
        return a * halfPower * halfPower;
    }
}
```

> 💡 **CP Must-Know:** Notice that we stored `powerRecursive(a, b / 2)` in a variable called `halfPower`. A very common beginner mistake is to write `return powerRecursive(a, b/2) * powerRecursive(a, b/2);`. This completely destroys the $O(\log b)$ time complexity and turns it back into $O(b)$ because you are making the exact same recursive call twice!

---

## 4. Iterative Implementation

While the recursive version is elegant, the iterative version is what professional competitive programmers actually use. It is slightly faster because it avoids the overhead of recursive function calls (saving stack memory).

Instead of thinking top-down, we think bottom-up. We continuously square $a$, and whenever the current power $b$ is odd, we multiply our running `ans` by $a$.

```cpp
// Time Complexity: O(log b)
// Space Complexity: O(1)
long long powerIterative(long long a, long long b) {
    long long ans = 1;
    
    while (b > 0) {
        // If b is odd, multiply the current 'a' into our answer
        if (b % 2 != 0) {
            ans = ans * a;
            b = b - 1; // Peel off 1 power (optional, division handles it)
        }
        
        // Square the base for the next step
        a = a * a;
        
        // Halve the power
        b = b / 2;
    }
    
    return ans;
}
```

---

## 5. Edge Cases & "Gotchas"

### Trap 1: Exponential Overflow
Even though $a^b$ is incredibly fast to compute, the *result* of $a^b$ grows monstrously fast. 
For example, $2^{60}$ easily fits into a 64-bit `long long` integer. But $2^{65}$ will immediately overflow and give you garbage values! 

In reality, most competitive programming problems that involve large exponents will ask you to compute $a^b \pmod M$. We will learn exactly how to combine this $O(\log b)$ code with Modular Arithmetic in the very next module!

### Trap 2: $0^0$
Mathematically, $0^0$ is often debated, but in programming and CP, it is universally agreed that `power(0, 0)` should return `1`. Our algorithms safely handle this because if $b = 0$, the loops immediately bypass and return `ans = 1`.

### Trap 3: Negative Exponents and the `INT_MIN` Disaster
If a problem asks for $a^{-b}$, you must mathematically rewrite it as $\frac{1}{a^b}$. This changes the answer from an integer to a floating-point number (`double`). 

> 🚨 **The `INT_MIN` Trap:** If the exponent $b$ is passed as a 32-bit signed `int`, its minimum possible value is `-2147483648`. If you try to make it positive by writing `b = -b`, it exceeds the maximum positive limit (`2147483647`) and overflows! **The Fix:** Always cast the exponent to a 64-bit `long long` before making it positive.

</READING_WIDGET>
