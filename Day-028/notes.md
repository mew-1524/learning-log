# Day 028 - Pandas Selection, Filtering and Cleaning

## Selecting Columns

df["Name"]

df[["Name", "Python"]]

## Selecting Rows

df.iloc[0]

df.iloc[0:3]

df.loc[0]

## Filtering

df[df["Python"] > 80]

## Multiple Conditions

AND:
(df["Python"] > 80) & (df["SQL"] > 80)

OR:
(df["City"] == "Mumbai") | (df["City"] == "Pune")

## Sorting

df.sort_values("Python")

Descending:

df.sort_values("Python", ascending=False)

## Adding Columns

df["Average"] = (df["Python"] + df["SQL"]) / 2

## Removing Columns

df.drop("Average", axis=1)

## Removing Rows

df.drop(0)

## Renaming

df.rename(columns={"Python": "Python_Marks"})

## Missing Values

df.isnull()

df.isnull().sum()

df.dropna()

df.fillna(0)

df["Marks"].fillna(df["Marks"].mean())

## Important

loc  = label based
iloc = integer position based

axis=0 → rows
axis=1 → columns

& → AND
| → OR
~ → NOT