# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a function to return the area of the biggest island. 

# DFS approach
# time complexity: O(M*N) space complexity: O(M*N) (worst case DFS recursive stack)
from typing import List


def visit_island_dfs(matrix, i, j):
    island_area = 0
    # check for edges of the matrix
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0
    # check for water cells
    if matrix[i][j] == 0:
        return 0

    # mark (i,j) as visited by making it a water cell
    matrix[i][j] = 0
    island_area += 1
    # visit neighbours of (i,j)
    # bottom
    island_area += visit_island_dfs(matrix, i+1, j) 
    # top
    island_area += visit_island_dfs(matrix, i-1, j)
    # right
    island_area += visit_island_dfs(matrix, i, j+1)
    # left
    island_area += visit_island_dfs(matrix, i, j-1)

    return island_area

def find_area_of_biggest_island(matrix: List[List[int]]):
    largest_area = 0
    rows = len(matrix)
    cols = len(matrix[0])
    # iterate through every location in the input matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                largest_area = max(largest_area, visit_island_dfs(matrix, i, j))

    return largest_area

if __name__ == "__main__":
    matrix = [[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]
    print(find_area_of_biggest_island(matrix))

    matrix = [[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
    print(find_area_of_biggest_island(matrix))