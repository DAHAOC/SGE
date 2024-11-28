class Colibri:
    # Constructor
    def __init__(self, name, speed, age):
        #Atributs
        self.name = name
        self.age = age
        self.speed = speed

    # Getters i Setters 
    def getName(self):
        return self.name
    def setName(self, new_name):
        self.name = new_name
    
    def getAge(self):
        return self.age
    def setAge(self, new_age):
        self.age = new_age

    def getSpeed(self):
        return self.speed
    def setSpeed(self, new_speed):
        self.speed = new_speed

    