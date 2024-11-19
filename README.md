# House-Price-Prediction

### Overview
This repository contains a comprehensive project focused on predicting house prices in Bengaluru using machine learning techniques. The project involves data cleaning, feature engineering, outlier detection, and regression modeling to provide accurate price predictions based on various property features.

[Check out the live app](https://home-price-prediction.streamlit.app/)
<a href="https://home-price-prediction.streamlit.app/" target="_blank">Check out the live app</a>


### Features
- **Data Loading and Preprocessing**: The dataset is loaded from a CSV file and initial preprocessing steps are performed, including handling missing values and dropping irrelevant columns.
- **Feature Engineering**: New features are created to enhance the model's predictive power, such as converting total square footage to a numeric format and calculating the price per square foot.
- **Dimensionality Reduction**: Techniques are applied to reduce the number of location categories by grouping less frequent locations into an 'others' category.
- **Outlier Detection and Removal**: Business logic and statistical methods are used to identify and remove outliers from the dataset.
- **Model Training**: Various regression models are trained and evaluated, including Linear Regression, Lasso, and Decision Tree Regressor.
- **Hyperparameter Tuning**: GridSearchCV is used to find the best model and hyperparameters for predicting house prices.
- **Visualization**: Scatter plots and histograms are used to visualize the data and the results of outlier removal.

### Data
The dataset used for this project is `Bengaluru_House_Data.csv`, which contains the following columns:
- `area_type`
- `availability`
- `location`
- `size`
- `society`
- `total_sqft`
- `bath`
- `balcony`
- `price`

### Key Functions
- **Data Cleaning**: Handles null values and irrelevant features.
- **Feature Engineering**: Adds new features like `bhk` (Bedrooms Hall Kitchen) and `price_per_sqft`.
- **Outlier Removal**: Uses logical and statistical methods to remove outliers.
- **Visualization**: Plots to help visualize data distribution and model results.
- **Model Training and Evaluation**: Trains various regression models and evaluates their performance using cross-validation.
- **Prediction**: A function to predict the price of a house given its features.

### Example Usage
```python
# Predict price for a 2 BHK house in 1st Phase JP Nagar with 1000 sqft and 2 bathrooms
predict_price('1st Phase JP Nagar', 1000, 2, 2)
```
Output: 83.86 Lakhs
```python
# Predict price for a 3 BHK house in Indira Nagar with 1000 sqft and 3 bathrooms
predict_price('Indira Nagar', 1000, 3, 3)
```
Output: 195.52 Lakhs

