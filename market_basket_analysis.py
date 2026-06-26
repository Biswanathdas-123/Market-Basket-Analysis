# Market Basket Analysis using Apriori Algorithm

import pandas as pd

# Load Dataset
data = pd.read_csv("Groceries_dataset.csv")

# Display first five rows
print("First Five Rows:")
print(data.head())

# Dataset Information
print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nProject: Market Basket Analysis")
