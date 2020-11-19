hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Please Enter a Number")
    quit()

def computepay(h,r):
    if h <= 40:
        p = h * r
    elif h > 40:
        p = ((h * r) + ((h - 40) / 2)* r )
    return p

print(computepay(h,r))
