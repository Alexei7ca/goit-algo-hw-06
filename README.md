# Graph Search Algorithms Analysis (DFS and BFS)

## Task 2: Comparison of Results

For the city transport network model (vertices A, B, C, D, E, F), paths were found from the starting vertex 'A' to the goal vertex 'F' using the DFS and BFS algorithms.

| Algorithm | Found Path | Path Length (Number of Edges) |
| :--- | :--- | :--- |
| **DFS** (Depth-First Search) | `['A', 'B', 'D', 'F']` | 3 |
| **BFS** (Breadth-First Search) | `['A', 'C', 'F']` | 2 |

---

## Justification for Path Differences

### 1. BFS (Breadth-First Search)

* **Principle:** FIFO (First-In, First-Out), uses a **Queue**.
* **Why this path:** BFS explores the graph layer by layer, expanding outward from the start vertex. It guarantees finding the **shortest path** in terms of the minimum **number of edges**.
* **Path:** The path found by BFS (length 2) is the shortest path in the unweighted graph.

### 2. DFS (Depth-First Search)

* **Principle:** LIFO (Last-In, First-Out), uses a **Stack**.
* **Why this path:** DFS prioritizes going as deep as possible along one branch before backtracking. The path order depends on the order of neighbors in the adjacency list.
* **Path:** The path found by DFS (length 3) is longer because the algorithm first went deep down the `A -> B -> D` branch before discovering the shorter route through 'C'. This demonstrates that **DFS does not guarantee finding the shortest path**.

**Conclusion:** For path optimization (minimum intersections in this case) in an unweighted graph, **BFS** should always be used.
