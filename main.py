import occurency
import huffman
import file_manager
from binary_tree import BTree

if __name__ == "__main__":
    name = 'textesimple.txt'
    f = open('assets/' + name, 'r')
    text = f.read()
    freq = occurency.finder(text)
    occurency.cleaner(freq)

    nodes = [BTree(occ[0], occ[1]) for occ in freq]
    root = huffman.create_tree(nodes)

    paths = huffman.code_tree(root)

    encoding = huffman.encode(paths, text)
    result = int(encoding, base=2).to_bytes((len(encoding)+7)//8, byteorder='big')

    file_manager.freq_writer(freq, name)
    file_manager.bin_writer(result, name)

    final_size = file_manager.get_size("results/" + name[:-4] + "_comp.bin") #+ file_manager.get_size("results/" + name[:-4] + "_freq.txt")
    initial_size = file_manager.get_size("assets/" + name)
    rate_compression = 1 - (final_size / initial_size)
