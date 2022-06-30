"""
Given an array of integers that are sorted, return a new array of the same
length with squares of the original integers in sorted order.

Note that there can be large but negative integers.

Example: 
Input: [-2, 1, 4]
Output: [1, 4, 16]

Created Tue Jun 28 2022
"""
from typing import List 

# Idea:
# In a sorted array, the largest square must be either 
# (arr[0])^2 or (arr[End]^2)
# Large Negative <----- 0 -----> Large Positive
# So can use two-pointer technique, start with L, R ends
# and put the largest square to the end of output array
# and continue incr L or decr R
def sorted_squared_array(arr: List[int]) -> List[int]:
    N = len(arr)
    arr_out = [0] * N 
    left, right = 0, N-1
    for i in reversed(range(N)):
        sqrL, sqrR = arr[left]**2, arr[right]**2
        if sqrL <= sqrR:
            arr_out[i] = sqrR
            right -= 1
        else:
            arr_out[i] = sqrL 
            left += 1
    return arr_out 

def main():
    arr = [-7, -2, 0, 1, 5]
    print(arr, " --> ", sorted_squared_array(arr))

    arr = [-2, -2, -1, 0, 2]
    print(arr, " --> ", sorted_squared_array(arr))

if __name__ == "__main__":
    main()