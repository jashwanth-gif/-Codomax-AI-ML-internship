import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# load data
df = pd.read_csv("student_scores.csv")

print("Dataset head")
print(df.head())

# features and target
X = df[["Hours"]]      # input
y = df["Scores"]       # output

print("X (Hours)")
print(X)

print("y (Scores)")
print(y)

# train–test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train")
print(X_train)

print("X_test")
print(X_test)

print("y_train")
print(y_train)

print("y_test")
print(y_test)

# build and train model
model = LinearRegression()
model.fit(X_train, y_train)

print("Trained model")
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)

# predictions on test set
y_pred = model.predict(X_test)
print("Predictions on test set")
print(y_pred)

# evaluation (basic)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# small extra: predict for a new value
new_hours = [[6]]
new_score_pred = model.predict(new_hours)
print("Predicted score for 6 study hours:", new_score_pred)