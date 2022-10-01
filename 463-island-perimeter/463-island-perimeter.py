class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)), DFS recursion stack space in worst case when all the cells are 1
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
                
        # linear traversal of grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    return self.__traverseIsland(grid, i, j, visited)
                    
                
        return 0
                
        
    def __traverseIsland(self, grid, x, y, visited):
        """DFS traverse of island using recursion
        """
        # boundary cases will be part of perimeter
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 1
        
        # water cells will be part of perimeter
        if grid[x][y] == 0:
            return 1
        
        # already visited cells don't contribute to perimeter
        if visited[x][y]:
            return 0
        
        # mark the current cell as visited
        visited[x][y] = True
        
        island_perimeter = 0
        # recursively traverse all the neighbours of (x,y) cell
        island_perimeter += self.__traverseIsland(grid, x, y+1, visited) #right
        island_perimeter += self.__traverseIsland(grid, x, y-1, visited) #left
        island_perimeter += self.__traverseIsland(grid, x-1, y, visited) #up
        island_perimeter += self.__traverseIsland(grid, x+1, y, visited) #down
        return island_perimeter