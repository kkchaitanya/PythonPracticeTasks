class Vehicle:
    def __init__(self, vehicle_number: str, brand: str,
                 driver_name: str, price_per_km: float):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.driver_name = driver_name
        self.price_per_km = price_per_km

    def calculate_fare(self, distance: float) -> float:
        return distance * self.price_per_km

    def display_info(self):
        print(f"Driver         : {self.driver_name}")
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Rate           : ₹{self.price_per_km}/KM")
