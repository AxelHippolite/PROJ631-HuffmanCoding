import occurency
import huffman
import file_manager
from binary_tree import BTree

if __name__ == "__main__":
    print("########## Compression ##########")
    name = input("Enter Name File : ") #ask the user for the name of the file to be compressed
    f = open('assets/' + name, 'r')
    text = f.read()
    freq = occurency.finder(text) #create a list of the number of times each character appears in the text
    occurency.cleaner(freq) #sorting the list

    nodes = [BTree(occ[0], occ[1]) for occ in freq] #creation of a tree/node for each occurrence
    root = huffman.create_tree(nodes) #construction of the tree

    paths = huffman.code_tree(root) #generation of huffman codes

    encoding = huffman.encode(paths, text) #text compression
    result = int(encoding, base=2).to_bytes((len(encoding)+7)//8, byteorder='big') #conversion of the binary string to binary in order to write it to the binary file

    file_manager.freq_writer(freq, name) #generation of the text file containing the alphabet
    file_manager.bin_writer(result, name) #generation of the binary file

    final_size = file_manager.get_size("results/" + name[:-4] + "_comp.bin") #+ file_manager.get_size("results/" + name[:-4] + "_freq.txt")
    initial_size = file_manager.get_size("assets/" + name)
    rate_compression = 1 - (final_size / initial_size) #compression ratio calculation

    average_bits = huffman.average_bits(paths) #calculation of the average length (in bits) of each code
    
    print("Compression Rate (without alphabet file) :", rate_compression) #display of results
    print("Average Bits per Encoded Character :", average_bits)
    print("#################################")
    input("Press any key to Continue...")
