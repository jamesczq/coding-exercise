"""
Given an array [a0, a1, ...] and a value h, find the largest 
subsum = a[i] + a[j] such that subsum <= h.
Assume all a[i] >= 0.

Created on Wed Jun 22 2022
"""

from typing import List
import random

from linear_sort import counting_sort


def find_two(arr: List[int], h: int) -> int:
    counting_sort(arr)
    B = [x for x in arr if x <= h]
    i = 0
    j = len(B) - 1
    subsum = 0
    while i < j:
        # store current i, j that before incrementing
        I, J = i, j
        subsum = B[i] + B[j]
        if subsum <= h:
            i += 1
        else:
            j -= 1
    return B[I], B[J], subsum


def main():
    u = random.randrange(20, 40)
    n = 10
    arr = [random.randrange(0, u) for _ in range(n)]
    h = int(1.5 * u)
    print(
        f"Problem: Find largest sum from two numbers in the array {arr} that is less than {h}."
    )
    ai, aj, subsum = find_two(arr, h)
    print(f"Solution: {ai} + {aj} = {subsum}")


if __name__ == "__main__":
    main()
