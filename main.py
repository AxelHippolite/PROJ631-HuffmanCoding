import occurency

if __name__ == "__main__":
    name = 'textesimple.txt'
    f = open('assets/' + name, 'r')
    text = f.read()
    freq = occurency.finder(text)
    occurency.cleaner(freq)

