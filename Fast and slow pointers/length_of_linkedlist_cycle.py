class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def find_cycle_length(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    slow, fast = head, head
    cycle_length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            cycle_length += 1
            while slow != fast:
                cycle_length += 1
                slow = slow.next
            return cycle_length
    return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Length of LinkedList cycle: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next
    print("Length of LinkedList cycle: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Length of LinkedList cycle: " + str(find_cycle_length(head)))


main()