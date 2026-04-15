class Animal:
    def __init__(self, animal_name, age, health_level = 50, happiness_level = 50):
        self.animal_name = animal_name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(f"Animal Name: {self.animal_name} , Health Level: {self.health_level} , Happiness Level: {self.happiness_level}")
        return self
    
    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self

class Lion(Animal):
    def __init__(self, animal_name, age , size = "large"):
        super(). __init__(animal_name, age)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f" , Size: {self.size}")  
        return self

    def feed(self):
        self.health_level += 20
        self.happiness_level += 5
        return self 


class Tiger(Animal):
    def __init__(self, animal_name, age, stripe_pattern = "Blod"):
        super().__init__(animal_name, age)
        self.stripe_pattern = stripe_pattern

    def display_info(self):
        super().display_info()
        print(f" , Stripe Pattern: {self.stripe_pattern}")  
        return self  


    def feed(self):
        self.health_level += 50
        self.happiness_level += 10
        return self   

class Monkey(Animal):
    def __init__(self, name, age, climbing_skill = "Expert"):
        super().__init__(name, age)
        self.climbing_skill = climbing_skill

    def display_info(self):
        super().display_info()
        print(f" , Climbing Skill: {self.climbing_skill}")  
        return self    

    def feed(self):  
        self.health_level += 5
        self.happiness_level += 20
        return self 

class Bear(Animal):
    def __init__(self, animal_name, age, strength=90):
        super().__init__(animal_name, age)
        self.strength = strength

    def display_info(self):
        super().display_info()
        print(f", Strength: {self.strength}")
        return self        

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self, animal_instance):
        self.animals.append(animal_instance)
        return self

    def print_all_info(self):
        print("-" * 20, self.name, "-" * 20)
        for animal in self.animals:
            animal.display_info()
        return self


my_zoo = Zoo("Wildlife Park")

my_zoo.add_animal(Lion("Simba", 5, "Extra Large")).add_animal(Tiger("Rajah", 3, "Striped")).add_animal(Bear("Baloo", 10, 90))
my_zoo.print_all_info()






