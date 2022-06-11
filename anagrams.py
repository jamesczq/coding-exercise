"""
Determine if two words are anagrams of each other (case-insensitive).

Example:
are_anagrams("python", "thonpy") = True

Created on Fri Jun 10 2022
"""
import argparse

def are_anagrams(str1: str, str2: str) -> bool:
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False
    else:
        arr1, arr2 = list(str1), list(str2)

        a_to_z_str1 = [0 for _ in range(26)]
        a_to_z_str2 = [0 for _ in range(26)]
        
        for char in arr1:
            idx = ord(char) - ord('a')
            a_to_z_str1[idx] += 1
        
        for char in arr2:
            idx = ord(char) - ord('a')
            a_to_z_str2[idx] += 1
        
        for i in range(26):
            if a_to_z_str1[i] != a_to_z_str2[i]:
                return False
        
        return True

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("str1", type=str)
    parser.add_argument("str2", type=str)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    return are_anagrams(args.str1, args.str2)

if __name__ == "__main__":
    print(main())        
