<VIDEO_WIDGET>

<VIDEO_ID></VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Greedy Team Selection: Sorting, Exchange Arguments, and a Heap

> *Choosing the people with the highest individual scores does not always produce the best team. When a team's score combines a sum with its slowest member's speed, every selection affects two quantities. We will fix the minimum speed first, then use an exchange argument to choose the remaining members.*

## 1. Problem Statement

There are `n` people. Person `i` has:

- Speed $s_i$.
- Efficiency $e_i$.

Choose **exactly `k` distinct people** to maximize:

$$
\boxed{\text{TeamScore}
=\left(\sum_{i\in\text{team}}e_i\right)
\left(\min_{i\in\text{team}}s_i\right).}
$$

Use these constraints:

- $1\le k\le n\le 10^5$.
- $1\le s_i,e_i\le 10^9$.
- Each person can be selected at most once.

The score uses **the sum of efficiencies multiplied by the minimum speed**. Keep these roles consistent throughout the solution.

The source program reads each person as `efficiency speed`. We will preserve that input order, even though we sort by speed internally.

### The Lecture Example

| Person | Speed | Efficiency |
| --- | --- | --- |
| 1 | 3 | 7 |
| 2 | 2 | 10 |
| 3 | 5 | 7 |

We must choose `k = 2` people.

| Team | Sum of efficiencies | Minimum speed | Score |
| --- | --- | --- | --- |
| `{1, 2}` | 17 | 2 | 34 |
| `{1, 3}` | 14 | 3 | 42 |
| `{2, 3}` | 17 | 2 | 34 |

The answer is **42**, achieved by people `1` and `3`.

The highest-efficiency person is excluded because their lower speed reduces the multiplier for the entire team.

## 2. Why Simple Rankings Fail

### Pick the Largest Efficiencies?

In the running example, including efficiency `10` gives a team score of only `34`. A smaller sum of efficiencies gives the larger answer because its minimum speed is higher.

### Pick the Largest Speeds?

Consider `k = 2`:

| Person | Speed | Efficiency |
| --- | --- | --- |
| A | 10 | 1 |
| B | 9 | 1 |
| C | 8 | 100 |

The two fastest people give:

$$
(1+1)\cdot9=18.
$$

Choosing `A` and `C` gives:

$$
(1+100)\cdot8=808.
$$

Sorting by speed alone cannot decide which people to keep.

### Pick the Largest Individual Products?

For `k = 2`, consider `(speed, efficiency)` pairs:

```text
A = (100, 2)   individual product = 200
B = (2, 60)    individual product = 120
C = (1, 110)   individual product = 110
```

The individual-product rule selects `A` and `B`, scoring `124`. The best team is `B` and `C`, scoring `170`.

Individual products do not capture how the minimum speed applies to the efficiencies of **all** selected people.

The lesson is to simplify the objective before trying to invent a ranking.

## 3. Fix the Member Who Determines the Minimum

Every valid team has a person whose speed equals the team's minimum speed.

Suppose we fix that person as `i`. Then:

- Person `i` must be selected.
- Every other selected person must have speed at least `s[i]`.
- The multiplier becomes the fixed value `s[i]`.

The remaining task is to maximize:

$$
e_i+\sum_{j\in\text{other members}}e_j.
$$

Since exactly `k` people are required, we need the largest `k - 1` efficiencies among eligible companions.

This is the central transformation:

> Fix the person establishing the minimum speed. Then maximize an efficiency sum among the people who can accompany them.

## 4. Why the Largest Eligible Efficiencies Are Optimal

Fix person `i` and a set of eligible companions.

Suppose our team contains a companion with efficiency `a`, but leaves out an eligible person with efficiency `b > a`.

Exchange those two people:

- The team still has exactly `k` members.
- The fixed person `i` remains selected.
- Every companion still has speed at least `s[i]`.
- The team's minimum speed stays exactly `s[i]`.

The change in score is:

$$
s_i(b-a)>0.
$$

Thus a team omitting a larger eligible efficiency in favor of a smaller one cannot be optimal for this fixed person.

Repeating such exchanges leaves the largest `k - 1` eligible efficiencies. Ties can be resolved arbitrarily because exchanging equal efficiencies does not change the score.

This is a **selection exchange argument**: we exchange a selected item with an unselected item, rather than swapping their positions in an ordering.

## 5. Use Sorting to Make Eligibility Easy

Sort all people by **nonincreasing speed**:

$$
s_1\ge s_2\ge\cdots\ge s_n.
$$

While processing person `i`, every earlier person has speed at least `s[i]`.

