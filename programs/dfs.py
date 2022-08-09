"""
Traverse a tree using the Depth First Search approach and output all of the 
nodes' names or values in an array.

Example:
Tree = 
             10
         /        \
       5          15
      /   \       /   \
     2     5    13     22
   /             \ 
  1               14

DFS output = [10, 5, 2, 1, 5, 15, 13, 14, 22]

Created on Mon Aug 08, 2022
"""
import bst 

def dfs_helper(root, array=[]):
    if root is None:
        return 
    array.append(root.value)
    dfs_helper(root.left, array)
    dfs_helper(root.right, array)

def dfs(root):
    array = []
    dfs_helper(root, array)
    return array 

def main():
    tree = bst.get_example_bst()
    print("BST:", bst.in_order_traversal(tree.root))
    print("Depth First Search:", dfs(tree.root))

if __name__ == "__main__":
    main()
