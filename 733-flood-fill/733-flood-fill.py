class Solution:
    """Time complexity: O(M*N), linear traversal of all elements of the grid
    Space complexity: O(min(M*N)), DFS recursion stack space in worst case when all the cells are 1
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        
        # visited matrix: boolean matrix to keep track of already visited cells
        visited= [[False for _ in range(cols)] for _ in range(rows)]
        
        start_color = image[sr][sc]
        self.__traverseIsland(image, sr, sc, visited, start_color, color)
        
        return image
                
        
    def __traverseIsland(self, image, x, y, visited, start_color, new_color):
        """DFS traverse of island using recursion
        """
        # boundary cases
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return
        
        # cell with color different than start color and already visited cells
        if image[x][y] != start_color or visited[x][y]:
            return 
        
        # mark the current cell as visited
        visited[x][y] = True
        image[x][y] = new_color
        
        # recursively traverse all the neighbours of (x,y) cell
        self.__traverseIsland(image, x, y+1, visited, start_color, new_color) #right
        self.__traverseIsland(image, x, y-1, visited, start_color, new_color) #left
        self.__traverseIsland(image, x-1, y, visited, start_color, new_color) #up
        self.__traverseIsland(image, x+1, y, visited, start_color, new_color) #down
        return
        
        