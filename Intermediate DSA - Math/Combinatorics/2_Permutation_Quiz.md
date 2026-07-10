<READING_WIDGET>
# Permutations Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many ways can 5 distinct books be arranged on a shelf?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Think about the factorial function. What is $5!$?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because all 5 books are distinct and order matters, the number of arrangements is $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                5
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                10
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                120
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                25
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A club has 10 members. How many ways can they elect a President, a Vice-President, and a Secretary, assuming no person can hold more than one office?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You are selecting 3 people out of 10, and the specific order (who gets which title) matters. Use the $^nP_r$ formula!
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because the roles are distinct, order matters. We use the permutation formula $P(10, 3) = \frac{10!}{(10 - 3)!} = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                120
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                720
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                1,000
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                3,628,800
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many 6-letter passwords can be formed using 26 letters, if repetition is allowed?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Use the Multiplication Principle! For each of the 6 slots, how many options do you have?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because repetition is allowed, you have 26 choices for the first letter, 26 choices for the second, and so on. By the multiplication principle: $26 \times 26 \times 26 \times 26 \times 26 \times 26 = 26^6$. This is NOT $P(26,6)$ because elements can be reused!
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                $26!$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                $26^6$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                $6!$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                $P(26,6)$
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many distinct ways can the letters in "AABBB" be arranged?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Since some letters are identical, you must divide out their internal permutations to avoid overcounting!
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        There are 5 total letters ($5!$), but there are 2 identical 'A's ($2!$) and 3 identical 'B's ($3!$). Applying the repetition formula: $\frac{5!}{2! \times 3!} = \frac{120}{2 \times 6} = \frac{120}{12} = 10$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                10
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                20
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                30
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                60
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many ways can 6 people be arranged in a line, if two specific people must always stand together?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Treat the two people who must stand together as a single unbreakable "block". How many objects are you arranging now?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        By grouping the two specific people into a single "block", we now only have 5 objects to arrange ($5! = 120$). However, those two people can swap places within their own block ($2! = 2$). Total ways = $120 \times 2 = 240$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                120
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                240
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                720
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                1440
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many 5-letter passwords can be formed using the 26 English alphabets, if no letter is repeated?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Because repetition is not allowed, you have one fewer choice for each subsequent letter. Use the Multiplication Principle!
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        First letter has 26 choices, the second has 25 choices, third has 24, and so on. $P(26, 5) = 26 \times 25 \times 24 \times 23 \times 22 = 7,893,600$. This directly contrasts with problems where repetition *is* allowed (which would be $26^5$).
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                7,893,600
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                6,500,000
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                3,900,000
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                1,200,000
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **In how many ways can 6 friends sit around a circular table?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        In a circle, there is no distinct "start" or "end". You must fix one person in a specific chair to break the rotational symmetry, leaving how many people left to arrange?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        This is a classic "Circular Permutation" problem. To prevent counting identical rotational arrangements multiple times, we fix the position of 1 person. The remaining $(N-1)$ people can then be arranged in $(N-1)!$ ways. For 6 people, it is $(6-1)! = 5! = 120$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                120
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                240
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                360
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                720
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Permutations, Circular Permutations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
