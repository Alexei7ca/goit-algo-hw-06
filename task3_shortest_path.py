import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque

# Creation of a Weighted Graph (Transport Network Model with Time/Distance)
G = nx.Graph()

# Adding edges with weight (Weight = time/distance between intersections)
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'D', weight=7)
G.add_edge('B', 'E', weight=12)
G.add_edge('C', 'F', weight=8)
G.add_edge('D', 'F', weight=1)
G.add_edge('E', 'F', weight=6)

# Custom Implementation of Dijkstra's Algorithm
def dijkstra_custom(graph, start_node):
    # Initialize distances dictionary: {vertex: distance}
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start_node] = 0
    
    # Initialize priority queue (min-heap) with (distance, vertex)
    # Using a min-heap ensures we always extract the unvisited node with the smallest distance
    priority_queue = [(0, start_node)]
    
    # Dictionary to store the shortest path trace
    predecessors = {node: None for node in graph.nodes()}

    while priority_queue:
        # Extract the node with the smallest current distance (O(log V))
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if a shorter path has already been found for this vertex
        if current_distance > distances[current_vertex]:
            continue

        # Relaxation step: Iterate over all neighbors
        for neighbor, data in graph[current_vertex].items():
            weight = data['weight']
            new_distance = current_distance + weight

            # Relaxation check: If a shorter path is found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                # Add the updated distance/vertex to the priority queue
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances, predecessors

# Helper function to reconstruct the path from the predecessors dictionary
def reconstruct_path(predecessors, start_node, target_node):
    path = deque()
    current = target_node
    while current is not None:
        path.appendleft(current)
        if current == start_node:
            return list(path)
        current = predecessors[current]
    return []

# Execution and Analysis
start_node = 'A'
distances, predecessors = dijkstra_custom(G, start_node)

print(f"--- Custom Dijkstra's Algorithm: Shortest Paths from {start_node} ---")

# Print results and reconstruct paths
for target_node, length in distances.items():
    path = reconstruct_path(predecessors, start_node, target_node)
    
    if length == float('infinity'):
        print(f"To {target_node}: Unreachable")
    else:
        print(f"To {target_node}: Length = {length}, Path = {path}")

# Visualization of the Weighted Graph (No Change)
plt.figure(figsize=(9, 7))
pos = nx.spring_layout(G, seed=42)

# Graph visualization
nx.draw(
    G, pos,
    with_labels=True,
    node_size=1500,
    node_color='lightgreen',
    font_size=16,
    font_weight='bold'
)

# Adding edge weights to the plot
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=14)

plt.title("City Transport Network Model (Weighted Graph)")
plt.show()