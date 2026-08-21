class Booking:
    def __init__(self, vehicle, distance: float):
        self.vehicle = vehicle
        self.distance = distance
        self.total_fare = vehicle.calculate_fare(distance)

    def print_receipt(self):
        print("\n========== BOOKING RECEIPT ==========")
        print(f"Driver       : {self.vehicle.driver_name}")
        print(f"Vehicle Type : {type(self.vehicle).__name__}")
        print(f"Distance     : {self.distance} KM")
        print(f"Rate         : ₹{self.vehicle.price_per_km}/KM")
        print(f"Total Fare   : ₹{self.total_fare}")
        print("=====================================")
