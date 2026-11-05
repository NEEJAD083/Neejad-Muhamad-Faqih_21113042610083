class Restaurant:
    """Model sederhana sebuah restoran."""
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
 
 
restaurant = Restaurant("Warung Sari", "Indonesian")
 
# Cetak kedua atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
 
# Panggil kedua method
restaurant.describe_restaurant()
restaurant.open_restaurant()
 