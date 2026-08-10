<READING_WIDGET>
# Prefix Sum Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When building a 1D Prefix Sum array, why do elite competitive programmers intentionally allocate an array of size `N + 1` (1-based indexing) with `P[0] = 0` instead of a standard `N`-sized array?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        The formula for a range sum is `P[R] - P[L - 1]`. What happens if the query asks for a range starting at index `0` in a 0-indexed array?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By padding the beginning of the array with a `0`, querying from the very start of the array evaluates to `P[R] - P[0]`. If you strictly use a 0-based array, `L - 1` evaluates to `-1`, triggering an Out-of-Bounds Segmentation Fault! Using 1-based indexing completely eliminates the need for slow, ugly `if (L == 0)` safety checks, allowing branch predictor hardware to run at maximum velocity.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because 1-based indexing forces the compiler to store the array in the L1 CPU Cache.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because it guarantees that `L - 1` will always resolve to a safe memory address (index 0), entirely eliminating the need for `if` statement boundary checks.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because `std::vector` natively throws an exception if an array is perfectly sized to `N`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It is a mathematical requirement to store the total sum of the entire array at `P[0]`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Prefix Sum, 1-Based Indexing, Branchless, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **To add a value `X` to all elements from index `L` to `R` in strictly $O(1)$ time, you must construct a 1D Partial Sum (Difference Array). What two physical markers must you drop into the array to accomplish this?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You need to start a wave of addition, and then stop it just past the target range.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        You must drop a `+X` marker at `L` to tell the resolution sweep to start adding `X`. You must then drop a `-X` marker at `R + 1` to act as the cutoff, neutralizing the wave so the addition stops bleeding into the rest of the array. A final cumulative sweep applies the updates in $O(N)$ time.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Drop a `+X` marker at `L`, and a `-X` marker at `R + 1`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Drop a `+X` marker at `L`, and a `+X` marker at `R`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Drop a `+X` marker at `L-1`, and a `-X` marker at `R`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Multiply `L` by `X` and divide `R` by `X`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Partial Sum, Difference Array, Range Updates, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When precomputing a 2D Prefix Sum matrix `P` using the Principle of Inclusion-Exclusion, you calculate the bounding box via: `P[i][j] = Arr[i][j] + P[i-1][j] + P[i][j-1]`. However, this math is incorrect. What critical final step must you apply?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If you add the entire rectangle above you, and the entire rectangle to your left, what happens to the area where they overlap?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because the bounding box above `P[i-1][j]` and the bounding box to the left `P[i][j-1]` physically overlap at their top-left diagonal, you just added that entire diagonal intersection twice! You must subtract it once (`- P[i-1][j-1]`) to mathematically correct the geometry.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                You must multiply the entire result by `-1` to invert the matrix.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                You must add the top-left diagonal cell `+ P[i-1][j-1]` to complete the square.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                You must subtract the top-left diagonal intersection `- P[i-1][j-1]` because it was accidentally added twice.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                You must divide the result by 2 to average out the matrix collisions.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, 2D Prefix Sum, Geometry, Inclusion-Exclusion, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **To execute an $O(1)$ update on a 2D matrix from top-left `(U, L)` to bottom-right `(D, R)` using a 2D Difference Array, you must drop 4 markers. You drop a `+X` origin marker at `(U, L)`, and two `-X` cutoff markers at `(U, R+1)` and `(D+1, L)`. Why must you drop a fourth `+X` marker at the bottom-right intersection `(D+1, R+1)`?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Just like the 2D Prefix Sum, what happens when the two `-X` cutoff waves mathematically overlap as they travel downwards and rightwards?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Both the horizontal cutoff wave and the vertical cutoff wave propagate down and right. This means the region starting at `(D+1, R+1)` will receive TWO separate `-X` waves! To neutralize this massive double-subtraction, we must add a `+X` intersection correction at `(D+1, R+1)`!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the `+X` marker ensures the final cumulative sum loop terminates exactly at the edge of the matrix.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the two `-X` cutoff markers overlap at `(D+1, R+1)` and cause a double-subtraction. Adding `+X` perfectly corrects this over-subtraction.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the `+X` marker tells the OS Memory Manager to flush the CPU cache and write the data back to RAM.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because every 2D Partial Sum must mathematically balance to a total net zero by the end of execution.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, 2D Partial Sum, Difference Array, Geometry, Intersection Correction, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **The Difference Array (Partial Sums) is universally categorized as an "Offline Algorithm". If a FAANG interviewer asks you to build a system that mixes thousands of Range Updates (`+X`) and Point Queries (`? i`) in real-time randomly, why will the Difference Array algorithm completely fail?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        To answer a single point query accurately, what must you do to the difference array first?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Difference Arrays are "Offline" because you must collect *all* updates first, and then run an $O(N)$ Prefix Sweep to resolve them. If you mix updates and queries, you are forced to resolve the entire array (taking $O(N)$ time) just to answer a single query! If you have $M$ queries, this degrades into an apocalyptic $O(N \times M)$ TLE. For real-time "Online" queries, you must abandon Difference Arrays and use a Segment Tree or Binary Indexed Tree.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Difference Arrays require a live internet connection to sync the prefix sum values.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because they cannot handle overlapping additions; only a single range update is allowed per array.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because you must execute an $O(N)$ resolution sweep to answer queries. Mixing updates and queries forces constant $O(N)$ sweeps, destroying the performance.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Difference Arrays use floating-point math, which degrades in precision over multiple real-time queries.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Partial Sum, Difference Array, Offline vs Online Queries, Segment Trees, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **When trying to find the maximum number of items a customer can buy with a specific budget, why is it mathematically safe to apply $O(\log N)$ Binary Search (`std::upper_bound`) directly onto the cumulative Prefix Sum array of item prices?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Can the cumulative cost of items ever decrease?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Binary Search strictly requires an array to be monotonically sorted. Because physical item prices cannot be negative, a Prefix Sum array of prices is mathematically guaranteed to be weakly monotonically increasing (or strictly increasing, if no items cost $0$). This perfect monotonicity naturally unlocks the ability to use Binary Search!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because physical item prices cannot be negative, the Prefix Sum array is mathematically guaranteed to be monotonically increasing, fulfilling the strict prerequisite of Binary Search.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because C++ `std::upper_bound` automatically sorts the prefix sum array in the background before searching it.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because Prefix Sum arrays are inherently stored in a Red-Black Tree.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                Because the Prefix Sum uses 1-based indexing, which magically aligns with the binary search median calculation.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Prefix Sum, Binary Search, Monotonicity, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **You are tasked with finding the number of continuous subarrays that sum exactly to $K$ in an array containing BOTH positive and negative numbers. Why is a standard Sliding Window guaranteed to fail, and what Elite CP architecture must you combine with Prefix Sums to achieve strict $O(N)$ time?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        If the array contains negative numbers, expanding the sliding window doesn't guarantee the sum will increase!
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A Sliding Window strictly requires Monotonicity (expanding the window *always* increases the sum, shrinking it *always* decreases the sum). Negative numbers break this rule! To achieve $O(N)$ time, Elite programmers combine a Prefix Sum with a **Hash Map**. As they iterate, they store the frequency of every prefix sum seen so far in the Hash Map, and instantly look up if `(current_sum - K)` exists in the map!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Sliding Window fails because it executes in $O(N^2)$ time. You must combine Prefix Sums with a Binary Indexed Tree.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Sliding Window fails because negative numbers destroy monotonicity (expanding the window might decrease the sum). You must combine Prefix Sums with a Hash Map and look up `(current_sum - K)`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Sliding Window fails because it only works on strings, not integers. You must combine Prefix Sums with a Min-Heap.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                A Sliding Window actually works perfectly here, the problem is just a trick question.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Prefix Sum, Hash Map, Subarray Sum to K, Sliding Window, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In many CP problems, you are asked to output the prefix sum range query modulo $10^9 + 7$. You precompute your array with `P[i] = (P[i-1] + arr[i]) % MOD` and execute your query as `(P[R] - P[L-1]) % MOD`. Why will this exact query equation occasionally result in a fatal Wrong Answer (WA) returning negative numbers, and how do you fix it?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Because of the modulo operations during precomputation, is it possible for `P[L-1]` to be a mathematically larger number than `P[R]`?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Yes! Because of the individual modulo boundaries, it is completely possible for the precomputed `P[L-1]` to be larger than `P[R]`. For example, `(5 - 10) % 7` in C++ evaluates to `-5`, not the true mathematical modulo of `2`! C++ calculates the remainder, not the Euclidean modulo. To safely prevent negative remainders, you must explicitly add the `MOD` back before the final modulo: `(P[R] - P[L-1] + MOD) % MOD`.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                It fails because the modulo operator `%` is incompatible with `long long`. You must use `fmod()`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It fails because `P[L-1]` might be larger than `P[R]` after precomputation modulos, causing C++'s remainder operator to return a negative number. You must use the safety net: `(P[R] - P[L-1] + MOD) % MOD`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It fails because C++ evaluates the `%` operator before the `-` operator. You just need to add parenthesis: `((P[R]) - (P[L-1])) % MOD`.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                It fails because $10^9 + 7$ is not a prime number.
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        C++, STL, Prefix Sum, Modulo Arithmetic, Negative Remainder, Math, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
