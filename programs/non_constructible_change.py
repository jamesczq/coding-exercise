"""
Given an array of positive integers representing the values of coins, return 
the minimum amount of change (min sum of coins) that you cannot create.

Examples:
Given coins= [], you cannot create a change of 1
Given coins = [1, 2, 5], you cannot create a change of 4
Given coints = [5, 7, 1, 1, 2, 3, 22], you cannot create a change of 20

Created on Wed Jul 20 2022
"""
from typing import List 
import argparse

# Main observation: In a sorted array, if you can create a change up to C 
# using a[0] ... a[i-1]. Now comes a[i]
# If a[i] <= C + 1, then any change from C + 1 up to C + a[i] may be made
# But if a[i] > C + 1, then the gap, C + 1, cannot be made.

def find_non_constructible_change(coins: List[int]):
    coins.sort()
    curr_change = 0
    for coin in coins:
        if coin > curr_change + 1:
            return curr_change + 1
        else:
            curr_change += coin
    return curr_change + 1

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coins", nargs="+", type=int, default=None, required=False)
    args = parser.parse_args()
    return args 

def main():
    parser = get_args()
    if parser.coins is None:
        coins = [1,2,5]
    else:
        coins = parser.coins 
    str_out = f"Min change of {find_non_constructible_change(coins)}"
    str_out += f" cannot be made out of {coins}"
    print(str_out)

if __name__ == "__main__":
    main()

