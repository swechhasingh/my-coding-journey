def cycle_in_circular_array(arr):
    # Time complexity: O(N^2)
    # Space complexity: O(1)
    
    for i in range(len(arr)):
        forward_direction = arr[i] >= 0
        slow, fast = i, i
        while True:
            slow = find_next_index(arr, slow, forward_direction)
            fast = find_next_index(arr, fast, forward_direction)
            if fast != -1:
                fast = find_next_index(arr, fast, forward_direction)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True

    return False


def find_next_index(arr, idx, forward_direction):
    direction = arr[idx] >= 0
    if direction != forward_direction:
        return -1

    # circular array
    next_idx = (idx + arr[idx]) % len(arr)
    
    if next_idx == idx:
        return -1

    return next_idx

def main():
    print(cycle_in_circular_array([1, 2, -1, 2, 2]))
    print(cycle_in_circular_array([2, 2, -1, 2]))
    print(cycle_in_circular_array([2, 1, -1, -2]))

main()