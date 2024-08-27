"""
Print a linked list in reverse without physically reversing it.

Created on Sun Jun 12 2022
"""

from linked_list import LinkedList


class MyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    # Use recursion to reverse print
    def print_reverse(self, tmp):
        if tmp:
            self.print_reverse(tmp.next)
            print(tmp.data, end=" <- ")
        else:
            return


if __name__ == "__main__":
    my_linked_list = MyLinkedList()
    ## Linked list becomes 6 -> None
    my_linked_list.append(6)
    my_linked_list.print_list()
    ## Linked list becomes 7 -> 6 -> None
    my_linked_list.push(7)
    my_linked_list.print_list()
    ## Linked list becomes 8 -> 7 -> 6 -> None
    my_linked_list.push(8)
    my_linked_list.print_list()
    my_linked_list.print_list()

    print("Reverse print:")
    my_linked_list.print_reverse(my_linked_list.head)
