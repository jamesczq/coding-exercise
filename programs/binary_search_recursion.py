"""
Binary search with recursion. Return the index of search target in the array.
If not found, return -1.

Created on Wed Jun 29 2022
"""

from typing import List
import random


def binary_search(arr: List[int], target: int) -> int:
    return binary_search_helper(arr, target, start=0, end=len(arr) - 1)


def binary_search_helper(arr, target, start, end):
    if end <= start:
        return -1
    mid = (start + end) // 2
    if arr[mid] < target:
        return binary_search_helper(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_search_helper(arr, target, start, mid)
    else:
        return mid


def main():
    a1 = random.randrange(-10, 10)
    a2 = random.randrange(20, 100)
    arr = list(range(a1, a2))
    x = random.randrange(-100, 100)
    idx = binary_search(arr, x)
    if idx == -1:
        print(f"{x} is Not in range({a1}, {a2})")
    else:
        print(f"{x} is in range({a1}, {a2}): arr[{idx}] == {x}")


if __name__ == "__main__":
    main()
