<VIDEO_WIDGET>

<VIDEO_ID>3232</VIDEO_ID>

</VIDEO_WIDGET>

<READING_WIDGET>

# Two Pointers: Form 3 — Multisequence Type

In Form 3, the pointers do not represent two boundaries of one window. Instead, they belong to different sequences:

- `tail` tracks the current element of the first sequence.
- `head` tracks the current element of the second sequence.
- A comparison between the current elements decides whether `tail`, `head`, or both should advance.

Each pointer remembers how much of its own sequence has already been processed.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/dd628fc4-3b80-4754-8dc7-1e243081d824.png" alt="Form 3 multisequence pattern" style="max-width: 100%; height: auto;" identifier="az-img-upload">

---

## 1. The Core Form 3 Pattern

For two sequences `A` and `B`, the general structure is:

~~~cpp
int tail = 0; // Pointer in A
int head = 0; // Pointer in B

while (tail < A.size() && head < B.size()) {
    if (A[tail] == B[head]) {
        // Use the match.
        tail++;
        head++;
    } else if (shouldMoveTail(A[tail], B[head])) {
        tail++;
    } else {
        head++;
    }
}
~~~

This is a pattern, not a complete algorithm. The problem determines:

- what a comparison means,
- when a pair should be used,
- which pointer can safely advance, and
- when the process is complete.

The central invariant is:

> Everything before each pointer has already been processed and will never be needed again.

Since the pointers never move backward, the total number of pointer movements is linear in the total input size.

---

## 2. How Form 3 Differs from Form 2

| Property | Form 2: Divergence | Form 3: Multisequence |
|---|---|---|
| Pointer locations | Opposite ends of one sequence | One pointer in each sequence |
| Initial positions | `tail = 0`, `head = n - 1` | Usually both begin at index `0` |
| Movement | Toward each other | Independently from left to right |
| Main question | Which endpoint can be eliminated? | Which sequence must advance? |
| Termination | The pointers meet | One required sequence is exhausted |

Do not classify a problem only by the number of pointers. Ask what each pointer represents.

---

## 3. How to Recognize Form 3

Consider Form 3 when:

1. Two or more sequences must be processed together.
2. The relative order inside every sequence is meaningful.
3. Only the current unprocessed element of each sequence is needed for the next decision.
4. A comparison proves that one or more current elements can be permanently skipped.
5. No pointer ever needs to move backward.

Common operations behind this form include:

- matching one sequence inside another,
- intersecting sorted sequences,
- merging sorted sequences, and
- coordinating one pointer in each of several sorted sequences.

The chapter uses only the three Form 3 problems from the reference material.

---

## 4. Question 1: Is $T$ a Subsequence of $S$?

### Problem

Given two strings `S` and `T`, determine whether `T` occurs in `S` as a subsequence.

A subsequence preserves order but does not require the selected characters to be adjacent.

For example:

~~~text
S = "abaccabadaba"
T = "bda"
~~~

the answer is:

~~~text
True
~~~

We can select:

~~~text
S[1] = 'b'
S[8] = 'd'
S[9] = 'a'
~~~

These characters appear in the same order as `T = "bda"`.

### Pointer Meaning

- `tail` scans the source string `S`.
- `head` tracks the next required character of `T`.

At every step:

- If `S[tail] == T[head]`, the next required character has been found, so both pointers advance.
- Otherwise, the current source character is not useful for the current match, so only `tail` advances.

The source pointer always advances because each source character is examined at most once.

### Why Is the Greedy Match Safe?

When `S[tail] == T[head]`, matching `T[head]` with the earliest available occurrence in `S` leaves the largest possible suffix of `S` for the remaining characters.

Choosing a later equal character cannot give us more options. Therefore, the earliest match is always safe.

### Dry Run

