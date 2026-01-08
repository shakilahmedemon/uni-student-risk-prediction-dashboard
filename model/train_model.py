import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os


# Step 1: Load the dataset

data_path = os.path.join("data", "student_data.csv")
df = pd.read_csv(data_path)

print("Dataset loaded successfully!")
print(df.head())


# Step 2: Preprocess dataset


# Encode Project Complexity: Low=0, Medium=1, High=2
complexity_map = {"Low": 0, "Medium": 1, "High": 2}
df["Project Complexity"] = df["Project Complexity"].map(complexity_map)

# Create a target column 'target_failed' based on simple heuristic rules
# For example:
# - Attendance < 60% OR Midterm < 50 OR Average Assignment < 50 OR Stress > 7 OR Late Submissions > 5
df["target_failed"] = np.where(
    (df["Attendance"] < 60) |
    (df["Midterm Exam Score"] < 50) |
    (df["Average Assignment Score"] < 50) |
    (df["Stress Level"] > 7) |
    (df["Late Submissions"] > 5),
    1, 0
)

# Select features for training
feature_columns = [
    "Attendance",
    "Behavior / Discipline Score",
    "Midterm Exam Score",
    "Average Assignment Score",
    "Late Submissions",
    "Team Collaboration",
    "Project Complexity",
    "Hours Studied per Week",
    "Number of Previous Failures",
    "Stress Level",
    "Average Submission Delay"
]

X = df[feature_columns]
y = df["target_failed"]


# Step 3: Split dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")


# Step 4: Train Random Forest Classifier

model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

print("Model training completed!")


# Step 5: Evaluate Model

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Step 6: Save Trained Model

os.makedirs("model", exist_ok=True)
model_path = os.path.join("model", "trained_model.pkl")
joblib.dump(model, model_path)

print(f"Model saved successfully at: {model_path}")
