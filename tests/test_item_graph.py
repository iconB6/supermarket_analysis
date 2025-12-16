from src.item_graph import ItemGraph

# ItemGraph initialization test
def test_item_graph_initialisation():
    graph = ItemGraph()
    assert graph is not None
    assert graph.graph == {} or len(graph.graph) == 0