| `tail` | `S[tail]` | `head` | Required `T[head]` | Decision |
|---:|:---:|---:|:---:|---|
| 0 | `a` | 0 | `b` | Move `tail` |
| 1 | `b` | 0 | `b` | Match; move both |
| 2 | `a` | 1 | `d` | Move `tail` |
| 3 | `c` | 1 | `d` | Move `tail` |
| 4 | `c` | 1 | `d` | Move `tail` |
| 5 | `a` | 1 | `d` | Move `tail` |
| 6 | `b` | 1 | `d` | Move `tail` |
| 7 | `a` | 1 | `d` | Move `tail` |
| 8 | `d` | 1 | `d` | Match; move both |
| 9 | `a` | 2 | `a` | Match; move both |

Now `head == T.size()`, which means every character of `T` has been matched.

### Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

void init() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

bool isSubsequence(const string& S, const string& T) {
    int tail = 0; // Pointer in S
    int head = 0; // Pointer in T

    while (tail < (int)S.size() && head < (int)T.size()) {
        if (S[tail] == T[head]) {
            head++;
        }

        tail++;
    }

    return head == (int)T.size();
}

void solve() {
    string S, T;
    cin >> S >> T;

    cout << (isSubsequence(S, T) ? "True" : "False") << endl;
}

int32_t main() {
    init();

    int _t = 1;
    cin >> _t;

    while (_t--) {
        solve();
    }

    return 0;
}
~~~

### Complexity

`tail` scans `S` once, while `head` moves at most `T.size()` times:

$$
\text{Time Complexity}=O(|S|)
$$

$$
\text{Extra Space}=O(1)
$$

If `T` is empty, it is a subsequence of every string. If `S` becomes exhausted before `T`, the answer is false.

---

## 5. Question 2: Documents Containing Every Query Word

### Problem

Given some query words and a collection of documents, return the documents in which every query word occurs at least once.

For the query:

~~~text
Word 1 = "Vivek"
Word 2 = "AlgoZenith"
~~~

and the documents:

~~~text
D1 = "Vivek has been coding DSA"
D2 = "AlgoZenith teaches DSA and CP"
D3 = "AlgoZenith also covers Dev now"
D4 = "Vivek is the founder of AlgoZenith"
D5 = "AlgoZenith is the best thing available"
~~~

the answer is:

~~~text
[D4]
~~~

### Build Posting Lists

Instead of scanning every document for every query, store a sorted list of document IDs for each word. This is an **inverted index**.

For the example:

| Word | Sorted document IDs |
|---|---|
| `Vivek` | `[1, 4]` |
| `AlgoZenith` | `[2, 3, 4, 5]` |
| `DSA` | `[1, 2]` |

A document contains every query word exactly when its ID occurs in the intersection of their posting lists.

For `Vivek` and `AlgoZenith`, we need:

$$
[1,4]\cap[2,3,4,5]=[4]
$$

For `AlgoZenith` and `DSA`:

$$
[2,3,4,5]\cap[1,2]=[2]
$$

### Intersect Two Sorted Lists

Let `tail` point into the first posting list and `head` point into the second.

- If the IDs are equal, the document belongs to both lists. Record it and move both pointers.
- If the first ID is smaller, it cannot appear later in the second sorted list. Move `tail`.
- If the second ID is smaller, move `head` for the symmetric reason.

~~~cpp
vector<int> intersectSorted(const vector<int>& first,
                            const vector<int>& second) {
    int tail = 0;
    int head = 0;
    vector<int> intersection;

    while (tail < (int)first.size() &&
           head < (int)second.size()) {
        if (first[tail] == second[head]) {
            intersection.push_back(first[tail]);
            tail++;
            head++;
        } else if (first[tail] < second[head]) {
            tail++;
        } else {
            head++;
        }
    }

    return intersection;
}
~~~

### Dry Run of the Intersection

For:

~~~text
first  = [1, 4]
second = [2, 3, 4, 5]
~~~

