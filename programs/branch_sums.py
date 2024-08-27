"""
Given a binary tree, return a list of its branch sums ordered from the 
leftmost branch sum to the rightmost branch sum, where a branch sum is
the sum of all values in a binary tree branch (path from root to leaf).

Example:

tree =             1
               /      \
             2          3
          /     \     /   \ 
        4        5   6     7
      /   \     /
    8      9  10

Output: branch sums = [15, 16, 18, 10, 11]
# 15 = 1 + 2 + 4 + 8
# 16 = 1 + 2 + 4 + 9
# 18 = 1 + 2 + 5 + 10
# etc.

Created on Mon Aug 08, 2022
"""

import bst


# Use recursion along the Depth First Search direction
def branch_sums_helper(node, running_sum=0, sums=[]):
    if node is None:
        return
    new_running_sum = running_sum + node.value
    if not (node.left or node.right):
        sums.append(new_running_sum)
        return
    branch_sums_helper(node.left, new_running_sum, sums)
    branch_sums_helper(node.right, new_running_sum, sums)


def branch_sums(tree):
    sums = []
    branch_sums_helper(tree.node, running_sum=0, sums=sums)
    return sums


def main():
    tree = bst.get_example_bst()
    sums = branch_sums(tree.root)
    print("BST:", bst.in_order_traversal(tree.root))
    print("Branch sums:")
    for s in sums:
        print(s)


if __name__ == "__main__":
    main()
