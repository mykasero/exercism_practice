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

    def from_pov(self, from_node):
        # new_root_flag = False
        # test1 = self.label
        # test2 = [test1] + [item.label for item in self.children]
        # if self.children == []:
        #     return Tree(self.label)
        # else:
        #     if len(test2) == 1:
        #         pass
        test = self.dig_recur(self.label,self.children)
        # else:
        #
        #     new_tree = []
        #     if self.label == from_node and new_root_flag == False:
        #         new_root_flag = True
        #         new_tree.append(self.label)
        #     elif new_root_flag == True:
        #         new_tree.append(self.label)
        #
        #     stop = "stop"


    def path_to(self, from_node, to_node):
        if self.children == []:
            return Tree(self.label)

        else:
            test = "test"


    def dig_recur(self, label, children):
        x = label
        y = children
        test = type(Tree)
        elements = []
        if isinstance(children, Tree) == True:
            elements.append(x)
            new_tree = self.dig_recur(y.label, y.children)

