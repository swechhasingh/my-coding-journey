class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def has_path_with_sum_s(node,sum):
    # Time complexity: O(N), where 'N' is number of nodes in the tree
    # Space complexity: space used by recursion stack O(N) in the worst case, when all the nodes have only one child node

    if node is None:
        return False
    
    sum = sum - node.val
    if not node.left and not node.right:
        return True if sum == 0 else False

    return has_path_with_sum_s(node.left,sum) or has_path_with_sum_s(node.right,sum)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(f"Tree has path: {has_path_with_sum_s(root,10)}")

main()