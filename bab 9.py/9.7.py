class User:
    """Profil pengguna sederhana."""
 
    def __init__(self, first_name, last_name, age, email, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0
 
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")
        print(f"  Occupation: {self.occupation}")
 
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
 
    def increment_login_attempts(self):
        self.login_attempts += 1
 
    def reset_login_attempts(self):
        self.login_attempts = 0
 
 
class Admin(User):
    """Administrator, sejenis user dengan hak istimewa."""
 
    def __init__(self, first_name, last_name, age, email, location, occupation):
        super().__init__(first_name, last_name, age, email, location, occupation)
        self.privileges = ["can add post", "can delete post", "can ban user"]
 
    def show_privileges(self):
        print(f"Privileges of admin {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
 
 
admin = Admin("Ada", "Lovelace", 36, "ada@example.com", "London", "Administrator")
admin.show_privileges()
 