fh = open('mbox-short.txt')

for leo in fh:
    le = leo.strip().upper()
    print(le)
