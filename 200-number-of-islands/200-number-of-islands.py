class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)) recursive DFS stack space in worst case
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        island_count = 0
        
        # linear traversal of grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    island_count += 1
                    self.__traverseIsland(grid, i, j, visited)
                
        return island_count
                
        
    def __traverseIsland(self, grid, x, y, visited):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        
        # water cells and already visited cells
        if grid[x][y] == '0' or visited[x][y]:
            return
        
        # mark the current cell as visited
        visited[x][y] = True
        
        # recursively traverse all the neighbours of (x,y) cell
        self.__traverseIsland(grid, x, y+1, visited) #right
        self.__traverseIsland(grid, x, y-1, visited) #left
        self.__traverseIsland(grid, x-1, y, visited) #up
        self.__traverseIsland(grid, x+1, y, visited) #down
        return
        