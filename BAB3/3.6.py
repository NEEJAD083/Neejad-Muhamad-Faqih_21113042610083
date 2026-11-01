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
 
# Good news: a bigger table!
print("\nGood news! I found a bigger dinner table, so I'm inviting more guests.")
 
guests.insert(0, "kirania")   # add to the beginning
guests.insert(2, "ndaru")    # add to the middle
guests.append("robert") # add to the end
 
print(f"\n{guests[0]}, I would be honored if you would join me for dinner.")
print(f"{guests[1]}, I would be honored if you would join me for dinner.")
print(f"{guests[2]}, I would be honored if you would join me for dinner.")
print(f"{guests[3]}, I would be honored if you would join me for dinner.")
print(f"{guests[4]}, I would be honored if you would join me for dinner.")
print(f"{guests[5]}, I would be honored if you would join me for dinner.")