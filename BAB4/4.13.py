menu = ("karedok", "jengkol", "pete", "lalapan", "sop iga")
 
print("Our menu:")
for food in menu:
    print(food)
 
# Tuples can't be changed, so Python rejects this assignment.
try:
    menu[0] = "pecel"
except TypeError as error:
    print(f"\nPython rejected the change: {error}")
 
# The menu changes: rewrite the whole tuple with two new foods.
menu = ("karedok", "jengkol", "tempe", "lalapan", "tahu")

print("\nOur revised menu:")
for food in menu:
    print(food)
 