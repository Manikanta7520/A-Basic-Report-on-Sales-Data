# Week 3 – Sales Data Analysis
# Developers Arena Data Science Internship

import pandas as pd

# Load dataset
df = pd.read_excel(r"C:\Users\MAAHEE\OneDrive\Desktop\Manikanta\Developers Intern\WEEK 3\sample_sales_data.xlsx")

# Total sales
total_sales = df["Sales Amount"].sum()

# Best-selling product (by total units sold)
best_product = df.groupby("Product")["Units Sold"].sum().idxmax()
best_units = df.groupby("Product")["Units Sold"].sum().max()

# Create a simple summary report
report = f"""
===== SALES REPORT =====

Total Sales: ₹{total_sales}

Best-Selling Product: {best_product}
Units Sold: {best_units}

========================
"""

print(report)
