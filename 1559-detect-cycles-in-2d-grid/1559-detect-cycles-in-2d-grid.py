class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)), DFS recursion stack space in worst case when all the cells are 1
    """
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        # linear traversal of grid
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if self.__traverseIsland(grid, i, j, visited, grid[i][j], -1, -1):
                        return True
                
        return False
                
        
    def __traverseIsland(self, grid, x, y, visited, start_value, prev_x, prev_y):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        
        # cell with different value from previous cell
        if grid[x][y] != start_value:
            return False

        # already visited cell and same value as the previous cell
        if visited[x][y]:
            return True
        
        # mark the current cell as visited
        visited[x][y] = True
        
        # recursively traverse all the neighbours of (x,y) cell
        # cannot move to the cell that was visited in the last move
        if y+1 != prev_y and self.__traverseIsland(grid, x, y+1, visited, start_value, x, y): #right
            return True
        if y-1 != prev_y and self.__traverseIsland(grid, x, y-1, visited, start_value, x, y): #left
            return True
        if x-1 != prev_x and self.__traverseIsland(grid, x-1, y, visited, start_value, x, y): #up
            return True
        if x+1 != prev_x and self.__traverseIsland(grid, x+1, y, visited, start_value, x, y): #down
            return True
        return False