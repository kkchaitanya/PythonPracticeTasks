import pandas as pd
import random

# -----------------------------
# Sample data
# -----------------------------

names = [
    "Rahul Sharma", "Priya Reddy", "Arjun Kumar", "Ananya Singh",
    "Vikram Patel", "Meera Nair", "Rohan Das", "Kavya Rao",
    "Aditya Verma", "Sneha Gupta", "Kiran Joshi", "Pooja Mehta",
    "Suresh Reddy", "Divya Kapoor", "Manoj Kumar", "Aisha Khan",
    "Nikhil Jain", "Swati Agarwal", "Varun Malhotra", "Isha Sharma"
]

cities = [
    "Hyderabad", "Mumbai", "Delhi", "Bangalore", "Chennai",
    "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Bhopal"
]

emails = [
    "rahul@gmail.com", "priya@gmail.com", "arjun@gmail.com",
    "ananya@gmail.com", "vikram@gmail.com", "meera@gmail.com",
    "rohan@gmail.com", "kavya@gmail.com", "aditya@gmail.com",
    "sneha@gmail.com"
]

data = []

for i in range(1, 121):

    name = random.choice(names)
    city = random.choice(cities)
    email = random.choice(emails)

    age = random.randint(18, 65)
    purchase_amount = round(random.uniform(100, 10000), 2)
    rating = random.randint(1, 5)

    # --------------------------------
    # Incorrect capitalization
    # --------------------------------
    if i % 7 == 0:
        name = name.upper()

    if i % 9 == 0:
        city = city.lower()

    # --------------------------------
    # Extra spaces
    # --------------------------------
    if i % 8 == 0:
        name = "  " + name + "  "

    if i % 11 == 0:
        city = " " + city + " "

    if i % 13 == 0:
        email = " " + email

    # --------------------------------
    # Missing / empty values
    # --------------------------------
    if i % 10 == 0:
        age = None

    if i % 12 == 0:
        city = ""

    if i % 15 == 0:
        email = None

    if i % 18 == 0:
        purchase_amount = None

    if i % 20 == 0:
        rating = None

    # --------------------------------
    # Wrong data types
    # --------------------------------
    if i % 16 == 0:
        age = "unknown"

    if i % 17 == 0:
        purchase_amount = "not available"

    if i % 19 == 0:
        rating = "five"

    # --------------------------------
    # Customer ID
    # --------------------------------
    customer_id = f"C{i:03d}"

    data.append([
        customer_id,
        name,
        age,
        city,
        email,
        purchase_amount,
        rating
    ])


# Create DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "customer_id",
        "name",
        "age",
        "city",
        "email",
        "purchase_amount",
        "rating"
    ]
)


# --------------------------------
# Add duplicate rows
# --------------------------------

df.loc[115] = df.loc[5]
df.loc[116] = df.loc[25]
df.loc[117] = df.loc[50]
df.loc[118] = df.loc[75]
df.loc[119] = df.loc[100]


# --------------------------------
# Save messy dataset
# --------------------------------

df.to_csv("messy_customers.csv", index=False)

print("Messy dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nDataset preview:")
print(df.head(10))
