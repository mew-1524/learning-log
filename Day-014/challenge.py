try:
    number = int(input("Enter a number: "))
    print("Square =", number * number)

except ValueError:
    print("Please enter a valid integer.")