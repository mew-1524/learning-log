import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Aadesh", "Rahul"],
    "Marks": [85, 78]
})

df2 = pd.DataFrame({
    "Name": ["Amit", "Riya"],
    "Marks": [92, 88]
})

result = pd.concat(
    [df1, df2]
)

print(result)