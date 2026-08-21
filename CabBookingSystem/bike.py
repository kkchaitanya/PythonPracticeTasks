from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, vehicle_number: str, brand: str,
                 driver_name: str, price_per_km: float, has_helmet: bool):
        super().__init__(vehicle_number, brand, driver_name, price_per_km)
        self.has_helmet = has_helmet

    def display_info(self):
        print("\n--- Bike Details ---")
        super().display_info()
        print(f"Helmet Provided: {'Yes' if self.has_helmet else 'No'}")
