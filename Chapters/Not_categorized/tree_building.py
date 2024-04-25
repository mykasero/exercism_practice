class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    rec_par_ids = []
    record_ids = []
    parent_ids = []
    node_ids = []
    children = []



    records.sort(key=lambda x: x.record_id)

    for item in records:
        record_ids.append(item.record_id)
        parent_ids.append(item.parent_id)
        rec_par_ids.append((item.record_id,item.parent_id))

    ordered_id = [i.record_id for i in records] # those are record ids

    #Errors are done, need to tweak it after writing the main code since
    #ValueError is raised in 5/6 tests that should not generate errors
    if records:
        flags_rec_ids = []
        flags_rec_par = []
        if ordered_id[0] > 0:
            raise ValueError("Record id is invalid or out of order.")
        elif parent_ids[0] > 0:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        for i in range(len(ordered_id)):
            if ordered_id[i] != i:
                raise ValueError("Record id is invalid or out of order.")
        for item in range(1,len(ordered_id)):
            if record_ids[item] == parent_ids[item]:
                raise ValueError("Only root should have equal record and parent id.")
            elif ordered_id[item-1] != ordered_id[item]-1:
                raise ValueError("Record id is invalid or out of order.")
            elif record_ids[item] != parent_ids[item] + 1:
                raise ValueError("Node parent_id should be smaller than it's record_id.")







    if len(record_ids) > 0:
        root = records[0]
    #
    #
    #
    # ordered_id = [i.record_id for i in records]
    # if records:
    #     if ordered_id[-1] != len(ordered_id) - 1:
    #         raise ValueError('broken tree')
    #     if ordered_id[0] != 0:
    #         raise ValueError('invalid')
    # trees = []
    # parent = {}
    # for i in range(len(ordered_id)):
    #     for j in records:
    #         if ordered_id[i] == j.record_id:
    #             if j.record_id == 0:
    #                 if j.parent_id != 0:
    #                     raise ValueError('error!')
    #             if j.record_id < j.parent_id:
    #                 raise ValueError('something went wrong!')
    #             if j.record_id == j.parent_id:
    #                 if j.record_id != 0:
    #                     raise ValueError('error!')
    #             trees.append(Node(ordered_id[i]))
    # for i in range(len(ordered_id)):
    #     for j in trees:
    #         if i == j.node_id:
    #             parent = j
    #     for j in records:
    #         if j.parent_id == i:
    #             for k in trees:
    #                 if k.node_id == 0:
    #                     continue
    #                 if j.record_id == k.node_id:
    #                     child = k
    #                     parent.children.append(child)
    # if len(trees) > 0:
    #     root = trees[0]
    return root
