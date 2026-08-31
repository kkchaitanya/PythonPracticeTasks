# ==========================================
# SALES DATA ANALYSIS USING PYTHON + PANDAS
# ==========================================

import pandas as pd


# ==========================================
# 1. Create and write sales.txt
# ==========================================

sales_data = """order_id,product,quantity,price,city
101,Laptop,1,65000,Bangalore
102,Mouse,2,1200,Delhi
103,Keyboard,1,2500,Hyderabad
104,Monitor,2,15000,Mumbai
105,Printer,1,12000,Chennai
106,Laptop,2,65000,Delhi
107,Mouse,5,1200,Bangalore
108,Keyboard,3,2500,Pune
109,Monitor,1,15000,Hyderabad
110,Printer,2,12000,Mumbai
111,Laptop,1,65000,Chennai
112,Mouse,3,1200,Delhi
113,Keyboard,2,2500,Bangalore
114,Monitor,3,15000,Pune
115,Printer,1,12000,Hyderabad
116,Laptop,1,65000,Mumbai
117,Mouse,4,1200,Chennai
118,Keyboard,2,2500,Delhi
119,Monitor,1,15000,Bangalore
120,Printer,3,12000,Pune
121,Laptop,2,65000,Hyderabad
122,Mouse,6,1200,Mumbai
123,Keyboard,1,2500,Chennai
124,Monitor,2,15000,Delhi
125,Printer,2,12000,Bangalore
126,Laptop,1,65000,Pune
127,Mouse,3,1200,Hyderabad
128,Keyboard,4,2500,Mumbai
129,Monitor,1,15000,Chennai
130,Printer,2,12000,Delhi
"""

with open("sales.txt", "w") as file:
    file.write(sales_data)

print("sales.txt created successfully.")


# ==========================================
# 2. Read sales.txt using normal Python
# file handling
# ==========================================

print("\n========== SALES.TXT CONTENTS ==========")

with open("sales.txt", "r") as file:
    content = file.read()

print(content)


# ==========================================
# 3. Load the same data using Pandas
# ==========================================

df = pd.read_csv("sales.txt")

print("========== DATAFRAME ==========")
print(df)


# ==========================================
# 4. Calculate revenue for every order
# revenue = quantity * price
# ==========================================

df["revenue"] = df["quantity"] * df["price"]

print("\n========== DATA WITH REVENUE ==========")
print(df)


# ==========================================
# 5. Total Revenue
# ==========================================

total_revenue = df["revenue"].sum()

print("\nTotal Revenue:", total_revenue)


# ==========================================
# 6. Average Order Value
# ==========================================

average_order_value = df["revenue"].mean()

print("Average Order Value:", average_order_value)


# ==========================================
# 7. Highest-value order
# ==========================================

highest_order = df.loc[df["revenue"].idxmax()]

print("\n========== HIGHEST-VALUE ORDER ==========")
print(highest_order)


# ==========================================
# 8. Lowest-value order
# ==========================================

lowest_order = df.loc[df["revenue"].idxmin()]

print("\n========== LOWEST-VALUE ORDER ==========")
print(lowest_order)


# ==========================================
# 9. Revenue product-wise
# ==========================================

product_revenue = df.groupby("product")["revenue"].sum()

print("\n========== PRODUCT-WISE REVENUE ==========")
print(product_revenue)


# ==========================================
# 10. Revenue city-wise
# ==========================================

city_revenue = df.groupby("city")["revenue"].sum()

print("\n========== CITY-WISE REVENUE ==========")
print(city_revenue)


# ==========================================
# 11. Save processed data as sales_report.csv
# ==========================================

df.to_csv("sales_report.csv", index=False)

print("\nsales_report.csv created successfully.")

