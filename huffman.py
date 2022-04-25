from binary_tree import BTree


def create_tree(nodes):
    while len(nodes) != 1:
        new_value = nodes[0].value + nodes[1].value
        new_bt = BTree(new_value, None, nodes[0], nodes[1])
        nodes.append(new_bt)
        nodes.remove(nodes[0]), nodes.remove(nodes[0])
        nodes.sort(key = lambda x : x.value)
    return nodes[0]
