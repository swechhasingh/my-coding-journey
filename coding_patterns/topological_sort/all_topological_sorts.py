# Find all possible topological sorts in a acyclic directed graph
# At any stage, if we have more than one source available and since
# we can choose any source, therefore, in this case, we will have multiple
# orderings of the tasks. We can use a recursive approach with Backtracking
# to consider all sources at any step.
from collections import deque

# O(v!*E)
def find_all_topological_orderings(v, edges):
    if v <= 0:
        return []
    # initalize graph
    graph = {i: [] for i in range(v)}
    in_degree = {i: 0 for i in range(v)}

    # build graph from input
    for e in edges:
        p, c = e
        graph[p] += [c]
        in_degree[c] += 1

    # get sources
    sources = deque([i for i in in_degree if in_degree[i] == 0])
    all_topological_order_helper(graph, in_degree, sources, [])


def all_topological_order_helper(graph, in_degree, sources, curr_sorted_order):
    if not sources:
        if len(curr_sorted_order) == len(graph):
            print(curr_sorted_order)
        return
    for source in sources:
        next_sources = sources.copy()
        next_sources.remove(source)
        next_sorted_order = curr_sorted_order + [source]
        # loop over childern of source
        for child in graph[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                next_sources.append(child)
        all_topological_order_helper(graph, in_degree, next_sources, next_sorted_order)
        # backtrack indegree for every child of source
        for child in graph[source]:
            in_degree[child] += 1


def main():
    # graph = (# Vertices, Edges list)
    graph1 = (3, [[0, 1], [1, 2]])
    find_all_topological_orderings(*graph1)

    graph2 = (4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    find_all_topological_orderings(*graph2)

    graph3 = (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
    find_all_topological_orderings(*graph3)


if __name__ == "__main__":
    main()
