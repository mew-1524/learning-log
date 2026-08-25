import pandas as pd

data = {
    "Name": ["Aadesh", "Rahul", "Amit"],
    "Age": [17, 18, 17],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)

print(df)