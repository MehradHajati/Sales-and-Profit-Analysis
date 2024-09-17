# Mehrad Hajati, 17/09/2024
# This file conducts EDA analysis on the data gotten from Kaggle and then displays different metrics on plots and charts.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'Sample - Superstore.csv'
data = pd.read_csv(file_path, encoding='latin1')

# Basic data overview
print(data.head())
print(data.info())
print(data.describe())

# Check for missing values
missing_values = data.isnull().sum()
print(f"Missing values:\n{missing_values}")

# Exploratory Data Analysis
# 1. Sales distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Sales'], bins=50, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# 2. Profit vs. Sales Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Sales', y='Profit', hue='Category')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

# 3. Sales by Category
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Category', y='Sales', estimator=sum, ci=None)
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.show()

# 4. Sales by Region
plt.figure(figsize=(12, 8))
sns.boxplot(data=data, x='Region', y='Sales')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.show()

# 5. Top 10 products by sales
top_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Let's visualize the top 10 products by sales using a bar plot for a presentable view.
plt.figure(figsize=(10, 6))
sns.barplot(y=top_products.index, x=top_products.values, palette='viridis')
plt.title('Top 10 Products by Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
# Reduce the font size of y-axis labels
plt.yticks(fontsize=5)
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
