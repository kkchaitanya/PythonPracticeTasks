class Product:
    def __init__(self, product_id, product_name, category, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.stock = stock

    def display_product(self):
        print(f"ID: {self.product_id} | Name: {self.product_name} | "
              f"Category: {self.category} | Price: ₹{self.price} | "
              f"Stock: {self.stock}")


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_product(self, product, quantity):
        if product.stock == 0:
            print(f"Cannot add '{product.product_name}'. Out of stock!")
            return

        if quantity > product.stock:
            print(f"Only {product.stock} units of '{product.product_name}' available.")
            return

        if product.product_id in self.cart:
            self.cart[product.product_id]["quantity"] += quantity
        else:
            self.cart[product.product_id] = {
                "product": product,
                "quantity": quantity
            }

        product.stock -= quantity
        print(f"{quantity} x {product.product_name} added to cart.")

    def remove_product(self, product_id):
        if product_id in self.cart:
            item = self.cart[product_id]
            item["product"].stock += item["quantity"]
            print(f"{item['product'].product_name} removed from cart.")
            del self.cart[product_id]
        else:
            print("Product not found in cart.")

    def display_cart(self):
        print("\n----- SHOPPING CART -----")
        if not self.cart:
            print("Cart is empty.")
            return

        for item in self.cart.values():
            product = item["product"]
            quantity = item["quantity"]
            subtotal = product.price * quantity

            print(f"{product.product_name} | Qty: {quantity} | "
                  f"Price: ₹{product.price} | Subtotal: ₹{subtotal}")

    def calculate_total(self):
        total = 0
        for item in self.cart.values():
            total += item["product"].price * item["quantity"]
        return total

    def check_availability(self, product):
        if product.stock > 0:
            print(f"{product.product_name} is available.")
        else:
            print(f"{product.product_name} is out of stock.")


# Creating 5 Products
p1 = Product(101, "Laptop", "Electronics", 50000, 5)
p2 = Product(102, "Smartphone", "Electronics", 20000, 10)
p3 = Product(103, "Headphones", "Accessories", 2000, 15)
p4 = Product(104, "Keyboard", "Accessories", 1500, 8)
p5 = Product(105, "Mouse", "Accessories", 800, 0)  # Out of stock

# Display Products
print("Available Products:")
products = [p1, p2, p3, p4, p5]

for product in products:
    product.display_product()

# Create Shopping Cart
cart = ShoppingCart()

# Customer purchases multiple products
cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.add_product(p3, 3)

# Try purchasing out-of-stock item
cart.add_product(p5, 1)

# Check availability
cart.check_availability(p5)

# Display Cart
cart.display_cart()

# Total Amount
print("\nTotal Amount: ₹", cart.calculate_total())

# Remove Product
cart.remove_product(103)

# Display Updated Cart
cart.display_cart()
print("\nUpdated Total Amount: ₹", cart.calculate_total())