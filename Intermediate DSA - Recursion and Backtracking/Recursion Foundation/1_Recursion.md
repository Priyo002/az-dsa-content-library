<VIDEO_WIDGET>

<VIDEO_ID>3626</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Recursion Foundation

Recursion is one of the most important ways of expressing a solution in programming. It allows us to describe a large problem using smaller versions of the same problem.

At the simplest level:

> **Recursion is a process in which a function calls itself.**

However, merely calling the same function again is not enough. A correct recursive solution must also know:

1. when to stop;
2. how the current problem becomes smaller; and
3. how the answer to the smaller problem helps solve the current problem.

In this lesson, we will learn how to visualize recursive execution and how to recognize the different ways in which recursion can be used to design algorithms.

---

## 1. What Is Recursion?

Suppose a function is responsible for solving a problem of size $n$. Instead of solving the entire problem directly, it may ask the same function to solve a smaller problem such as size $n-1$.

This produces a chain of related function calls:

```text
solve(n)
  asks solve(n - 1)
    asks solve(n - 2)
      ...
```

Every recursive function needs two parts.

### Base case

The **base case** is a problem small enough to answer directly. It stops the recursion.

### Recursive case

The **recursive case** expresses the current answer using one or more smaller recursive calls.

A useful way to think about a recursive function is:

```text
Answer for the current problem
=
work done now
+
answer or answers from smaller problems
```

The recursive calls must make progress toward the base case. Otherwise, the function will keep creating new calls until the program runs out of stack space.

> 💡 **Interview Insight:** Interviewers usually care less about whether you remember recursive syntax and more about whether you can define what the function means. State the function's responsibility, its base case, and why every recursive call moves toward that base case before writing code.

---

## 2. How to Visualize Recursion Better

Recursion can be understood in three complementary ways:

1. intuition from the code;
2. a recursion tree; and
3. the recursion stack.

Each view answers a different question.

| View | What it helps us understand |
|---|---|
| **Intuition-based view** | The mathematical or logical relation between the current problem and smaller problems |
| **Recursion tree** | Every recursive call generated during the complete execution |
| **Recursion stack** | Which function calls are active at one particular moment |

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/b72003ee-5668-4c5d-911a-9a6e9e55d9ec.png" alt="Three ways to visualize recursion: intuition, recursion tree, and recursion stack" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### 2.1 Intuition-based visualization

Some recurrences can be understood almost directly from their definitions.

For example, the Fibonacci sequence is defined as:

$$
F(n) =
\begin{cases}
n, & n \le 1 \\
F(n-1) + F(n-2), & n > 1
\end{cases}
$$

The definition tells us exactly what to code:

- if $n$ is $0$ or $1$, return $n$;
- otherwise, calculate the previous two Fibonacci values and add them.

This method works well when the recurrence itself clearly describes the solution.

### 2.2 Recursion-tree visualization

A **recursion tree** displays every recursive call as a node.

- The first call is the root.
- Its recursive calls are its children.
- Calls that reach a base case are leaves.
- The edges show which call created which smaller call.

The tree helps us understand:

- how the problem branches;
- how many calls are generated;
- where base cases occur; and
- whether the same smaller problem is solved repeatedly.

### 2.3 Recursion-stack visualization

The **recursion stack** displays only the function calls that are currently active.

Whenever a function is called, a new stack frame is created. That frame stores information such as:

- the function parameters;
- local variables; and
- the point to which execution must return.

When the function finishes, its frame is removed and execution continues inside the function that called it.

> **Recursion tree versus recursion stack:** The tree represents all calls made during the complete execution. The stack represents only one currently active path through that tree.

> 💡 **Interview Insight:** Do not use recursion depth as the time complexity. Time depends on the total number of calls in the recursion tree, while auxiliary space depends on the maximum number of simultaneously active stack frames. A recursion may make exponentially many calls while using only linear stack space.

