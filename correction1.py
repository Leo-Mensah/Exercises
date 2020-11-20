home = open('mbox-short.txt')

count = 0
for hannah in home:
    hannah = hannah.strip()
    han = hannah.split()
    if len(han) < 1 :
        continue
    if han[0] != 'From' :
        continue
    count = count + 1
    print(han[1])
print(count)
