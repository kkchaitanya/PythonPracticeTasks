# ==========================================
# MULTIPLE INHERITANCE IN PYTHON
# Camera + MusicPlayer + GPS -> SmartPhone
# ==========================================


# ------------------------------------------
# Parent Class 1: Camera
# ------------------------------------------

class Camera:

    def take_photo(self):
        print("Taking a photo...")

    def record_video(self):
        print("Recording video...")


# ------------------------------------------
# Parent Class 2: MusicPlayer
# ------------------------------------------

class MusicPlayer:

    def play_music(self):
        print("Playing music...")

    def stop_music(self):
        print("Music stopped.")


# ------------------------------------------
# Parent Class 3: GPS
# ------------------------------------------

class GPS:

    def current_location(self):
        print("Current location: Hyderabad")

    def navigate(self):
        print("GPS navigation started...")


# ------------------------------------------
# Child Class: SmartPhone
# Inherits from Camera, MusicPlayer and GPS
# ------------------------------------------

class SmartPhone(Camera, MusicPlayer, GPS):

    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: ₹", self.price)
        print("Storage:", self.storage)


# ==========================================
# Creating 3 Smartphone Objects
# ==========================================

phone1 = SmartPhone(
    "Samsung",
    "Galaxy S25",
    79999,
    "256GB"
)

phone2 = SmartPhone(
    "Apple",
    "iPhone 16",
    89999,
    "256GB"
)

phone3 = SmartPhone(
    "OnePlus",
    "OnePlus 13",
    69999,
    "512GB"
)


# ==========================================
# Smartphone 1
# ==========================================

print("\n========== SMARTPHONE 1 ==========")

phone1.display_details()

print("\nCamera Features:")
phone1.take_photo()
phone1.record_video()

print("\nMusic Features:")
phone1.play_music()
phone1.stop_music()

print("\nGPS Features:")
phone1.current_location()
phone1.navigate()


# ==========================================
# Smartphone 2
# ==========================================

print("\n========== SMARTPHONE 2 ==========")

phone2.display_details()

print("\nCamera Features:")
phone2.take_photo()
phone2.record_video()

print("\nMusic Features:")
phone2.play_music()
phone2.stop_music()

print("\nGPS Features:")
phone2.current_location()
phone2.navigate()


# ==========================================
# Smartphone 3
# ==========================================

print("\n========== SMARTPHONE 3 ==========")

phone3.display_details()

print("\nCamera Features:")
phone3.take_photo()
phone3.record_video()

print("\nMusic Features:")
phone3.play_music()
phone3.stop_music()

print("\nGPS Features:")
phone3.current_location()
phone3.navigate()
