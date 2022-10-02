def find_single_number(arr):
    xor = arr[0]
    for i in range(1,len(arr)):
        xor ^= arr[i]

    return xor
    
def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()