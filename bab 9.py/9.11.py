class Privileges:
	def __init__(self):
		self.privileges = [
			"can add post",
			"can delete post",
			"can ban user",
		]

	def show_privileges(self):
		print("Privileges:")
		for privilege in self.privileges:
			print(f"- {privilege}")


class Admin:
	def __init__(self, first_name, last_name, age, email, location, role):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.location = location
		self.role = role
		self.privileges = Privileges()


admin = Admin("Budi", "Santoso", 29, "budi@example.com", "Semarang", "Administrator")
admin.privileges.show_privileges()
 