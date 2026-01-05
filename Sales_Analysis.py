# Sales Data Analysis
# Week 3 – Introduction to Data Analysis
# Developers Arena Internship

import pandas as pd

# -----------------------------
# STEP 1: Load the dataset
# -----------------------------
df = pd.read_csv("sales_data.csv")

# Handle missing values (fill numeric columns with 0)
df.fillna(0, inplace=True)

# -----------------------------
# STEP 2: Data Cleaning
# -----------------------------
# Remove duplicate rows if any
df.drop_duplicates(inplace=True)

# -----------------------------
# STEP 3: Data Analysis
# -----------------------------
# Total Sales
total_sales = df["Total_Sales"].sum()

# Average Sales
average_sales = df["Total_Sales"].mean()

# Maximum and Minimum Sales
max_sales = df["Total_Sales"].max()
min_sales = df["Total_Sales"].min()

# Best-selling product (based on Total Sales)
best_selling_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_selling_value = df.groupby("Product")["Total_Sales"].sum().max()

# -----------------------------
# STEP 4: Create Basic Report
# -----------------------------
print("\n===== SALES ANALYSIS REPORT =====")
print(f"Total Sales Amount   : ₹{total_sales:,.2f}")
print(f"Average Sales        : ₹{average_sales:,.2f}")
print(f"Highest Sale         : ₹{max_sales:,.2f}")
print(f"Lowest Sale          : ₹{min_sales:,.2f}")
print(f"Best-Selling Product : {best_selling_product}")
print(f"Sales Value          : ₹{best_selling_value:,.2f}")