We will consider teams where person `i` is the **last selected person in this sorted order**. Such a team consists of:

1. The current person `i`.
2. Exactly `k - 1` people from the earlier prefix.

The current person's speed is then the team's minimum speed.

For each `i`, if enough earlier people exist, evaluate:

$$
\text{candidate}_i
=s_i\left(e_i+\text{sum of the largest }k-1
\text{ efficiencies before }i\right).
$$

### Why Looking Only at Earlier People Is Enough

Take any valid team and choose its last member in the sorted order. All its other members occur earlier. Therefore, that team belongs to one of the cases our scan considers.

This remains true when speeds tie. Fix any order among equal-speed people and choose the last team member in that order. We do not need to process equal speeds as a separate batch.

## 6. Maintain the Best `k - 1` Values with a Min-Heap

As the prefix grows, we need to maintain its largest `k - 1` efficiencies and their sum.

Use a **min-heap**:

- It stores the efficiencies we currently keep.
- Its top is the smallest retained efficiency.
- If inserting a value makes the heap too large, remove that smallest value.

Why a min-heap? Among the retained values, the smallest is the first one we should discard when a better value arrives.

### The Invariant

Immediately before evaluating the current person:

> The heap contains the largest `min(k - 1, number of earlier people)` efficiencies from the earlier prefix, and `sum` equals their total.

For each person:

1. If the heap contains `k - 1` values, evaluate the team made of those companions and the current person.
2. Insert the current efficiency for use by later people.
3. Add it to `sum`.
4. If the heap size exceeds `k - 1`, subtract and remove its smallest value.

The update preserves the invariant: after one new value is added, removing the smallest from an oversized set leaves the largest `k - 1` values of the extended prefix.

### Why Evaluate Before Inserting?

The heap must contain only **earlier** people when we build the candidate. The current person is added separately.

Inserting first and also adding the current efficiency separately could count the same person twice.

### What Happens When `k = 1`?

We need zero companions. The heap is empty when each candidate is evaluated:

$$
\text{candidate}_i=s_i e_i.
$$

After insertion, the value is immediately removed to restore capacity zero. The same code naturally handles this boundary case.

## 7. Dry Run on the Lecture Example

After sorting by decreasing speed:

| Processing order | Original person | Speed | Efficiency |
| --- | --- | --- | --- |
| 1 | 3 | 5 | 7 |
| 2 | 1 | 3 | 7 |
| 3 | 2 | 2 | 10 |

Since `k = 2`, we keep the largest **one** earlier efficiency.

| Current person | Heap before evaluation | Candidate | Best score | Heap after update |
| --- | --- | --- | --- | --- |
| Person 3: `(5, 7)` | `[]` | Not enough companions | 0 | `[7]` |
| Person 1: `(3, 7)` | `[7]` | $(7+7)\cdot3=42$ | 42 | `[7]` |
| Person 2: `(2, 10)` | `[7]` | $(7+10)\cdot2=34$ | 42 | `[10]` |

The final answer is **42**.

The table writes heap contents in sorted order for readability; the internal heap representation need not be fully sorted.

## 8. Full Correctness Proof

We need to justify both the maintained heap and the candidates considered by the scan.

### Lemma 1: The Heap Gives the Best Companions

Before each evaluation, the heap stores the largest `k - 1` efficiencies among earlier people, or all earlier efficiencies if fewer are available.

This is true initially because the prefix is empty. Inserting a new efficiency and removing the smallest when the capacity is exceeded preserves the property.

By the exchange argument, these companions maximize the efficiency sum for the current fixed member.

### Lemma 2: Every Evaluated Candidate Is a Valid Team

We evaluate only when the heap contains exactly `k - 1` earlier people. Adding the current person gives exactly `k` distinct members.

All companions have speed at least the current speed, so the minimum speed is exactly the current speed. Therefore, the computed product is the actual score of that team.

### Lemma 3: An Optimal Team Is Covered

Take an optimal team and let `j` be its last member in sorted order.

- Its other `k - 1` members are in the earlier prefix.
- Its minimum speed is `s[j]`.
- Our heap's companion sum is at least the sum of those `k - 1` members.

When we process `j`, our candidate therefore has score at least that optimal team's score.

But every candidate is a valid team and cannot exceed the global optimum. Hence the best candidate equals the optimum.

> **Interview Insight:** Separate the two reasons this works: sorting makes the current person a valid minimum-speed member, and the exchange argument makes the heap's companions optimal for that person.

## 9. C++ Implementation

**Input:** `n k`, followed by `n` lines containing `efficiency speed`.

