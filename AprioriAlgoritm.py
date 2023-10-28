from itertools import combinations

def load_data():
    # Replace this with your dataset or load data from a file.
    data = [
        ['item1', 'item2', 'item5'],
        ['item2', 'item4'],
        ['item2', 'item3'],
        ['item1', 'item2', 'item4'],
        ['item1', 'item3'],
        ['item2', 'item3'],
        ['item1', 'item3'],
        ['item1', 'item2', 'item3', 'item5'],
        ['item1', 'item2', 'item3'],
    ]
    return data

def create_candidates(itemset, length):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            candidate = list(set(itemset[i]) | set(itemset[j]))
            if len(candidate) == length:
                candidates.append(candidate)
    return candidates

def prune_candidates(candidates, prev_frequent_itemsets):
    pruned_candidates = []
    for candidate in candidates:
        is_valid = True
        for subset in combinations(candidate, len(candidate) - 1):
            if list(subset) not in prev_frequent_itemsets:
                is_valid = False
                break
        if is_valid:
            pruned_candidates.append(candidate)
    return pruned_candidates

def apriori(data, min_support):
    frequent_itemsets = []
    transaction_list = list(map(set, data))
    itemset = list(set(item for transaction in transaction_list for item in transaction))

    k = 1
    while itemset:
        if k == 1:
            candidates = [[item] for item in itemset]
        else:
            candidates = create_candidates(itemset, k)

        # Count support for candidates
        candidate_counts = {}
        for transaction in transaction_list:
            for candidate in candidates:
                if set(candidate).issubset(transaction):
                    if tuple(candidate) in candidate_counts:
                        candidate_counts[tuple(candidate)] += 1
                    else:
                        candidate_counts[tuple(candidate)] = 1

        # Prune candidates that don't meet the minimum support
        candidates = [list(candidate) for candidate in candidates if
                    candidate_counts.get(tuple(candidate), 0) >= min_support]

        frequent_itemsets.extend(candidates)
        k += 1

        itemset = list(set(item for candidate in candidates for item in candidate))

    return frequent_itemsets

if __name__ == '__main__':
    data = load_data()
    min_support = int(input("Enter the minimum support count : "))
    frequent_itemsets = apriori(data, min_support)
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)
