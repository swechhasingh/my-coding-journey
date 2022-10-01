import math
from typing import List

class InfiniteArray:
    def __init__(self, nums:List[int]):
        self.nums = nums

    def get(self, index):
        if index >= len(self.nums):
            return math.inf
        return self.nums[index]

def binary_search(arr, start, end, key):
    while start <= end:
        mid = (start + end)//2
        if arr.get(mid) == key:
            return mid
        if arr.get(mid) > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search_in_infinite_array(arr, key):
    start = 0
    end = 1
    # keep increasing exponentially (double) until we find the range that  can have the key
    while key > arr.get(end):
        new_end = end + (end - start + 1)*2
        start = end + 1
        end = new_end
    return binary_search(arr, start, end, key)


def main():
    inf_arr = InfiniteArray([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(inf_arr, 16)) # ans=6
    print(search_in_infinite_array(inf_arr, 11)) # ans=-1
    inf_arr = InfiniteArray([1, 3, 8, 10, 15]) 
    print(inf_arr.get(10))
    print(search_in_infinite_array(inf_arr, 15)) # ans=4
    print(search_in_infinite_array(inf_arr, 200)) #ans=-1


main()