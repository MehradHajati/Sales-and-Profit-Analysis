# MEhrad Hajati, 17/09/2024
# This file is meant to engineer new features and introduce them to the dataset, then create a new cvs with the new data.
# The new features are meant to provide a better picture of the sales of the superstore and inform managers of where they should focus their attention.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Sample - Superstore.csv'
data = pd.read_csv(file_path, encoding='latin1')

# 1. Profit Margin: Profit as a percentage of Sales
data['Profit Margin'] = (data['Profit'] / data['Sales']) * 100

# 2. Days to Ship: Difference between Ship Date and Order Date
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])
data['Days to Ship'] = (data['Ship Date'] - data['Order Date']).dt.days

# 3. Order Month and Order Year: Extract month and year from Order Date
data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year

# 4. Sales Category: Categorize sales into bins (Low, Medium, High)
# Define bins and labels for sales categorization
bins = [0, 100, 500, data['Sales'].max()]
labels = ['Low', 'Medium', 'High']
data['Sales Category'] = pd.cut(data['Sales'], bins=bins, labels=labels, include_lowest=True)

# Let's create an image of the table containing the engineered features using matplotlib.
# Select the columns to display
columns_to_display = ['Sales', 'Profit', 'Profit Margin', 'Days to Ship', 'Order Month', 'Order Year', 'Sales Category']

# Create a figure and axis to display the table
fig, ax = plt.subplots(figsize=(12, 4))  # Adjust the size as needed
ax.axis('off')  # Hide the axes

# Create the table
table = ax.table(cellText=data[columns_to_display].head(10).values,  # Display the first 10 rows for better clarity
                 colLabels=columns_to_display, 
                 cellLoc='center', 
                 loc='center')

# Adjust the table's font size
table.auto_set_font_size(False)
table.set_fontsize(10)

# Save the table as an image
table_image_path = 'Feature Table.png'
plt.savefig(table_image_path, bbox_inches='tight', dpi=300)

# Export the dataset with engineered features to a CSV file
data.to_csv('new_superstore.csv', index=False)

