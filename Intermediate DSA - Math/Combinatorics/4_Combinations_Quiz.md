<READING_WIDGET>
# Combinations Quiz

Choose the correct answer for each question.
</READING_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **How many ways can a 4-member team be selected from 10 people?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Does the order of the people on the team matter? Use the $^nC_r$ formula!
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Order does not matter when selecting a team. This is a simple combination problem: $C(10, 4) = \frac{10!}{4!6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 210$.
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
                210
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                5040
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                45
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Combinations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A basket contains 5 distinct apples, 4 distinct oranges, and 3 distinct bananas. How many ways can you select exactly 3 fruits?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        Since all the fruits are distinct, how many total distinct fruits do you have to choose from?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Because all fruits are distinctly identifiable, you essentially have a pool of $5 + 4 + 3 = 12$ unique items. You want to select 3, and order doesn't matter. $C(12, 3) = \frac{12!}{3!9!} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$. *(Note: If the problem stated the fruits were identical, this would be a "stars and bars" problem instead!)*
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                12
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                15
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                24
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                220
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Combinations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A student must select 2 books from a collection of 7 books. How many ways can they do this?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        You are selecting 2 items from 7 without caring about order.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Using the combinations formula: $C(7, 2) = \frac{7!}{2!5!} = \frac{7 \times 6}{2 \times 1} = 21$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                14
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                21
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                35
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                42
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Combinations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **A club has 8 men and 6 women. How many ways can a 3-person committee be formed with AT LEAST one woman?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        It is much faster to use the complement approach! Total possible committees minus the committees with ZERO women.
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        Total possible 3-person committees from 14 people = $C(14, 3) = 364$. <br>Committees with exactly zero women (meaning all 3 are chosen from the 8 men) = $C(8, 3) = 56$. <br>Therefore, the committees with *at least* one woman = $364 - 56 = 308$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                252
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                280
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                308
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                364
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Combinations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>

<MCQ_WIDGET>
    <MCQ_DESCRIPTION>
        **If 10 people shake hands with each other exactly once, how many handshakes occur in total?**
    </MCQ_DESCRIPTION>
    <MCQ_HINT>
        A handshake is just a unique selection of 2 people from the group of 10. Does the order of the two people matter?
    </MCQ_HINT>
    <MCQ_EXPLANATION>
        A handshake happens between any pair of 2 people, and the order of selection doesn't matter (Person A shaking B's hand is the same as Person B shaking A's hand). Therefore, the number of handshakes is exactly the number of ways to choose 2 people from 10: $C(10, 2) = \frac{10!}{2!8!} = \frac{10 \times 9}{2} = 45$.
    </MCQ_EXPLANATION>
    <MCQ_OPTIONS>
        <OPTION_ITEM>
            <OPTION_BODY>
                20
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                36
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                45
            </OPTION_BODY>
            <OPTION_IS_CORRECT>1</OPTION_IS_CORRECT>
        </OPTION_ITEM>
        <OPTION_ITEM>
            <OPTION_BODY>
                55
            </OPTION_BODY>
            <OPTION_IS_CORRECT>0</OPTION_IS_CORRECT>
        </OPTION_ITEM>
    </MCQ_OPTIONS>
    <MCQ_TAGS>
        Math, Combinatorics, Combinations, Quiz
    </MCQ_TAGS>
</MCQ_WIDGET>
