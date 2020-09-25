import matplotlib.pyplot as plt
import networkx as nx
import argparse

#--------------------------------------#
# Parse Command Line Arguments
#--------------------------------------#
parser = argparse.ArgumentParser(description='Visualise basic connections within the mutual graph.')
parser.add_argument('--egos', dest='ego_users', nargs='+', 
                    action='store',
                    help='Users to analyse mutuals of.')
args = parser.parse_args()

#--------------------------------------#
# Reading Graph
#--------------------------------------#
G = nx.read_adjlist("graph.adjlist")

#--------------------------------------#
# Show only users that are mutual to the given users
#--------------------------------------#
subgraph_nodes = set()

for user in args.ego_users:
    subgraph_nodes.add(user)
    subgraph_nodes.update(G.neighbors(user))

subgraph = G.subgraph(subgraph_nodes)

## Filter by minimum degree
minimum_degree = 2
removed_nodes = [user for user in subgraph_nodes if subgraph.degree(user) < minimum_degree]
G.remove_nodes_from(removed_nodes)

nx.draw(subgraph, with_labels=True, node_size = 100)
plt.show()