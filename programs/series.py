"""
Define classes and use inheritance to define arithmetic, geometric, and 
Fibonacci series.

Created on Sun Mar 19 2023
"""


class Progression:
    def __init__(self, start):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def print_progression(self, n):
        print(" ".join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, start=0, increment=1):
        super().__init__(start)
        self._incr = increment

    def _advance(self):
        self._current += self._incr


class GeometricProgression(Progression):
    def __init__(self, start=1, base=2):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


def main():
    N = 10

    print("Test Progression class:")
    Progression(start=1).print_progression(N)

    print("Test Arithmetic Progression class:")
    ArithmeticProgression(start=2, increment=2).print_progression(N)

    print("Test Geometric Progression class:")
    GeometricProgression(start=1, base=2).print_progression(N + 1)

    print("Test Fibonacci Progression class:")
    FibonacciProgression(first=0, second=1).print_progression(2 * N)

    print("Test Fibonacci Progression class:")
    FibonacciProgression(first=3, second=4).print_progression(2 * N)


if __name__ == "__main__":
    main()
