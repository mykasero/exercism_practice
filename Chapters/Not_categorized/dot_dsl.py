NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        self.data = data

        if data is not None:
            if isinstance(self.data,int) or isinstance(self.data,str):
                raise TypeError("Graph data malformed")

            elif len(self.data[0]) < 2:
                raise TypeError("Graph item incomplete")

            elif self.data is not None:
                for item in self.data:
                    if item[0] == 0:
                        if len(item) > 3:
                            raise ValueError("Node is malformed")
                        else:
                            self.nodes.append(Node(item[1],item[2]))
                    elif item[0] == 1:
                        if len(item) < 4:
                            raise ValueError("Edge is malformed")
                        else:
                            self.edges.append(Edge(item[1],item[2],item[3]))
                    elif item[0] == 2:
                        if len(item) > 3:
                            raise ValueError("Attribute is malformed")
                        else:
                            self.attrs[item[1]] = item[2]
                    elif item[0] > 2:
                        raise ValueError("Unknown item")


'''
Instructions
A Domain Specific Language (DSL) is a small language optimized for a specific domain. Since a DSL is targeted, 
it can greatly impact productivity/understanding by allowing the writer to declare what they want rather than how.

One problem area where they are applied are complex customizations/configurations.

For example the DOT language allows you to write a textual description of a graph which is then transformed into a
picture by one of the Graphviz tools (such as dot). A simple graph looks like this:

graph {
    graph [bgcolor="yellow"]
    a [color="red"]
    b [color="blue"]
    a -- b [color="green"]
}
Putting this in a file example.dot and running dot example.dot -T png -o example.png creates an image example.png with red and blue circle 
connected by a green line on a yellow background.

Write a Domain Specific Language similar to the Graphviz dot language.

Our DSL is similar to the Graphviz dot language in that our DSL will be used to create graph data structures. However, unlike the DOT Language, 
our DSL will be an internal DSL for use only in our language.

More information about the difference between internal and external DSLs can be found here.

Description of DSL
A graph, in this DSL, is an object of type Graph. This takes a list of one or more tuples that describe:

attributes
Nodes
Edges
The implementations of a Node and an Edge are provided in dot_dsl.py.

For more details on the DSL's expected design and the expected error types and messages, take a look at the test cases in dot_dsl_test.py
'''
'''
import unittest
from dot_dsl import Graph, Node, Edge, NODE, EDGE, ATTR
class DotDslTest(unittest.TestCase):
    def test_empty_graph(self):
        g = Graph()
        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})
    def test_graph_with_one_node(self):
        g = Graph([
            (NODE, "a", {})
        ])
        self.assertEqual(g.nodes, [Node("a", {})])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})
    def test_graph_with_one_node_with_keywords(self):
        g = Graph([
            (NODE, "a", {"color": "green"})
        ])
        self.assertEqual(g.nodes, [Node("a", {"color": "green"})])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {})
    def test_graph_with_one_edge(self):
        g = Graph([
            (EDGE, "a", "b", {})
        ])
        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [Edge("a", "b", {})])
        self.assertEqual(g.attrs, {})
    def test_graph_with_one_attribute(self):
        g = Graph([
            (ATTR, "foo", "1")
        ])
        self.assertEqual(g.nodes, [])
        self.assertEqual(g.edges, [])
        self.assertEqual(g.attrs, {"foo": "1"})
    def test_graph_with_attributes(self):
        g = Graph([
            (ATTR, "foo", "1"),
            (ATTR, "title", "Testing Attrs"),
            (NODE, "a", {"color": "green"}),
            (NODE, "c", {}),
            (NODE, "b", {"label": "Beta!"}),
            (EDGE, "b", "c", {}),
            (EDGE, "a", "b", {"color": "blue"}),
            (ATTR, "bar", "true")
        ])
        self.assertEqual(g.nodes, [Node("a", {"color": "green"}),
                                   Node("c", {}),
                                   Node("b", {"label": "Beta!"})])
        self.assertEqual(g.edges, [Edge("b", "c", {}),
                                   Edge("a", "b", {"color": "blue"})])
        self.assertEqual(g.attrs, {
            "foo": "1",
            "title": "Testing Attrs",
            "bar": "true"
        })
    def test_malformed_graph(self):
        with self.assertRaises(TypeError) as err:
            Graph(1)
        self.assertEqual(type(err.exception), TypeError)
        self.assertEqual(err.exception.args[0], "Graph data malformed")
        with self.assertRaises(TypeError) as err:
            Graph("problematic")
        self.assertEqual(type(err.exception), TypeError)
        self.assertEqual(err.exception.args[0], "Graph data malformed")
    def test_malformed_graph_item(self):
        with self.assertRaises(TypeError) as err:
            Graph([()])
        self.assertEqual(type(err.exception), TypeError)
        self.assertEqual(err.exception.args[0], "Graph item incomplete")
        with self.assertRaises(TypeError) as err:
                Graph([(ATTR, )])
        self.assertEqual(type(err.exception), TypeError)
        self.assertEqual(err.exception.args[0], "Graph item incomplete")
    def test_malformed_attr(self):
        with self.assertRaises(ValueError) as err:
            Graph([(ATTR, 1, 2, 3)])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Attribute is malformed")
    def test_malformed_node(self):
        with self.assertRaises(ValueError) as err:
            Graph([(NODE, 1, 2, 3)])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Node is malformed")
    def test_malformed_EDGE(self):
        with self.assertRaises(ValueError) as err:
            Graph([(EDGE, 1, 2)])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Edge is malformed")
    def test_unknown_item(self):
        with self.assertRaises(ValueError) as err:
            Graph([(99, 1, 2)])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "Unknown item")
'''
