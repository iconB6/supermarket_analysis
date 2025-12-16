import networkx as nx
import matplotlib.pyplot as plt

def build_summary_text(G, top_k=5):
    """
    Build a textual summary of the strongest item associations.
    """
    edges = sorted(
        G.edges(data=True),
        key=lambda x: x[2]["weight"],
        reverse=True
    )

    if not edges:
        return "No strong associations found."

    lines = ["Strongest associations:"]
    for u, v, data in edges[:top_k]:
        lines.append(f"- {u} & {v} (frequency: {data['weight']})")

    return "\n".join(lines)


def visualise_item_graph(item_graph, min_weight=2, top_n=15):
    """
    Visualise the item co-purchase graph, showing only strong associations.
    """
    # 1. Select top-N items by total co-purchase frequency
    scores = {
        item: sum(neighbors.values())
        for item, neighbors in item_graph.graph.items()
    }
    top_items = sorted(scores, key=scores.get, reverse=True)[:top_n]

    G = nx.Graph()

    for item in top_items:
        for neighbor, weight in item_graph.graph[item].items():
            if neighbor in top_items and weight >= min_weight:
                G.add_edge(item, neighbor, weight=weight)

    # 2. Layout optimisation
    pos = nx.spring_layout(G, k=1.4, iterations=60, seed=42)

    fig, ax = plt.subplots(figsize=(12, 9))


    # 3. Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=900,
        node_color="#A7C7E7",
        edgecolors="#4A6FA5",
        linewidths=1
    )

    # 4. Edge styling
    edges = G.edges(data=True)
    strong_edges = [(u, v) for u, v, d in edges if d["weight"] >= min_weight * 2]
    weak_edges = [(u, v) for u, v, d in edges if d["weight"] < min_weight * 2]

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=weak_edges,
        width=1,
        alpha=0.3,
        edge_color="#FFA6CB87",
        style="dashed"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=strong_edges,
        width=2,
        alpha=0.7,
        edge_color="#FF80C691",
        style="dashdot"
    )


    nx.draw_networkx_labels(
        G,
        pos,
        font_size=7,
        font_color="#000000"
    )

    summary_text = build_summary_text(G, top_k=5)

    # Add text box on the right side
    ax.text(
        1.02, 0.5,                 
        summary_text,
        transform=ax.transAxes,    
        fontsize=9,
        verticalalignment="center",
        bbox=dict(
            boxstyle="round,pad=0.4",
            facecolor="#F4F6F7",
            edgecolor="#BDC3C7"
        )
    )


    plt.title("Item Co-Purchase Network\n(Top Items and Strong Associations)",
        fontsize=12)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
