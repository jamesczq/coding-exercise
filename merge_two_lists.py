"""
Merge two sorted lists

Given two sorted lists, merge them into a sorted list.

Example: 
list1 = [1, 5, 7]
list2 = [3, 11]
merged = [1,3,5,7,11]

Created on Thu Jun 09 2022
"""
from typing import List 
import argparse

def merge_two_lists(arr1: List[int], arr2: List[int]) -> List[int]:
    merged = []
    i, j = 0, 0
    while (i < len(arr1)) and (j < len(arr2)):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Append whichever array that still has some elements left over
    if arr1[i:]:
        merged += arr1[i:]
    if arr2[j:]:
        merged += arr2[j:]
    return merged 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a1', "--array1", nargs="+", type=int)
    parser.add_argument('-a2', "--array2", nargs="+", type=int)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    merged = merge_two_lists(args.array1, args.array2)
    return args.array1, args.array2, merged 

if __name__ == "__main__":
    a1, a2, a = main()
    print("\nMerge two sorted lists:")
    print(f"Merge({a1}, {a2}) = {a}\n")
