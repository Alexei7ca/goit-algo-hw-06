import networkx as nx
import matplotlib.pyplot as plt

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

# Implementation of Dijkstra's Algorithm (Using NetworkX)
start_node = 'A'

# Finding the shortest path from 'A' to all other vertices
shortest_paths = nx.shortest_path(G, source=start_node, weight='weight')
shortest_path_lengths = nx.shortest_path_length(G, source=start_node, weight='weight')

print(f"--- Dijkstra's Algorithm: Shortest Paths from {start_node} ---")

for target, length in shortest_path_lengths.items():
    path = shortest_paths[target]
    print(f"To {target}: Length = {length}, Path = {path}")

# Visualization of the Weighted Graph
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