<VIDEO_WIDGET>

<VIDEO_ID>3569</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

<READING_WIDGET>

# STL Algorithms: Random & Shuffling

> _Welcome to the `<random>` library! In Competitive Programming, you will often need to generate random test cases, randomize QuickSort pivots to avoid $O(N^2)$ worst cases, or randomize array states. Let's learn how to do this safely and efficiently using modern C++._

---

## 1. The Problem with Legacy `rand()`

If you search the internet for "how to generate a random number in C++," you will almost certainly find old tutorials telling you to use `rand() % N`. **Do not do this in Competitive Programming!**

The legacy `rand()` function (inherited from C) has three massive flaws:

1. **Low Maximum Limit:** On many compilers, `rand()` can only generate numbers up to `32767`. If you try to generate a random array index of size $10^5$, it will literally be impossible to reach the end of the array!
2. **Modulo Bias:** Doing `rand() % N` mathematically favors smaller numbers. It is not perfectly uniform.
3. **Predictability:** It uses a weak algorithm (Linear Congruential Generator) that can easily be "hacked" on platforms like Codeforces.

Modern C++ provides the `<random>` library to solve all these issues.

---

## 2. The Mersenne Twister (`mt19937`)

To generate true, robust random numbers, C++ gives us the **Mersenne Twister** algorithm, accessed via `std::mt19937`.

Just like a real-world machine, a random number generator needs a "seed" (a starting value) to kickstart its calculations. If you give it the same seed every time, it will generate the exact same sequence of random numbers! To ensure we get fresh numbers every run, we use `std::random_device` as our seed.

```cpp
#include <iostream>
#include <random> // Required for modern randomness
using namespace std;

int main() {
    // 1. Create a "True Random" device to get a fresh, unpredictable seed
    random_device rd;

    // 2. Initialize the Mersenne Twister generator using that seed
    mt19937 rng(rd());

    // 3. Generate a massive 32-bit random number!
    cout << "Random Number: " << rng() << "\n";

    return 0;
}
```

> 💡 **CP Insight: Need a `long long`?**
> Standard `mt19937` only generates 32-bit integers. If you are doing advanced randomized algorithms (like String Hashing with massive primes) and need massive 64-bit random numbers, C++ provides a dedicated 64-bit generator! Just append `_64` to the type:
> `mt19937_64 rng(seed);`

---

## 3. Generating Random Numbers in a Range

Now that we have a powerful generator (`rng`), we usually want to restrict its output to a specific range, like picking a random index between $0$ and $N-1$, or simulating a dice roll between $1$ and $6$.

Instead of using the flawed modulo (`%`) operator, we use `std::uniform_int_distribution`.

```cpp
#include <iostream>
#include <random>
using namespace std;

int main() {
    random_device rd;
    mt19937 rng(rd());

    // Define a perfectly uniform distribution from 1 to 6 (inclusive)
    uniform_int_distribution<int> dist(1, 6);

    // Pass our generator into the distribution to "roll the dice"
    for (int i = 0; i < 5; i++) {
        cout << "Dice Roll: " << dist(rng) << "\n";
    }

    return 0;
}
```

---

## 4. Shuffling Arrays (`std::shuffle`)

If you want to perfectly scramble a vector into a random permutation, C++ provides `std::shuffle`. It runs in exactly $O(N)$ time.

> 🚨 **The CP Trap: `random_shuffle` is DEAD!**
> Before C++17, competitive programmers used `std::random_shuffle(v.begin(), v.end())`. However, because it relied on the terrible legacy `rand()` function, the C++ Standards Committee **permanently deleted it** from the language! If you submit code using `random_shuffle` on a modern CP judge, you will get a **Compilation Error**. You MUST use `std::shuffle` and pass it your `mt19937` generator!

```cpp
#include <iostream>
#include <vector>
#include <random>
#include <algorithm> // Required for shuffle
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5};

    random_device rd;
    mt19937 rng(rd());

    // Perfectly scramble the array using our generator!
    shuffle(v.begin(), v.end(), rng);

    for (int x : v) cout << x << " ";
    cout << "\n";

    return 0;
}
```

---

## 5. 💡 The Codeforces Seed Trick

On some online judges (specifically Codeforces running on Windows servers), `std::random_device` is fundamentally broken. It acts completely deterministically, meaning your "random" numbers will be the exact same every single time the judge runs your code! This allows malicious users to hack your solution by generating test cases that force your code into $O(N^2)$ worst-case scenarios.

**The Fix:** Instead of relying on `random_device`, you should seed your generator using the system's high-precision clock! Since the exact nanosecond the code executes will always be different, the seed is completely unhackable.

```cpp
#include <iostream>
#include <random>
#include <chrono> // Required for the clock
using namespace std;

int main() {
    // Obtain the exact number of nanoseconds since the UNIX epoch
    long long seed = chrono::steady_clock::now().time_since_epoch().count();

    // Seed the generator using the clock!
    mt19937 rng(seed);

    cout << "Unhackable Random Number: " << rng() << "\n";

    return 0;
}
```

_Tip: Always use this `chrono` trick when competing on Codeforces!_

---

## 6. Practice Problem: Pick Random Element (Easy)

**The Problem:** You are given an array of names representing a group of students. Write a program to randomly select a winner. Every student must have an exact, mathematically equal chance of winning.
**The Direct Application:** Instead of complex class-based shuffling, this problem tests the absolute core of randomness: generating a perfectly uniform index!

**How does randomness work under the hood? (For Interviews):**
If you ever use `std::shuffle` in an interview, the interviewer will ask you how it works. Under the hood, C++ uses the **Fisher-Yates (or Knuth) Shuffle** algorithm to guarantee a perfectly uniform distribution in exactly $O(N)$ time:

1. Start from the last element (index $i = N - 1$).
2. Pick a random index $j$ between $0$ and $i$ (inclusive).
3. Swap the element at $i$ with the element at $j$.
4. Decrement $i$ and repeat until you reach the front of the array.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/58e3c97d-c019-4b0a-9309-a7c6b9b9053b.jpg" alt="Fisher-Yates Shuffle Algorithm Diagram" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### The Code (C++)

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <chrono>
using namespace std;

int main() {
    vector<string> students = {"Alice", "Bob", "Charlie", "David", "Eve"};

    // 1. Initialize our hacker-proof generator
    long long seed = chrono::steady_clock::now().time_since_epoch().count();
    mt19937 rng(seed);

    // 2. We want a random index from 0 to N-1
    int n = students.size();
    uniform_int_distribution<int> dist(0, n - 1);

    // 3. Roll the dice to pick a winner!
    int winning_index = dist(rng);

    cout << "The winner is: " << students[winning_index] << "!\n";

    return 0;
}
```

---

> 🚀 **Next Up:** You've mastered manipulating data! Next, we will dive into an incredibly powerful class of algorithms that can mathematically summarize entire arrays and sequences. Let's move on to the **Numeric Algorithms** (`accumulate`, `gcd`, `lcm`)!

</READING_WIDGET>
