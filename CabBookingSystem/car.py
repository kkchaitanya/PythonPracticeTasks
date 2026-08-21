from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_number: str, brand: str,
                 driver_name: str, price_per_km: float, seating_capacity: int):
        super().__init__(vehicle_number, brand, driver_name, price_per_km)
        self.seating_capacity = seating_capacity

    def display_info(self):
        print("\n--- Car Details ---")
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity} persons")
