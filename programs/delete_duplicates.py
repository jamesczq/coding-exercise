"""
Delete duplicated elements from a sorted list.

Example:
[2, 3, 5, 5, 7, 11, 11, 11, 13] -> [2, 3, 5, 7, 11, 13]

Created on Thu Jun 09 2022
"""
from typing import List
import argparse

def get_unique_indices(arr: List[int]) -> List[int]:
    """Return indices of unique, non-duplicate, elements of a sorted list."""
    list_out = [0]
    non_dup_index = 1
    for i in range(1, len(arr)):
        if arr[non_dup_index - 1] != arr[i]:
            list_out.append(i)
            non_dup_index += 1
        else:
            non_dup_index = i + 1
    return list_out

def get_unique_values(arr: List[int]) -> List[int]:
    non_dup_indices = get_unique_indices(arr)
    return [arr[i] for i in non_dup_indices]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', "--array", nargs="+", type=int, required=False)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    if not args.array:
        arr = [1, 2, 3, 3, 5, 5, 5, 9, 9]
        arr2 = get_unique_values(arr)
        str_out = f"Example: DeleteDups({arr}) = {arr2}"
    else:
        arr2 = get_unique_values(args.array)
        str_out = f"DeleteDups({args.array}) = {arr2}"
    return str_out
        
if __name__ == "__main__":
    print("\nDelete duplicates from a sorted array:")
    print(main() + "\n")