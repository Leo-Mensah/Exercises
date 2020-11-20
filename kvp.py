jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}

for aaa, bbb in jjj.items() :
    print(aaa, bbb)


for aaa in jjj.keys() :
    print(aaa)

for bbb in jjj.values() :
    print(bbb)


for j in jjj:
    jjj[j] = jjj.get(j, 0) + 1
print(j, jjj.values())
