# ============================================
#      SHOPPING CART PROGRAM
# ============================================

# Product catalog with prices
products = {
    "laptop":   {"name": "Laptop",   "price": 65000},
    "phone":    {"name": "Phone",    "price": 25000},
    "mouse":    {"name": "Mouse",    "price": 800},
    "keyboard": {"name": "Keyboard", "price": 1200},
    "monitor":  {"name": "Monitor",  "price": 9000},
    "speaker":  {"name": "Speaker",  "price": 2500}
}

# Empty cart to store selected items
cart = {}

# Welcome message
print("=" * 50)
print("    WELCOME TO THE SHOPPING CART  ")
print("=" * 50)
# Display available products
print("\n Available Products:")
print("-" * 35)
for key in products:
    print(f"  {products[key]['name']:<10} → ₹{products[key]['price']}")
print("-" * 35)

# Add products to cart
while True:
    choice = input("\nEnter product name (or 'done' to finish): ").strip().lower()

    if choice == "done":
        break

    if choice not in products:
        print(" Invalid product! Choose from the list.")
        continue

    try:
        qty = int(input(f"Enter quantity for {products[choice]['name']}: "))
        if qty <= 0:
            print("Quantity must be greater than 0.")
            continue
    except ValueError:
        print(" Please enter a valid number.")
        continue

    # Add to cart (merge if already exists)
    if choice in cart:
        cart[choice]["quantity"] += qty
    else:
        cart[choice] = {
            "name": products[choice]["name"],
            "price": products[choice]["price"],
            "quantity": qty
        }

    print(f"Added {qty} x {products[choice]['name']} to cart.")
# Check if cart is empty
if not cart:
    print("\n Cart is empty. No invoice generated.")
else:
    # Calculate subtotal
    subtotal = 0
    for item in cart.values():
        subtotal += item["price"] * item["quantity"]

    # Determine discount
    if subtotal > 60000:
        discount_rate = 15
    elif subtotal > 30000:
        discount_rate = 10
    elif subtotal > 10000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount_amount = subtotal * discount_rate / 100
    final_amount = subtotal - discount_amount

    # Print invoice
    print("\n")
    print("=" * 55)
    print("                 INVOICE")
    print("=" * 55)
    print(f"{'Item':<12}{'Qty':>6}{'Price':>12}{'Total':>15}")
    print("-" * 55)

    for item in cart.values():
        line_total = item["price"] * item["quantity"]
        print(f"{item['name']:<12}{item['quantity']:>6}"
              f"{'₹' + str(item['price']):>12}{'₹' + str(line_total):>15}")

    print("-" * 55)
    print(f"{'Subtotal':<29}{'₹' + format(subtotal, ','):>16}")
    print(f"{'Discount (' + str(discount_rate) + '%)':<29}"
          f"{'-₹' + format(round(discount_amount, 2), ','):>16}")
    print("=" * 55)
    print(f"{'Final Amount':<29}{'₹' + format(round(final_amount, 2), ','):>16}")
    print("=" * 55)
    print(" Thank you for shopping with us! ")
    print("=" * 55)