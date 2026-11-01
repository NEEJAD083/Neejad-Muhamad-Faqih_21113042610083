animals = ["beruk", "monyet", "anjing"]
 
# First, just print the name of each animal.
for animal in animals:
    print(animal)
 
# Now print a statement about each animal.
print()
for animal in animals:
    print(f"A {animal} would make a great pet.")
 
# This line is outside the loop, so it prints only once.
print("\nAny of these animals would make a great pet!")