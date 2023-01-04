# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.


from typing import List, Tuple

# time (fill the whole image) and space (DFS recursion stack) comlexity: O(M*N)
def color_image(image: List[List[int]], x: int, y: int, old_color: int, new_color: int):
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
        return
    if image[x][y] != old_color:
        return
    image[x][y] = new_color
    color_image(image, x + 1, y, old_color, new_color)
    color_image(image, x - 1, y, old_color, new_color)
    color_image(image, x, y + 1, old_color, new_color)
    color_image(image, x, y - 1, old_color, new_color)
    return


def flood_fill_image(image: List[List[int]], start_pixel: Tuple, new_color: int):

    old_color = image[start_pixel[0]][start_pixel[1]]
    color_image(image, start_pixel[0], start_pixel[1], old_color, new_color)
    return image


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    print(flood_fill_image(matrix, (1, 3), 2))

    matrix = [
        [1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ]
    print(flood_fill_image(matrix, (2, 2), 3))
