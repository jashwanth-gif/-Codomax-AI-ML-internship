import pandas as pd

df = pd.read_csv("student_scores.csv")

print("First 5 rows")
print(df.head())

print("Last 5 rows")
print(df.tail())

print("Shape")
print(df.shape)

print("Columns")
print(df.columns)

print("Data types")
print(df.dtypes)

print("Info")
print(df.info())

print("Describe")
print(df.describe())

print("First row using iloc")
print(df.iloc[0])

print("First 3 rows using iloc")
print(df.iloc[:3])

print("First row using loc")
print(df.loc[0])

print("Hours column")
print(df["Hours"])

print("Count of non-null values")
print(df.count())

print("Null values in each column")
print(df.isnull().sum())

print("Students with Hours greater than 5")
print(df[df["Hours"] > 5])

print("Students with Scores greater than 70")
print(df[df["Scores"] > 70])

print("Students with Hours less than or equal to 4")
print(df[df["Hours"] <= 4])

print("Students with Hours between 3 and 6")
print(df[(df["Hours"] >= 3) & (df["Hours"] <= 6)])

print("Students with Hours 2 or 5")
print(df[df["Hours"].isin([2, 5])])

if "Gender" in df.columns:
    print("Gender value counts")
    print(df["Gender"].value_counts())

    print("Only Male students")
    print(df[df["Gender"] == "Male"])

    print("Only Female students")
    print(df[df["Gender"] == "Female"])