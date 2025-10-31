Sales Prediction using Simple Linear Regression

## 🧠 Overview
This mini project demonstrates the use of **Simple Linear Regression** to study the linear relationship between **Advertising budget** and **Sales** for a dietary weight control product.  
It aims to understand how advertising expenditure influences product sales using Python’s **Scikit-learn** library.

---

## 🎯 Objective
To build and evaluate a simple linear regression model that predicts product sales based on the advertising budget.

---

## 🧩 Steps Involved

1. **Import Required Libraries**  
   Libraries like `pandas`, `numpy`, and `scikit-learn` are used for data handling, modeling, and evaluation.

2. **Load and Explore the Dataset**  
   The dataset contains two columns:
   - `Advertising` → Amount spent on advertising  
   - `Sales` → Units sold of the dietary product  

3. **Split the Dataset**  
   Data is divided into **training (80%)** and **testing (20%)** sets using `train_test_split()`.

4. **Model Training**  
   The **LinearRegression()** model from Scikit-learn is trained on the training data using:
   ```python
   model.fit(X_train, y_train)
