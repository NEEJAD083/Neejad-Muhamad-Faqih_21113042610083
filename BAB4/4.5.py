import time
 
numbers = list(range(1, 1_000_001))
 
print(f"Smallest number: {min(numbers)}")
print(f"Largest number: {max(numbers)}")
 
start = time.perf_counter()
total = sum(numbers)
elapsed = time.perf_counter() - start
 
print(f"Sum: {total}")
print(f"Adding a million numbers took {elapsed:.4f} seconds.")