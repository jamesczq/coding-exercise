"""
Given two arrays, determine if one array is the subarray of the other.

Created on Fri Jun 10 2022
"""
from typing import List
import argparse

def is_subarray(arr1: List[int], arr2: List[int]) -> bool:
    if len(arr1) <= len(arr2):
        smallerArr, largerArr = arr1, arr2
    else:
        smallerArr, largerArr = arr2, arr1 
    
    largerHash = {item:True for item in largerArr}

    for item in smallerArr:
        if not item in largerHash:
            return False 
    
    return True

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a1", "--array1", nargs="+", type=int)
    parser.add_argument("-a2", "--array2", nargs="+", type=int)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    if is_subarray(args.array1, args.array2):
        if len(args.array1) <= len(args.array2):
            str_out = f"The 1st array {args.array1} is a subarray of the 2nd array {args.array2}"
        else:
            str_out = f"The 2nd array {args.array2} is a subarray of the 1st array {args.array1}"
    else:
        str_out = "The 1st, 2nd arrays are NOT subarray of each other"
    return str_out 

if __name__ == "__main__":
    print("\n" + main() + "\n")