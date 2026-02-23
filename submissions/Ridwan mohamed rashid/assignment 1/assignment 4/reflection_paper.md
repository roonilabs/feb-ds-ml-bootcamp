House Price Prediction – Reflec Paper

1. What Did I Implement?

In this assignment, I implemented a house price prediction system using two regression models: Linear Regression and Random Forest Regressor.

First, I loaded a cleaned dataset and separated the features (X) from the target variable (Price). I then split the dataset into training (80%) and testing (20%) sets using random_state=42 to ensure reproducibility.

After splitting the data, I trained two models:
 • A Linear Regression model to capture linear relationships between features and house prices.
 • A Random Forest Regressor with 100 trees to capture more complex, non-linear relationships.

Both models were evaluated using R², MAE, MSE, and RMSE.


2. Comparison of Models

When testing the models using the sanity check, the predictions from Linear Regression were sometimes less accurate compared to Random Forest.

Random Forest generally produced more realistic price estimates because it can model complex patterns and interactions between features. Linear Regression assumes a linear relationship, which may not fully represent real-world housing data.


3. Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees.

Instead of relying on a single tree, it builds many decision trees using different subsets of data and features. Each tree makes a prediction, and the final prediction is calculated by averaging the results of all trees (in regression problems).

This averaging reduces overfitting and improves model stability and accuracy.


4. Metrics Discussion

The Random Forest model achieved a higher R² score and lower error metrics (MAE and RMSE) compared to Linear Regression.

A higher R² means the model explains more variance in house prices. Lower MAE and RMSE indicate smaller prediction errors.

This suggests that Random Forest is better at capturing complex patterns in the dataset, while Linear Regression performs better when relationships are strictly linear.


5. My Findings

Based on the results, I prefer Random Forest for house price prediction tasks. Housing data often contains complex interactions between variables such as location, size, number of rooms, and age of the property.

Random Forest can handle these complex relationships more effectively than Linear Regression. However, Linear Regression remains useful due to its simplicity and interpretability.