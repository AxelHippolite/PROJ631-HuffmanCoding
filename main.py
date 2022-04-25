import occurency
import huffman
from binary_tree import BTree

if __name__ == "__main__":
    name = 'textesimple.txt'
    f = open('assets/' + name, 'r')
    text = f.read()
    freq = occurency.finder(text)
    occurency.cleaner(freq)

    nodes = [BTree(occ[0], occ[1]) for occ in freq]
    root = huffman.create_tree(nodes)
