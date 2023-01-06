from typing import List


def visit_island_dfs(matrix: List[List[int]], x: int, y: int):

    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 0
    if matrix[x][y] == 0:
        return 1

    # mark visited by making it water cell
    matrix[x][y] = 0

    is_closed_island = (
        visit_island_dfs(matrix, x + 1, y)
        and visit_island_dfs(matrix, x - 1, y)
        and visit_island_dfs(matrix, x, y + 1)
        and visit_island_dfs(matrix, x, y - 1)
    )
    return is_closed_island


def find_number_of_closed_islands(matrix: List[List[int]]):
    rows = len(matrix)
    cols = len(matrix[0])
    num_closed_islands = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                num_closed_islands += visit_island_dfs(matrix, i, j)
    return num_closed_islands


if __name__ == "__main__":
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print(find_number_of_closed_islands(matrix))

    matrix = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    print(find_number_of_closed_islands(matrix))
