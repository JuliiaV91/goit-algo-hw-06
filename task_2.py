
import networkx as nx
from task_1 import G

def print_path(algorithm, source, target):
    if algorithm == "DFS":
        path = nx.dfs_tree(G, source=source)
    elif algorithm == "BFS":
        path = nx.bfs_tree(G, source=source)
    
    try:
        print(f"{algorithm} path from {source} to {target}: {nx.shortest_path(path, source=source, target=target)}")
    except nx.NetworkXNoPath:
        print(f"No {algorithm} path from {source} to {target}")

print_path("DFS", "Ravensburg", "Dresden")
print_path("BFS", "Ravensburg", "Dresden")

