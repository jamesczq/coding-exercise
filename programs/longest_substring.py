"""
Longest substring without repeating characters

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Created on Wed Jun 15 2022
"""
import argparse 

# Use sliding window plus hashset to achieve O(n) runtime:
# - Use a hashSet to store the chars in the current window [i, j)
# - If s[j] is not in hashSet, slide j to the right until s[j] is in the hashSet
# - Do this for i
def longest_substr(s: str) -> int:
    chars = [0]*128
    i, j = 0, 0
    res = 0

    while j < len(s):
        r_char = s[j]
        chars[ord(r_char)] += 1

        while chars[ord(r_char)] > 1:
            l_char = s[i]
            chars[ord(l_char)] -= 1
            i += 1
        
        res = max(res, j - i + 1)

        j += 1 
    
    return res 

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", type=str, default=None, required=False)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    print("String | Len(longest substr, no repeat chars)")
    if not args.s:
        s_arr = ["abcabcbb", "bbbbb", "pwwkew"]
        for s in s_arr:
            print(s, " | ", longest_substr(s))
    else:
        print(args.s, " | ", longest_substr(args.s))

if __name__ == "__main__":
    main()
