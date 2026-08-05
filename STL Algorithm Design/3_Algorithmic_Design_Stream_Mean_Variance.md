<VIDEO_WIDGET>

<VIDEO_ID>360</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Algorithmic Design: Stream Mean and Variance

> *In system design and competitive programming, you'll often encounter "Data Stream" problems. Instead of being handed a static array, data arrives continuously in real-time. Let's design a mathematical architecture that tracks the Mean and Variance of an infinite stream in flawless $O(1)$ time!*

---

## 1. The Mathematical Challenge

**The Problem:** For a running stream of integers, support queries to answer the current Mean and Variance.
You must implement the following operations, and they **must** all run in $O(1)$ Time Complexity:
1. `add(int x)`: Add a new number to the running stream.
2. `mean()`: Returns the Mean of all the numbers added till now.
3. `variance()`: Returns the Variance of all the numbers added till now.

If we simply stored all the incoming numbers in a `std::vector` and looped through them every time `mean()` or `variance()` was called, the time complexity would be $O(N)$ per query. For an infinite stream, this would result in an immediate **Time Limit Exceeded (TLE)**. 

To achieve $O(1)$, we must maintain a mathematical **Running State**.

---

## 2. Deriving the Running State

What exactly do we need to store to calculate these values instantly?

### The Mean ($\mu$)
The Mean is simply the sum of all elements divided by the total number of elements.
$\mu = \frac{\sum x_i}{N}$

To answer this in $O(1)$, we only need to maintain two variables:
- `N`: The total count of elements.
- `Sum`: The running sum of all elements ($\sum x_i$).

### The Variance ($\sigma^2$)
The standard mathematical definition of Variance is the average squared deviation from the mean:
$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$

If we tried to use this formula, every time $\mu$ changes (which happens on every single `add`), we would have to recalculate the difference $(x_i - \mu)^2$ for every single past element. That's $O(N)$! 

We must expand and simplify the Variance formula:
$$ \sigma^2 = \frac{\sum (x_i^2 - 2x_i\mu + \mu^2)}{N} $$
$$ \sigma^2 = \frac{\sum x_i^2}{N} - 2\mu \left( \frac{\sum x_i}{N} \right) + \mu^2 $$

Since $\frac{\sum x_i}{N}$ is exactly $\mu$, this beautifully simplifies to:
$$ \sigma^2 = \frac{\sum x_i^2}{N} - 2\mu^2 + \mu^2 $$
$$ \sigma^2 = \frac{\sum x_i^2}{N} - \mu^2 $$

**The Revelation:** To calculate Variance in $O(1)$, we don't need to remember past elements at all! We just need to maintain one additional variable:
- `SqSum`: The running sum of the squares of all elements ($\sum x_i^2$).

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/92e9e427-5db5-44fa-b2c7-c891cb950ae8.jpg" alt="Stream Mean and Variance State" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 3. The Implementation

> 🚨 **The CP Trap: Massive Precision Loss**
> When dealing with squares of large numbers ($\sum x_i^2$), standard integer types will overflow almost instantly. Even `long long` can overflow if the stream is massive. Furthermore, Mean and Variance are strictly decimal values. 
> **You must use `double` or `long double` for your running state variables to preserve precision and prevent overflow!**

```cpp
#include <iostream>
using namespace std;

class StreamTracker {
private:
    double n;
    double sum;
    double sqSum;

public:
    // Initialize the running state
    StreamTracker() {
        n = 0;
        sum = 0;
        sqSum = 0;
    }

    // Time Complexity: O(1)
    void add(int x) {
        double val = (double)x;
        n += 1.0;
        sum += val;
        sqSum += (val * val);
    }

    // Time Complexity: O(1)
    double mean() {
        if (n == 0) return 0.0; // Guard against Division by Zero
        return sum / n;
    }

    // Time Complexity: O(1)
    double variance() {
        if (n == 0) return 0.0; // Guard against Division by Zero
        
        double current_mean = mean();
        // Variance = (Sum of Squares / N) - (Mean * Mean)
        return (sqSum / n) - (current_mean * current_mean);
    }
};

int main() {
    StreamTracker tracker;
    
    tracker.add(10);
    tracker.add(20);
    
    // Mean of [10, 20] is 15
    cout << "Mean: " << tracker.mean() << "\n"; 
    
    // Variance is ((100 + 400)/2) - (15*15) = 250 - 225 = 25
    cout << "Variance: " << tracker.variance() << "\n"; 
    
    return 0;
}
```

### Complexity Breakdown:
*   **Time Complexity:** $O(1)$ for all operations (`add`, `mean`, `variance`). We are only doing basic arithmetic!
*   **Space Complexity:** $O(1)$. No matter if the stream has 10 elements or 10 billion elements, we only ever store exactly three `double` variables.

</READING_WIDGET>
