from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def copy(self):
        return Tree(self.label, [c.copy() for c in self.children])

    def from_pov(self, from_node: str) -> "Tree":
        new_tree = self.copy()

        if new_tree.label == from_node:
            return new_tree
        path = new_tree.path_from_self(from_node)

        if not path:
            raise ValueError("Tree could not be reoriented")

        assert path[0] is new_tree

        for a, b in zip(path[0:-1], path[1:]):
            a.children.remove(b)
            b.children.append(a)

        return path[-1]

    def path_to(self, from_node: str, to_node: str) -> list[str]:
        new_tree = self.from_pov(from_node)
        path = new_tree.path_from_self(to_node)

        if not path:
            raise ValueError("No path found")

        return [node.label for node in path]

    def path_from_self(self, to_node: str) -> list["Tree"]:
        if self.label == to_node:
            return [self]

        for c in self.children:
            res = c.path_from_self(to_node)
            if res:
                return [self] + res

        else:
            return []  # node not found in tree
'''
Instructions
Reparent a tree on a selected node.

A tree is a special type of graph where all nodes are connected but there are no cycles. 
That means, there is exactly one path to get from one node to another for any pair of nodes.

This exercise is all about re-orientating a tree to see things from a different point of view. 
For example family trees are usually presented from the ancestor's perspective:

    +------0------+
    |      |      |
  +-1-+  +-2-+  +-3-+
  |   |  |   |  |   |
  4   5  6   7  8   9
But there is no inherent direction in a tree. 
The same information can be presented from the perspective of any other node in the tree, by pulling it up to the root and dragging its relationships along with it. 
So the same tree from 6's perspective would look like:

        6
        |
  +-----2-----+
  |           |
  7     +-----0-----+
        |           |
      +-1-+       +-3-+
      |   |       |   |
      4   5       8   9
This lets us more simply describe the paths between two nodes. 
So for example the path from 6-9 (which in the first tree goes up to the root and then down to a different leaf node) can be seen to follow the path 6-2-0-3-9.

This exercise involves taking an input tree and re-orientating it from the point of view of one of the nodes.
'''
# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/pov/canonical-data.json
