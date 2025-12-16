from src.item_graph import ItemGraph

# ItemGraph initialization test
def test_item_graph_initialisation():
    graph = ItemGraph()
    assert graph is not None
    assert graph.graph == {} or len(graph.graph) == 0

# Transaction processing test
def test_add_single_transaction():
    """
    Normal case: adding a valid transaction with two items.
    """
    graph = ItemGraph()
    graph.add_transaction(["bread", "milk"])

    assert graph.graph["bread"]["milk"] == 1
    assert graph.graph["milk"]["bread"] == 1


def test_item_graph_initialisation():
    """
    Edge case: empty graph initialisation.
    """
    graph = ItemGraph()
    assert graph is not None
    assert graph.graph == {} or len(graph.graph) == 0


def test_add_transaction_with_single_item():
    """
    Edge case: transaction with only one item should not create edges.
    """
    graph = ItemGraph()
    graph.add_transaction(["bread"])

    assert "bread" not in graph.graph or graph.graph["bread"] == {}