**Output:** the maximum score of a team containing exactly `k` people.

The efficiency sum is at most $10^{14}$ and fits in `long long`. Multiplying it by a speed as large as $10^9$ can produce $10^{23}$, so the result uses the GCC/Clang `__int128` extension.

```cpp
#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

using i128 = __int128_t;

struct Person {
    long long efficiency;
    long long speed;
    int id;
};

void printInt128(i128 value) {
    if (value == 0) {
        cout << '0';
        return;
    }
    string digits;
    while (value > 0) {
        digits.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(digits.begin(), digits.end());
    cout << digits;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<Person> people(n);
    for (int i = 0; i < n; ++i) {
        cin >> people[i].efficiency >> people[i].speed;
        people[i].id = i + 1;
    }

    sort(people.begin(), people.end(),
         [](const Person& a, const Person& b) {
             if (a.speed != b.speed) return a.speed > b.speed;
             return a.id < b.id;
         });

    priority_queue<long long, vector<long long>, greater<long long>> best;
    long long sum = 0;
    i128 answer = 0;
    int companionCount = k - 1;

    for (const Person& person : people) {
        // The current person is not in the heap yet.
        if (int(best.size()) == companionCount) {
            i128 candidate = i128(sum + person.efficiency) * person.speed;
            answer = max(answer, candidate);
        }

        // Make this person available to later candidates.
        best.push(person.efficiency);
        sum += person.efficiency;

        if (int(best.size()) > companionCount) {
            sum -= best.top();
            best.pop();
        }
    }

    printInt128(answer);
    cout << '\n';
}
```

Example input:

```text
3 2
7 3
10 2
7 5
```

Output:

```text
42
```

The code stores IDs only to make the speed-sort tie-break deterministic. The answer is the score; it does not output the chosen team.

## 10. Time and Space Complexity

- Sorting people: $O(n\log n)$.
- Heap insertion and possible removal per person: $O(\log(k+1))$.
- Computing each candidate from the maintained sum: $O(1)$.

Total time is:

$$
O(n\log n+n\log(k+1))=O(n\log n).
$$

The `k + 1` expression also covers `k = 1`, when the heap operations have constant cost.

Storage consists of:

- $O(n)$ for the people.
- $O(k)$ for the heap.
- The sorting stack.

Total storage is $O(n+k)=O(n)$. If input records are excluded, the extra storage is $O(k+\log n)$ in the usual sorting implementation.

Maintaining `sum` is important. Recomputing it by traversing the heap for every candidate would introduce an unnecessary factor of `k`.

## 11. Two Valid Heap Formulations—Keep Their Invariants Separate

There is another common version of this algorithm:

```text
sort by decreasing speed
for each person:
    insert their efficiency
    remove the smallest if heap size exceeds k
    if heap size equals k:
        answer = max(answer, current speed * heap sum)
```

This version keeps the largest **`k`** efficiencies in the entire processed prefix. It is also correct under the positive-value assumptions here, but its interpretation is slightly different.

The current person can be removed from the heap. In that case, the retained team's true minimum speed may be greater than the current speed. The product being evaluated is a **lower bound** on that retained team's score, rather than necessarily its exact score.

Why is the final answer still correct?

1. At every iteration, the retained team has minimum speed at least the current speed. With positive efficiencies, its actual score is at least the evaluated product, so the evaluated product cannot exceed the global optimum.
2. Consider the iteration corresponding to the last member of an optimal team. The processed prefix contains that entire team. The heap has at least its efficiency sum, and the current speed equals that team's minimum speed. The evaluated product is at least the optimum.

Together, these observations force the maximum evaluated product to equal the optimum.

### The Important Distinction

| Formulation | Heap capacity | When to evaluate | Candidate sum |
| --- | --- | --- | --- |
| Current person must be included | `k - 1` | Before inserting current person | `heap sum + current efficiency` |
| Best team from processed prefix | `k` | After inserting and trimming | `heap sum` |

Both formulations work. Combining the capacity from one with the candidate formula from the other does not.

### A Counterexample to the Mixed Version

Let `k = 2`, all speeds be `1`, and efficiencies be `[10, 9, 8]`.

The correct answer is:

$$
(10+9)\cdot1=19.
$$

If the heap keeps two earlier efficiencies and we add the current efficiency separately, the third iteration evaluates:

$$
(10+9+8)\cdot1=27.
$$

That is the score of three people, which violates the required team size.

The implementation in this session consistently uses **`k - 1` earlier members plus the current person**.

## 12. Common Implementation Mistakes

