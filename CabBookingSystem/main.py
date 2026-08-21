from car import Car
from bike import Bike
from booking import Booking

def main():
    # Create vehicles
    vehicles = [
        Car("KA-01-1234", "Honda City",   "Rahul", 20.0, 4),
        Car("KA-02-5678", "Hyundai Verna","Priya", 22.0, 4),
        Bike("KA-03-9012", "Royal Enfield","Amit", 12.0, True),
        Bike("KA-04-3456", "Honda Activa", "Sneha", 8.0, True),
    ]

    # Display all available vehicles
    print("===== AVAILABLE VEHICLES =====")
    for v in vehicles:
        v.display_info()

    # Book trips
    trips = [
        Booking(vehicles[0], 15),  # Rahul's Car, 15 KM
        Booking(vehicles[1], 10),  # Priya's Car, 10 KM
        Booking(vehicles[2], 8),   # Amit's Bike, 8 KM
        Booking(vehicles[3], 5),   # Sneha's Bike, 5 KM
    ]

    # Print all receipts
    for trip in trips:
        trip.print_receipt()

if __name__ == "__main__":
    main()
