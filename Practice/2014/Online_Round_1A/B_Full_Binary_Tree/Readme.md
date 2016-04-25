Full Binary Tree
---

A tree is a connected graph with no cycles.

A rooted tree is a tree in which one special vertex is called the root. If there is an edge between  **X**  and  **Y**  in a rooted tree, we say that  **Y**  is a child of  **X**  if  **X**  is closer to the root than  **Y**  (in other words, the shortest path from the root to  **X**  is shorter than the shortest path from the root to  **Y**).

A full binary tree is a rooted tree where every node has either exactly 2 children or 0 children.

You are given a tree  **G**  with  **N**  nodes (numbered from  **1**  to  **N**). You are allowed to delete some of the nodes. When a node is deleted, the edges connected to the deleted node are also deleted. Your task is to delete as few nodes as possible so that the remaining nodes form a full binary tree for some choice of the root from the remaining nodes.

### Input

The first line of the input gives the number of test cases,  **T**.  **T**  test cases follow. The first line of each test case contains a single integer  **N**, the number of nodes in the tree. The following  **N**-1 lines each one will contain two space-separated integers:  **Xi**  **Yi**, indicating that  **G**  contains an undirected edge between  **Xi**  and  **Yi**.

### Output

For each test case, output one line containing "Case #**x**:  **y**", where  **x**  is the test case number (starting from 1) and  **y**  is the minimum number of nodes to delete from  **G**  to make a full binary tree.

### Limits

1 ≤  **T**  ≤ 100.  
1 ≤  **Xi**,  **Yi**  ≤  **N**  
Each test case will form a valid connected tree.

#### Small dataset

2 ≤  **N**  ≤ 15.  

#### Large dataset

2 ≤  **N**  ≤ 1000.  

### Sample

#### Input  
    3
    3
    2 1
    1 3
    7
    4 5
    4 2
    1 2
    3 1
    6 4
    3 7
    4
    1 2
    2 3
    3 4
  
#### Output  
    Case #1: 0
    Case #2: 2
    Case #3: 1

