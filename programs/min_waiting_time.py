"""
Given a non-empty array of positive integers representing amounts of time the
specific queries take to execute. Only one query at a time, but the queries 
can be excuted in any order.

A query's waiting time is defined as the time it must wait for all its 
preceding queries to finish. For example, say [q1=1, q2=4, q3=4], the waiting
time for q2 is 1, the waiting time for q3 is 1 + 4 = 5.

Write a function that returns the minimum amount of total waiting time for 
all the queries.

Example:
queries = [3, 2, 1, 2, 6]
output = 17
# 17 = min_waiting_time([1, 2, 2, 3, 6]) = 0 + 1 + (1+2) + (1+2+2) + (1+2+2+3)
"""

from typing import List


def min_waiting_time_v1(queries: List[int]):
    n = len(queries)
    if n <= 1:
        return 0
    queries.sort()
    cum_sum = 0
    cum_sums = []
    for i in range(n - 1):
        cum_sum += queries[i]
        cum_sums.append(cum_sum)
    waiting_time = 0
    for s in cum_sums:
        waiting_time += s
    return waiting_time


def main():
    queries = [3, 2, 1, 2, 6]
    print("Queries:", queries)
    print("Min waiting time:", min_waiting_time_v1(queries))


if __name__ == "__main__":
    main()
