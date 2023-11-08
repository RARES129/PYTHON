class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def move(self):
        print(f"{self.name} is moving.")


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def feed_young(self):
        print(f"{self.name} is feeding its young.")


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying.")


class Fish(Animal):
    def __init__(self, name, habitat, water_type):
        super().__init__(name, habitat)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} is swimming.")


def main():
    lion = Mammal("Lion", "Savannah", "Golden")
    lion.move()
    lion.feed_young()

    eagle = Bird("Eagle", "Mountains", 2.5)
    eagle.move()
    eagle.fly()

    shark = Fish("Shark", "Ocean", "Saltwater")
    shark.move()
    shark.swim()


main()
