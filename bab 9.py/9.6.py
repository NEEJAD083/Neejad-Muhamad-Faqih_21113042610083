class Restaurant:
    """Model sederhana sebuah restoran."""
 
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
 
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")
 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
 
    def set_number_served(self, number):
        self.number_served = number
 
    def increment_number_served(self, increment):
        self.number_served += increment
 
 
class IceCreamStand(Restaurant):
    """Kedai es krim, sejenis restoran."""
 
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mango"]
 
    def display_flavors(self):
        print(f"Flavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")
 
 
stand = IceCreamStand("Es Krim Kita")
stand.describe_restaurant()
stand.display_flavors()
 