guests = ["meysa", "salsa", "nayya"]
 
print(f"{guests[0]}, I would be honored if you would join me for dinner.")
print(f"{guests[1]}, I would be honored if you would join me for dinner.")
print(f"{guests[2]}, I would be honored if you would join me for dinner.")
 
# One guest can't make it.
print(f"\nUnfortunately, {guests[1]} can't make it to dinner.")
 
# Replace that guest with someone new.
guests[1] = "sulaiman"
 
print(f"\n{guests[0]}, I would be honored if you would join me for dinner.")
print(f"{guests[1]}, I would be honored if you would join me for dinner.")
print(f"{guests[2]}, I would be honored if you would join me for dinner.")