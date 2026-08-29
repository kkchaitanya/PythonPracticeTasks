import pandas as pd

# ==========================================
# 1. LOAD THE MESSY DATASET
# ==========================================

df = pd.read_csv("messy_customers.csv")

print("Original Dataset:")
print(df.head())


# ==========================================
# 2. isnull()
# Check which values are missing
# ==========================================

print("\n--- isnull() ---")
print(df.isnull())


# ==========================================
# 3. isnull().sum()
# Count missing values in each column
# ==========================================

print("\n--- Missing Values ---")
print(df.isnull().sum())


# ==========================================
# 4. dropna()
# Remove rows containing missing values
# ==========================================

df_dropna = df.dropna()

print("\n--- After dropna() ---")
print(df_dropna)


# ==========================================
# 5. fillna()
# Fill missing values
# ==========================================

df["age"] = df["age"].fillna(df["age"].median())

df["city"] = df["city"].fillna("Unknown")

df["email"] = df["email"].fillna("unknown@email.com")

df["purchase_amount"] = df["purchase_amount"].fillna(0)

df["rating"] = df["rating"].fillna(0)

print("\n--- After fillna() ---")
print(df.head())


# ==========================================
# 6. duplicated()
# Find duplicate rows
# ==========================================

print("\n--- duplicated() ---")
print(df.duplicated())


# Count duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# ==========================================
# 7. drop_duplicates()
# Remove duplicate rows
# ==========================================

df = df.drop_duplicates()

print("\n--- After drop_duplicates() ---")
print(df)


# ==========================================
# 8. astype()
# Convert data types
# ==========================================

# Convert customer_id to string
df["customer_id"] = df["customer_id"].astype(str)

# Convert name and city to string
df["name"] = df["name"].astype(str)
df["city"] = df["city"].astype(str)
df["email"] = df["email"].astype(str)

print("\n--- Data Types ---")
print(df.dtypes)


# ==========================================
# 9. str.strip()
# Remove extra spaces
# ==========================================

df["name"] = df["name"].str.strip()
df["city"] = df["city"].str.strip()
df["email"] = df["email"].str.strip()

print("\n--- After str.strip() ---")
print(df[["name", "city", "email"]].head())


# ==========================================
# 10. str.lower()
# Convert text to lowercase
# ==========================================

df["email"] = df["email"].str.lower()

print("\n--- After str.lower() ---")
print(df["email"].head())


# ==========================================
# 11. str.upper()
# Convert text to uppercase
# ==========================================

df["customer_id"] = df["customer_id"].str.upper()

print("\n--- After str.upper() ---")
print(df["customer_id"].head())


# ==========================================
# 12. str.title()
# Convert names and cities to title case
# ==========================================

df["name"] = df["name"].str.title()
df["city"] = df["city"].str.title()

print("\n--- After str.title() ---")
print(df[["name", "city"]].head())


# ==========================================
# 13. replace()
# Replace incorrect values
# ==========================================

# Replace incorrect text values in age
df["age"] = df["age"].replace("unknown", 0)

# Replace incorrect purchase amount
df["purchase_amount"] = df["purchase_amount"].replace(
    "not available", 0
)

# Replace incorrect rating
df["rating"] = df["rating"].replace("five", 5)

# Replace empty city values
df["city"] = df["city"].replace("", "Unknown")

# Replace empty email values
df["email"] = df["email"].replace("", "unknown@email.com")

print("\n--- After replace() ---")
print(df.head())


# ==========================================
# 14. Convert numeric columns properly
# ==========================================

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["purchase_amount"] = pd.to_numeric(
    df["purchase_amount"],
    errors="coerce"
)
df["rating"] = pd.to_numeric(
    df["rating"],
    errors="coerce"
)


# Fill any new NaN values created by conversion
df["age"] = df["age"].fillna(df["age"].median())
df["purchase_amount"] = df["purchase_amount"].fillna(0)
df["rating"] = df["rating"].fillna(0)


# ==========================================
# 15. FINAL CLEAN DATASET
# ==========================================

print("\n================================")
print("FINAL CLEAN DATASET")
print("================================")

print(df.head(20))

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFinal Missing Values:")
print(df.isnull().sum())


# ==========================================
# 16. SAVE CLEAN DATASET
# ==========================================

df.to_csv("clean_customers.csv", index=False)

print("\nClean dataset saved as:")
print("clean_customers.csv")
