from collections import deque


class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.next = None

def connectAllLevelOrderSiblings(root):
    # Time complexity: O(N), visiting every node once
    # Space complexity: O(N), at last level queue will have N/2 node (total no. of leaf nodes in a binary tree)

    if root is None:
        return

    queue = deque()
    queue.append(root)
    prevNode = None
    while queue:
        # levelSize = len(queue)
        # for _ in range(levelSize):
        curr = queue.popleft()
        if prevNode:
            prevNode.next = curr
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
        prevNode = curr

def print_all_level_order_sibling(root):
    while root is not None:
        print(root.val, end=" ")
        root = root.next
    print()

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    connectAllLevelOrderSiblings(root)
    print_all_level_order_sibling(root)

main()