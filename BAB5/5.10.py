current_users = ['admin', 'Erin', 'JohnDoe', 'Maya', 'sam']
new_users = ['Maya', 'alex', 'SAM', 'nina', 'Kim']
 
# Make a lowercase copy so the comparison is case insensitive.
current_users_lower = [user.lower() for user in current_users]
 
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, {new_user} is taken. Please enter a new username.")
    else:
        print(f"The username {new_user} is available.")
 