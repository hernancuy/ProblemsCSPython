import functools
from typing import Dict
from functools import lru_cache
from typing import Generator
from unittest import case


memo: Dict[int, int] = {0: 0, 1: 1} # our base cases



def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

def fib2(n: int) -> int:
    if n < 2: # base case
        return n
    return fib2(n - 2) + fib2(n - 1) # recursive base

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # memoization
    return memo[n]

@lru_cache(maxsize=None)
def fib4(n: int) -> int: # same definition as fib2()
    if n < 2: # base case
        return n
    return fib4(n - 2) + fib4(n - 1) # recursive base

def fib5(n: int) -> int:
    if n == 0: return n # sepecial case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

## generating Fibonacci numbers with a generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 #special case
    last : int = 0 # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step


if __name__ =="__main__":
    #print(fib5(5))
    #print(fib5(50))
    for i in fib6(50):
        print(i)
