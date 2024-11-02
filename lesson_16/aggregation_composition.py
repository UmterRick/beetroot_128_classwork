# aggregation - weak ref
# composition - strong ref



# composition - strong ref
class Room:
    def __init__(self, area):
        self.area = area


class House:

    def __init__(self, foundament):
        self.foundament = foundament
        self.rooms = []

    def get_total_area(self):
        return sum([room.area for room in self.rooms])

    def add_room_aggregation(self, room: Room):

        self.rooms.append(room)

    def add_room_composition(self, area):
        new_room = Room(area)
        self.rooms.append(new_room)


house = House("concrete")
house_2 = House("concrete")

room_1 = Room(50)

house.add_room_aggregation(room_1)
house_2.add_room_aggregation(room_1)


print(house)
print(room_1)
del house

# print(house)
print(room_1)


house_3 = House("concrete")
house_3.add_room_composition(40)
house_3.add_room_composition(20)
house_3.add_room_composition(140)
print(house_3.rooms)

living_room = house_3.rooms[2]
print(living_room)

del house_3

print(living_room)