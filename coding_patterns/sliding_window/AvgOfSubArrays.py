# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.
from typing import List


def average_of_subarrays_of_size_K(array: List[int], K: int):
    avg_sums = []
    sum = 0
    # sum of elemnts form 0 to K-1 indices
    for i in range(K):
        sum += array[i]
    avg_sums.append(sum / K)
    start = 0
    for end in range(K, len(array)):
        sum = sum - array[start] + array[end]
        avg_sums.append(sum / K)
        start += 1
    return avg_sums


if __name__ == "__main__":
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(average_of_subarrays_of_size_K(array, 5))
