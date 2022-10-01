def bitonic_array_maximum(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] > arr[mid+1]: #right half
            end = mid
        else: #left half
            start = mid +1
    # while loop breaks when 'start==end', and we have found the max element in bitonic arr
    return arr[start]

def main():
    print(bitonic_array_maximum([1, 3, 8, 12, 4, 2]))
    print(bitonic_array_maximum([3, 8, 3, 1]))
    print(bitonic_array_maximum([1, 3, 8, 12]))
    print(bitonic_array_maximum([10, 9, 8]))


main()