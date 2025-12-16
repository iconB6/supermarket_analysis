import csv
from collections import defaultdict

def load_transactions_from_csv(file_path):
    transactions = defaultdict(list)

    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = (row["Member_number"], row["Date"])
            transactions[key].append(row["itemDescription"])

    return list(transactions.values())