| `first[tail]` | `second[head]` | Decision | Result |
|---:|---:|---|---|
| 1 | 2 | $1<2$, move `tail` | `[]` |
| 4 | 2 | $4>2$, move `head` | `[]` |
| 4 | 3 | $4>3$, move `head` | `[]` |
| 4 | 4 | Match; record 4 and move both | `[4]` |

### More Than Two Query Words

Intersect the posting lists one at a time:

~~~cpp
vector<int> documentsContainingAll(
    const vector<string>& queryWords,
    const unordered_map<string, vector<int>>& postingList) {

    if (queryWords.empty()) {
        return {};
    }

    auto firstWord = postingList.find(queryWords[0]);
    if (firstWord == postingList.end()) {
        return {};
    }

    vector<int> answer = firstWord->second;

    for (int i = 1; i < (int)queryWords.size(); i++) {
        auto currentWord = postingList.find(queryWords[i]);

        if (currentWord == postingList.end()) {
            return {};
        }

        answer = intersectSorted(answer, currentWord->second);

        if (answer.empty()) {
            break;
        }
    }

    return answer;
}
~~~

Assuming every posting list is already sorted, the intersection work is linear in the total number of document IDs examined.

> **Implementation Note:** While building the inverted index, add a document ID only once per word, even if that word appears multiple times in the same document.

---

## 6. Question 3: Minimum Range Using One Element from Every Row

### Problem

Given an $N\times M$ integer matrix, select exactly one value from each row.

Let:

$$
V_{\max}=\text{maximum selected value}
$$

and:

$$
V_{\min}=\text{minimum selected value}
$$

Minimize:

$$
\text{score}=V_{\max}-V_{\min}
$$

For:

~~~text
grid = [
    [1, 5, 2],
    [10, 3, 7],
    [4, 8, 2]
]
~~~

the answer is:

~~~text
1
~~~

We can select $2$ from the first row, $3$ from the second row, and $2$ from the third row:

$$
3-2=1
$$

### Convert Rows into Sorted Sequences

Sort every row:

~~~text
Row 1: [1, 2, 5]
Row 2: [3, 7, 10]
Row 3: [2, 4, 8]
~~~

Now maintain one pointer in every row. The values under all pointers form the current selection.

This is the $K$-sequence generalization of Form 3: instead of only `tail` and `head`, we maintain a pointer for every sequence.

<img src="https://d3pdqc0wehtytt.cloudfront.net/media/9651/8ff19792-ec02-4f00-adea-e2464bfac31b.png" alt="K-sequence smallest-range movement" style="max-width: 100%; height: auto;" identifier="az-img-upload">

### Which Pointer Should Move?

Suppose the current selected values have minimum $V_{\min}$ and maximum $V_{\max}$.

To reduce the range, we must try to increase the minimum. Moving any row other than the one containing $V_{\min}$ leaves the same minimum in the selection and cannot produce a smaller range.

Therefore:

> Advance the pointer belonging to the row that currently contributes the minimum value.

We use:

- a min-heap to find the current minimum and its row,
- a variable to maintain the current maximum, and
- one pointer position for every row.

### Dry Run

After sorting, the initial pointers select:

~~~text
[1, 3, 2]
~~~

so:

$$
V_{\min}=1,\qquad V_{\max}=3,\qquad \text{score}=2
$$

The minimum value $1$ belongs to Row 1, so advance Row 1's pointer:

~~~text
[2, 3, 2]
~~~

Now:

$$
V_{\min}=2,\qquad V_{\max}=3,\qquad \text{score}=1
$$

The process continues until one row is exhausted. At that moment, no further complete selection containing one value from every row is possible.

### Implementation

~~~cpp
#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

void init() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

