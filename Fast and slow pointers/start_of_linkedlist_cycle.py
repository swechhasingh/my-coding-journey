class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def start_of_cycle(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    slow, fast = head, head
    cycle_length = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = cal_cycle_length(slow)
            return find_start_of_cycle(head,cycle_length)
    return None

def find_start_of_cycle(head,cycle_length):
    p1, p2 = head, head
    while cycle_length > 0:
        p1 = p1.next
        cycle_length -= 1
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1.val

def cal_cycle_length(slow):
    cycle_length = 0
    curr = slow.next
    while curr != slow:
        cycle_length += 1
        curr = curr.next
    cycle_length += 1
    return cycle_length

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Start of LinkedList cycle: " + str(start_of_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("Start of LinkedList cycle: " + str(start_of_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Start of LinkedList cycle: " + str(start_of_cycle(head)))


main()