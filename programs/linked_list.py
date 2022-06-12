"""
Linked List

* Traverse a linked list
* Insert a node
* Delete a node

Created on Sat Jun 11 2022
"""
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    # This method traverses a linked list
    def print_list(self):
        temp = self.head
        str_out = f"head="
        while temp:
            str_out += f"{temp.data} -> "
            temp = temp.next
        str_out += f"{temp}"
        print(str_out)
    
    # Insert 1: push to the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head # At this moment, head -> (old) FirstNode
        self.head = new_node 
    
    # Insert 2: insert after a node ("prev_node" below)
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the linked list!")
            return 
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node 
    
    # Insert 3: append to the end 
    def append(self, new_data):
        new_node = Node(new_data)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node 
            return 
        
        # Else: traverse to the very last node
        last = self.head 
        while last.next:
            last = last.next 
        last.next = new_node

    # Delete first occurence of a node whose data == key
    def delete_node(self, key):
        tmp = self.head 

        # If the head node happens to hold data that equals key
        if tmp is not None:
            if tmp.data == key:
                self.head = tmp.next 
                tmp = None
                return 
        
        # Search for the node whose data == key
        # also, need to store this node's previous node
        while (tmp is not None):
            if tmp.data == key:
                break 
            prev = tmp 
            tmp = tmp.next

        prev.next = tmp.next 

        tmp = None

if __name__ == "__main__":
    # Test 1: Traverse a linked list
    print("\n1. Traverse a linked list\n")
    my_linked_list = LinkedList()
    
    my_linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    my_linked_list.head.next = second 
    second.next = third 

    my_linked_list.print_list()
    print("\n----------------------\n")

    # Test 2: Inserts
    print("\n2. Inserts\n")
    my_linked_list = LinkedList()
    ## Linked list becomes 6 -> None
    my_linked_list.append(6)
    my_linked_list.print_list()
    ## Linked list becomes 7 -> 6 -> None
    my_linked_list.push(7)
    my_linked_list.print_list()
    ## Linked list becomes 9 -> 7 -> 6 -> None
    my_linked_list.push(9)
    my_linked_list.print_list()
    ## Linked list becomes 10 -> 9 -> 7 -> 6 -> None
    my_linked_list.push(10)
    my_linked_list.print_list()
    ## Linked list becomes 10 -> 9 -> 8 -> 7 -> 6 -> None
    my_linked_list.insert_after(my_linked_list.head.next, 8)
    my_linked_list.print_list()
    print("\n----------------------\n")

    # Test 3: Delete
    print("\n3. Deletes\n")
    my_linked_list.print_list()
    my_linked_list.delete_node(7)
    my_linked_list.print_list()
    my_linked_list.delete_node(9)
    my_linked_list.print_list()
    print("\n")

