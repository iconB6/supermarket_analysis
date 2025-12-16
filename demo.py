from src.data_loader import load_transactions_from_csv
from src.item_graph import ItemGraph
from src.visualisation import visualise_item_graph

transactions = load_transactions_from_csv("Supermarket_dataset_PAI.csv")

graph = ItemGraph()
for t in transactions:
    graph.add_transaction(t)

visualise_item_graph(graph, min_weight=5)
