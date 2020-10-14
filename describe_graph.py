import networkx as nx
import argparse

#--------------------------------------#
# Reading Graph
#--------------------------------------#
G = nx.read_adjlist("graph.adjlist")

print(f"Users: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
