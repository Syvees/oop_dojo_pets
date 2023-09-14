class Ninja:
    def __init__ (self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name="Shobe", pet_type="dog", tricks="give paw")

    def walk (self):
        print("Time for play!")
        self.pet.play()
        return self

    def feed (self):
        print(f"Feeding {self.pet.name} some {self.pet_food}!")
        self.pet.eat()
        return self
    
    def bathe (self):
        print(f"Time for bath {self.pet.name}!")
        self.pet.noise()
        return self
    
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
    
hermione = Ninja ("Hermione", "Granger", "pumpkin biscuits", "vegetables")
hermione.feed().walk().bathe().pet.sleep()