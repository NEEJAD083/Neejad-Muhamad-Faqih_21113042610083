from random import sample

pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [3, 7, 'a', 'e']  # tiket saya: 4 item

attempts = 0
while True:
    attempts += 1
    winning_ticket = sample(pool, 4)
    # Tiket menang jika keempat item sama, urutan tidak dipermasalahkan
    if set(winning_ticket) == set(my_ticket):
        break

print(f"My ticket: {my_ticket}")
print(f"It took {attempts} tries to win with this ticket.")