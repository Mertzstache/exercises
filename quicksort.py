#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Quicksort"""

#import sys
import numpy as np
#import os
#import shutil

#****************************************
# quicksort.py
# Sorts a list
# $python quicksort.py
#****************************************

def swap(lst, i, j):
    """swaps items in ls at index i and j"""
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def quicksort(lst, lower, upper, its):
    """sorts a list and returns sorted list and number of its"""

    i = lower
    j = upper
    pivot = choose_pivot(lst, lower, upper)
    while i <= j:
        while lst[i] < lst[pivot]:
            i += 1
        while lst[j] > lst[pivot]:
            j -= 1
        if i <= j:
            swap(lst, i, j)
            i += 1
            j -= 1
    if lower < j:
        its = quicksort(lst, lower, j, its + 1)[1]
    if i < upper:
        its = quicksort(lst, i, upper, its + 1)[1]

    return lst, its


def choose_pivot(lst, lower, upper):
    # """choose a pivot INDEX here"""
    smallest_index = 0
    smallest_diff = 99999999
    if lower != upper:
        avg_lst = lst[lower:upper]
        avg = sum(avg_lst)/len(avg_lst)
        for index in range(len(avg_lst)):
            print(index)
            if avg_lst[index] - avg < smallest_diff:
                smallest_index = index
                smallest_diff = avg_lst[index] - avg
    return lower + smallest_index
    # return lower + (upper - lower)//2

def main():
    """main function"""
    lst = [2, 4, 7, 119, 4, 6, 2, 11, 78, 22, 100, 44, 77, 82, 61, 3]
    #lst = [2, 4, 7, 3]
    print("unsorted list ", lst)
    lst, num_its = quicksort(lst, 0, len(lst) - 1, 0)
    print("sorted list ", lst)
    print("number of iterations ", num_its)

    exit()

if __name__ == "__main__":
    main()
