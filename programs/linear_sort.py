"""
Implement direct-access-array sort and counting sort, both of which are 
linear time complexity. In this algorithm, 
an int k is placed at k-th index of an aux array and the read off the 
aux array to get sorted array of the original one.

This assumes the array to sort consists of integers between 0 and u.

The sorting methods are in-place ones.

Created on Tue Jun 21 2022
"""
from typing import List
import random

from sampling import permutation


def direct_access_array_sort(arr: List[int]) -> None:
    """In-place sorting. This requires array elements are unique!"""
    u = 1 + max(arr)
    aux = [None] * u 
    for k in arr:
        aux[k] = k

    i = 0
    for j in range(u):
        if aux[j]: # i.e. if aux[k] is not None
            arr[i] = aux[j]
            i += 1 

def counting_sort(arr: List[int]) -> None:
    """In-place sorting. This does not require unique array elements."""
    u = 1 + max(arr)
    aux = [[] for _ in range(u)]
    for k in arr:
        aux[k].append(k)

    i = 0
    for chain in aux:
        for x in chain:
            arr[i] = x
            i += 1

def main():
    # Generate 10 random ints between 0 and u, no repeating ones
    u = 100
    n = 10
    arr = permutation(n, u)

    print("\n*Direct-access-array sort (only for arrays of unique elements)")
    print("Array before sorting:", arr)
    direct_access_array_sort(arr)
    print("Array after sorting: ", arr)

    # Generate 10 random ints between 0 and u, repeating ones allowed
    u = 20
    n = 10
    arr = [random.randrange(0, u) for _ in range(n)]

    print("\n*Counting sort (can have duplicates in array)")
    print("Array before sorting:", arr)
    counting_sort(arr)
    print("Array after sorting: ", arr)
    print("\n")

if __name__ == "__main__":
    main()



