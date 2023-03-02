# Alien dictionary
from collections import deque

# O(v!*E)
def find_all_topological_orderings(words):
    if len(words) <= 0:
        return []
    L = len(words)
    graph = dict()
    vertices = set()
    for i in range(L - 1):
        curr_w, next_w = words[i], words[i + 1]
        for p, c in zip(curr_w, next_w):
            if p == c:
                if p not in graph:
                    graph[p] = set()
                    vertices.add(p)
                continue
            if p in graph:
                vertices.add(c)
                graph[p].add(c)
            else:
                vertices.add(p)
                vertices.add(c)
                graph[p] = set([c])
            break

    v = len(vertices)
    # initalize graph
    in_degree = {node: 0 for node in vertices}

    # build graph from input
    for p in graph:
        for c in graph[p]:
            in_degree[c] += 1
    # get sources
    sources = deque([i for i in in_degree if in_degree[i] == 0])
    char_order = []
    while sources:
        curr_source = sources.popleft()
        char_order.append(curr_source)
        if curr_source in graph:
            for child in graph[curr_source]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

    print("".join(char_order))


def main():
    # graph = (# Vertices, Edges list)
    words = ["ba", "bc", "ac", "cab"]
    find_all_topological_orderings(words)

    words = ["cab", "aaa", "aab"]
    find_all_topological_orderings(words)

    words = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
    find_all_topological_orderings(words)


if __name__ == "__main__":
    main()
