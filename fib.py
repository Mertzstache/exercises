#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementation of the fib sequence algo based off of dynamic programming, NOT recursion"""

def fib(num=10):
    """gets the numTH number in the fib sequence, with a default value of 10
    ATTN: 0 INDEXED"""
    fib_minus_2 = 0
    fib_minus_1 = 1

    while num > 0:
        intermediary = fib_minus_2 + fib_minus_1
        fib_minus_2 = fib_minus_1
        fib_minus_1 = intermediary
        num -= 1

    return fib_minus_1

def main():
    """driver program"""
    # 1 1 2 3 5 8 13 21 34 55 89
    print(fib(10))
if __name__ == "__main__":
    main()
