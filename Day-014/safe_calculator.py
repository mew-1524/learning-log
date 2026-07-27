try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    choice = input("Enter (+, -, *, /): ")

    if choice == "+":
        print("Answer =", num1 + num2)

    elif choice == "-":
        print("Answer =", num1 - num2)

    elif choice == "*":
        print("Answer =", num1 * num2)

    elif choice == "/":
        print("Answer =", num1 / num2)

    else:
        print("Invalid operator.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

finally:
    print("Thank you for using the calculator!")