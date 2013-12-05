roomSizeArray = {1: "Small", 2: "Large", 3: "Super Large"}
class Room:
    class RoomEnum:
        Small = 1
        Large = 2
        SuperLarge = 3
    Name = ""
    RoomSize = RoomEnum.Small
    FreeSpaces = 0
    Inhabitants = []
    TotalConstraints = 0

    def __init__(self, name, roomSize):
        self.Name = name
        self.RoomSize = roomSize
        self.FreeSpaces = self.RoomSize
        self.Inhabitants = []
        self.TotalConstraints = 0

    def Assign(self, person):
        if self.FreeSpaces <= 0 or person.StayingIn:
            return False
        self.Inhabitants.append(person)
        self.FreeSpaces -= 1
        person.StayingIn = self
        return True

    def Remove(self, person):
        person.StayingIn = None
        self.Inhabitants.remove(person)
        self.FreeSpaces += 1

    def Print(self):
        print("Name: {0}".format(self.Name))
        print("RoomSize: {0}".format(roomSizeArray[self.RoomSize]))
        print("FreeSpaces: {0}".format(self.FreeSpaces))
        print("Inhabitants:")
        for inhabitant in self.Inhabitants:
            inhabitant.Print()

