"""
Two Sum

Given an array of integers nums and an integer target, return the two numbers
such that they add up to target, if they exist.

You can assume that each input would have exactly one solution, and you may 
not use the same element twice.

Created on Wed Jun 08 2022
"""
from typing import List, Tuple, Union
import argparse

def two_sum_v1(nums: List[int], target: int) -> Union[Tuple, None]:
    visited = {nums[0]: 0}
    for i in range(1, len(nums)):
        x = nums[i]
        y = target - x
        if y in visited:
            return (x, y)
        else:
            visited[x] = i 
    return None

def two_sum_v2(nums: List[int], target: int) -> Union[Tuple, None]:
    arr = sorted(nums)
    i, j = 0, len(arr) - 1
    while i < j:
        mysum = arr[i] + arr[j]
        if mysum < target:
            i += 1
        elif mysum  > target:
            j -= 1
        else:
            return (arr[i], arr[j])
    return None

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', "--version", type=int, default=1)
    parser.add_argument('--nums', nargs="+", type=int)
    parser.add_argument('--target', type=int)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if args.version == 1:
        ans = two_sum_v1(args.nums, args.target)
    else:
        ans = two_sum_v2(args.nums, args.target)
    return ans

if __name__ == "__main__":
    ans = main()
    if ans:
        x, y = ans[0], ans[1]
        print(x, y)
    else: 
        print("No such two numbers found!")

