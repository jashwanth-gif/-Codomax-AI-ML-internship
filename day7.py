import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("student_scores.csv")

print("Dataset")
print(df.head())

X = df[["Hours"]]
y = df["Scores"]

print("X")
print(X)

print("y")
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X_train")
print(X_train)

print("X_test")
print(X_test)

print("y_train")
print(y_train)

print("y_test")
print(y_test)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model score")
print(model.score(X_test, y_test))

print("Coefficient")
print(model.coef_)

print("Intercept")
print(model.intercept_)

y_pred = model.predict(X_test)
print("Predictions")
print(y_pred)