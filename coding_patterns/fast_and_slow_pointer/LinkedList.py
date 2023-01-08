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
    return slow.val


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    print(f"Middle of LinkedList: {find_middle(head)}")

    head.next.next = Node(3)
    print(f"Middle of LinkedList: {find_middle(head)}")

    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")
    print(f"Middle of LinkedList: {find_middle(head)}")

    head.next.next.next.next.next.next = head.next.next
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")

    head.next.next.next.next.next.next = head.next.next.next
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"start of cycle: {find_start_of_cycle(head)}")

    head.next.next.next.next.next.next = head
    print(f"LinkedList has cycle: {has_cycle_and_cycle_length(head)}")
    print(f"Start of cycle: {find_start_of_cycle(head)}")
