#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementation of the Linked List Class"""

class LLN():
    """simple implementation of a linked list node"""

    def __init__(self, data=None, next_node=None):
        """initializes the LLN class with defaults to None"""
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return "Linked List Node object with Data: " + str(self.data) + '\n'

    def get_data(self):
        """simply returns data from node"""
        return self.data

    def get_next(self):
        """simply returns next node"""
        return self.next_node

    def update_next(self, new_node):
        """updates the next_node value of this LNN to new_node"""
        self.next_node = new_node

class LL():
    """simple implementation of a linked list"""

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """converts this to string"""
        string = "This Linked List object has size " + str(self.size())
        string += " and contains the following nodes and values: \n"

        curr = self.head
        ctr = 1

        while curr:
            string += "Node number: " + str(ctr) + '\t Data: ' + str(curr.data) + '\n'
            curr = curr.next_node
            ctr += 1

        return string

    def insert(self, new_data):
        """takes in a new data value, and puts it at the head of the list
        Time Complexity: O(1)"""
        new_node = LLN(new_data, self.head)
        # new_node.update_next(self.head)
        self.head = new_node

    def size(self):
        """gets the size of the linked list
        Time Complexity: O(n)"""
        curr = self.head
        ctr = 0

        while curr:
            ctr += 1
            curr = curr.get_next()

        return ctr

    def search(self, target_data):
        """goes through list and returns node if it finds target_data.
        if not, then it raises a value error
        Time Complexity: O(n)"""
        curr = self.head

        while curr:
            if curr.data == target_data:
                return curr
            curr = curr.get_next()

        raise ValueError("Data not in list")

    def delete(self, delete_data):
        """goes through list and makes updates to list in regards
        to removing the node that contains delete_data
        Time Complexity: O(n)"""
        previous_size = self.size()
        curr = self.head
        prev = None

        while curr:
            if curr.data == delete_data:
                if prev:
                    prev.update_next(curr.get_next())
                else:
                    self.head = curr.get_next()
            prev = curr
            curr = curr.next_node

        if previous_size == self.size():
            raise ValueError("Data not in list")


def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(999)
        tail = dummy
        
        while True:
            if not l1:
                tail.next_node = l2
                break
            elif not l2:
                tail.next_node = l1
                break            
            if l1.data <= l2.data:
                tail.next_node = l1
                l1 = l1.next_node
            else:
                tail.next_node = l2
                l2 = l2.next_node
            tail = tail.next_node
            
        return dummy.next_node


def main():
    """main function - all testing moved to linked_list_test.py, run that file for the tests"""

    # node = LLN(data=1)
    # linked_list = LL(head=node)
    # linked_list.insert(2)
    # print(linked_list)
    # print(linked_list.search(2))

    # linked_list.insert(4)
    # print(linked_list)
    # linked_list.delete(2)
    # print(linked_list)
    # linked_list.delete(4)
    # print(linked_list)

if __name__ == "__main__":
    main()
