
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from(["Ravensburg", "Stuttgart", "München", "Frankfurt", "Berlin", "Dresden", "Düsseldorf", "Wiesbaden"])

G.add_edge("Stuttgart", "Ravensburg", weight=2) 
G.add_edge("Ravensburg", "München", weight=3)
G.add_edge("München", "Berlin", weight=11)
G.add_edge("München", "Dresden", weight=5)
G.add_edge("München", "Frankfurt", weight=6)
G.add_edge("München", "Düsseldorf", weight=9)
G.add_edge("München", "Stuttgart", weight=4)
G.add_edge("Frankfurt", "Düsseldorf", weight=2)
G.add_edge("Frankfurt", "Stuttgart", weight=4)
G.add_edge("Frankfurt", "Berlin", weight=8)
G.add_edge("Frankfurt", "Wiesbaden", weight=1)
G.add_edge("Düsseldorf", "Berlin", weight=4)
G.add_edge("Düsseldorf", "Stuttgart", weight=5)
G.add_edge("Düsseldorf", "Dresden", weight=3)
G.add_edge("Dresden", "Berlin", weight=5)
G.add_edge("Berlin", "Stuttgart", weight=6)
G.add_edge("Stuttgart", "München", weight=4)

num_nodes = G.number_of_nodes() 
num_edges = G.number_of_edges()

print (num_nodes)
print (num_edges)
print(G.degree)

options = {
    'node_color': ['yellow','magenta','lightblue','lightgreen','pink', 'red', 'green', 'grey'],     # color of node
    'node_size': 3500,          # size of node
    'width': 5,                 # line width of edges
    'edge_color':'blue',        # edge color
}
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, **options)
nx.draw_networkx_edge_labels(
    G, 
    pos,
    edge_labels={
        ("Stuttgart", "Ravensburg"): "2 hours", 
        ("Ravensburg", "München"): "3 hours",
        ("Wiesbaden", "Frankfurt"): "1 hour",
        ("München", "Frankfurt"): "6 hours",
        ("München", "Berlin"): "11 hours",
        ("Berlin", "Dresden"): "5 hours",
        ("Frankfurt", "Berlin"): "8 hours",
        ("Frankfurt", "Düsseldorf"): "2 hours",
        ("Frankfurt", "Stuttgart"): "4 hours",
        ("Dresden", "München"): "5 hours",
        ("Düsseldorf", "München"): "9 hours",
        ("Berlin", "Düsseldorf"): "4 hours",
        ("Stuttgart", "Berlin"): "6 hours",
        ("Stuttgart", "München"): "4 hours"
    },
    font_color='red'
)
plt.show()

