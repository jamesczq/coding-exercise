"""
Find all triplets in an array that sum up to a given target, using 
two-pointer technique.

Example: 
array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

Time: O(n^2)
Space: O(n)

Created on Fri Aug 12, 2022
"""

from typing import List


def find_triplets(array: List[int], target: int) -> List[List[int]]:
    arr_out = []
    array.sort()
    for i in range(len(array) - 2):
        left, right = i + 1, len(array) - 1
        while left < right:
            tri_sum = array[i] + array[left] + array[right]
            if tri_sum < target:
                left += 1
            elif tri_sum > target:
                right -= 1
            else:  # tri_sum == target
                arr_out.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
    return arr_out


def main():
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    str_out = f"Triplets in {arr} that sum up to {target} are:\n"
    str_out += f"{find_triplets(arr, target)}"
    print(str_out)


if __name__ == "__main__":
    main()
