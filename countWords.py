def countWords():
    fileName = input("Enter the file name:")
    file = open(fileName, "r")
    count = 0
    for line in file:
        words = line.split()
        count = count + len(words)
    print("Number of words:")
    print(count)

countWords()