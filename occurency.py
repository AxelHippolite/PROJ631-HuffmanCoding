def finder(text):
    """
    input: text to compress (string)
    output: list
    return a list of tuples where each tuple contains a character and its number of occurrence in the text
    """
    freq = []
    for i in range(256):
        if text.count(chr(i)) > 0:
            freq.append((text.count(chr(i)), chr(i)))
    return freq

def cleaner(freq):
    """
    input: list
    output: list
    returns the same list as the finder() function but ordered by increasing frequency
    """
    return freq.sort(key = lambda x : x[0])
    
            
