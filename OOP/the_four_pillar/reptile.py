from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # should be set as not all reptiles are tetrapods...
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("it's chilly outside, where's the sun or a decent hot spring")

    def hunt(self):
        print("wait for it, wait for it..... and pounce")

    def use_venom(self):
        print("if I've got it I'm using it")

    def attract_mate_through_scent(self):
        print("time to throw on the eau de toilette")
reptile = Reptile.attract_mate_through_scent("1")
print(reptile)