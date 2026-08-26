import pandas as pd

df = pd.read_csv("products.csv")
print(f"head {df.head()}")
print(f"tail {df.tail()}")
print(f"describe {df.describe()}")
print(f"hinfoead {df.info()}")
print(f"shape {df.shape}")
print(f"columns {df.columns}")

#Find total products.
print(f"total products : {len(df)}")

#Find unique categories.
print(df["category"].unique())
#Find unique brands.
print(df["brand"].unique())
#Count products category-wise.
print(df.groupby("category")["product_id"].count())
#Find average price.
print(f"price : {df['price'].mean()}")
#Find highest-priced product.
#print(df.loc(df["price"].idxmax()))
print(df[df["price"]==df["price"].max()])
#Find lowest-priced product.
print(df[df["price"]==df["price"].min()])
#Find products priced above ₹50,000.
print(df[df["price"]>50000])
#Find products with rating greater than 4.
df = df[df["rating"]>4]
#Sort products by price.
df =  df.sort_values(["price"])
#Sort products by rating.
df =  df.sort_values(["rating"])
#Find products with stock below 10.
df= df[df["stock"]<10]
#Create discount_amount.
df["discount_amount"] = df["price"] *df["discount"]/100
#Create final_price.
df["final_price"] = df["price"]- df["discount_amount"]

#Find average price by category.
print(df.groupby("category")["price"].mean())
#Find average rating by brand.
print(df.groupby("brand")["rating"].mean())
#Find maximum product price category-wise.
print(df.groupby("category")["price"].max())

print(df)
df.to_csv("products_filter.csv", index=False)