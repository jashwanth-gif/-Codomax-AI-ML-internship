# Day 12 – Project Improvement

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("Codomax Student Score Project – Day 12")


# 1. Load dataset
# (Assuming you moved the CSV into a data/ folder. If not, use "student_scores.csv")
df = pd.read_csv("student_scores.csv")

print("\nDataset head")
print(df.head())

print("\nDataset info")
print(df.info())


# 2. Select feature and target
# input: study hours, output: exam scores
X = df[["Hours"]]
y = df["Scores"]

print("\nFeature (Hours) and target (Scores) ready")


# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTrain and test shapes")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


# 4. Build and train model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained")
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)


# 5. Predictions and evaluation
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = (mse ** 0.5)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation metrics")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)


# 6. Error table
results = pd.DataFrame({
    "Hours": X_test["Hours"].values,
    "Actual": y_test.values,
    "Predicted": y_pred,
    "Error": y_test.values - y_pred
})

print("\nError table")
print(results)


# 7. Plot regression line with data
plt.figure(figsize=(6, 4))
plt.scatter(df["Hours"], df["Scores"], color="blue", label="Data")
line = model.predict(df[["Hours"]])
plt.plot(df["Hours"], line, color="red", label="Regression line")
plt.title("Study Hours vs Scores – Linear Regression")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.legend()
plt.grid(True)
plt.show()