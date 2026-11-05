from random import sample

# 10 angka dan 5 huruf
pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Pilih 4 item berbeda secara acak
winning_ticket = sample(pool, 4)

print(
    "Any ticket matching these 4 numbers or letters wins a prize: "
    + ", ".join(str(item) for item in winning_ticket)
)