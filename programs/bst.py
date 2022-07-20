"""
Implement Binary Search Tree, only upto inserting tree nodes.

Created on Wed Jul 20, 2022
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BST:
    def __init__(self):
        self.root = None 
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return 
        
        currNode = self.root 
        while True:
            if value < currNode.value:
                if currNode.left is None:
                    currNode.left = Node(value)
                    break 
                currNode = currNode.left 
            else:
                if currNode.right is None:
                    currNode.right = Node(value)
                    break 
                currNode = currNode.right 

def in_order_traversal(root):
    if root is None:
        return []
    left_list = in_order_traversal(root.left)
    right_list = in_order_traversal(root.right)
    return left_list + [root.value] + right_list

def get_example_bst(values = [10, 5, 2, 1, 5, 15, 13, 14, 22]):
    tree = BST()
    for value in values:
        tree.insert(value)
    return tree 

def main():
    tree = get_example_bst()
    print(in_order_traversal(tree.root))

if __name__ == "__main__":
    main()
