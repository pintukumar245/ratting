import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pickle

# Step 1: Load Data
df = pd.read_csv("final_dataset.csv")
print("Dataset shape:", df.shape)
print(df.head())

# Step 2: Features and Target
X = df[["experience_years", "skills_count", "projects_count", "feedback_score"]]
y = df["mentor_rating"]

# Step 3: Train XGBoost Model
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

# Cross validation (5 fold)
cv_scores = cross_val_score(model, X, y, cv=5, scoring="r2")
print(f"\nCross Validation R2 Scores: {cv_scores}")
print(f"Average R2 Score          : {cv_scores.mean():.2f}")

# Step 4: Train on Full Data & Evaluate
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)

print(f"\nModel Performance on Test Data:")
print(f"  MAE (Mean Absolute Error) : {mae:.2f}")
print(f"  R2 Score                  : {r2:.2f}")
print(f"  Accuracy                  : {round(r2*100, 2)}%")

# Step 5: Feature Importance
print("\nFeature Importance:")
for feat, imp in zip(X.columns, model.feature_importances_):
    print(f"  {feat:20s} : {imp:.4f}")

# Step 6: Save the Model
with open("mentor_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("\nModel saved as mentor_model.pkl")

# Step 7: Predict a New Mentor
print("\n--- Predicting for a NEW Mentor ---")
new_mentor = pd.DataFrame([{
    "experience_years": 6,
    "skills_count"    : 12,
    "projects_count"  : 10,
    "feedback_score"  : 4.5
}])

predicted_rating = model.predict(new_mentor)[0]
print(f"Input  : experience=6yrs, skills=12, projects=10, feedback=4.5")
print(f"Predicted Mentor Rating : {predicted_rating:.2f} / 100")

if predicted_rating >= 80:
    grade = "Excellent"
elif predicted_rating >= 60:
    grade = "Good"
elif predicted_rating >= 40:
    grade = "Average"
else:
    grade = "Poor"

print(f"Mentor Grade            : {grade}")