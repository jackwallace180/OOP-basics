from animal_class import *


my_animal = Animal('Rick')
print(my_animal)
print(type(my_animal))

print(my_animal.eat('taco'))
print(my_animal.potty())

print(my_animal.name)
print(my_animal.number_of_eyes)
print(my_animal.number_of_legs)

my_animal2 = Animal('frank', 8)
print(my_animal2.name)
print(my_animal2.number_of_eyes)
print(my_animal2.number_of_legs)

my_animal3 = Animal('Tony',8,10)
print(my_animal3.name)
print(my_animal3.number_of_eyes)
print(my_animal3.number_of_legs)
print(my_animal3.heart())