| Mistake | Correction |
| --- | --- |
| Sorting speeds in increasing order | Use decreasing speed so earlier people are valid companions. |
| Keeping the smallest efficiencies | Use a min-heap to remove the smallest and retain the largest. |
| Calling `priority_queue.insert()` | The insertion method is `push()`. |
| Updating the answer with `min` | The objective is maximization; use `max`. |
| Forgetting to subtract a removed efficiency | Update `sum` whenever the heap changes. |
| Evaluating before enough companions exist | Require heap size exactly `k - 1`. |
| Keeping `k` companions and then adding the current person | That creates `k + 1` members; keep `k - 1`. |
| Multiplying in `int` or assuming the final product fits in 64 bits | Check the full bound and promote before multiplication. |
| Reading `speed efficiency` when the format says `efficiency speed` | Keep the input contract consistent. |

If a problem asks for the answer modulo some number, first find the maximum using the actual scores, then reduce the final maximum. Taking a modulus before comparison can change which score appears larger.

## 13. Edge Cases and Useful Checks

| Case | Expected behavior |
| --- | --- |
| `n = k = 1` | Return that person's efficiency times speed. |
| `k = 1` | Return the largest individual product. |
| `k = n` | Select everyone; use total efficiency times global minimum speed. |
| All speeds equal | Select the `k` largest efficiencies. |
| All efficiencies equal | Select a team with the largest possible minimum speed, obtainable from the `k` largest speeds. |
| Equal speeds and efficiencies | Ties do not affect the score. |
| A very efficient but slow person | Evaluate the trade-off; their inclusion is not automatically beneficial. |

For the full upper bounds, if all `100000` selected people have efficiency and speed `1000000000`, the score is:

```text
100000000000000000000000
```

This is $10^{23}$ and demonstrates why the final answer needs wider arithmetic than `long long`.

## 14. Interview and Competitive Programming Insights

**Look for a minimum that can be fixed by sorting.** Expressions such as “sum of one attribute multiplied by minimum of another” suggest sorting by the attribute inside the minimum. This turns a global restriction into prefix eligibility.

**Name what the heap represents before coding.** “The heap stores the best `k - 1` earlier efficiencies” immediately explains its capacity, why the smallest is removed, and why evaluation happens before insertion.

**Exactly `k` and at most `k` are different.** Even with positive attributes, adding a slow person can reduce the score. If selecting at most `k` people is allowed, the optimum need not use all `k`. In the forced-current formulation, evaluate every person using the retained `min(k - 1, earlier count)` companions rather than waiting for a full heap. For that fixed current speed, positive efficiencies make every available companion slot beneficial.

**Recovering the team needs IDs.** Store `(efficiency, id)` in the heap. To avoid copying `k` IDs at every improvement, record the winning iteration, rerun the prefix scan to that iteration, and collect its `k - 1` companions plus the fixed member. With deterministic ties, this reproduces a winning team without an $O(nk)$ copying cost.

**Test the cardinality invariant explicitly.** On small inputs, enumerate all subsets of size `k` and compare their scores with the greedy result. Include `k = 1`, `k = n`, equal speeds, and the three-person counterexample above. These checks are particularly good at finding the mixed-formulation bug.

## 15. Practice Check

1. Why does the heap contain `k - 1` people in the main implementation?
2. Why do tied speeds not require special grouping?
3. For speeds `[4, 4, 4]`, efficiencies `[2, 9, 5]`, and `k = 2`, what is the answer?
4. For `k = 1`, should we select the fastest person or the most efficient person?

**Answers:**

1. The current person is selected separately, making exactly `k` distinct members.
2. Every team has a last member in any fixed sorted order, including within a tied-speed group.
3. Choose efficiencies `9` and `5`; the score is $(9+5)\cdot4=56$.
4. Neither rule alone is sufficient. Select the person with the largest `speed * efficiency`.

## Quick Recap

- Fix the person supplying the team's minimum speed.
- Sort by decreasing speed so all earlier people are eligible companions.
- Use an exchange argument to select the largest `k - 1` earlier efficiencies.
- Maintain those efficiencies and their sum with a min-heap.
- Evaluate the current person before inserting them into the companion heap.
- Every candidate is a valid team, and the last member of an optimal team guarantees that the scan finds the optimum.
- The solution runs in $O(n\log n)$ time.

Across these three sessions, the common habit is to compare the effect of a small change before committing to a greedy rule: swap two pairings, exchange adjacent tasks, move a meeting point, or replace one selected team member. Once we can prove that the change cannot hurt, we can turn the rule into an efficient algorithm.

</READING_WIDGET>
