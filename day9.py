import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("student_scores.csv")

print("Dataset head")
print(df.head())

X = df[["Hours"]]
y = df["Scores"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained")

print("Test set hours")
print(X_test)

print("Actual test scores")
print(y_test)

y_pred = model.predict(X_test)
print("Predicted test scores")
print(y_pred)

# predictions for custom study hours
hours_list = [[2], [4], [6], [8], [9.25]]
pred_scores = model.predict(hours_list)

print("Custom predictions")
for h, s in zip(hours_list, pred_scores):
    print(f"Hours: {h[0]} -> Predicted Score: {s}")