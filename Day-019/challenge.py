def multiply(*numbers):

    result = 1

    for number in numbers:
        result *= number

    print("Product =", result)

multiply(2, 3, 4)