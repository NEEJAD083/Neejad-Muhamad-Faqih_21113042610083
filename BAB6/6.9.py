favorite_places = {
    'neejad': ['tangerang', 'merbau'],
    'sultan': ['serang', 'kandang beruk', 'bromo'],
    'sulaiman': ['kamar mandi', 'dapur', 'kamar tidur'],
}
 
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"  {place}")
    print()
 