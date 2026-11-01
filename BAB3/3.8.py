places = ["tangerang", "bekasi", "depok", "bogor", "jakarta"]
 
print("Original order:")
print(places)
 
print("\nAlphabetical order, using sorted():")
print(sorted(places))
 
print("\nStill in the original order:")
print(places)
 
print("\nReverse-alphabetical order, using sorted():")
print(sorted(places, reverse=True))
 
print("\nStill in the original order:")
print(places)
 
places.reverse()
print("\nAfter reverse():")
print(places)
 
places.reverse()
print("\nAfter reverse() again, back to the original order:")
print(places)
 
places.sort()
print("\nAfter sort(), stored in alphabetical order:")
print(places)
 
places.sort(reverse=True)
print("\nAfter sort(reverse=True), stored in reverse-alphabetical order:")
print(places)
