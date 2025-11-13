# Sales Prediction using Simple Linear Regression

##  Overview
This mini project demonstrates the application of **Simple Linear Regression** to analyze and predict the relationship between **Advertising Budget** and **Product Sales** for a dietary weight-control product.  
The project uses Python’s **Scikit-Learn** library to train, test, and evaluate a regression model.

This is a standalone project and does not depend on any other datasets or mini projects.

---

##  Objectives
- Understand the working of Simple Linear Regression  
- Explore how advertising expenditure impacts sales  
- Train and evaluate a regression model using Scikit-Learn  
- Calculate evaluation metrics such as **Mean Squared Error (MSE)** and **R² Score**  
- Predict sales for new advertising values  

---

## Project Structure

mini_project_2_sales_prediction/ │ ├── main.py                # Model training and evaluation code ├── requirements.txt       # Required Python libraries └── model/                 # Saved trained model (auto-created)

---

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Joblib  

---

##  Installation & Setup

### Step 1 — Install required libraries
```bash
pip install -r requirements.txt

Step 2 — Run the project

python main.py

A trained Linear Regression model will be created and saved in the model/ folder.


---

 Model Training

The model learns the relationship:

Sales = b_0 + b_1 \times Advertising

Where:

Advertising → independent variable

Sales → dependent variable



---

 Evaluation Metrics

After training, the model is evaluated using:

Metric	Description

Mean Squared Error (MSE)	Measures average squared difference between actual & predicted values
R² Score	Indicates how well the model fits the data (closer to 1 = better fit)



---

 Sample Output

Dataset Loaded Successfully!

Model training completed!
Trained model saved successfully.

Model Evaluation Results:
Mean Squared Error (MSE): 0.2480
R-squared (R2 Score): 0.9874

Sales = -1.33 + 0.24 * Advertising

Predicted Sales for Advertising = 150 → 34.79

 Project Completed Successfully!


---

 Saved Model

model/
└── linear_regression_sales.joblib

This allows you to load and use the model later without retraining.


---

 Conclusion

The project successfully demonstrates how Simple Linear Regression can be used to predict product sales based on advertising investment. The model achieved a strong R² score, indicating a clear positive correlation between advertising and sales. This project provides practical understanding of regression analysis using Python and Scikit-Learn.


---

 Author

Sai Praneel
Department of Computer Science & Engineering

---
