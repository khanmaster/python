class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("nom nom nom nom")

    def procreate(self):
        print("time to find a mate")

    def move(self):
        print("onwards and upwards")
cat = Animal()
print(cat)
cat.breathe()
cat.eat()
cat.procreate()
cat.move()