#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Quicksort"""


import pprint

def longest_common_subsequence(word1, word2, table):
    """uses iterative dword2namic programming to edit table bword2 reference and return value"""
    for letter1 in range(len(word2) + 1):
        for letter2 in range(len(word1)+1):
            if letter1 == 0 or letter2 == 0:
                table[letter1][letter2] = 0
            elif word2[letter1 - 1] == word1[letter2 - 1]:
                table[letter1][letter2] = 1 + table[letter1 -1][letter2 - 1]
            else:
                table[letter1][letter2] = max(table[letter1][letter2-1], table[letter1-1][letter2])
    return table[len(word2)][len(word1)]


def main():
    """main function"""
    # Driver program to test the above function
    word1 = "BCDEHI"
    word2 = "BFEGIS"

    table = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]

    value = longest_common_subsequence(word1, word2, table)

    print("LCS value: ", value)

    print("Table:")
    printer = pprint.PrettyPrinter(indent=4)
    printer.pprint(table)

if __name__ == '__main__':
    main()
    