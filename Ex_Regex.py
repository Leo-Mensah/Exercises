import re
word = open('regex_sum_1073299.txt')

addInt = 0

for r in word:
    ls = re.findall('[0-9]+',r)
    if len(ls) < 1 : continue
    for rst in ls:
        wordint = int(rst)
        addInt += wordint
print(addInt)
