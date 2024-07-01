from functools import partial

class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, tree, parents=[]):
        self.tree, self.parents = tree, parents

        for val in ('left', 'right', 'value'):
            setattr(self, 'set_%s' % val, partial(self.set,val))
            setattr(self, val, partial(self.get,val))

    def get(self, key):
        if key == 'value':
            return self.tree['value']

        if self.tree[key]:
            return (Zipper(self.tree[key], self.parents + [self]))
        else:
            return (None)


    def set(self, key, item):
        self.tree[key] = item

        if self.parents:
            return self.parents[0]
        else:
            return self


    def up(self):
        if self.parents:
            return (self.parents[-1])
        else:
            return (None)


    def to_tree(self):
        if self.parents:
            return self.parents[0].tree
        else:
            return self.tree
