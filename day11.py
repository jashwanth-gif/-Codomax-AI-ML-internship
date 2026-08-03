import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

print("Student Score Prediction App")
df = pd.read_csv("student_scores.csv")
print("Dataset head")
print(df.head())

# features and target
X = df[["Hours"]]
y = df["Scores"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained")
while True:
    try:
        hours = float(input("\nEnter study hours (or -1 to exit): "))
        if hours == -1:
            print("Exiting app.")
            break

        # use DataFrame so feature name matches training ("Hours")
        user_X = pd.DataFrame({"Hours": [hours]})
        predicted_score = model.predict(user_X)[0]

        print(f"Predicted score for {hours} hours: {predicted_score:.2f}")
    except ValueError:
        print("Please enter a valid number.")