# Day 31 - Pandas Data Cleaning

## Reading CSV

pd.read_csv("file.csv")

Reads a CSV file into a Pandas DataFrame.

## Inspecting Data

head() → first 5 rows
tail() → last 5 rows
shape → rows and columns
columns → column names
info() → information about DataFrame
describe() → statistical summary

## Missing Values

isnull() → checks missing values
isnull().sum() → counts missing values

fillna() → fills missing values
dropna() → removes rows with missing values

## Duplicate Data

duplicated() → finds duplicate rows
drop_duplicates() → removes duplicate rows

## Other Functions

rename() → changes column names
astype() → changes data type
to_csv() → saves DataFrame as CSV

## Important Difference

fillna() → Fill missing data
dropna() → Remove missing data

duplicated() → Find duplicates
drop_duplicates() → Remove duplicates