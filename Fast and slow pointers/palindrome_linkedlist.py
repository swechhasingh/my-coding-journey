class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

def palindrome_linkedlist(head):
    # Time complexity: O(N)
    # Space complexity: O(1)
    if head is None or head.next is None:
        return True

    # find the middle of linkedlist
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of linkedlist
    tail = reverse_linkedlist(slow)

    print("First half of the linkedlist:")
    print_linked_list(head)
    print("Reversed second half of the linkedlist:")
    print_linked_list(tail)

    # check if palindrome or not
    ans = is_palindrome(head, tail)

    # reverse the second half to get linkedlist in it's original form
    _ = reverse_linkedlist(tail)

    print("Return to original linkedlist:")
    print_linked_list(head)

    return ans

def print_linked_list(head):
    print("LinkedList: ")
    while head is not None:
        print(head.val)
        head = head.next

def reverse_linkedlist(head):
    prev = None
    curr= head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # return tail of the linkedlist
    return prev

def is_palindrome(head,tail):
    left, right = head, tail
    while left is not None and right is not None:
        if left.val == right.val:
            left = left.next
            right = right.next
        else:
            return False
    return True


    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    print("Original linkedlist:")
    print_linked_list(head)
    print("Is palindrome LinkedList: " + str(palindrome_linkedlist(head)))

    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(4)
    print("Original linkedlist:")
    print_linked_list(head)
    print("Is palindrome LinkedList: " + str(palindrome_linkedlist(head)))

main()