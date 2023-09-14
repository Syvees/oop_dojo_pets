class Pet:
    def __init__ (self, name, pet_type, tricks):
        self.name = name
        self.pet_type = pet_type
        self.tricks = tricks
        self.health = 50
        self.energy = 50

    def sleep (self):
        print(f"Rest time for {self.name}!")
        self.energy +=25
        print (f"Energy level increased to: {self.energy}")
        return self
    
    def eat (self):
        self.energy +=5
        self.health +=10
        print (f"Energy level increased to: {self.energy}")
        print (f"Health level increased to: {self.health}")
        return self
    
    def play (self):
        self.health +=5
        print (f"Health level increased to: {self.health}")
        return self

    def noise (self):
        print (f"{self.name}: ruff! ruff!")
        return self