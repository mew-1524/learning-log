age = int(input("Enter your age: "))

if age < 18:
    raise Exception("You are not eligible to vote.")

print("You are eligible.")