import os

def freq_writer(freq, name):
    """
    input: list of the number of occurrences, name of the original file
    output: nothing
    generates the text file that will contain the alphabet of the original text 
    """
    file = open("results/" + name[:-4] + "_freq.txt", "w")
    file.write(str(len(freq)) + '\n')
    for occ in freq:
        if occ[1] == '\n':
            file.write("\\n " + str(occ[0]) + '\n')
        else:
            file.write(occ[1] + " " + str(occ[0]) + '\n')
    file.close()

def bin_writer(encoding, name):
    """
    input: binary encoding of compressed text, name of the original file
    output: nothing
    generates the binary file that will contain the compressed text
    """
    file = open("results/" + name[:-4] + "_comp.bin", "wb")
    file.write(encoding)
    file.close()

def get_size(path):
    """
    input: path of the fil
    output: float
    return the size(in bytes) of the file
    """
    return os.path.getsize(path)
