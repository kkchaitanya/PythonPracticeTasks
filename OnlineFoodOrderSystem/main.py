# ============================================================
# Online Food Ordering System
# Demonstrates OOP: Classes, Objects, Encapsulation, Composition
# ============================================================


# ---------- 1. FoodItem Class ----------
class FoodItem:
    """Represents a single food item on the menu."""

    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"


# ---------- 2. Restaurant Class ----------
class Restaurant:
    """Represents a restaurant that holds a menu of food items."""

    def __init__(self, name: str):
        self.name = name
        self.menu = []  # list of FoodItem objects

    def add_food_item(self, food_item: FoodItem):
        """Add a food item to the menu."""
        self.menu.append(food_item)

    def show_menu(self):
        """Display all available food items."""
        print(f"\n--- {self.name} Menu ---")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item}")
        print("-" * 30)


# ---------- 3. Customer Class ----------
class Customer:
    """Represents a customer placing an order."""

    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


# ---------- 4. Order Class ----------
class Order:
    """Represents an order placed by a customer."""

    def __init__(self, order_id: int, customer: Customer, restaurant: Restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.items = []  # list of (FoodItem, quantity) tuples

    def add_item(self, food_item: FoodItem, quantity: int = 1):
        """Add a food item with a given quantity to the order."""
        self.items.append((food_item, quantity))

    def calculate_total(self) -> float:
        """Calculate the total bill for the order."""
        return sum(item.price * qty for item, qty in self.items)

    def display_summary(self):
        """Display the full order summary."""
        print("\n" + "=" * 45)
        print(f"           ORDER SUMMARY #{self.order_id}")
        print("=" * 45)
        print(f"Restaurant : {self.restaurant.name}")
        print(f"Customer   : {self.customer.name} ({self.customer.phone})")
        print("-" * 45)
        print(f"{'Item':<20}{'Qty':<8}{'Price':<10}{'Subtotal'}")
        print("-" * 45)

        for item, qty in self.items:
            subtotal = item.price * qty
            print(f"{item.name:<20}{qty:<8}${item.price:<9.2f}${subtotal:.2f}")

        print("-" * 45)
        print(f"{'TOTAL BILL:':<38}${self.calculate_total():.2f}")
        print("=" * 45)


# ---------- 5. Demonstration ----------
def main():
    # ----- Create a Restaurant -----
    restaurant = Restaurant("Tasty Bites")

    # ----- Create at least 5 Food Items and add to menu -----
    food1 = FoodItem("Margherita Pizza", "Main Course", 12.99)
    food2 = FoodItem("Cheeseburger",      "Main Course", 9.50)
    food3 = FoodItem("Caesar Salad",      "Starter",     7.25)
    food4 = FoodItem("French Fries",      "Side",        3.99)
    food5 = FoodItem("Chocolate Cake",    "Dessert",     5.50)
    food6 = FoodItem("Coca Cola",         "Beverage",    2.00)

    for item in (food1, food2, food3, food4, food5, food6):
        restaurant.add_food_item(item)

    restaurant.show_menu()

    # ----- Customer 1 Order -----
    customer1 = Customer("Alice Johnson", "555-1234")
    order1 = Order(order_id=101, customer=customer1, restaurant=restaurant)
    order1.add_item(food1, quantity=2)   # 2 Pizzas
    order1.add_item(food4, quantity=2)   # 2 Fries
    order1.add_item(food6, quantity=2)   # 2 Cokes
    order1.display_summary()

    # ----- Customer 2 Order -----
    customer2 = Customer("Bob Smith", "555-5678")
    order2 = Order(order_id=102, customer=customer2, restaurant=restaurant)
    order2.add_item(food2, quantity=1)   # 1 Burger
    order2.add_item(food3, quantity=1)   # 1 Salad
    order2.add_item(food5, quantity=3)   # 3 Cakes
    order2.add_item(food6, quantity=1)   # 1 Coke
    order2.display_summary()


if __name__ == "__main__":
    main()
