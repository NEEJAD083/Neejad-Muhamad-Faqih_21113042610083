# This program uses every list function from this chapter at least once.
 
mountains = ["Everest", "K2", "Kilimanjaro"]
print(f"Starting list: {mountains}")
 
# Access an element by index (including negative indexes).
print(f"First mountain: {mountains[0]}")
print(f"Last mountain: {mountains[-1]}")
 
# Change an element.
mountains[1] = "Matterhorn"
print(f"After changing an element: {mountains}")
 
# append() adds an item to the end.
mountains.append("Fuji")
print(f"After append(): {mountains}")
 
# insert() adds an item at a specific position.
mountains.insert(0, "Rinjani")
print(f"After insert(): {mountains}")
 
# del removes an item by position.
del mountains[1]
print(f"After del: {mountains}")
 
# pop() removes an item and lets you use it.
popped_mountain = mountains.pop()
print(f"After pop(): {mountains} (popped {popped_mountain})")
 
# remove() removes an item by value.
mountains.remove("Matterhorn")
print(f"After remove(): {mountains}")
 
# Add a couple more so the sorting examples are more interesting.
mountains.append("Denali")
mountains.append("Elbrus")
print(f"List before sorting: {mountains}")
 
# sorted() returns a sorted copy without changing the original.
print(f"sorted(): {sorted(mountains)}")
print(f"Original is unchanged: {mountains}")
 
# sort() sorts the list permanently.
mountains.sort()
print(f"After sort(): {mountains}")
 
mountains.sort(reverse=True)
print(f"After sort(reverse=True): {mountains}")
 
# reverse() flips the current order.
mountains.reverse()
print(f"After reverse(): {mountains}")
 
# len() gives the number of items.
print(f"The list has {len(mountains)} mountains.")