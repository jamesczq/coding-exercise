"""
Valid Subsequence

Given two non-empty arrays of integers, determine whether the 2nd array is a 
subsequence of the 1st array.

A subsequence of an array is a set of numbers that are not necessarily 
adjacent in that array but are in the same order as they appear in the
array.

Example: [2, 4] is a valid subsequence of [1, 2, 3, 4]

Created on Mon Jun 27 2022
"""
from typing import List

# Method: two-pointer technique: traverse the main array to see if one of 
# its element is found in the sequence in the same order.
# The traverse is done when seq-pointer is beyond sequence length.

def is_valid_subseq(arr: List[int], seq: List[int]) -> bool:
    lenArr, lenSeq = len(arr), len(seq)

    if lenArr < lenSeq: 
        return False

    seqIdx = 0
    for x in arr:
        if x == seq[seqIdx]:
            seqIdx += 1
        if seqIdx == lenSeq:
            break 
    
    return seqIdx == lenSeq 

def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]

    sequences =[
        [1, 6, -1, 10],
        [5, 1, 22, 25, 6, -1, 8, 10],
        [5, 1, 22, 6, -1, 8, 10],
        [22, 25, 6],
        [25],
        [5, 1, 22, 25, 6, -1, 8, 10, 12],
        [5, 1, 22, 23, 6, -1, 8, 10],
        [1, 6, -1, -1],
        [5, 1, 22, 25, 6, -1, 8, 10, 10]
    ]

    print("Array =", array)
    for seq in sequences:
        str_out = "IS" if is_valid_subseq(array, seq) else "IS NOT"
        print(f"{seq}\n {str_out} a subsequence of the array.")
    
if __name__ == "__main__":
    main()