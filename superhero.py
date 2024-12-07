# Superhero class with encapsulation
class Superhero:
    def __init__(self, name, superpower, weakness):
        self.name = name  # public attribute
        self._superpower = superpower  # protected attribute
        self.__weakness = weakness  # private attribute (encapsulated)
    
    # Getter method for the private attribute
    def get_weakness(self):
        return self.__weakness
    
    def move(self):
        print(f"{self.name} is flying through the skies!")
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Superpower: {self._superpower}")
        print(f"Weakness: {self.get_weakness()}")  # Accessing private attribute via getter


# Villain class inheriting from Superhero and demonstrating polymorphism
class Villain(Superhero):
    def __init__(self, name, superpower, weakness, evil_plan):
        super().__init__(name, superpower, weakness)
        self.evil_plan = evil_plan
    
    def move(self):
        print(f"{self.name} is scheming in the shadows!")
    
    def display_info(self):
        super().display_info()
        print(f"Evil Plan: {self.evil_plan}")


# Create objects for Superhero and Villain
hero = Superhero("Captain Power", "Invisibility", "Loud noises")
villain = Villain("Dr. Doom", "Mind control", "Water", "World domination")

# Display their info
hero.display_info()
villain.display_info()

# Demonstrating polymorphism
hero.move()  # Hero's move method
villain.move()  # Villain's move method
