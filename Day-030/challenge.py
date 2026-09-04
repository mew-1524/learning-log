import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "City": ["Mumbai", "Pune", "Mumbai", "Nashik", "Pune"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Python": [85, 78, 92, 88, 75],
    "SQL": [90, 80, 89, 85, 82]
})