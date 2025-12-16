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

def test_add_transaction_with_single_item():
    """
    Edge case: transaction with only one item should not create edges.
    """
    graph = ItemGraph()
    graph.add_transaction(["bread"])

    assert "bread" not in graph.graph or graph.graph["bread"] == {}

# Linear Search test
def test_is_frequently_bought_linear_search():
    """
    Edge cases:
    - frequent pair exists
    - queried pair does not exist
    """
    graph = ItemGraph()
    graph.add_transaction(["bread", "milk"])
    graph.add_transaction(["bread", "milk"])

    assert graph.is_frequently_bought("bread", "milk", threshold=2) is True
    assert graph.is_frequently_bought("bread", "eggs", threshold=1) is False


def test_is_frequently_bought_item_not_in_graph():
    """
    Edge case: querying items not present in the graph.
    """
    graph = ItemGraph()
    assert graph.is_frequently_bought("bread", "milk", threshold=1) is False

