def finder(text):
    freq = []
    for i in range(256):
        if text.count(chr(i)) > 0:
            freq.append((text.count(chr(i)), chr(i)))
    return freq

def cleaner(freq):
    return freq.sort(key = lambda x : x[0])
    
            
