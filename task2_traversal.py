import networkx as nx
from collections import deque
import os

# Graph definition from Task 1 (Adjacency List structure for easy traversal)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['C', 'D', 'E']
}

# DFS (Iterative - Stack)
def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            # Add neighbors in reverse order to maintain desired traversal preference
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# BFS (Iterative - Queue)
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Execution and Data Collection
start_node = 'A'
goal_node = 'F'

dfs_result = dfs_path(graph, start_node, goal_node)
bfs_result = bfs_path(graph, start_node, goal_node)

dfs_length = len(dfs_result) - 1 if dfs_result else 'N/A'
bfs_length = len(bfs_result) - 1 if bfs_result else 'N/A'

# Generate README.md content
readme_content = f"""# Graph Search Algorithms Analysis (DFS and BFS)

## Task 2: Comparison of Results

For the city transport network model (vertices A, B, C, D, E, F), paths were found from the starting vertex '{start_node}' to the goal vertex '{goal_node}' using the DFS and BFS algorithms.

| Algorithm | Found Path | Path Length (Number of Edges) |
| :--- | :--- | :--- |
| **DFS** (Depth-First Search) | `{dfs_result}` | {dfs_length} |
| **BFS** (Breadth-First Search) | `{bfs_result}` | {bfs_length} |

---

## Justification for Path Differences

### 1. BFS (Breadth-First Search)

* **Principle:** FIFO (First-In, First-Out), uses a **Queue**.
* **Why this path:** BFS explores the graph layer by layer, expanding outward from the start vertex. It guarantees finding the **shortest path** in terms of the minimum **number of edges**.
* **Path:** The path found by BFS (length {bfs_length}) is the shortest path in the unweighted graph.

### 2. DFS (Depth-First Search)

* **Principle:** LIFO (Last-In, First-Out), uses a **Stack**.
* **Why this path:** DFS prioritizes going as deep as possible along one branch before backtracking. The path order depends on the order of neighbors in the adjacency list.
* **Path:** The path found by DFS (length {dfs_length}) is longer because the algorithm first went deep down the `A -> B -> D` branch before discovering the shorter route through 'C'. This demonstrates that **DFS does not guarantee finding the shortest path**.

**Conclusion:** For path optimization (minimum intersections in this case) in an unweighted graph, **BFS** should always be used.
"""

# Write content to readme.md
with open("readme.md", "w") as f:
    f.write(readme_content)

print(f"--- Transport Network Path Analysis ---")
print(f"Start Node: {start_node}")
print(f"Goal Node: {goal_node}")
print("-" * 30)

print(f"DFS Path (Depth-First Search): {dfs_result}")
print(f"DFS Path Length (Number of Edges): {dfs_length}")
print("-" * 30)

print(f"BFS Path (Breadth-First Search): {bfs_result}")
print(f"BFS Path Length (Number of Edges): {bfs_length}")
print("-" * 30)
print(f"'readme.md' file successfully generated with results.")