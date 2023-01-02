# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target

from typing import List

# time complexity: O(N) and space complexity: O(1)
def find_pair_with_target_sum(array: List[int], target: int):
    start, end = 0, len(array) - 1
    while start < end:
        if array[start] + array[end] == target:
            return [array[start], array[end]]
        elif array[start] + array[end] < target:
            start += 1
        else:
            end -= 1

    return []

if __name__ == "__main__":
    array = [0,1,2,3,4,5,6,7,8,9]
    target = 13
    print(find_pair_with_target_sum(array,target))

    array = [0,1,2,3,4,5,6,7,8,9]
    target = 20
    print(find_pair_with_target_sum(array,target))

    array = [0,1,2,3,4,5,6,7,8,9]
    target = -1
    print(find_pair_with_target_sum(array,target))

    array = [0,1,2,3,4,5,6,7,8,9]
    target = 4
    print(find_pair_with_target_sum(array,target))
