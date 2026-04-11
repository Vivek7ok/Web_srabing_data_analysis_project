# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Setting up logging
logging.basicConfig(
    filename='log_file.log',
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

# Importing dataset
df = pd.read_csv(r"D:\Data_set\Data_set_21\Data\Books_data.csv")

# Basic information about the dataset
print(df.head())   # First 5 rows
print(df.tail())   # Last 5 rows
print(df.info())   # Data types and structure

# Shape of dataset
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Checking for null values
print(df.isnull().sum())
logging.info("Checked for null values")

# Column names
print(f'Column names: {df.columns}')

# Converting 'Price' column from object to float
print(df['Price'])
df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)
print(df['Price'])

# Converting 'Rating' column from object to integer
print(df['Rating'])
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df['Rating'] = df['Rating'].map(rating_map)
print(df['Rating'])

# Number of books in each category
category = df['Category'].value_counts()
print(category)

# Top 5 categories with highest total ratings
gp_1 = df.groupby('Category')['Rating'].sum().sort_values(ascending=False).head()
print(gp_1)

# Top 5 most expensive books
gp_1 = df.groupby('Name')['Price'].sum().sort_values(ascending=False).head()
print(gp_1)

# Top 5 highest rated books
gp_2 = df.groupby('Name')['Rating'].sum().sort_values(ascending=False).head()
print(gp_2)

# Average rating per category
gp_3 = df.groupby('Category')['Rating'].mean()
print(gp_3)

# -------------------- Visualization --------------------

# Top 5 categories by average rating
df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head().plot(
    kind='bar',
    color='skyblue'
)
plt.title("Top 5 Categories by Average Rating")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 5 categories by number of books
df['Category'].value_counts().head().plot(
    kind='bar',
    color='orange'
)
plt.title("Top 5 Categories by Number of Books")
plt.xlabel("Category")
plt.ylabel("Number of Books")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top 5 highest rated books
df.groupby('Name')['Rating'].sum().sort_values(ascending=False).head().plot(
    kind='barh',
    color='green'
)
plt.title("Top 5 Highest Rated Books")
plt.xlabel("Total Rating")
plt.ylabel("Book Name")
plt.tight_layout()
plt.show()

# Top 5 most expensive books
df.groupby('Name')['Price'].sum().sort_values(ascending=False).head().plot(
    kind='barh',
    color='red'
)
plt.title("Top 5 Most Expensive Books")
plt.xlabel("Price")
plt.ylabel("Book Name")
plt.tight_layout()
plt.show()

# Top 5 categories by total price
df.groupby('Category')['Price'].sum().sort_values(ascending=False).head().plot(
    kind='barh',
    color='purple'
)
plt.title("Top 5 Categories by Total Price")
plt.xlabel("Total Price")
plt.ylabel("Category")
plt.tight_layout()
plt.show()