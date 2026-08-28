
# Part 4 — Pandas Analysis
# Using Pandas, determine
import pandas as pd
from reports import generate_reports
def pandas_analysis():
    products_df = pd.read_csv("products.csv")
    sales_df = pd.read_csv("sales.csv")
    # print(sales_df)


    # Total sales transactions
    print("\nTotal sales Transactions")
    print(len(sales_df))
    # Total quantity sold
    print("Total quantity sold")
    print(sales_df["quantity"].sum())
    # Total revenue
    print("Total revenue")
    sales_df["total_revenue"] = (sales_df["price"] * sales_df["quantity"])
    print(sales_df["total_revenue"].sum()) 
    # Average transaction value
    print("Average transaction value")
    print(sales_df["total_revenue"].mean()) 
    # Highest-value transaction
    print("Highest-value transaction")
    print(sales_df.loc[sales_df["total_revenue"].idxmax()]) 
    # Lowest-value transaction
    print("Lowest-value transaction")
    print(sales_df.loc[sales_df["total_revenue"].idxmin()]) 
    # Best-selling product
    print("Best-selling product")
    print(sales_df.groupby("product_name")["quantity"].sum().idxmax())
    # Lowest-selling product
    print("Lowest-selling product")
    print(sales_df.groupby("product_name")["quantity"].sum().idxmin())
    # Sales category-wise
    print("Sales category-wise")
    print(sales_df.groupby("category")["quantity"].sum())
    # Revenue category-wise
    print("Revenue category-wise")
    print(sales_df.groupby("category")["total_revenue"].sum())
    # Revenue product-wise
    print("Revenue product-wise")
    print(sales_df.groupby("product_name")["total_revenue"].sum())
    # Revenue city-wise
    print("Revenue city-wise")
    print(sales_df.groupby("customer_city")["total_revenue"].sum())
    # Payment-method distribution
    print("Payment-method distribution")
    print(sales_df["payment_method"].value_counts())
    # Top 5 products
    print("Top 5 products")
    print(sales_df.groupby("product_name")["total_revenue"]
    .sum()
    .sort_values(ascending=False).head(5))
    # Bottom 5 products
    print("Bottom 5 products")
    print(sales_df.groupby("product_name")["total_revenue"]
    .sum()
    .sort_values(ascending=False).tail(5))
    # Average product price
    print("Average product price")
    print(products_df["price"].mean())
    # Maximum product price
    print("Maximum product price")
    print(products_df["price"].max())
    # Minimum product price
    print("Minimum product price")
    print(products_df["price"].min())
    # Products having stock below 10
    print("Products having stock below 10")
    print(products_df[products_df["stock"]<10])
    # Products priced above average
    print("Products priced above average")
    print(products_df[products_df["price"] >  products_df["price"].mean()])

    ## trigger reports ###
    generate_reports(sales_df)
