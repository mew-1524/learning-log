import pandas as pd

df = pd.DataFrame({
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "Marks": [85, 72, 91, 68, 95],
    "Age": [17, 18, 17, 18, 17]
})

print("Original DataFrame:")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nStudents above 80:")
print(df[df["Marks"] > 80])