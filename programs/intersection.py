"""
Intersection between two *sorted arrays

It takes as input two sorted arrays and returns a new array containing 
elements present in both of the input arrays. 
The input arrays may have duplicate entries but the returned array 
should be free of duplicates.

Example: Intersection(
    [2, 3, 3, 5, 5, 6, 7, 7, 8, 12],
    [5, 5, 6, 8, 8, 9, 10, 10]) = [5, 6, 8]

Created on Tue Jun 14 2022
"""

from typing import List
import argparse
import bisect


# Version 1: first, iterate through the first array and use binary search to
# test if the element is present in the second array.
# Time complexity O(m log n)
def intersect_v1(A: List[int], B: List[int]) -> List[int]:
    def is_in(x: int, arr: List[int]) -> bool:
        i = bisect.bisect_left(arr, x)
        return i < len(arr) and arr[i] == x

    if len(A) < len(B):
        shorter_arr, longer_arr = A, B
    else:
        shorter_arr, longer_arr = B, A

    return [
        k
        for i, k in enumerate(shorter_arr)
        if (i == 0 or k != shorter_arr[i - 1]) and is_in(k, longer_arr)
    ]


# Version 2: achieve linear runtime by simultaneously advancing through the
# two input arrays in increasing order.
# At each iteration,
# - if the array elements differ, the smaller one can be eliminated
# - if they are equal, add that value to intersection and advance both
def intersect_v2(A: List[int], B: List[int]) -> List[int]:
    intersection_A_B = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:  # A[i] > B[j]
            j += 1
    return intersection_A_B


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a1", "--array1", nargs="+", type=int)
    parser.add_argument("-a2", "--array2", nargs="+", type=int)
    parser.add_argument("-v", "--version", type=int, default=1)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    if args.version == 1:
        return intersect_v1(args.array1, args.array2)
    else:
        return intersect_v2(args.array1, args.array2)


if __name__ == "__main__":
    print(main())
