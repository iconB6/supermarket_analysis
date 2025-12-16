from src.data_loader import load_transactions_from_csv
from src.item_graph import ItemGraph


def main():
    # 1. Load dataset
    csv_path = "Supermarket_dataset_PAI.csv"
    transactions = load_transactions_from_csv(csv_path)

    # 2. Build item graph
    graph = ItemGraph()
    for transaction in transactions:
        graph.add_transaction(transaction)

    print("=== Item Recommendation Demo ===")
    print("Type an item name to get recommendations.")
    print("Type 'exit' to quit.\n")

    # 3. Interactive query loop
    while True:
        user_input = input("Enter an item: ").strip().lower()

        if user_input == "exit":
            print("Exiting recommendation demo.")
            break

        if not user_input:
            print("⚠️  Please enter a valid item name.\n")
            continue

        recommendations = graph.recommend_items([user_input], k=5)

        if not recommendations:
            print(f"No recommendations found for '{user_input}'.\n")
            continue

        print(f"Items frequently bought with '{user_input}':")
        for item, score in recommendations:
            print(f"  - {item} (frequency: {score})")
        print()


if __name__ == "__main__":
    main()
