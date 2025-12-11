import networkx as nx
import matplotlib.pyplot as plt

# Graph Creation: City Transport Network Model
# Nodes: Intersections (A, B, C, D, E, F)
# Edges: Roads between intersections
G = nx.Graph()

# Adding edges (roads)
G.add_edges_from([
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'),
    ('D', 'F'),
    ('E', 'F')
])

# Analysis of main characteristics
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()

# Calculating the degree for each vertex
degrees = dict(G.degree())

print(f"--- City Transport Network Graph Analysis ---")
print(f"Number of vertices (Intersections): {num_vertices}")
print(f"Number of edges (Road segments): {num_edges}")
print("Vertex Degrees (Number of roads exiting an intersection):")
for vertex, degree in degrees.items():
    print(f"  Intersection {vertex}: {degree}")

# Graph Visualization
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_size=1500,
    node_color='lightcoral',
    font_size=16,
    font_weight='bold'
)
plt.title("City Transport Network Model (Unweighted Graph)")
plt.show()