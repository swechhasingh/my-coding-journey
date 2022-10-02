# number ^ complement = all_bits_set
# number ^ number ^ complement = number ^ all_bits_set
# 0 ^ complement = number ^ all_bits_set
# complement = number ^ all_bits_set
def calculate_bitwise_complement(num):
    n_bits = 0
    x = num
    while x > 0:
        n_bits += 1
        x >>= 1 # divide by 2 until quotient is 0

    all_bit_set_num = pow(2,n_bits)-1

    return num ^ all_bit_set_num
    
print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))
