pets = [
    {'animal': 'snake', 'name':'zaroo', 'owner': 'areez'},
     {'animal': 'cat', 'name':'cutie', 'owner': 'uzair'},
      {'animal': 'dog', 'name':'lilly', 'owner': 'areez'},
]

for pet in pets:
    print(f"\nHere's what I know about the {pet['animal']}:")
    for key, value in pet.items():
        print(f"{key}{ value}:")




