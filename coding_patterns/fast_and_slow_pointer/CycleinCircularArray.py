# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

from typing import List

# time complexity: O(N^2) (iterating all elements of the array and trying to find a cycle for each element)
# and space complexity: O(1)
def is_cycle_in_circular_array(arr: List[int]):
    N = len(arr)
    for curr in range(N):
        slow = curr
        fast = curr
        # cycle direction; 1 for forward and -1 for backward
        is_forward = 1 if arr[curr] >= 0 else -1
        while True:
            next = fast + arr[fast]
            if next < 0:
                fast = N - (abs(next) % N)
            else:
                fast = next % N
            curr_direction = 1 if arr[fast] >= 0 else -1
            # direction changed
            if curr_direction != is_forward:
                break
            # cycle found
            if slow == fast:
                return True
            slow = slow + 1 * is_forward
            if slow < 0:
                slow = N - (abs(slow) % N)
            else:
                slow = slow % N
    return False


if __name__ == "__main__":
    print(is_cycle_in_circular_array([1, 2, -1, 2, 2]))
    print(is_cycle_in_circular_array([2, 2, -1, 2]))
    print(is_cycle_in_circular_array([2, 1, -1, -2]))
