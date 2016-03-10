dictionary = []
dictfile = open("dictionary.txt", "r")
for x in range(9315):
    dictword = dictfile.readline()
    dictword = dictword.rstrip("\n")
    dictionary.append(dictword)
