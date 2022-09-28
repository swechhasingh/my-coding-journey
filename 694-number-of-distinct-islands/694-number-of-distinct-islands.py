class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)), DFS recursion stack space in worst case when all the cells are 1
    """
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        distinct_islands = set()
        
        # linear traversal of grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_traverse = self.__traverseIsland(grid, i, j, visited, "O")
                    distinct_islands.add(island_traverse)
        print(distinct_islands)
        return len(distinct_islands)
                
        
    def __traverseIsland(self, grid, x, y, visited, island_traverse):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return ""
        
        # water cells and already visited cells
        if grid[x][y] == 0 or visited[x][y]:
            return ""
        
        # mark the current cell as visited
        visited[x][y] = True
        
        
        # recursively traverse all the neighbours of (x,y) cell
        island_traverse += self.__traverseIsland(grid, x, y+1, visited, "R") #right
        island_traverse += self.__traverseIsland(grid, x, y-1, visited, "L") #left
        island_traverse += self.__traverseIsland(grid, x-1, y, visited, "U") #up
        island_traverse += self.__traverseIsland(grid, x+1, y, visited, "D") #down
        island_traverse += 'B' # key to differentiate paths
        return island_traverse