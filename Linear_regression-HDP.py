import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load dataset
data = pd.read_csv('heart.csv')

# Display the first few rows of the dataset
print(data.head())

# Check data types and missing values
print(data.info())

# Get summary statistics
print(data.describe())

X = data[['age', 'sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope']]  # Replace with your feature names
y = data['target']  # Replace with your target variable name


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")
