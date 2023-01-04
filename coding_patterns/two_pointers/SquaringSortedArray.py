# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

from typing import List

# time complexity: O(N) and space complexity: O(N)
def square_sorted_array(array: List[int]):
    # find the positon of first non-negative number
    pos_pointer = 0
    while pos_pointer < len(array):
        if array[pos_pointer] >= 0:
            break
        pos_pointer += 1

    sq_array = []
    left, right = pos_pointer - 1, pos_pointer
    while left >= 0 and right < len(array):
        left_sq = array[left] * array[left]
        right_sq = array[right] * array[right]
        if left_sq <= right_sq:
            sq_array.append(left_sq)
            left -= 1
        else:
            sq_array.append(right_sq)
            right += 1
    while left >= 0:
        sq_array.append(left_sq)
        left -= 1

    while right < len(array):
        sq_array.append(right_sq)
        right += 1
    return sq_array


if __name__ == "__main__":
    a = [-2, -1, 0, 2, 3]
    print(square_sorted_array(a))

    a = [-3, -1, 0, 1, 2]
    print(square_sorted_array(a))
