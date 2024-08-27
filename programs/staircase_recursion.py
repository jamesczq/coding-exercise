"""
Solve the Staircase Problem: Say a cat can go up staris
- one step a time
- two steps a time
- three steps a time.
Now for a staircase of N steps, how many different possible paths 
can the cat take to reach the top?

Example: say N = 4, the following are possible paths:
1 -> 1 -> 1 -> 1
1 -> 1 -> 2
1 -> 2 -> 1
1 -> 3
2 -> 1 -> 1
2 -> 2
3 -> 1
so there are 7 ways when N = 4.

Created on Thu Jun 23 2022
"""

import argparse


# To jump to the N-th step, the cat can jump from
# (N-1)th step with a jump of one step, or
# (N-2)th step with a jump of two steps, or
# (N-3)th step with a jump of three steps,
# since the cat can jump 1 or 2 or 3 steps a time (given).
# Thus the recursive relation is
# num_paths(N) = num_paths(N-1) + num_paths(N-2) + num_paths(N-3)
# Now all we need to do is to figure out the base case
def num_paths(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4  # 1,1,1, or 1,2, or 2,1, or 3
    return num_paths(n - 1) + num_paths(n - 2) + num_paths(n - 3)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    print(num_paths(args.n))


if __name__ == "__main__":
    main()
