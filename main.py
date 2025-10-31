import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

data = {
    'Advertising': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Sales': [12, 14, 17, 18, 21, 22, 25, 28, 30, 32]
}
df = pd.DataFrame(data)
print("Dataset Loaded Successfully!\n")
print(df.head())

X = df[['Advertising']]  
y = df['Sales']          

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel training completed!")

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/linear_regression_sales.joblib")
print("Trained model saved successfully.\n")

y_pred = model.predict(X_test)
print("Predictions on test data:", y_pred)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Results:")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"R-squared (R2 Score): {r2:.4f}")

print("\nThe linear relationship can be represented as:")
print(f"Sales = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Advertising")

new_ad = [[150]]
predicted_sales = model.predict(new_ad)
print(f"\nIf Advertising = 150, Predicted Sales = {predicted_sales[0]:.2f}")

print("\n✅ Project Completed Successfully!")