#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementation of the Stack and Queue class using previously built linnked list class"""
from linked_list import LL, LLN
class Stack():
    """implementing stack functionality as a linked list"""
    def __init__(self, data):
        """initialization"""
        self.linked_list = LL(LLN(data))

    def __str__(self):
        """tostring method"""
        return str(self.linked_list).replace('Linked List', 'Stack')

    def peek(self):
        """get top of stack"""
        return self.linked_list.head

    def pop(self):
        """popping off the last value (first value in LL)"""
        node = self.linked_list.head
        self.linked_list.head = self.linked_list.head.get_next()
        return node

    def push(self, new_value):
        """pushing stuff onto list (onto top of LL))"""
        self.linked_list.insert(new_value)

class Queue():
    """implementing queue functionality from LL"""
    def __init__(self, data):
        """init"""
        self.linked_list = LL(LLN(data))

    def __str__(self):
        """tostring method"""
        return str(self.linked_list).replace('Linked List', 'Queue')

    def enqueue(self, new_value):
        """enqueuing stuff onto list (onto top of LL))"""
        self.linked_list.insert(new_value)

    def dequeue(self):
        """takes the last thing off of the list"""
        curr = self.linked_list.head
        prev = None
        while curr.get_next():
            prev = curr
            curr = curr.get_next()

        if prev:
            prev.update_next(None)
            return curr
        else:
            raise ValueError("Cant remove last element of queue")


def main():
    """main function - all testing moved to linked_list_test.py, run that file for the tests"""
    stack = Stack(1)
    stack.push(3)
    stack.push(8)
    stack.push(2)
    print("Original value\n" + str(stack))
    print("Peek value\n" + str(stack.peek()))
    print("Pop value\n" + str(stack.pop()))
    print("Post-Pop value\n" + str(stack))

    queue = Queue(1)
    queue.enqueue(3)
    queue.enqueue(8)
    queue.enqueue(2)
    print("Original value\n" + str(queue))
    print("Dequeued value\n" + str(queue.dequeue()))
    print("Post-Dequeue value\n" + str(queue))



if __name__ == "__main__":
    main()
