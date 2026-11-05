class User:
    """Profil pengguna sederhana."""
 
    def __init__(self, first_name, last_name, age, email, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0  # nilai default
 
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
        print(f"  Occupation: {self.occupation}")
 
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
 
    def increment_login_attempts(self):
        """Tambah login_attempts sebanyak 1."""
        self.login_attempts += 1
 
    def reset_login_attempts(self):
        """Reset login_attempts menjadi 0."""
        self.login_attempts = 0
 
 
user = User("Budi", "Santoso", 29, "budi@example.com", "Semarang", "Software Engineer")
 
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # 3
 
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")  # 0
 