import pandas as pd

data = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "Marks": [85, 72, 91, 68, 95]
}

df = pd.DataFrame(data)

print(df.sort_values("Marks"))