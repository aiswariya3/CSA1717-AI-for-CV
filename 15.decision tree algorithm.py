import math
from collections import Counter

def entropy(data):
    total = len(data)
    label_counts = Counter([row[-1] for row in data])
    return -sum((count/total) * math.log2(count/total) for count in label_counts.values())

def split(data, column, value):
    true_split = [row for row in data if row[column] == value]
    false_split = [row for row in data if row[column] != value]
    return true_split, false_split

def best_split(data):
    best_gain = 0
    best_col = None
    best_val = None
    current_entropy = entropy(data)
    n_features = len(data[0]) - 1

    for col in range(n_features):
        values = set(row[col] for row in data)
        for val in values:
            true_rows, false_rows = split(data, col, val)
            if not true_rows or not false_rows:
                continue
            p = len(true_rows) / len(data)
            gain = current_entropy - (p * entropy(true_rows) + (1 - p) * entropy(false_rows))
            if gain > best_gain:
                best_gain, best_col, best_val = gain, col, val

    return best_col, best_val

def build_tree(data):
    col, val = best_split(data)
    if col is None:
        return Counter(row[-1] for row in data).most_common(1)[0][0]
    true_rows, false_rows = split(data, col, val)
    return {
        'column': col,
        'value': val,
        'true_branch': build_tree(true_rows),
        'false_branch': build_tree(false_rows)
    }

# Example dataset: [color, diameter, label]
dataset = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

tree = build_tree(dataset)
print("Decision Tree:", tree)
