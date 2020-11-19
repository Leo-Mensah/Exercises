# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    lin = float(line[-7:-1])
    sum = sum + lin
    count = count + 1
    print(lin)
avg = sum / count

print(sum, count, avg)

print("Done")
