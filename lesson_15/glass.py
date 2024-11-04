

class Glass:

    def __init__(self, material, volume, shape):
        self.material = material
        self.shape = shape
        self.volume = volume
        self.free_volume = volume
        self.content = None

    def fill(self, liquid, volume):
        self.content = liquid
        if volume > self.free_volume:
            raise ValueError("Its too mush liquid for this glass")
        self.free_volume -= volume




my_favourite_glass = Glass("glass", 250, "cylinder")
my_favourite_glass.fill("Coffee", 200)
print(my_favourite_glass.content)
print(my_favourite_glass.free_volume)

my_favourite_glass.fill("Coffee", 100)

