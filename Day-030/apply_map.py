import pandas as pd

df = pd.DataFrame({
    "Grade": ["A", "B", "A", "C", "B"]
})

grade_points = {
    "A": 90,
    "B": 80,
    "C": 70
}

df["Points"] = df["Grade"].map(grade_points)

print(df)