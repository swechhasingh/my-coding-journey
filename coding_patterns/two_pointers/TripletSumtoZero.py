# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.


from typing import List

# time complexity: O(NlogN + N^2) -> O(N^2) and space complexity: O(N)
def find_all_unique_triplets(array: List[int]):
    # sort the array, in-place sorting
    array.sort()
    triplets = []
    for i in range(len(array)):
        # skip duplicate number to get unique triplets
        if i > 0 and array[i] == array[i - 1]:
            continue
        search_triplets(array, triplets, i + 1, -array[i])

    return triplets


def search_triplets(array, triplets, left, target_sum):
    right = len(array) - 1
    while left < right:
        curr_sum = array[left] + array[right]
        if curr_sum == target_sum:
            triplets.append([-target_sum, array[left], array[right]])
            left += 1
            right -= 1
            # skip duplicate number to get unique triplets
            while left < right and array[left] == array[left - 1]:
                left += 1
            # skip duplicate number to get unique triplets
            while left < right and array[right] == array[right + 1]:
                right -= 1
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    array = [-3, 0, 1, 2, -1, 1, -2]
    print(find_all_unique_triplets(array))

    array = [-5, 2, -1, -2, 3]
    print(find_all_unique_triplets(array))
