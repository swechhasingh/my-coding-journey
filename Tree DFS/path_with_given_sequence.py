from turtle import left, right
from typing import Sequence


class TreeNonde:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

# their solution
def find_path_recursive(currentNode, sequence, sequenceIndex):
    
    if currentNode is None:
        return False

    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False

    # if the current node is a leaf, add it is the end of the sequence, we have found 
    # a path!
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
    find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)



def path_with_given_sequence_rec(current_node, sequence, seq_curr_idx):
    # Time complexity: O(N), each node visited once by recursive call
    # Space complexity: O(N), recursion stack
    if current_node is None:
        return False
    
    if seq_curr_idx == len(sequence)-1 and current_node.val == sequence[seq_curr_idx]:
        if not current_node.left and not current_node.right:
            return True
    elif current_node.val == sequence[seq_curr_idx] and seq_curr_idx < len(sequence)-1:
        return path_with_given_sequence_rec(current_node.left, sequence, seq_curr_idx+1) or path_with_given_sequence_rec(current_node.right, sequence, seq_curr_idx+1)
    return False



def path_with_given_sequence(root,sequence):
    # empty sequence and empty tree
    if not root:
        return len(sequence) == 0
    return path_with_given_sequence_rec(root, sequence, 0)





def main():
    root = TreeNonde(1)
    root.left = TreeNonde(7)
    root.right = TreeNonde(9)
    root.right.left = TreeNonde(2)
    root.right.right = TreeNonde(9)
    sequence = [1,9,9]
    print(f"Path with {sequence} sequence: {path_with_given_sequence(root,sequence)}")

main()

