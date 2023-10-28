import numpy as np

def page_rank(links, num_iterations=100, damping_factor=0.85):
    num_pages = len(links)
    initial_rank = np.ones(num_pages) / num_pages
    rank = initial_rank.copy()

    for _ in range(num_iterations):
        for i in range(num_pages):
            rank[i] = (1 - damping_factor) / num_pages
            for j in range(num_pages):
                if links[j, i]:
                    rank[i] += damping_factor * rank[j] / links[j].sum()

    return rank

# Example:
# Let's create a simple example with 4 web pages and their links:
# Page A links to Page B and Page C
# Page B links to Page C
# Page C links to Page A
# Page D has no links.

links = np.array([
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
])

result = page_rank(links)

# Print the result 
# ans
for i, rank in enumerate(result):
    print(f"Page {i}: Rank = {rank:.4f}")
