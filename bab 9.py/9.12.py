class Privileges:
	def show_privileges(self):
		print("This administrator has all privileges.")


class Admin:
	def __init__(self, first_name, last_name, age, email, location, role):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.location = location
		self.role = role
		self.privileges = Privileges()


admin = Admin("Ada", "Lovelace", 36, "ada@example.com", "London", "Administrator")
admin.privileges.show_privileges()
 