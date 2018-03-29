#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementation of a simple dynamic program that optimizes """
from graph import GraphNode, Graph
def shortest_path(graph, start, end, current_value, visited, path):
	if start not in visited:
		minimum = 1000
		index = -1
		for i, node in [node for ls in start.get_children() if node not in visited]:
			val = shortest_path(graph, node[0], end, current_value + node[1], visited.append(node[0]))
			if val < minimum:
				minimum = val
				index = i
	else:
		return 1000



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
    graph.add_node(node5)
    print(shortest_path(graph, node1, node2, 0, []))

if __name__ == "__main__":
    main()
