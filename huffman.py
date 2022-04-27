from binary_tree import BTree

def create_tree(nodes):
    """
    input: list of nodes
    output: BTree/nodes
    returns the constructed huffman tree
    """
    while len(nodes) != 1:
        new_value = nodes[0].value + nodes[1].value
        new_bt = BTree(new_value, None, nodes[0], nodes[1])
        nodes.append(new_bt)
        nodes.remove(nodes[0]), nodes.remove(nodes[0])
        nodes.sort(key = lambda x : x.value)
    return nodes[0]

def code_tree(tree, code=''):
    """
    input: root of the BTree/BTree
    output: dictionnary
    returns a dictionary containing each character and its code
    """
    if tree.isLeaf():
        return {tree.label: code}
    (left, right) = (tree.left_ch, tree.right_ch)
    d = dict()
    d.update(code_tree(left, code + '0'))
    d.update(code_tree(right, code + '1'))
    return d

def encode(dic, text):
    """
    input: dictionnary, original text
    output: string
    return the code representing the compressed file in binary form (bit string)
    """
    code = ''
    for i in text:
        code += dic[i]
    return code

def average_bits(dic):
    """
    input: dictionnary
    output: integer
    returns the average length in bits of the character codes
    """
    return sum([len(x) for x in list(dic.values())])/len([len(x) for x in list(dic.values())])
