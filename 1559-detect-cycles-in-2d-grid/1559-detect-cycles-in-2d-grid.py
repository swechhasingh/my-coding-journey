class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)), DFS recursion stack space in worst case when all the cells are 1
    """
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        # linear traversal of grid, input (-1,-1) bcoz cannot move to the cell that was visited in the last move.
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if self.__traverseIsland(grid, i, j, visited, -1, -1):
                        return True
                
        return False
                
        
    def __traverseIsland(self, grid, x, y, visited, prev_x, prev_y):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        
        # water cells and already visited cells
        if prev_x > -1 and prev_y > -1:
            if grid[x][y] != grid[prev_x][prev_y]:
                return False
        
            if visited[x][y] and grid[x][y] == grid[prev_x][prev_y]:
                return True
        
        # mark the current cell as visited
        visited[x][y] = True
        
        # recursively traverse all the neighbours of (x,y) cell
        if y+1 != prev_y and self.__traverseIsland(grid, x, y+1, visited, x, y): #right
            return True
        if y-1 != prev_y and self.__traverseIsland(grid, x, y-1, visited, x, y): #left
            return True
        if x-1 != prev_x and self.__traverseIsland(grid, x-1, y, visited, x, y): #up
            return True
        if x+1 != prev_x and self.__traverseIsland(grid, x+1, y, visited, x, y): #down
            return True
        return False