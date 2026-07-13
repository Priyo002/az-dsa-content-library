<VIDEO_WIDGET>

<VIDEO_ID>3506</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Inverse of Modulo

In the previous module, we learned the rules for Addition, Subtraction, and Multiplication. We conspicuously left out Division. Why?

Because in the world of modular arithmetic, **division does not exist**.
You cannot simply say $(a / b) \pmod m = ((a \pmod m) / (b \pmod m)) \pmod m$. It mathematically fails.

Instead of dividing, we do what mathematicians do when they are stuck: we turn the division into multiplication!
Dividing by $b$ is the exact same thing as multiplying by $\frac{1}{b}$.

In modular arithmetic, this $\frac{1}{b}$ is called the **Modular Multiplicative Inverse**.

---

## 1. What is the Modular Inverse?

The modular inverse of an integer $b$ modulo $m$ (denoted as $b^{-1}$) is a number such that when you multiply it by $b$, the remainder is $1$.

$$b \times b^{-1} \equiv 1 \pmod m$$

If we can find this magical number $b^{-1}$, we can solve our division problem instantly:
$$(a / b) \pmod m = (a \times b^{-1}) \pmod m$$

### Existence of the Inverse (The Co-Primality Rule)

Before we try to calculate $b^{-1}$, we must know if it even exists.
Not every number has an inverse! An integer $b$ has a modular inverse modulo $m$ **if and only if $b$ and $m$ are coprime**.

Being coprime means their Greatest Common Divisor (GCD) is exactly 1:
$$\text{gcd}(b, m) = 1$$

If $\text{gcd}(b, m) > 1$, the inverse mathematically does not exist, and division is impossible.

> 💡 **Debunking a Common Myth:** A common misconception is that if $b$ and $m$ share a factor, then $b \% m$ must equal $0$. This is absolutely false! For example, $10$ and $6$ share the factor $2$, but $10 \% 6 = 4$, not $0$. The _true_ mathematical reason inverses fail when they share a factor requires advanced group theory. For competitive programming, simply memorize the ironclad rule: **Inverse exists $\iff \text{gcd}(b, m) = 1$**.

---

## 2. Fermat's Little Theorem (FLT)

So, how do we find $b^{-1}$?
If our modulus $m$ is a prime number (like $10^9 + 7$), we can use one of the most famous theorems in number theory: **Fermat's Little Theorem**.

Fermat's Little Theorem states that if $p$ is a prime number, and $b$ is an integer not divisible by $p$, then:
$$b^{p-1} \equiv 1 \pmod p$$

_Example:_ If $p=5$ and $b=2$:
$2^{5-1} \Rightarrow 2^4 = 16$. And $16 \equiv 1 \pmod 5$. It works!

### Deriving the Inverse

Let's take Fermat's equation and do some basic algebra. We know:
$$b^{p-1} \equiv 1 \pmod p$$

If we physically split one $b$ away from the exponent, we get:
$$b \times b^{p-2} \equiv 1 \pmod p$$

Look closely at this equation. It perfectly matches the definition of our modular inverse ($b \times b^{-1} \equiv 1 \pmod p$)!
Therefore, we have just magically discovered the formula for the modular inverse:

$$b^{-1} \equiv b^{p-2} \pmod p$$

---

## 3. Writing the Code: Modular Division

To divide $a$ by $b$ modulo $p$, we simply calculate $a \times b^{p-2} \pmod p$.
And how do we calculate $b^{p-2}$? We use the exact $O(\log N)$ **Modular Binary Exponentiation** function we wrote in the last module!

```cpp
// 1. O(log b) Exponentiation function from the previous module
long long powerModulo(long long base, long long exp, long long mod) {
    long long ans = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 != 0) ans = (ans * base) % mod;
        base = (base * base) % mod;
        exp = exp / 2;
    }
    return ans;
}

// 2. Finding the Inverse
long long modInverse(long long b, long long m) {
    // Using Fermat's Little Theorem: b^(m-2) % m
    return powerModulo(b, m - 2, m);
}

// 3. Performing Modular Division
long long modDivide(long long a, long long b, long long m) {
    a = a % m;
    long long inv = modInverse(b, m);
    return (a * inv) % m; // Multiply by inverse and modulo!
}
```

> 💡 **CP Must-Know:** Using FLT to find the inverse ($b^{p-2}$) only works if $p$ is prime. This is exactly why competitive programming platforms almost universally use $10^9 + 7$! Because it is prime, you are guaranteed that every single number from $1$ to $10^9+6$ is coprime to it, meaning you can safely divide by any valid number using Fermat's Little Theorem!

_(Note: If a problem ever gives you a modulus $m$ that is **not prime**, you cannot use Fermat's Little Theorem. You must find the inverse using an advanced mathematical technique called the **Extended Euclidean Algorithm**, which we will cover in the Intermediate Mathematics section later on)._

</READING_WIDGET>
