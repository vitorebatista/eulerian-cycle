from matplotlib import pyplot as plt
import networkx as nx

def image(graph):
    G=nx.Graph()
    G.add_nodes_from(graph.get_vertices())
    G.add_edges_from(graph.get_edges())
    # print("Nodes of graph: ")
    # print(G.nodes())
    # print("Edges of graph: ")
    # print(G.edges())
    
    nx.draw(G, node_size = 800, node_color="red", with_labels = True)
    plt.savefig(graph.image_file().replace('graph','png'))
    plt.show()