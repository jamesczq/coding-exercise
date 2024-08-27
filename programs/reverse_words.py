"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 
Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
from typing import List

def locs_of_words(str_in:str) -> List[List[int]]:
    """_summary_

    Args:
        str_in (str): _description_

    Returns:
        List[List[int]]: _description_
    """
    S0 = " "
    arr_out = []
    arr_tmp = []
    for i, ch in enumerate(str_in):
        if ch != S0:
            arr_tmp.append(i)
        else:
            arr_tmp = []
            arr_out.append(arr_tmp)    
    return [arr for arr in arr_out if arr]

def str2words(str_in: str) -> List[str]:
    """_summary_

    Args:
        str_in (str): _description_

    Returns:
        List[str]: _description_
    """
    word_locs = locs_of_words(str_in)
    arr_out = []
    for sublist in word_locs:
        str_tmp = ""
        for i in sublist:
            str_tmp += str_in[i] 
        arr_out.append(str_tmp)
    return arr_out

def reverse_string(str_in: str) -> str:
    """_summary_

    Args:
        str_in (str): _description_

    Returns:
        str: _description_
    """
    words = str2words(str_in)
    str_out = ""
    for i in range(len(words)-1, 0, -1):
        str_out += words[i]
        str_out += " "
    str_out += words[0]
    return str_out

def main():
    test_strings = ["  hello world  ", "a good   example", "the sky is blue"]
    for str_in in test_strings:
        print(f'String = "{str_in}"')
        print("Words:", str2words(str_in), " are located at:", locs_of_words(str_in))
        print("When reversed, they become:", f'"{reverse_string(str_in)}"')
        print("\n")

if __name__ == "__main__":
    main()