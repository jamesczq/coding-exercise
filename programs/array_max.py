"""
Use recursion to return the max of an array.

Created on Fri Jun 10 2022
"""

from typing import List
import argparse


def max_v1(arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    submax = max_v1(arr[1:])
    if arr[0] >= submax:
        return arr[0]
    else:
        return submax


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("array", nargs="+", type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    return max_v1(args.array)


if __name__ == "__main__":
    print(main())
