def get_bitonic_array_maximum_index(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] > arr[mid+1]: #right half
            end = mid
        else: #left half
            start = mid +1
    # while loop breaks when 'start==end', and we have found the max element in bitonic arr
    return start

def order_agnostic_binary_search(arr, key, start, end):
    isAsc = arr[start] < arr[end]
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        if isAsc:
            if arr[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if arr[mid] > key:
                start = mid + 1
            else:
                end = mid - 1
    return -1

def find_key_in_bitonic_array(arr, key):
    max_idx = get_bitonic_array_maximum_index(arr)
    # search in left ascending part
    idx = order_agnostic_binary_search(arr, key, 0, max_idx)
    if idx != -1:
        return idx
    return order_agnostic_binary_search(arr, key, max_idx+1, len(arr)-1)

def main():
    print(find_key_in_bitonic_array([1, 3, 8, 4, 3], 4))
    print(find_key_in_bitonic_array([3, 8, 3, 1], 8))
    print(find_key_in_bitonic_array([1, 3, 8, 12], 12))
    print(find_key_in_bitonic_array([10, 9, 8], 10))


main()