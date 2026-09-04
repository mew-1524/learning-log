# Day 030 - Pandas Advanced Data Manipulation

## merge()

merge() combines DataFrames using a common column/key.

Example:

pd.merge(df1, df2, on="ID")

## Merge Types

inner → common records
left → all left records
right → all right records
outer → all records from both

## concat()

Used to combine DataFrames.

Rows:

pd.concat([df1, df2])

Columns:

pd.concat([df1, df2], axis=1)

ignore_index=True
resets the index.

## join()

Used mainly to combine DataFrames using index.

df1.join(df2)

## apply()

Used to apply a function to values.

df["Result"] = df["Marks"].apply(function)

## lambda

Short function.

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

## map()

Used to map values.

df["Points"] = df["Grade"].map({
    "A": 90,
    "B": 80
})

## replace()

Used to replace values.

df["City"] = df["City"].replace(
    "Bombay",
    "Mumbai"
)

## Remember

merge → KEY
join → INDEX
concat → STACK
apply → FUNCTION
map → MAPPING
replace → REPLACE VALUES