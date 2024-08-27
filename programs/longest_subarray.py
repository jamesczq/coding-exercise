"""
Longest subarray that sums to zero.

Example:
arr = [15, -2, 2, -8, 1, 7, 10, 23]
Ouput: the longest subarray summing to 0 is [-2, 2, -8, 1, 7]

Example:
arr = [1, 2, 3]
Output: None

Created on Fri Jun 17 2022
"""

from typing import List
import argparse

# Idea: Use hash map
# Let prefix(i) = arr[0] + arr[1] + ... + arr[i]
#     prefix(j) = arr[0] + arr[1] + ... + arr[j], j > i
# If prefix(i) == prefix(j), it means
# arr[i+1] + ... + arr[j] = 0

# Algo:
# 1. Create extra space for array prefix[i], a var sum, a var max_len,
# and a hash map to store the sum-index pair
# 2. Iterate through the input array
# 3. For every index, update sum += arr[i]
# 4. Check every index to see if the current sum in the hash map
# - if yes: update max_len = max((current_index - index_in_hash), max_len)
# - else: put the sum in the hash map


def max_subarr(arr: List[int]) -> int:
    hashmap = dict()
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if arr[i] == 0 and max_len == 0:
            max_len = 1

        if curr_sum == 0:
            max_len += 1

        if curr_sum in hashmap:
            max_len = max(max_len, i - hashmap[curr_sum])
        else:
            hashmap[curr_sum] = i

    return max_len


arr = [15, -2, 2, -8, 1, 7, 10, 13]

print(max_subarr(arr))
