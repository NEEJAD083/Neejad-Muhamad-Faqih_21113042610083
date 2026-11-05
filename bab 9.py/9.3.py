class User:
    """Profil pengguna sederhana."""
 
    def __init__(self, first_name, last_name, age, email, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.occupation = occupation
 
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
        print(f"  Occupation: {self.occupation}")
 
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
 
 
users = [
    User("Ada", "Lovelace", 36, "ada@example.com", "London", "Mathematician"),
    User("Budi", "Santoso", 29, "budi@example.com", "Semarang", "Software Engineer"),
    User("Maria", "Garcia", 41, "maria@example.com", "Madrid", "Teacher"),
]
 
for user in users:
    user.describe_user()
    user.greet_user()
    print()
 