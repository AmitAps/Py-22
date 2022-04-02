#
# Pylint Tutorial
#

class Car:
    def __init__(self,color):
        self.color =  color

my_car = Car('blue')

def crash(car1, car2):
    car1.color = 'red'

crash(car('blue'), my_car)
