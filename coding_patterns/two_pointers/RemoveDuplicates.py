# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once.

from typing import List


def remove_duplicates(array: List[int]):
    # pointer for placing the next non-duplicate number
    left = 0
    # pointer for iterating the array
    right = 0
    while right < len(array):
        while array[left] == array[right]:
            right += 1
            if right == len(array):
                return array[: left + 1]
        left += 1
        array[left] = array[right]
        right += 1
    return array[: left + 1]


# time complexity: O(N) and space complexity: O(1)
def remove_duplicates2(array: List[int]):
    # pointer for placing the next non-duplicate number
    next_non_duplicate = 0
    # pointer for iterating the array
    next = 0
    while next < len(array):
        if array[next_non_duplicate - 1] != array[next]:
            array[next_non_duplicate] = array[next]
            next_non_duplicate += 1
        next += 1
    return array[:next_non_duplicate]


# time complexity: O(N) and space complexity: O(1)
def remove_duplicates_from_unsorted_array(array: List[int], key: int):
    # pointer for placing the next non-duplicate number
    next_element = 0
    # pointer for iterating the array
    next = 0
    while next < len(array):
        if array[next] != key:
            array[next_element] = array[next]
            next_element += 1
        next += 1
    return array[:next_element]


if __name__ == "__main__":
    array = [2, 3, 3, 3, 6, 9, 9]
    print(remove_duplicates2(array))

    array = [2, 2, 2, 11]
    print(remove_duplicates2(array))

    array = [3, 2, 3, 6, 3, 10, 9, 3]
    print(remove_duplicates_from_unsorted_array(array, key=3))

    array = [2, 11, 2, 2, 1]
    print(remove_duplicates_from_unsorted_array(array, key=2))
