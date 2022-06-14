"""
Sampling without replacement (permutation):

Return a permutation: choose m samples without replacement from [0, 1, 2, ..., n-1].
 
Created on Mon Jun 13 2022
"""
import argparse
import random

def permutation(m, n):
    """Return m samples permutation of [0, 1, 2, ..., n-1]"""
    perm = list(range(n))

    for i in range(m):
        r = random.randrange(i, n)
        perm[i], perm[r] = perm[r], perm[i]
    
    return perm[:m]

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int, help="sample size")
    parser.add_argument("n", type=int, help="range") 
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    return permutation(args.m, args.n)

if __name__ == "__main__":
    print(main())
