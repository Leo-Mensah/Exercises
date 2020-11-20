fname = open("mbox-short.txt")

count = 0
lst = list()
for name in fname:
    ls = name.rstrip()
    if not ls.startswith("From") :
        continue
    else:
        words = ls.split()
        word = words[1]

        wd = word.split()

        for i in wd:
            if i in lst :
                continue
            else:
                lst.append(i)
print(lst)
print(len(lst))
#            if i in lst:
#        print(i)
#        print(words)
#    count = count + 1
#    print(word)
#    print(count)
#    print(ls)
#    words = ls.split()
#    print(words)
#    for i in words:
#        print(i)
