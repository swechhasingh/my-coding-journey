def find_single_numbers(arr):
    num1_xor_num2 = 0
    for x in arr:
        num1_xor_num2 ^= x

    #find the rightmost '1' bit in num1_xor_num2
    rightmost_one_bit = 1
    while (rightmost_one_bit & num1_xor_num2 == 0):
        rightmost_one_bit <<= 1
    
    num1, num2 = 0, 0
    for x in arr:
        if (x & rightmost_one_bit) != 0: #the bit is set
            num1 ^= x
        else: #the bit is not set
            num2 ^= x

    return num1, num2
    
def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()