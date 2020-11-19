score = input("Enter Score between (0.0 - 1.0): ")

try:
    x = float(score)
    if (x <= 0 or x > 1):
        quit()
except :
    print("Value is out of range")
    quit()

if x >= 0.9 :
    print("A")

elif x >= 0.8 :
    print("B")

elif x >= 0.7 :
    print("C")

elif x >= 0.6 :
    print("D")

else :
    print("F")
