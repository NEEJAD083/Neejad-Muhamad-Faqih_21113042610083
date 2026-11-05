class Restaurant:
    """Model sederhana sebuah restoran."""
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # nilai default
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
 
    def set_number_served(self, number):
        """Atur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number
 
    def increment_number_served(self, increment):
        """Tambahkan jumlah pelanggan yang dilayani."""
        self.number_served += increment
 
 
restaurant = Restaurant("Warung Sari", "Indonesian")
 
# Cetak nilai awal, ubah langsung lewat atribut, lalu cetak lagi
print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 25
print(f"Customers served: {restaurant.number_served}")
 
# Ubah lewat set_number_served()
restaurant.set_number_served(40)
print(f"Customers served: {restaurant.number_served}")
 
# Tambah lewat increment_number_served()
restaurant.increment_number_served(15)
print(f"Customers served: {restaurant.number_served}")
 