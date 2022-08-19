class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

def sum_of_path_numbers(root):
    paths = []

    sum_of_path_numbers_recursive(root,[],paths)
    return sum(paths)

def list_to_number(num_list):
    num = 0
    for i in range(len(num_list)):
        num += num_list[i]*10**(len(num_list)-i-1)
    return num

def sum_of_path_numbers_recursive(root, path=[],paths=[]):
    # Time complexity: O(N*log(N)), where 'N' is number of nodes in the tree
    # Space complexity: O(N*log(N)), log(N) space required to store each path to leaf node

    if root is None:
        return

    path.append(root.val)
    if not root.left and not root.right:
        paths.append(list_to_number(path))
    else:
        sum_of_path_numbers_recursive(root.left, path, paths)
        sum_of_path_numbers_recursive(root.right, path, paths)
    del path[-1]
    return


def find_sum_of_path_numbers(root):
  return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(currentNode, pathSum):
    # Time complexity: O(N), where 'N' is number of nodes in the tree
    # Space complexity: O(N)

    if currentNode is None:
        return 0

    # calculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.val

    # if the current node is a leaf, return the current path sum
    if currentNode.left is None and currentNode.right is None:
        return pathSum

    # traverse the left and the right sub-tree
    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)



def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print(f"Sum of path numbers: {find_sum_of_path_numbers(None)}")
    print(f"Sum of path numbers: {find_sum_of_path_numbers(root)}")


main ()

