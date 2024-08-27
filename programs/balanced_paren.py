"""
Balanced parenthese

Write a program that tests if a string containing balanced pairs of 
(), [], {} that match in the correct order.

For example:
"([]){()}" is balanced
"[()[]{()}]" is balanced
"{(})" is not balanced
"[()[]{()" is not balanced

Hint: which left parenthesis does a right parenthesis match with?

Created on Thu Jun 16 2022
"""

import argparse


# Use Stack
# - Store the unmatched (yet) left ( or [ or {
# - if a right ) or ] or } is encountered and the stack is empty or
# the top of the stack is a different type of parenthesis,
# then the right parenthesis is Not matched
def is_balanced(s: str) -> bool:
    left_paren = []
    parenL = set(["(", "[", "{"])
    parenR = set([")", "]", "}"])
    lookup = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in parenL:
            left_paren.append(char)
        elif char in parenR:
            if not left_paren or lookup[left_paren.pop()] != char:
                return False
    return not left_paren


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("s", type=str)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    return is_balanced(args.s)


if __name__ == "__main__":
    print(main())
