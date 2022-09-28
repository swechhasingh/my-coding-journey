class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)) recursive DFS stack space in worst case when all the cells are 1
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        n_closed_islands = 0
        
        # linear traversal of grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and not visited[i][j]:
                    if self.__traverseIsland(grid, i, j, visited):
                        n_closed_islands += 1
                
        return n_closed_islands
                
        
    def __traverseIsland(self, grid, x, y, visited):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        
        # water cells and already visited cells
        if grid[x][y] == 1 or visited[x][y]:
            return True
        
        # mark the current cell as visited
        visited[x][y] = True
        
        is_closed = True
        # recursively traverse all the neighbours of (x,y) cell
        is_closed &= self.__traverseIsland(grid, x, y+1, visited) #right
        is_closed &= self.__traverseIsland(grid, x, y-1, visited) #left
        is_closed &= self.__traverseIsland(grid, x-1, y, visited) #up
        is_closed &= self.__traverseIsland(grid, x+1, y, visited) #down
        return is_closed