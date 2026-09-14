import pandas as pd

df = pd.read_csv("students.csv")

print(df)
df = df.rename(columns={
    "Python": "Python_Marks",
    "SQL": "SQL_Marks"
})

print(df)

#change data tyepe
df["Age"] = df["Age"].astype(int)

#Save Cleaned Data
df.to_csv("students_cleaned.csv", index=False)