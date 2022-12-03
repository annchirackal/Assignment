def analyzeFile(filename):
    f = open(filename,"r")
    data = []
    for line in f:
        for words in line:
            data.append(words)
    return(data)
words = analyzeFile("out.txt")
print(words)