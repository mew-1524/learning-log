try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Invalid input.")

except Exception as e:
    print("Error:", e)