# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not and also find find the length of the cycle.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# time complexity: O(N) and space complexity: O(1)
def has_cycle_and_cycle_length(head: Node):
    slow, fast = head, head
    length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length += 1
            slow = slow.next
            while slow != fast:
                length += 1
                slow = slow.next
            return True, length
    return False, length


# time complexity: O(N) and space complexity: O(1)
def find_start_of_cycle(head: Node):
    cycle_present, length = has_cycle_and_cycle_length(head)

    if cycle_present:
        slow, fast = head, head
        while length:
            fast = fast.next
            length -= 1
        start = 0
        while slow != fast:
            slow = slow.next
            fast = fast.next
            start += 1
        return start, slow.val
    return -1


# time complexity: O(N) and space complexity: O(1)
def find_middle(head: Node):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow


# time complexity: O(N) and space complexity: O(1)
def reverse(head: Node):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


# time complexity: O(N) and space complexity: O(1)
def is_palindrome(head: Node):
    # find middle of linkedlist and reverse the second half,
    # then iterate both halfs simultaneously
    # return true if all the nodes match otherwise return False
    mid = find_middle(head)
    secondhalf_head = reverse(mid)
    copy_secondhalf_head = secondhalf_head
    while head is not None and secondhalf_head is not None:
        if head.val != secondhalf_head.val:
            return False
        head = head.next
        secondhalf_head = secondhalf_head.next
    reverse(copy_secondhalf_head)
    return True


def rearrange_linkedlist(head: Node):
    mid = find_middle(head)
    second_half_head = mid.next
    mid.next = None
    second_half_head = reverse(second_half_head)
    curr = head
    while second_half_head is not None:
        next = curr.next
        curr.next = second_half_head
        second_half_head = second_half_head.next
        curr.next.next = next
        curr = next
    return head


def print_linkedlist(head: None):
    while head is not None:
        print(head.val, end=", ")
        head = head.next
    print()


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    print(f"Middle of LinkedList: {find_middle(head).val}")

    head.next.next = Node(3)
    print(f"Middle of LinkedList: {find_middle(head).val}")

    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")
    print(f"Middle of LinkedList: {find_middle(head).val}")

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"start of cycle: {find_start_of_cycle(head)}")

    head.next.next.next.next.next.next = head
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print(f"Is palindrome: {is_palindrome(head)}")

    head.next.next.next.next.next = Node(2)
    print(f"Is palindrome: {is_palindrome(head)}")

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    print_linkedlist(head)
    print_linkedlist(rearrange_linkedlist(head))
    head.next.next.next.next.next = Node(12)
    print_linkedlist(head)
    print_linkedlist(rearrange_linkedlist(head))
