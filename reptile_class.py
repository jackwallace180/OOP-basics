from animal_class import *
class Reptile(Animal):

    def __init__(self, name, number_Hearts, chamo, eyes = 2 , legs = 4):
        super(). __init__(name, legs, eyes)   # run in the init in the parent class
        self.number_hearts = number_Hearts
        self.chamo = chamo


    def eat(self, food = 'bugs'):   # method polymorphism where we override the method eat()
        return 'waaiitt for ittttt .... waaaiittt AND POUNCE!! NOM ' + food

    def seek_heat(self):   #adding new methods to this class -- Polymorphing how the class looks
        return 'Hmmmm bit chilly, where that sun at? why did i sit at the back'

    pass