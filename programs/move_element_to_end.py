"""
Given an array of integers A and an integer k, move all A[i] that equal k to 
the end of A. 

Perform this task in place; you don't need to maintain the order of the other
integers in the original array.

Example:
array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
output: [1, 3, 4, 2, 2, 2, 2, 2]

Created on Fri Aug 05, 2022
"""

from typing import List


def move(array: List[int], toMove: int) -> List[int]:
    # Use two-pointer technique
    i, j = 0, len(array) - 1
    while i < j:
        if array[i] == toMove and array[j] == toMove:
            j -= 1
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if array[i] != toMove:
            i += 1
    return array


def main():
    arr = [2, 5, 1, 5, 2, 5, 3, 4, 2, 5, 5]
    toMove = 5
    str_out = f"Moving all {toMove}s to the end of {arr}\n gives"
    str_out += f"{move(arr, toMove)}"
    print(str_out)


if __name__ == "__main__":
    main()
