from dog import Dog

dogs = [
    {"name" : "Bello",
     "age": 12,
     "breed": "Bulldog"},
    {"name": "Tom",
     "age": 4,
     "toys":["ball", "rubber-bone"]}
    ]


bello = Dog("Bello", 12)
tom = Dog("Tom", "2")
dogs = [bello, tom]

tom.add_toy("stick")
tom.breed = "Huskey"

print(bello.species)
print(bello.name)
print(bello.get_birth_year())

print(tom)

