from random import randint


class Die:
    """Dadu dengan jumlah sisi tertentu (default 6)."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Cetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


d6 = Die()      # dadu 6 sisi (nilai default)
d10 = Die(10)   # dadu 10 sisi
d20 = Die(20)   # dadu 20 sisi

for die in (d6, d10, d20):
    print(f"\nMelempar dadu {die.sides} sisi sebanyak 10 kali:")
    for _ in range(10):
        die.roll_die()

