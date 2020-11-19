# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
for i in fh:
    i = i + 1
    print(i)
