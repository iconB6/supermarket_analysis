# 📊 Supermarket Item Relationship Analysis

## Overview

This project implements **Task 2: Data Structure and Algorithm** for the PAI Individual Assessment.

The system analyses a supermarket transaction dataset to model relationships between purchased items using an efficient data structure. It supports algorithmic queries and application-specific extensions, including:

* Recommendation-style queries
* Visualisation of strong item associations

A **test-driven development (TDD)** approach was adopted throughout the implementation.

---

## Dataset

* **File:** `Supermarket_dataset_PAI.csv`
* **Description:** Transactional supermarket purchase data
* Each row represents a transaction containing one or more purchased items

The dataset is preprocessed to extract transactions in a suitable format for graph construction.

---

## Data Structure Design

An **undirected weighted graph** is used to model item relationships:

* **Nodes:** Individual items
* **Edges:** Co-purchase relationships between items
* **Edge weights:** Frequency of co-occurrence

This structure efficiently supports:

* Incremental updates from transaction data
* Neighbour-based queries
* Graph traversal and ranking operations

---

## Algorithms Implemented

The following algorithms from the module content are used:

* **Linear Search** – querying co-purchase frequencies
* **Depth-First Search (DFS)** – discovering indirectly related items
* **Merge Sort** – ranking items by co-purchase frequency

No algorithms outside the taught syllabus are used.

---

## Application-Specific Extensions

### 1️⃣ Recommendation-Style Query (Command Line)

A recommendation-style query allows users to input an item and retrieve the most frequently co-purchased items.

#### How to Run

From the project root directory:

```bash
python demo_recom_query.py
```

#### Example Interaction

```text
=== Item Recommendation Demo ===
Enter an item: whole milk
Items frequently bought with 'whole milk':
  - other vegetables (frequency: 222)
  - rolls/buns (frequency: 209)
  - soda (frequency: 174)
  - yogurt (frequency: 167)
  - sausage (frequency: 134)
```

This script demonstrates how the recommendation-style query can be applied interactively without modifying the core analysis code.

---

### 2️⃣ Item Relationship Graph Visualisation

A visual representation of the item relationship graph is provided to highlight **strong co-purchase associations**.

Key features of the visualisation:

* Only the most frequently purchased items are displayed
* Weak associations are filtered out using a frequency threshold
* Strong associations are visually emphasised
* A textual summary highlights the strongest relationships shown in the graph

#### How to Run

From the project root directory:

```bash
python demo_visualization.py
```

The resulting figure can be displayed or captured for inclusion in the report.

---

## Testing and TDD Approach

Automated tests are provided in the `tests/` directory and were written **before or alongside** implementation to support a TDD workflow.

### Run Tests

```bash
pytest
```

### Test Coverage Includes

* Empty graph initialisation
* Single-item and multi-item transactions
* Queries for non-existent items
* DFS traversal edge cases
* Recommendation query correctness

---

## Project Structure

```text
.
├── src/
│   ├── data_loader.py
│   ├── item_graph.py
│   └── visualisation.py
│
├── tests/
│   ├── test_data_loader.py
│   └── test_item_graph.py
│
├── demo_recom_query.py
├── demo_visualization.py
│
├── Supermarket_dataset_PAI.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Notes

* Visualisation components focus on **presentation and interpretability** and do not affect the underlying algorithms.
* All core logic is implemented using data structures and algorithms covered in the module.
* Version control was managed using Git, with incremental commits reflecting the TDD workflow.

---

### 🔹 Environment Setup

This project uses a small number of standard Python libraries.
It is recommended to create a virtual environment before installing dependencies.

#### 1. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
```

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS / Linux:**

```bash
source venv/bin/activate
```

#### 2. Install dependencies using `requirements.txt`

```bash
pip install -r requirements.txt
```

#### 3. Run tests

```bash
pytest
```

#### 4. Run application demos

Recommendation-style query:

```bash
python demo_recom_query.py
```

Item relationship visualisation:

```bash
python demo_visualization.py
```
---
