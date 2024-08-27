"""
Fibonacci[n]

Use dynamic programming (e.g. memoization) to compute n-th Fibonacci number
Fib seq = {0, 1, 1, 2, 3, 5, 8, 13, 21, ...}.

Created on Fri Jun 10 2022
"""

import argparse


def fib_v1(n: int, memo=dict()):
    if n == 0 or n == 1:
        return n
    if not memo.get(n):
        memo[n] = fib_v1(n - 1, memo) + fib_v1(n - 2, memo)
    return memo[n]


def fib_v2(n: int):
    fib_array = [0] * (n + 1)
    fib_array[0], fib_array[1] = 0, 1
    for i in range(2, n + 1):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[-1]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("-v", "--version", type=int, default=1)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    if args.version == 1:
        return args.n, fib_v1(args.n)
    else:
        return args.n, fib_v2(args.n)


if __name__ == "__main__":
    n, fib = main()
    print(f"\nThe {n}th Fibonacci number is {fib}.\n")
