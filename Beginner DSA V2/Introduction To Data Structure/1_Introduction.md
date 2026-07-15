<VIDEO_WIDGET>

<VIDEO_ID>3515</VIDEO_ID> <!-- Required -->

</VIDEO_WIDGET>

<READING_WIDGET>

# Introduction to Data Structures

In the previous modules, you learned how to write algorithms, analyze their Time and Space Complexities, and utilize fundamental mathematics. But algorithms do not exist in a vacuum—they need **data** to operate on.

How you store and organize that data dictates how fast your algorithm can run. This is where **Data Structures** come in.

---

## What is a Data Structure?

A **Data Structure** is a specialized format for organizing, processing, retrieving, and storing data in a computer's memory.

Think of a data structure as a physical container. If you want to store water, you use a bottle (great for drinking) or a bucket (great for washing). You wouldn't use a flat plate to store water! Similarly, in programming, if you need to access data instantly by an index, you use an Array. If you need to constantly add and remove data from the ends, an Array becomes terribly inefficient, so you use a Linked List or a Queue.

In Competitive Programming, choosing the correct Data Structure is often the entire key to solving the problem within the strict $1$-second Time Limit.

---

## The Two Families of Data Structures

Data structures are broadly classified into two main categories based on how the data is logically arranged in memory: **Linear** and **Non-Linear**.

### 1. Linear Data Structures

In a Linear Data Structure, elements are arranged sequentially (in a straight line). Every element is connected to exactly one previous element and exactly one next element.

Because the data is strictly sequential, you can traverse all the elements in a single run (like walking down a hallway).

**Key Examples:**

- **Arrays:** A fixed-size, continuous block of memory. Perfect for instant $O(1)$ access, but terrible for inserting/deleting elements in the middle.
- **Linked Lists:** Elements are scattered in memory but connected via pointers. Great for dynamic sizing and fast insertions/deletions, but terrible for random access (you must walk the list from the beginning).
- **Stacks:** A Last-In-First-Out (LIFO) structure. Think of a stack of plates; you can only add or remove from the very top.
- **Queues:** A First-In-First-Out (FIFO) structure. Think of a line at a ticket counter; the first person to join the line is the first person to get a ticket.

> 💡 **CP Insight:** Linear data structures are the foundation of basic array manipulation, sliding window techniques, and simple simulations.

### 2. Non-Linear Data Structures

In a Non-Linear Data Structure, elements are _not_ arranged strictly in a sequence. Instead, a single element can be connected to multiple other elements, forming complex hierarchical or interconnected networks.

You cannot simply traverse these structures in a single straight line.

**Key Examples:**

- **Trees:** A hierarchical structure containing a "root" node that branches out to "child" nodes. (e.g., A family tree, or the folder structure on your computer). The most famous variant in CP is the **Binary Search Tree (BST)**, which allows incredibly fast $O(\log N)$ searching.
- **Graphs:** A network of interconnected "nodes" (or vertices) linked by "edges". Unlike trees, graphs can have loops and disconnected parts. (e.g., Google Maps routing, or a social network where people are nodes and friendships are edges).

> 💡 **CP Insight:** Non-linear data structures are what separate beginners from advanced programmers. Mastering Trees and Graphs unlocks the ability to solve massive, complex pathfinding and hierarchical problems.

---

> 🚀 **Next Up:** Now that you have a bird's-eye view of how we organize data, it's time to dive into our very first structured container: the **Stack**! Let's see how this Last-In-First-Out structure works.

</READING_WIDGET>