int minimumScore(vector<vector<int>>& grid) {
    int n = grid.size();

    if (n == 0) {
        return 0;
    }

    for (auto& row : grid) {
        if (row.empty()) {
            return -1;
        }

        sort(row.begin(), row.end());
    }

    // {value, row, position inside that row}
    using State = tuple<int, int, int>;
    priority_queue<State, vector<State>, greater<State>> minimumHeap;

    int currentMaximum = LLONG_MIN;

    for (int row = 0; row < n; row++) {
        minimumHeap.push({grid[row][0], row, 0});
        currentMaximum = max(currentMaximum, grid[row][0]);
    }

    int answer = LLONG_MAX;

    while (true) {
        auto [currentMinimum, row, position] = minimumHeap.top();
        minimumHeap.pop();

        answer = min(answer, currentMaximum - currentMinimum);

        int nextPosition = position + 1;

        // This row is exhausted, so no complete future selection exists.
        if (nextPosition == (int)grid[row].size()) {
            break;
        }

        int nextValue = grid[row][nextPosition];
        minimumHeap.push({nextValue, row, nextPosition});
        currentMaximum = max(currentMaximum, nextValue);
    }

    return answer;
}

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m));

    for (int row = 0; row < n; row++) {
        for (int column = 0; column < m; column++) {
            cin >> grid[row][column];
        }
    }

    cout << minimumScore(grid) << endl;
}

int32_t main() {
    init();

    int _t = 1;
    cin >> _t;

    while (_t--) {
        solve();
    }

    return 0;
}
~~~

### Complexity

Sorting all $N$ rows of length $M$ costs:

$$
O(NM\log M)
$$

Across the heap process, every matrix element is inserted and removed at most once. The heap contains $N$ elements, so this phase costs:

$$
O(NM\log N)
$$

The total time is:

$$
O(NM\log M+NM\log N)
$$

The heap and row pointers require:

$$
O(N)
$$

extra space, excluding the storage of the matrix.

---

## 7. Two-Sequence and $K$-Sequence Forms

| Variant | State | Movement decision |
|---|---|---|
| Subsequence matching | One pointer in each string | Always move the source pointer; move the target pointer on a match |
| Sorted-list intersection | One pointer in each list | Move the smaller ID; move both on equality |
| Minimum range across rows | One pointer in every sorted row | Advance the row contributing the current minimum |

The number of pointers may change, but the shared idea remains:

> Compare the current elements, use any valid combination, and permanently advance the sequence whose current element cannot help later.

---

## 8. Common Mistakes

### Treating Both Pointers as Boundaries of One Window

In Form 3, the pointers belong to different sequences. Expressions such as `head - tail + 1` usually have no meaning because the indices use different coordinate systems.

### Moving Both Pointers on Every Comparison

Move both only when both current elements have been fully processed. In a sorted intersection, unequal values require moving only the smaller one. In subsequence matching, a mismatch moves only the source pointer.

### Moving the Wrong Pointer After a Mismatch

Every movement needs a proof. For subsequence matching, the required target character cannot be discarded merely because the current source character differs.

### Forgetting That Posting Lists Must Be Sorted

The smaller-ID elimination rule depends on sorted order. Without it, an ID skipped from one list might still appear later in the other list.

### Forgetting to Sort the Matrix Rows

The minimum-range algorithm advances within a row to the next greater candidate. That progression is valid only after every row is sorted.

### Continuing After One Required Sequence Is Exhausted

For intersection, no additional common value exists after either list ends. For the matrix problem, a complete selection is impossible after any row ends.

---

## 9. Form 3 Summary

- Form 3 coordinates pointers that belong to different sequences.
- `tail` tracks the first sequence and `head` tracks the second sequence.
- Both pointers usually start at index $0$ and move only forward.
- A comparison decides whether `tail`, `head`, or both should advance.
- Everything before a pointer is permanently processed.
- Subsequence matching greedily uses the earliest available match.
- Sorted posting lists are intersected by moving the pointer with the smaller document ID.
- The pattern generalizes to $K$ sequences by maintaining one pointer per sequence.
- For the minimum-range problem, advance the row that supplies the current minimum.
- The key Form 3 question is: **Which sequence's current element can be discarded safely?**

</READING_WIDGET>
