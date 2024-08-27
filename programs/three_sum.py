"""
Triplet that add to a given value

Example:
Input: arr = [1,2,3,4,5], sum = 9
Output: {1,3,5}

Created on Sat Jun 18 2022
"""

from typing import List
import argparse

# Algo: extension of the two_sum problem; use Hashmap
# Two for loops:
# i from 0 to end, j from i+1 to end
# Create a hashmap to check if there is a number in the hashmap
# which is equal to x - arr[i] - arr[j]


def find_triplet(arr: List[int], target: int) -> List[int]:
    n = len(arr)
    for i in range(n):
        # Find a pair in A[i+1], ..., A[n-1] that sum to Target - A[i]
        s = set()
        curr_sum = target - arr[i]
        for j in range(i + 1, n):
            delta = curr_sum - arr[j]
            if delta in s:
                return [arr[i], arr[j], delta]
            else:
                s.add(arr[j])
    return []


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--array", nargs="+", type=int)
    parser.add_argument("-t", "--target", type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    print(find_triplet(args.array, args.target))


if __name__ == "__main__":
    main()