> 🚨 **The Systems Trap: The Call Stack Is Finite**
>
> Every active recursive call consumes space for a stack frame. The process stack is separate from the dynamic storage used by objects such as a vector's element buffer, and it is usually much smaller.
>
> On Linux, `RLIMIT_STACK` controls the maximum process-stack size; reaching it raises `SIGSEGV`. Many Linux environments use a limit around 8 MiB, but the actual value is platform- and judge-dependent. The maximum safe recursion depth also depends on the size of each frame, so $10^5$ calls is a warning scale—not a universal safe cutoff.
>
> For a potentially deep $O(N)$ traversal, inspect the constraints. Prefer an iterative solution or an explicit stack when $N$ can approach $10^5$ or more, especially if each call has large local variables. See the [Linux `RLIMIT_STACK` documentation](https://man7.org/linux/man-pages/man2/getrlimit.2.html) for the system-level behavior.

### 2.4 Tail Recursion and Tail Call Optimization

A function is **tail-recursive** when its recursive call is the final operation on that execution path. After the recursive call returns, the current function has no pending calculation left to perform.

For example:

```cpp
long long sumTail(int n, long long answer) {
    if (n == 0) {
        return answer;
    }

    return sumTail(n - 1, answer + n);
}
```

The recursive call is returned directly. Its caller does not need the current stack frame to perform more work afterward.

This version is not tail-recursive:

```cpp
long long sumNotTail(int n) {
    if (n == 0) {
        return 0;
    }

    return n + sumNotTail(n - 1);
}
```

The addition by `n` is still waiting after `sumNotTail(n - 1)` returns, so the current frame must remain active.

### What Tail Call Optimization can do

When a compiler performs **Tail Call Optimization (TCO)**, it may reuse the current frame or turn the final call into a jump. In that compiled program, a linear tail recursion can run with constant stack space.

GCC provides `-foptimize-sibling-calls` for sibling and tail-recursive calls and enables it at optimization levels such as `-O2`, `-O3`, and `-Os`. See the [GCC optimization documentation](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#index-foptimize-sibling-calls).

However:

- the C++ language does **not** guarantee Tail Call Optimization;
- optimization settings, target architecture, calling conventions, debugging, and function details can affect whether it is applied; and
- a recursive call being in tail position makes optimization possible, not mandatory.

Therefore, do not depend on TCO to pass a recursion-depth constraint. If constant auxiliary space is required, write the loop explicitly:

```cpp
long long sumIterative(int n) {
    long long answer = 0;

    while (n > 0) {
        answer += n;
        n--;
    }

    return answer;
}
```

> 💡 **Interview Insight:** Mentioning tail recursion shows useful systems knowledge, but claiming that it is automatically $O(1)$ space in C++ is unsafe. Analyze it as $O(N)$ stack space unless TCO is known to occur; use an iterative implementation when the space guarantee matters.

---

## 3. How to Design Recursive Solutions Better

Before writing code, define the responsibility of the recursive function in one sentence.

For example:

> `fib(n)` returns the nth Fibonacci number.

> `isPalindrome(left, right)` returns whether the substring from `left` to `right` is a palindrome.

> `move(n, from, to, aux)` moves the top `n` disks from rod `from` to rod `to`, using rod `aux` as temporary storage.

Once the meaning is clear, answer these questions:

1. **State:** What information completely describes the current problem?
2. **Base case:** Which state can be answered immediately?
3. **Transition:** Which smaller recursive call or calls are required?
4. **Combination:** How are the smaller answers used to produce the current answer?

> 💡 **Interview Insight:** A strong recursive explanation begins with a sentence such as “`solve(state)` returns ...”. This recursive contract makes the base case and transition easier to verify and gives the interviewer a clear correctness argument.

In this course, recursive designs will be organized into four broad directions.

### 3.1 Recursion-based or Divide and Conquer

The current problem is reduced to one or more smaller problems, and their answers are used to construct the current answer.

Examples include:

- Fibonacci recurrence;
- binary search;
- merge sort; and
- inversion counting.

In Divide and Conquer, the subproblems are usually independent, and their answers are combined after the recursive calls return.

### 3.2 Backtracking

The function tries multiple choices while building a valid solution. If one choice cannot lead to an answer, the function returns and tries another choice.

The later Backtracking section will organize this process using **LCCM**:

- **Level** — which decision is being made;
- **Choice** — which options can be tried;
- **Check** — whether an option is currently valid; and
- **Move** — apply the option, recurse, and restore shared state when necessary.

### 3.3 Kth Generation or Kth Form

Sometimes we do not want to generate every valid solution. We want only the kth solution in a particular order.

The recursive search can count how many solutions belong to a branch and skip that entire branch when the kth answer is not inside it.

We will later study this form through the problem of finding the kth move in Tower of Hanoi.

### 3.4 Fractals

A fractal is formed by repeatedly applying the same construction at a smaller scale. Recursion is a natural way to describe this self-similarity.

At each level, the same rule creates smaller copies or regions until the required depth is reached.

These four directions will be explored in detail throughout the Recursion and Backtracking course. At this stage, the goal is to recognize that recursive functions can represent different kinds of problem structures.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/ba5d48c4-e8d5-4ad6-81ce-8276d12995a4.png" alt="Four recursive design directions: Divide and Conquer, Backtracking LCCM, Kth Form, and Fractals" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 4. Fibonacci Through a Recursion Tree

Consider the following recursive implementation:

```cpp
int fib(int n) {
    if (n <= 1) { // Base case
        return n;
    }

    // Recursive case
    return fib(n - 1) + fib(n - 2);
}
```

The function follows the Fibonacci recurrence directly.

### Meaning of the function

> `fib(n)` returns the nth Fibonacci number.

### Base case

When $n$ is $0$ or $1$, the answer is simply $n$.

### Recursive case

When $n > 1$, the answer is the sum of the previous two Fibonacci values:

$$
F(n) = F(n-1) + F(n-2)
$$

For `fib(5)`, the recursion begins like this:

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2)
│   │   │   ├── fib(1)
│   │   │   └── fib(0)
│   │   └── fib(1)
│   └── fib(2)
│       ├── fib(1)
│       └── fib(0)
└── fib(3)
    ├── fib(2)
    │   ├── fib(1)
    │   └── fib(0)
    └── fib(1)
```

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/7231a766-cc98-4b16-8283-70dde403be66.png" alt="Fibonacci recursion tree showing repeated computation of the same states" style="max-width: 100%; height: auto;" identifier="az-img-upload">

The leaf calls `fib(0)` and `fib(1)` return immediately. Their values are then added while the recursive calls return upward.

The tree also reveals that calls such as `fib(3)` and `fib(2)` are evaluated more than once. Therefore, this direct implementation is useful for understanding recursion, but it is not an efficient way to calculate large Fibonacci numbers.

> 💡 **Interview Insight:** Repeated calls with the same parameters are a signal to consider memoization or Dynamic Programming. Before optimizing, identify the state—in this example, the state is only `n`—and cache the answer for each distinct state.

Use the [VisuAlgo Recursion Tree visualizer](https://visualgo.net/en/recursion) with a small value such as $5$ to observe:

- the call created at every node;
- the order in which the tree is explored;
- which nodes are base cases; and
- how returned values move upward.

> Use small inputs when visualizing a branching recurrence. The number of calls grows quickly.

---

## 5. Fibonacci Through the Recursion Stack

Now consider the same function inside a complete C++ program:

```cpp
#include <bits/stdc++.h>
using namespace std;

int fib(int x) {
    if (x <= 1) {
        return x;
    }

    return fib(x - 1) + fib(x - 2);
}

int main() {
    fib(5);
    return 0;
}
```

We can use the [Python Tutor C++ visualizer](https://pythontutor.com/cpp.html#mode=edit) to inspect the active stack frames.

For the purpose of a hand trace, suppose `fib(x - 1)` is explored first. The stack initially grows along this path:

```text
fib(5)
fib(4)
fib(3)
fib(2)
fib(1)  ← base case
```

At this moment, five calls are active. When `fib(1)` returns, its frame is removed. Execution resumes inside `fib(2)`, which still needs the result of `fib(0)`.

After `fib(0)` returns, `fib(2)` can calculate:

$$
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
$$

Its frame is then removed, and the returned value is received by `fib(3)`. This process continues until the initial call `fib(5)` receives both of its required answers.

The most important observations are:

- every function call has its own value of `x`;
- a function can pause while waiting for another recursive call;
- the deepest active path determines the maximum stack depth; and
- returned values travel back in the reverse order of active calls.

For Fibonacci, the recursion tree contains many calls, but the maximum stack depth is only proportional to $n$. Total calls and maximum active calls are different measurements.

---

## 6. Recursion Examples

The following examples demonstrate different ways to define a recursive state and use work before or after the recursive call.

### 6.1 Check whether a string is a palindrome

A string is a palindrome when it reads the same from left to right and right to left.

Instead of reversing the complete string, compare the two outer characters. If they match, recursively check the substring between them.

Define:

> $P(l,r)$ is true when the substring from index $l$ to index $r$ is a palindrome.

The recurrence is:

$$
P(l,r) =
\begin{cases}
\text{true}, & l \ge r \\
\text{false}, & s[l] \ne s[r] \\
P(l+1,r-1), & s[l] = s[r]
\end{cases}
$$

```cpp
bool isPalindrome(const string& s, int left, int right) {
    if (left >= right) {
        return true;
    }

    if (s[left] != s[right]) {
        return false;
    }

    return isPalindrome(s, left + 1, right - 1);
}
```

The initial call for a non-empty string is:

```cpp
isPalindrome(s, 0, static_cast<int>(s.size()) - 1);
```

Every recursive call moves both boundaries inward, so the problem becomes smaller.

> 💡 **Interview Insight:** Passing the string by `const` reference and moving indices is preferable to creating a new substring at every call. Repeated substring copies can silently increase both time and memory usage.

---

### 6.2 Calculate $\binom{n}{r}$ using recursion

To choose $r$ elements from $n$ elements, consider one particular element.

- Do not choose it: choose all $r$ elements from the remaining $n-1$ elements.
- Choose it: choose the remaining $r-1$ elements from the remaining $n-1$ elements.

Therefore:

$$
\binom{n}{r} = \binom{n-1}{r} + \binom{n-1}{r-1}
$$

The base cases are:

$$
\binom{n}{0} = 1
\qquad\text{and}\qquad
\binom{n}{n} = 1
$$

```cpp
long long nCr(int n, int r) {
    if (r < 0 || r > n) {
        return 0;
    }

    if (r == 0 || r == n) {
        return 1;
    }

    return nCr(n - 1, r) + nCr(n - 1, r - 1);
}
```

This recursion creates two choices—take the selected element or do not take it. Like Fibonacci, the direct implementation may calculate the same states repeatedly, but it clearly demonstrates how a combinatorial recurrence becomes recursive code.

> 💡 **Interview Insight:** The pair `(n, r)` completely identifies an $nCr$ subproblem. If the constraints are too large for direct recursion, memoize this pair or build Pascal's triangle iteratively. Always compare the recursive state count with the input constraints.

---

### 6.3 Print $n, n-1, \ldots, 1, 2, \ldots, n-1, n$

For example, when $n=5$, print:

```text
5 4 3 2 1 2 3 4 5
```

The key is to print once before the recursive call and once after it returns.

```cpp
void printPattern(int n) {
    cout << n << " ";

    if (n == 1) {
        return;
    }

    printPattern(n - 1);

    cout << n << " ";
}
```

The first `cout` runs while recursion moves downward:

```text
n, n-1, n-2, ..., 1
```

The second `cout` runs while calls return upward:

```text
2, 3, ..., n-1, n
```

The value $1$ is printed only once because the base-case call returns before reaching the second `cout`.

> 💡 **Interview Insight:** Moving an operation from before the recursive call to after it often reverses the processing order. This same idea appears in tree traversals: preorder performs work before child calls, while postorder performs work after them.

---

### 6.4 Tower of Hanoi

Tower of Hanoi contains three rods and $n$ disks of different sizes. Initially, all disks are on the source rod, arranged with the largest disk at the bottom.

The goal is to move every disk to the destination rod while following these rules:

1. Move only one disk at a time.
2. Move only the top disk of a rod.
3. Never place a larger disk on top of a smaller disk.

You can experiment with these rules using the [Tower of Hanoi interactive puzzle](https://www.mathsisfun.com/games/towerofhanoi.html).

### Define the recursive function

> `move(n, from, to, aux)` moves the top `n` disks from rod `from` to rod `to`, using rod `aux` as temporary storage.

To move $n$ disks:

1. Move the top $n-1$ disks from `from` to `aux`.
2. Move the largest remaining disk from `from` to `to`.
3. Move the $n-1$ disks from `aux` to `to`.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/ac204690-5e12-476f-abe4-ba5e30d4d92d.png" alt="The three recursive steps for solving Tower of Hanoi" style="max-width: 100%; height: auto;" identifier="az-img-upload">

```cpp
void move(int n, int from, int to, int aux) {
    if (n == 1) {
        cout << from << " -> " << to << '\n';
        return;
    }

    move(n - 1, from, aux, to);

    cout << from << " -> " << to << '\n';

    move(n - 1, aux, to, from);
}
```

For three disks, the initial call can be:

```cpp
move(3, 1, 3, 2);
```

The function first solves a smaller Tower of Hanoi problem for $n-1$ disks. After moving the largest disk, it solves another problem of size $n-1$.

If $M(n)$ is the number of moves required for $n$ disks, then:

$$
M(n) = 2M(n-1) + 1
$$

with:

$$
M(1) = 1
$$

This produces:

$$
M(n) = 2^n - 1
$$

Tower of Hanoi is especially useful because the same recursive structure can later be revisited in **Kth Form**, where we find a particular move without generating every earlier move.

> 💡 **Interview Insight:** When only the kth generated action is required, avoid producing all earlier actions. Tower of Hanoi has predictable subtree sizes, so complete recursive branches can be counted and skipped—a pattern that also appears in kth permutation and kth valid-sequence problems.

---

## 7. What to Take Away

When reading or designing a recursive function, do not focus only on the fact that it calls itself. Ask:

1. What does the function promise to compute or perform?
2. What is its base case?
3. How does each call move toward that base case?
4. Does it make one recursive call or branch into several calls?
5. What work happens before recursion?
6. What work happens after recursion returns?
7. Am I looking at the complete recursion tree or only the active recursion stack?

The examples in this lesson illustrate several recurring ideas:

- Fibonacci demonstrates a branching recurrence.
- Palindrome checking moves two boundaries inward.
- $\binom{n}{r}$ models take-or-not-take choices.
- The printing pattern demonstrates work before and after recursion.
- Tower of Hanoi solves two smaller problems around one central move.

These ideas form the foundation for Brute Force, the LCCM Backtracking Framework, Kth Form, Divide and Conquer, and Fractal Form.

</READING_WIDGET>
