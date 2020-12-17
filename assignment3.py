largest = None
smallest = None

while True:
    try:
        num = input("Enter a number \n Type done if completed: ")
        if num == 'done':
            break
        n = int(num)
        if largest is None or n > largest:
            largest = n
        if smallest is None or n < smallest:
            smallest = n
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
