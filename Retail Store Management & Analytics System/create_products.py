# Part 2 — Product File
# Store product information inside
# products.csv
# Include at least 30 products.
# Use Python file handling to
# Create the file
# Write data
# Append products
# Read product records
import csv

import pandas as pd
import random

file_name="products.csv"
def write_products():
    products = []

    # Electronics
    for i in range(1, 11):
        products.append([
            f"E{i}",
            f"Laptop{i}",
            "Dell",
            random.randint(40000, 90000),
            random.randint(5, 50),
            "Electronics"
        ])

    # Clothing
    for i in range(1, 11):
        products.append([
            f"C{i}",
            f"TShirt{i}",
            "Puma",
            random.randint(500, 3000),
            random.randint(5, 50),
            "Clothing"
        ])

    # Books
    for i in range(1, 11):
        products.append([
            f"B{i}",
            f"Book{i}",
            "Penguin",
            random.randint(300, 1500),
            random.randint(5, 50),
            "Books"
        ])

    df = pd.DataFrame(
        products,
        columns=[
            "product_id",
            "name",
            "brand",
            "price",
            "stock",
            "category"
        ]
    )
    df.to_csv(f"{file_name}", index=False)
    print(f"{file_name} created successfully")

def append_products():
    new_products = []
    for i in range(16,25):
            new_products.append([
                f"C{i}",
                f"TShirt{i}",
                "Puma",
                random.randint(500, 3000),
                random.randint(5, 50),
                "Clothing"
            ])
    with open(f"{file_name}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(new_products)
    print("Records appended successfully.")

def read_products():
    return pd.read_csv(f"{file_name}")
