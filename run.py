from animal_class import *
from reptile_class import *

my_animal = Animal('Rick')
print(my_animal)
print(type(my_animal))

print(my_animal.eat('taco'))
print(my_animal.potty())

my_reptile = Reptile('Ringo', 5, 'translucent')

print(my_reptile.name)
print(my_reptile.age)
print(my_reptile.chamo)
print(my_reptile.number_hearts)
print(my_reptile.eat('a baby zebra'))
print(my_animal.eat('fajita'))
print(my_reptile.seek_heat())

#print(my_animal.name)
#print(my_animal.number_of_eyes)
#print(my_animal.number_of_legs)

#my_animal2 = Animal('frank', 8)
#print(my_animal2.name)
#print(my_animal2.number_of_eyes)
#print(my_animal2.number_of_legs)

#my_animal3 = Animal('Tony',8,10)
#print(my_animal3.name)
#print(my_animal3.number_of_eyes)
#print(my_animal3.number_of_legs)
#print(my_animal3.heart())