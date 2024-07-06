def tree_from_traversals(preorder, inorder):
    final = {}

    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    else:
        uniques = dict()
        #count repeats

        for item in preorder:
            if item not in inorder:
                raise ValueError("traversals must have the same elements")
            if item in uniques.keys():
                uniques[item] += 1
            else:
                uniques[item] = uniques.get(item, 1)

            if uniques[item] > 1:
                raise ValueError("traversals must contain unique items")

        return build_tree(preorder, inorder)


def build_tree(preorder, inorder):
    if len(preorder) == 0:
        return {}

    value = preorder[0]
    idx = inorder.index(value)

    return {
        'v': value,
        'l': build_tree(preorder[1:1 + idx], inorder[:idx]),
        'r': build_tree(preorder[idx + 1:], inorder[idx + 1:]),
    }