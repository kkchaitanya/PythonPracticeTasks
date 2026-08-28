# Part 3 — Sales Data
# Create
# sales.csv
# Include at least 50 transactions.
# Columns
# transaction_id
# product_id
# product_name
# category
# quantity
# price
# customer_city
# payment_method
import random

import pandas as pd

def sales_data():
    products = pd.read_csv("products.csv")
    cities = [
            "Hyderabad",
            "Bangalore",
            "Chennai",
            "Mumbai",
            "Delhi"
            ]

    payments = [
            "UPI",
            "Card",
            "Cash",
            "Net Banking"
            ]

    sales = []
    for i in range(1, 51):
        product = products.sample(1).iloc[0]
        sales.append([  
            i,
            product["product_id"],
            product["name"],
            product["category"],
            random.randint(1, 5),
            product["price"],
            random.choice(cities),
            random.choice(payments)
            ])
    df = pd.DataFrame(
            sales,
            columns=[
            "transaction_id",
            "product_id",
            "product_name",
            "category",
            "quantity",
            "price",
            "customer_city",
            "payment_method"
            ]
            )
    df.to_csv("sales.csv", index=False)
    print("sales.csv created")
