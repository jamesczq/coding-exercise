"""
Find the greatest common divider (gcd) using Euclid's algorithm

Example:
gcd(1440, 408) = 24

Created on Sun Jun 19 2022
"""
import argparse

def gcd(p: int, q: int) -> int:
    if p < q: 
        p, q = q, p 
    if q == 0:
        return p 
    return gcd(q, p % q)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("q", type=int)
    args = parser.parse_args()
    return args 

def main():
    args = get_args()
    print(f"\ngcd({args.p}, {args.q}) = {gcd(args.p, args.q)}\n")

if __name__ == "__main__":
    main()