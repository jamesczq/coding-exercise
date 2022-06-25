"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found; if not, return the index the target'd be if inserted.

Example: 
Input: nums = [1,3,5,6], target = 2
Output = 1

Created on Fri Jun 24 2022
"""
from typing import List

# Method: two-pointer technique
def search(arr: List[int], target: int) -> int:
    l, r = 0, len(arr)-1

    while l <= r:
        index = (l + r)//2
        if arr[index] < target:
            l = index + 1
        elif arr[index] > target:
            r = index - 1
        else: # arr[index] == target
            return index

    if arr[index] < target:
        return index + 1
    else:
        return index

def main():
    arrs = [[1,3,5,6]] * 3
    targets = [5, 2, 7]
    for arr, target in zip(arrs, targets):
        idx = search(arr, target)
        print(f"{target} -> {arr}: insert at {idx}")

if __name__ == "__main__":
    main()