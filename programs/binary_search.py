"""
Binary search a sorted array using a built-in library Bisect.

The main working function is bisect.bisect_left(a, x, lo=0, hi=len(a)):
- It locates the insertion point for x in a to maintain sorted order. 
- If x is already present in a, the insertion point will be before (to the 
left of) any existing entries. 
- The return value is suitable for use as the first parameter to list.insert() 
assuming that a is already sorted.
- The returned insertion point i partitions the array a into two halves so 
that all(val < x for val in a[lo : i]) for the left side and 
all(val >= x for val in a[i : hi]) for the right side.

Created on Tue Jun 14 2022.
"""
from typing import List, Union
import argparse
import bisect
import random 

from sampling import permutation

def main(arr: List[int], x: int) -> Union[int, None]:
    i = bisect.bisect_left(arr, x)
    return i if i < len(arr) and arr[i] == x else None

if __name__ == "__main__":
    a1 = random.randrange(-10, 10)
    a2 = random.randrange(50, 100)
    arr = range(a1, a2)
    x = random.randrange(-100, 100)
    idx = main(arr, x)
    if idx is None:
        print(f"{x} is Not in {arr}")
    else:
        print(f"{x} is in {arr}: arr[{idx}] == {x}")
        
