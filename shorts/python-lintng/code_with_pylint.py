"""
Pylint Tutorial
"""

#pylint: disable=too-few-public-methods
class Car:
    """Car class with color method."""
    def __init__(self, color):
        self.color =  color

MY_CAR = Car('blue')

def crash(car1, car2): #pylint: disable=unused-argument
    """ Example function"""
    car1.color = 'brunt'

crash(Car('blue'), MY_CAR)
