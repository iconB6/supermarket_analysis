from src.data_loader import load_transactions_from_csv

def test_load_transactions_structure():
    transactions = load_transactions_from_csv("Supermarket_dataset_PAI.csv")

    assert isinstance(transactions, list)
    assert isinstance(transactions[0], list)
    assert len(transactions[0]) >= 1