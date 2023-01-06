# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
from typing import List


def smallest_subarray_with_greater_sum(array: List[int], target_sum: int):
    smallest_window = len(array)
    start, end = 0, 0
    window_sum = 0
    while end < len(array):
        window_sum += array[end]
        while window_sum >= target_sum and start <= end:
            smallest_window = min(smallest_window, end - start + 1)
            window_sum -= array[start]
            start += 1
        end += 1
    return smallest_window


if __name__ == "__main__":
    array = [2, 1, 5, 2, 3, 2]
    print(smallest_subarray_with_greater_sum(array, 7))

    array = [2, 1, 5, 2, 8]
    print(smallest_subarray_with_greater_sum(array, 7))

    array = [3, 4, 1, 1, 6]
    print(smallest_subarray_with_greater_sum(array, 8))
