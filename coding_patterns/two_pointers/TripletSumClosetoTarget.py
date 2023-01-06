# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return **the sum of the triplet with the smallest sum**.

import math
from typing import List

# time complexity: O(NLogN+N^2) and space complexitty: O(N)
def find_triplet_sum_close_to_target(array: List[int], target_sum: int):
    array.sort()
    min_diff = math.inf
    triplet_sum = 0
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            curr_triplet_sum = array[i] + array[left] + array[right]
            curr_diff = target_sum - curr_triplet_sum
            if curr_diff == 0:
                return curr_triplet_sum

            # If there are more than one such triplet, return the sum of the triplet with the smallest sum
            if abs(curr_diff) < abs(min_diff) or (
                abs(curr_diff) == abs(min_diff) and curr_triplet_sum < triplet_sum
            ):
                min_diff = curr_diff
                triplet_sum = curr_triplet_sum
            if curr_diff > 0:
                left += 1
            else:
                right -= 1

    return triplet_sum


if __name__ == "__main__":
    print(find_triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(find_triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(find_triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(find_triplet_sum_close_to_target([0, 0, 1, 1, 2, 6], 5))
