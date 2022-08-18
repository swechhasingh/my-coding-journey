class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def all_paths_for_a_sum(root, required_sum):
    paths = []
    all_paths_for_a_sum_recursive(root, required_sum, [], paths)
    return paths

def all_paths_for_a_sum_recursive(root, required_sum, path=[], paths=[]):
    # Time complexity: O(N*log(N)), where 'N' is number of nodes in the tree
    # Space complexity: O(N*log(N)), log(N) space required to store each path to leaf node

    if root is None:
        return

    required_sum = required_sum - root.val
    path.append(root.val)
    if not root.left and not root.right and required_sum == 0:
        paths.append(list(path))
    else:
        all_paths_for_a_sum_recursive(root.left, required_sum, path, paths)
        all_paths_for_a_sum_recursive(root.right, required_sum, path, paths)
    del path[-1]
    return

def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)
    print(f"Tree has path: {all_paths_for_a_sum(root,12)}")


main ()

