import pandas as pd

df = pd.read_csv("student_scores.csv")

print("Original data")
print(df)

print("Missing values")
print(df.isnull().sum())

print("Duplicate rows")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("After drop duplicates")
print(df)

df["Hours"] = df["Hours"].fillna(df["Hours"].mean())
df["Scores"] = df["Scores"].fillna(df["Scores"].mean())

if "Gender" in df.columns:
    df["Gender"] = df["Gender"].fillna("Unknown")

print("After filling missing values")
print(df)

print("Drop any remaining missing rows")
df = df.dropna()

print("Final cleaned dataset")
print(df)

print("Summary")
print(df.describe())