"""
Given a BST and a target value, return the closest value to that target in the BST.

Example:

tree =      10
          /    \
         5     25
        / \    / \
       2   5  13  22
      /        \ 
     1          14

target = 12

Then the nearest(tree, target) = 13

Created on Wed Jul 20, 2022
"""
import bst 

# Non recursion
def nearest_value_in_bst_v1(tree, target):
    currNode = tree.root # Same as currNode = tree.root
    nearest = float("inf")
    while currNode is not None:
        if abs(target - currNode.value) < abs(target - nearest):
            nearest = currNode.value 
        if target < currNode.value:
            currNode = currNode.left 
        elif target > currNode.value:
            currNode = currNode.right
        else: # target == currNode.value
            break
    return nearest

# Recursion
def nearest_value_in_bst_v2(tree, target):
    # Write your code here.
    return nearest_value_in_bst_v2_helper(tree.root, target, nearest=float('inf'))

def nearest_value_in_bst_v2_helper(tree_node, target, nearest):
    if tree_node is None:
        return nearest
    if abs(target - tree_node.value) < abs(target - nearest):
        nearest = tree_node.value
    if target < tree_node.value:
        return nearest_value_in_bst_v2_helper(tree_node.left, target, nearest)
    elif target > tree_node.value:
        return nearest_value_in_bst_v2_helper(tree_node.right, target, nearest)
    else: # target == tree_node.value
        return nearest

def main():
    tree = bst.get_example_bst()
    target = 12.5
    print(f"BST in-order traversal: {bst.in_order_traversal(tree.root)}")
    print(f"Nearest to target = {target} in the BST is:")
    print(nearest_value_in_bst_v1(tree, target))
    print(nearest_value_in_bst_v2(tree, target))

if __name__ == "__main__":
    main()
