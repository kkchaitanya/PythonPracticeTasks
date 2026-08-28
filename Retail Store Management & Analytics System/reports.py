import os

def generate_reports(sales_df):
    os.makedirs("output", exist_ok=True)

    sales_df.to_csv(
        "output/cleaned_sales.csv",
        index=False
    )

    product_report = (
        sales_df.groupby("product_name")
        ["total_revenue"]
        .sum()
        .reset_index()
    )

    product_report.to_csv(
        "output/product_report.csv",
        index=False
    )

    city_report = (
        sales_df.groupby("customer_city")
        ["total_revenue"]
        .sum()
        .reset_index()
    )

    city_report.to_csv(
        "output/city_sales_report.csv",
        index=False
    )

    category_report = (
        sales_df.groupby("category")
        ["total_revenue"]
        .sum()
        .reset_index()
    )

    category_report.to_csv(
        "output/category_report.csv",
        index=False
    )

    summary = f"""
    RETAIL STORE SALES REPORT

    Total Transactions : {len(sales_df)}

    Total Revenue : {sales_df['total_revenue'].sum():,.2f}

    Average Transaction Value :
    {sales_df['total_revenue'].mean():,.2f}

    Best Selling Product :
    {sales_df.groupby('product_name')['quantity'].sum().idxmax()}

    Highest Revenue Category :
    {sales_df.groupby('category')['total_revenue'].sum().idxmax()}

    Highest Revenue City :
    {sales_df.groupby('customer_city')['total_revenue'].sum().idxmax()}
    """

    with open(
            "output/sales_summary.txt",
            "w"
    ) as file:
        file.write(summary)

    print("Reports Generated Successfully")