from collections import deque


class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def rightViewOfBinaryTree(root):
    # Time complexity: O(N), visiting every node once
    # Space complexity: O(N), at last level queue will have N/2 node (total no. of leaf nodes in a binary tree)

    if root is None:
        return

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            curr = queue.popleft()
            # for left view of bianry tree
            # if not i:
            #     print(curr.val, end=" ")
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        # for right view of binary tree
        print(curr.val, end=" ")
    print()

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    rightViewOfBinaryTree(root)

main()