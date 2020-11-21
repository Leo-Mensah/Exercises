fname = open('mbox-short.txt')
lst = dict()
for name in fname:
    nam = name.strip()
    leo = nam.split()
    if len(leo) < 1 : continue
    if leo[0] != 'From' : continue
    fii = leo[5:6]
    for k in fii:
        j = k[:2]
        dst = j.split()
        for vp in dst:
            lst[vp] = lst.get(vp, 0) + 1

for k, v in sorted(lst.items()):
    print(k,v)
