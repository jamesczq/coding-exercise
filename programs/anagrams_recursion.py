"""
Return all possible anagrams of a string of length n.

For example:
anagrams("abc") = [abc, acb, bac, bca, cab, cba]

A string of length n should have n! anagrams.

Created on Thu Jun 23 2022
"""
from typing import List
import argparse

# Use recursion: say to find anagrams of "abcd",
# imagine you already have a list of anagrams of "abc".
# So the problem becomes inserting "d" to each of the anagrams of "abc":
# d-abc, a-d-bc, ab-d-c, abc-d, 
# d-bac, b-d-ac, ba-d-c, bac-d, etc.
def get_anagrams(s: str) -> List[str]:
    if len(s) == 1: return [s[0]]

    collection = []
    substring_anagrams = get_anagrams(s[1:])
    for anagram in substring_anagrams:
        # An easy logic error is to iterate j from range(len(anagram))
        # That's wrong: there should be 1 + len(anagram) places for s[0]
        # Thus j should be in range(1 + len(anagram)) or simply range(len(s))
        for j in range(len(s)):
            collection.append(anagram[:j] + s[0] + anagram[j:])

    return collection

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("s", type=str)
    parser.add_argument("-d", "--details", type=bool, default=False)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    collection = get_anagrams(args.s)
    if args.details:
        print(f"There are {len(collection)} for '{args.s}' of length {len(args.s)}:\n{collection}")
    else:
        print(f"There are {len(collection)} for '{args.s}' of length {len(args.s)}")

if __name__ == "__main__":
    main()