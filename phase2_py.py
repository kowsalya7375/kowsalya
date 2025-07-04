# -*- coding: utf-8 -*-
"""phase2.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CqISdi2TPLb0TCzuD7uMcWL29m7BFL8z
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

# Load dataset
data = pd.read_csv('ecommerce_customer_dataset.csv')

# 1. Min-Max Scaling for 'Annual_Income' and 'Spending_Score'
minmax_scaler = MinMaxScaler()
data[['Annual_Income', 'Spending_Score']] = minmax_scaler.fit_transform(data[['Annual_Income', 'Spending_Score']])

# 2. Z-score Normalization for 'Purchase_Frequency'
standard_scaler = StandardScaler()
data[['Purchase_Frequency']] = standard_scaler.fit_transform(data[['Purchase_Frequency']])

# 3. One-Hot Encoding for 'Gender'
data = pd.get_dummies(data, columns=['Gender'], drop_first=True)

# 4. Label Encoding for 'Preferred_Category'
label_encoder = LabelEncoder()
data['Preferred_Category'] = label_encoder.fit_transform(data['Preferred_Category'])

# Save the transformed data to a new CSV file
data.to_csv('ecommerce_customer_dataset.csv', index=False)

# Display the transformed DataFrame
print("Transformed Data:")
print(data.head())