class Animal():

    # characteristics
    def __init__(self, name, legs = 4, eyes = 2):  #runs only once when you initialise an object
        self.name = name
        self.number_of_eyes = eyes
        self.number_of_legs = legs
        self.alive = True
        self.number_animal_eaten = 0
        self.age = 0

    # behaviours - functions that belong to a class
    # methods - functions that can only be used on this classes instant
    def eat(self, food = ' '):
        return 'NOM NOM NOM ' + food
    def sleep(self):
        return 'zzZZZZZzzzzZZZZzzzZZZZZZZzz'
    def hunt(self):
        return 'ATTTAAACCCKKKKKK!!! THIS IS SPARTA'
    def potty(self):
        return ' O_O ... HUNNNN o_O ....HUUUHNNN!! o_o SPLASH! -.- :D'
    def heart(self):
        return ' BBMMBBMMM BMMMBMMMM BMMMBMMMM'

#create an object of class animal
  # AKA initialising an object

#my_animal = Animal() #this is creating an instance of class animal

#print(my_animal)
#print(type(my_animal))





