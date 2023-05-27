from datetime import date

class Dog:
    """Class to store dog details"""
    species = "Canis familiaris"

    def __init__(self, name, age, breed=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.toys = []

    def speak(self, sound="Blaf"):
        return f"{self.name} says {sound}"
    
    def add_toy(self, toy):
        self.toys += [toy]
    
    def get_birth_year(self):
        return  date.today().year - self.age
    
    def __str__(self):
        return self.speak()
        #return f"{self.name} is {self.age} years old. He has {len(self.toys)} toy(s)."

