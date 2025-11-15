
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


data = {
    'Advertising': [230, 44, 17, 151, 180, 8, 57, 120, 90, 200],
    'Sales': [22, 10, 6, 16, 18, 4, 9, 14, 12, 20]
}

df = pd.DataFrame(data)

print("Dataset Loaded Successfully")
print(df.head())  

X = df[['Advertising']]  
y = df['Sales']          

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining and Testing Split Done!")

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Training Completed!")
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

plt.scatter(df['Advertising'], df['Sales'], color='blue', label='Actual Data')
plt.plot(df['Advertising'], model.predict(df[['Advertising']]), color='red', label='Regression Line')

plt.title("Simple Linear Regression: Sales vs Advertising")
plt.xlabel("Advertising Budget")
plt.ylabel("Sales")
plt.legend()
plt.show()

print("\nProgram Completed Successfully!")

