# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

from typing import List

# time complexity: O(N) and space complexity: O(1)
def max_sum_subarray(array: List[int], K: int):
    max_sum = 0
    curr_sum = 0
    start = 0
    for i in range(len(array)):
        if i < K:
            curr_sum += array[i]
        if i >= K:
            max_sum = max(max_sum, curr_sum)
            curr_sum = curr_sum + array[i] - array[start]
            start += 1
    return max_sum


if __name__ == "__main__":
    array = [2, 1, 5, 1, 3, 2]
    print(max_sum_subarray(array, 3))

    array = [2, 3, 4, 1, 5]
    print(max_sum_subarray(array, 2))
