def search_min_diff_element(arr, target):
    # boundary cases
    if target > arr[-1]:
        return arr[-1]
    if target < arr[0]:
        return arr[0]
    
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return arr[mid] # if the target is present then min diff element will be target itself

    # while loop breaks when 'start == end+1'
    # when target is not present in the arr, start will point to number greater than target and end will point to number less than target
    # i.e arr[end] < target < arr[start]
    if (arr[start]-target) < (target-arr[end]):
        return arr[start]
    return arr[end]

def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
