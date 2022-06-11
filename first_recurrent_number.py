"""
Given array = [2, 5, 1, 2, 3, 5, 1, 2, 4],
it should return 2

Given array = [2, 1, 1, 2, 3, 5, 1, 2, 4],
it should return 1

Given array = [2, 3, 4, 5],
it should return None

Created on Fri Jun 10 2022
"""
from typing import List, Union
import argparse

def get_first_recur(arr: List[int]) -> Union[int, None]:
    visited = {arr[0]: 1}
    for i in range(1, len(arr)):
        if arr[i] in visited:
            return arr[i]
        else:
            visited[arr[i]] = 1
    return None 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("array", nargs="+", type=int)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    return get_first_recur(args.array)

if __name__ == "__main__":
    print(main())

