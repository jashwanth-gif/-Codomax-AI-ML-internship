
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# create a bigger synthetic dataset
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]

scores = [18, 22, 35, 40, 49, 55, 68, 78, 85, 95,
          20, 28, 38, 45, 52, 60, 70, 80, 88, 98]

df = pd.DataFrame({"Hours": hours, "Scores": scores})

print("Full dataset")
print(df)

X = df[["Hours"]]
y = df["Scores"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

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

y_pred = model.predict(X_test)

print("Actual test scores")
print(y_test.values)

print("Predicted test scores")
print(y_pred)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# small error table
results = pd.DataFrame({
    "Hours": X_test["Hours"].values,
    "Actual": y_test.values,
    "Predicted": np.round(y_pred, 2),
    "Error": np.round(y_test.values - y_pred, 2)
})

print("Error table")
print(results)

# plot regression line with data
plt.figure(figsize=(6, 4))
plt.scatter(df["Hours"], df["Scores"], color="blue", label="Data")
line_pred = model.predict(df[["Hours"]])
plt.plot(df["Hours"], line_pred, color="red", label="Regression line")
plt.title("Study Hours vs Scores (Regression Line)")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.legend()
plt.grid(True)
plt.show()