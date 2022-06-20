"""
Find if there is a subarray with zero sum.

Example:
Input: [4, 2, -3, 1, 6]
Output: True

Example:
Input: [4, 2, 0, 1, 6]
Output: False

Created on Sun Jun 19 2022
"""
from typing import List
import argparse

# Logic/key observation:
# Use hashing to store running sum (+= arr[i]).
# If a sum is seen before in the hashing,
# it means there is a zero-sum subarray:
# 0 + a[i+1] + ... + a[j] = a[i+1] + ... + a[j]

def subarr_exists(arr: List[int]) -> bool:
    curr_sum = 0
    s = set()
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum == 0 or curr_sum in s:
            return True 
        s.add(curr_sum)
    return False 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("array", nargs="+", type=int)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    if subarr_exists(args.array):
        print("Zero-sum subarray exists!")
    else:
        print("Zero-sum subarray does not exist!")

if __name__ == "__main__":
    main()
