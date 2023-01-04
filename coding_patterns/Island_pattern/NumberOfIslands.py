# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

from typing import List
from collections import deque

# DFS approach
# time complexity: O(M*N) space complexity: O(M*N) (worst case DFS recursive stack)
def visit_island_dfs(matrix, i, j):
    # check for edges of the matrix
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    # check for water cells
    if matrix[i][j] == 0:
        return

    # mark (i,j) as visited by making it a water cell
    matrix[i][j] = 0

    # visit neighbours of (i,j)
    # bottom
    visit_island_dfs(matrix, i + 1, j)
    # top
    visit_island_dfs(matrix, i - 1, j)
    # right
    visit_island_dfs(matrix, i, j + 1)
    # left
    visit_island_dfs(matrix, i, j - 1)


# time complexity: O(M*N) and space complexity: O(min(M,N)) (worst case deque size)
def visit_island_bfs(matrix, i, j):
    neighbours = deque([(i, j)])
    while neighbours:
        x, y = neighbours.popleft()
        # check for edges of the matrix
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            continue
        # check for water cells
        if matrix[x][y] == 0:
            continue

        # mark (x,y) as visited by making it a water cell
        matrix[x][y] = 0

        # push all the neighbours of (x,y) in the neighbours queue
        neighbours.extend([(x + 1, y)])
        neighbours.extend([(x - 1, y)])
        neighbours.extend([(x, y + 1)])
        neighbours.extend([(x, y - 1)])


def find_number_of_islands(matrix: List[List[int]]):
    count_islands = 0
    rows = len(matrix)
    cols = len(matrix[0])
    # iterate through every location in the input matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count_islands += 1
                visit_island_bfs(matrix, i, j)

    return count_islands


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print(find_number_of_islands(matrix))

    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    print(find_number_of_islands(matrix))
