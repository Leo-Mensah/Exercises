mbox = open("mbox-short.txt")
counts = dict()

for mb in mbox :
    mbl = mb.split()
    if len(mbl) < 1 : continue #Pass empty list
    if mbl[0] != 'From' : continue  # Pass lists without From keyword
    mst = mbl[1]
    msts = mst.split()
    for mail in msts:
        counts[mail] = counts.get(mail, 0) + 1
#        print(counts)

maxmail = None
mailnum = None
for k,v in counts.items():
    if maxmail is None or v > mailnum:
        maxmail = k
        mailnum = v
print(maxmail,mailnum)
