
#Allows the creation of functions with unlimited arguments that can be accessed by position
# *args passes the arguments to the function as tuple
def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(5,6,7,8,3)     )

# **kwargs passes the arguments to the function as a dictionary
#def calculate(**kwargs):

class Car:
    def __init__(self, **kw):
        #use the .get notation to access properties and avoid errors
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car= Car( make="Nissan")

print(my_car.make)