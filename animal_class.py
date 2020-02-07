class Animal():       # you define a class like this. they allow us to make our own objects
    # characteristics
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    # behaviours


# Let's create an instance of an Animal object (we will assign it to a variable):

animal1 = Animal(legs = 4, name = 'Randy Marsh')  # we can specify using =, or follow and order like animal2
animal2 = Animal('Cartman', 4)

print(animal1) # every time you print it's a new instance in memory

print(type(animal1)) # prints __main__.Animal since we are in the file where the class was created

print(animal1.tasty)
print(animal2.tasty)

