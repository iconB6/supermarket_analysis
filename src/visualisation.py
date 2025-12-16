import networkx as nx
import matplotlib.pyplot as plt


def visualise_item_graph(item_graph, min_weight=2):
    """
    Visualise the item co-purchase graph, showing only strong associations.
    """
    G = nx.Graph()

    for item, neighbors in item_graph.graph.items():
        for neighbor, weight in neighbors.items():
            if weight >= min_weight:
                G.add_edge(item, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    edge_weights = [G[u][v]["weight"] for u, v in G.edges()]

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1500,
        font_size=9,
        width=edge_weights
    )

    plt.title("Item Co-Purchase Network (Strong Associations)")
    plt.show()
