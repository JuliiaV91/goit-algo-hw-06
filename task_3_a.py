
import networkx as nx
from task_1 import G

shortest_paths = nx.single_source_dijkstra_path(G, source = "Ravensburg", cutoff=None, weight='weight')
print(shortest_paths)

shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source= "Ravensburg")
print(shortest_path_lengths)

