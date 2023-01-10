# The given matrix has only one island, write a function to find the perimeter of that island.


from typing import List

# DFS approach
# time complexity: O(M*N) space complexity: O(M*N) (visited matrix and worst case DFS recursive stack)
def visit_island_dfs(matrix, i, j, visited):
    perimeter = 0
    # check for edges of the matrix
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 1
    # check for water cells
    if matrix[i][j] == 0:
        return 1
    if visited[i][j]:
        return 0

    # mark (i,j) as visited
    visited[i][j] = True

    # visit neighbours of (i,j)
    # bottom
    perimeter += visit_island_dfs(matrix, i + 1, j, visited)
    # top
    perimeter += visit_island_dfs(matrix, i - 1, j, visited)
    # right
    perimeter += visit_island_dfs(matrix, i, j + 1, visited)
    # left
    perimeter += visit_island_dfs(matrix, i, j - 1, visited)

    return perimeter


def find_island_perimeter(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                return visit_island_dfs(matrix, i, j, visited)


if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print(f"Island perimeter: {find_island_perimeter(matrix)}")

    matrix = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0]]
    print(f"Island perimeter: {find_island_perimeter(matrix)}")
