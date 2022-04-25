import os

def freq_writer(freq, name):
    file = open("results/" + name[:-4] + "_freq.txt", "w")
    file.write(str(len(freq)) + '\n')
    for occ in freq:
        if occ[1] == '\n':
            file.write("\\n " + str(occ[0]) + '\n')
        else:
            file.write(occ[1] + " " + str(occ[0]) + '\n')
    file.close()

def bin_writer(encoding, name):
    file = open("results/" + name[:-4] + "_comp.bin", "wb")
    file.write(encoding)
    file.close()

def get_size(path):
    return os.path.getsize(path)
