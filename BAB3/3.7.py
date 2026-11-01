guests = ["meysa", "nayya", "salsa"]
 
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
 
# Bad news: the new table won't arrive in time.
print("\nSorry, the new table won't arrive in time. I can invite only two people.")
 
# Use pop() to remove guests until only two remain.
removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry, I can't invite you to dinner.")
removed_guest = guests.pop()
print(f"{removed_guest}, I'm sorry, I can't invite you to dinner.")
 
# The two remaining guests are still invited.
print(f"\n{guests[0]}, you are still invited to dinner.")
print(f"{guests[1]}, you are still invited to dinner.")
 
# Use del to empty the list.
del guests[-1]
del guests[-1]
 
print(guests)