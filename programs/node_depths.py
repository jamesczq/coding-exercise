"""
Write a function that takes a binary tree and returns the sum of the deptsh of 
all its nodes.

A depth of a tree node is the distance between the root and the node.

Example:
Tree = 
             10
         /        \
       5          15
      /   \       /   \
     2     5    13     22
   /             \ 
  1               14

sumDepths = 1 + 1 + 2 + 2 + 2 + 2 + 3 + 3 = 16

Created on Mon Aug 08 2022
"""
import bst 

# Use recursion.
# Key: f(node,depth) = depth + f(node.left,depth+1) + f(node.right,depth+1)
# Time: O(n); Space: O(h)

def node_depths(node, depth=0):
    # Base case
    if node is None: 
        return 0
    return depth + node_depths(
        node.left, depth + 1) + node_depths(node.right, depth+1)
    
def main():
    tree = bst.get_example_bst()
    sum_depths = node_depths(tree.root, depth=0)
    print("BST:", bst.in_order_traversal(tree.root))
    print("Sum of node depths:", sum_depths)

if __name__ == "__main__":
    main()