"""
Find a root of a polynomial such that
a[n]*x^n + a[n-1]*x^(n-1) + ... +a1*x + a0 = 0,
using Newton's method.

Example:
root([1,0,-1], 0) find a root of x^2 - 1 = 0 around 0.

Created on Mon Jun 20 2022
"""

from typing import List
import argparse


def pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    return x * pow(x, n - 1)


def polynomial(x: float, coeffs: List[float]) -> float:
    """Param Coeffs: lists the coefficients of x^n, x^(n-1), ..., x, C."""

    # say coeffs = [30, 20, 10], it corresponds to 30 x^2 + 20 x + 10,
    # so the exponents for x are [2, 1, 0]
    n = len(coeffs) - 1
    exponents = range(n, -1, -1)

    powsum = 0.0
    for i, coeff in enumerate(coeffs):
        powsum += coeff * pow(x, exponents[i])

    return powsum


def polynomial_derivative(x: float, coeffs: List[float]) -> float:
    """d/dx (a[n] * x^n + a[n-1) * x^(n-1) + ... + a1 * x + a0) =
    n*a[n]*x^(n-1) + (n-1)*a[n-1]*x^(n-2) + ... + a1
    """
    n = len(coeffs) - 1
    # Coeffs_n = [n, n-1, ..., 1]
    coeffs_n = range(n, 0, -1)
    # Exponents = [n-1, n-2, ..., 1, 0]
    exponents = range(n - 1, -1, -1)

    powsum = 0.0
    for i, coeff in enumerate(coeffs[:-1]):
        powsum += coeffs_n[i] * coeff * pow(x, exponents[i])

    return powsum


def polynomial_root(coeffs: List[float], x0: float, eps=1e-12) -> float:
    x_old, x_new = x0, 0
    while True:
        deriv = polynomial_derivative(x_old, coeffs)  # Avoid */0 error
        if abs(deriv) < eps:
            deriv += eps
        x_new = x_old - polynomial(x_old, coeffs) / deriv
        x_old = x_new
        if abs(polynomial(x_new, coeffs)) < eps:
            break
    return x_new


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coeffs", nargs="+", type=float)
    parser.add_argument("--x0", type=float)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    r = polynomial_root(args.coeffs, args.x0)

    # Formatted print out
    n = len(args.coeffs) - 1
    exponents = range(n, 0, -1)
    str_out = ""
    for i, coeff in enumerate(args.coeffs[:-1]):
        str_out += f"{coeff} * x^{exponents[i]} + "
    str_out += f"{args.coeffs[-1]}"
    print(f"\nr = {r:.4f} is a root of {str_out} around x_init = {args.x0}")

    str_out = ""
    for i, coeff in enumerate(args.coeffs[:-1]):
        str_out += f"{coeff} * r^{exponents[i]} + "
    str_out += f"{args.coeffs[-1]}"
    print(f"Check: {str_out} = {polynomial(r, args.coeffs):.4f}\n")


if __name__ == "__main__":
    main()
