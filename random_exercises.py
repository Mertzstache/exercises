#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""random exercises"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(n):
        """
        :type n: int
        :rtype: bool
        """
        #find the divisor to pick off the first digit
        divisor = 1
        while (n / divisor >= 10):
            divisor *= 10

        while (n != 0):
            #truncate the rest of the digits off bc they become decimals
            leading = n // divisor 
            trailing = n % 10

            # first and last not the same
            if (leading != trailing): 
                return False

            # first remove the first digit by using modulo, then truncate the last one
            n = (n % divisor)//10

            # make divisor go down by a factor of 100 since we removed two digits
            divisor = divisor/10**2

        return True

def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        numtomap = {}
        string = "_@abcdefghijklmnopqrstuvwxyz"
        for i in range(10):
            if i < 2:
                numtomap[str(i)] = string[0]
                string = string[1:]
            else:
                numtomap[str(i)] = [string[j] for j in range(3 + i//7 - i//8 + i//9)]
                string = string[3 +  i//7 - i//8 + i//9:]
        
        combinations = numtomap[digits[0]]
        digits = digits[1:]
        for char in digits:
            new_combos = []
            for digits in numtomap[char]:
                new_combos += [combo+digits for combo in combinations]
            combinations = new_combos
            
        return combinations

def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(100)
        tail = dummy
        
        result = 0
        multiplier = 1
        while l1 or l2 or result != 0:
            if l1 and l2:
                result += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
                
            elif not l1 and l2:
                result +=  l2.val
                l2 = l2.next
            elif not l2 and l1:
                result +=  l1.val
                l1 = l1.next
            tail.next = ListNode(result%10)
            tail = tail.next
            result = result //10
            
        return dummy.next


def main():
    print(isPalindrome(999))
    # print(letterCombinations('2039799555'))



if __name__ == "__main__":
    main()