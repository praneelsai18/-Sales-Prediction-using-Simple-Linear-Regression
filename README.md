# Mini Project 2 — Sales Prediction using Simple Linear Regression

## Overview
This mini project demonstrates the application of **Simple Linear Regression** to analyze the relationship between **Advertising Budget** and **Sales** for a dietary weight control product.  
The model is implemented using Python and Scikit-Learn and shows how advertising expenditure influences sales performance.

This project also includes a regression line visualization using Matplotlib.

---

## Objectives
- Understand the concept of Simple Linear Regression  
- Load and explore a sample advertising dataset  
- Split data into training and testing sets  
- Train a Linear Regression model  
- Evaluate the model using MSE and R² Score  
- Visualize the regression line  
- Predict sales based on advertising budget  

---

## Project Structure
mini_project_2_sales_prediction/
│
├── main.py # Linear Regression code (this project)
├── requirements.txt # Required libraries
└── README.md # Project documentation (this file)

yaml
Copy code

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Matplotlib  

---

## How to Run the Project

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
Step 2 — Run the Python script
bash
Copy code
python main.py
Dataset Description
This project uses a sample dataset containing two columns:

Feature	Description
Advertising	Money spent on promoting the product
Sales	Units sold

Example data used in this project:

makefile
Copy code
Advertising: [230, 44, 17, 151, ...]
Sales: [22, 10, 6, 16, ...]
You may also replace this with your own CSV dataset if needed.

Model Training
The code trains a Linear Regression model using:

python
Copy code
model.fit(X_train, y_train)
The model learns the equation:
Sales=m×Advertising+c
Where:
m = slope (coefficient)
c = intercept

Evaluation Metrics
The model is evaluated using:

✔ Mean Squared Error (MSE)
Measures how far predictions are from actual values.

✔ R² Score
Indicates how well the model fits the data (range: 0–1).

Both metrics are printed in the terminal.

Visualization
The project generates a scatter plot of actual sales vs. advertising budget, along with the best-fit regression line.

This helps visually understand how sales increase with advertising efforts.

Sample Output Log
mathematica
Copy code
Dataset Loaded Successfully
Training and Testing Split Done!
Model Training Completed!
Coefficient (Slope): 0.075
Intercept: 4.52

Model Evaluation:
Mean Squared Error (MSE): 1.32
R² Score: 0.94

Program Completed Successfully!
Future Enhancements
Add CSV support for large datasets

Add multiple regression with more features

Save model using joblib

Deploy using Streamlit

Author
Sai Praneel
