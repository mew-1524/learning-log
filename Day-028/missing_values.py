import pandas as pd

data = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "Marks": [85, 72, 91, 68, 95]
}

data = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya"],
    "Marks": [85, None, 91, None]
}

df = pd.DataFrame(data)

print(df)