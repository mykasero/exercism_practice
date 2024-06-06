class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = tree_data

    def data(self):
        if len(self.tree) == 1:
            return TreeNode(self.tree[0],None,None)
        else:
            left = []
            right = []

            for i in range(1,len(self.tree)):
                if int(self.tree[i]) <= int(self.tree[0]):
                    left.append(self.tree[i])
                else:
                    right.append((self.tree[i]))
            if len(left) > 0 and len(right) > 0:
                total = [left, right]
            elif len(left) > 0 and len(right) == 0:
                total = [left]
            else:
                total = [right]

            for i in range(len(total)):
                total[i] = sorted(total[i])

            commands= []

            for item in total:
                if len(item) == 3:
                    x = TreeNode(item[1],TreeNode(item[0],None,None),TreeNode(item[2],None,None))
                    commands.append(x)
                    x = None
                elif len(item) == 2:
                    pass
                else:
                    x = TreeNode(item[0],None,None)
                    commands.append(x)
                    x = None

            if len(right) == 0:
                return TreeNode(self.tree[0],commands[0],None)
            elif len(left) == 0:
                return TreeNode(self.tree[0], None, commands[0])
            else:
                return TreeNode(self.tree[0], commands[0], commands[1])
    def sorted_data(self):
        return sorted(self.tree)


