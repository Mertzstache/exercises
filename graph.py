#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementation of a graph and a graph node class"""

import time

class GraphNode():
    """graph nodes contain child nodes (one way connection) and a weight"""
    def __init__(self, name=str(int(time.time())), value=None, children=[]):
        """initialize unique name and child nodes"""
        self.name = name
        self.value = value
        self.children = children


    def __str__(self):
        """simple tostring method"""
        child_names = []
        for child in self.children:
            child_names.append(str(child[0].get_name()) + ' with weight: ' + str(child[1]))

        string = "Graph Node with name: " + str(self.name)
        string += " and value: " + str(self.value)
        string += " and has children: ["  + ', '.join(child_names) + "]\n"
        return string

    def get_name(self):
        """gets name"""
        return self.name

    def get_value(self):
        """gets value"""
        return self.value

    def get_children(self):
        """gets children"""
        return self.children

    def add_children(self, new_children):
        """adds a list of children to the current list of children"""
        self.children = self.get_children() + new_children

    # def remove_child(self, remove_me):
    #     """removes a specific reference to a child"""
    #     self.children.remove(remove_me)

class Graph():
    """graph class, a dicitonary of GraphNode objects"""

    def __init__(self, graph_nodes=[]):
        self.nodes = {}
        for node in graph_nodes:
            self.nodes[node.get_name()] = node

    def __str__(self):
        string = "List of nodes:\n\n"
        for node in self.nodes.values():
            string += str(node)
        return string

    def add_node(self, node):
        self.nodes[node] = node        


def main():
    """main function"""

    node1 = GraphNode(name="1", value=1)
    node2 = GraphNode(name="2", value=2)
    node3 = GraphNode(name="3", value=3)
    node4 = GraphNode(name="4", value=4)

    node1.add_children([(node3, 3), (node4, 10)])
    node3.add_children([(node2, 1), (node1, 2)])
    node4.add_children([(node2, 4)])

    node5 = GraphNode(name="5", value=5, children=[(node1, 10)])

    graph = Graph([node1, node2, node3, node4])
    print(graph)
    graph.add_node(node5)
    print(graph)

if __name__ == "__main__":
    main()
