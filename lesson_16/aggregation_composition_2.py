# aggregation - weak ref
# composition - strong ref

# aggregation - weak ref
class Case:
    def __init__(self, material):
        self.material = material

class CameraModule:
    def __init__(self, megapixels):
        self.megapixels = megapixels

    def photo(self):
        ...


class DisplayModule:
    def __init__(self, resolution):
        self.resolution = resolution

    def display(self):
        ...

class Battery:
    def __init__(self, volume):
        self.volume = volume

    def charge(self, percents):
        ...



class Phone:
    def __init__(self, camera, display, battery, case):
        self.camera = camera
        self.screen = display
        self.accumulator = battery
        self.case = case



c = CameraModule(1000)
d = DisplayModule("FullHD 8K")
b = Battery(10000)
case = Case("Gold")


super_phone = Phone(c, d, b, case)

super_phone_2 = Phone(c, d, b, case)



