"""
demo_sort_benchmark.py

Benchmark Quick Sort and Merge Sort under two scenarios:
1. Neighbour list sizes derived from the current supermarket dataset
2. Simulated larger-scale neighbour lists for future scalability analysis

This script is for experimental validation only.
"""

import time
import random
import csv
from collections import defaultdict
from src.item_graph import ItemGraph


# ---------- Scenario 1: Based on current dataset ----------

def load_neighbour_sizes_from_csv(csv_path):
    """
    Load the supermarket dataset and estimate neighbour list sizes
    based on co-occurring items in each transaction.
    """
    transactions = defaultdict(set)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            transaction_id = row[0]
            item = row[1]
            transactions[transaction_id].add(item)

    neighbour_sizes = []
    for items in transactions.values():
        size = len(items)
        if size > 1:
            neighbour_sizes.append(size - 1)

    return neighbour_sizes


# ---------- Scenario 2: Simulated large-scale data ----------

def generate_mock_neighbours(n):
    """
    Generate a mock neighbour list of (item, frequency) tuples.
    """
    return [(f"Item_{i}", random.randint(1, 1000)) for i in range(n)]


# ---------- Benchmark ----------

def benchmark_sort(graph, data):
    """
    Benchmark quick sort and merge sort on the same data.
    """
    data_quick = data.copy()
    data_merge = data.copy()

    start = time.perf_counter()
    graph.quick_sort(data_quick)
    quick_time = time.perf_counter() - start

    start = time.perf_counter()
    graph.merge_sort(data_merge)
    merge_time = time.perf_counter() - start

    return quick_time, merge_time


def benchmark_current_dataset(graph, csv_path):
    print("\nScenario 1: Current Dataset (Neighbour Sizes)")
    print("-" * 55)

    sizes = load_neighbour_sizes_from_csv(csv_path)
    sample_sizes = sorted(set(sizes))[:5]
    print(f"sample_sizes is {sample_sizes}\n")

    for n in sample_sizes:
        data = generate_mock_neighbours(n)
        qt, mt = benchmark_sort(graph, data)
        print(
            f"n={n:<4} | "
            f"Quick Sort: {qt:.6f}s | "
            f"Merge Sort: {mt:.6f}s"
        )


def benchmark_future_scale(graph):
    print("\nScenario 2: Simulated Large-Scale Data")
    print("-" * 55)

    for n in [50, 100, 500, 1000, 5000]:
        data = generate_mock_neighbours(n)
        qt, mt = benchmark_sort(graph, data)
        print(
            f"n={n:<5} | "
            f"Quick Sort: {qt:.6f}s | "
            f"Merge Sort: {mt:.6f}s"
        )


def main():
    graph = ItemGraph()

    print("Sorting Algorithm Benchmark")
    print("=" * 55)

    benchmark_current_dataset(
        graph,
        "Supermarket_dataset_PAI.csv"
    )

    benchmark_future_scale(graph)


if __name__ == "__main__":
    main()
