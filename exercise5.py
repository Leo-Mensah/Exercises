first = input("Enter the file name: ")
fname = open(first)
lst = list()
for name in fname:
    flist = name.split()
    for i in flist:
        if i in lst :
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)
