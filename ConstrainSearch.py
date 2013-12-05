from Person import *
from Room import *


def Pop(persons):
    if not persons:
        return None
    return persons.pop(0)


def PopPopMostConststrained(persons, rooms):
    largestNoOfConstraints = 0
    mostConstrainedPerson = None
    for p in persons:
        personalConstraints = 0
        for r in rooms:
            if not CanAssign(r, p):
                personalConstraints += 1
        if personalConstraints > largestNoOfConstraints:
            mostConstrainedPerson = p
            largestNoOfConstraints = personalConstraints
    if persons:
        persons.remove(mostConstrainedPerson)
        return mostConstrainedPerson
    else:
        return None


def SortForLeastConstrainedRoom(rooms, persons, selectedPerson):
    for room in rooms:
        if CanAssign(room, selectedPerson):
            room.Assign(selectedPerson)
            room.TotalConstraints = 0
            for p in persons:
                for innerRoom in rooms:
                    if not CanAssign(innerRoom, p):
                        room.TotalConstraints += 1
            room.Remove(selectedPerson)
    return sorted(rooms, key=lambda lr: lr.TotalConstraints)


def TryPlace(room, p):
    if not CanAssign(room, p):
        return False
    room.Assign(p)
    return True


def CanAssign(room, p):
    for constraint in ConstrainSearch.flist:
        if not constraint(room, p):
            return False
    return True


def HighStatus(room, person):
    if person.Status == Person.StatusEnum.Head or person.Status == Person.StatusEnum.Professor:
        if room.RoomSize == Room.RoomEnum.Small:
            return False
    return True


def Smoker(room, person):
    for p in room.Inhabitants:
        if not p.Smoking == person.Smoking:
            return False
    return True


def LiveAlone(room, person):
    if person.Status == Person.StatusEnum.Head or person.Status == Person.StatusEnum.Professor:
        if room.Inhabitants:
            return False
    else:
        for p in room.Inhabitants:
            if p.Status == Person.StatusEnum.Head or p.Status == Person.StatusEnum.Professor:
                return False
    return True


def ManyVisitors(room, person):
    if person.Visitors == Person.VisitorEnum.Few:
        return True
    for p in room.Inhabitants:
        if p.Visitors == Person.VisitorEnum.Many:
            return False
    return True

#noinspection PyUnusedLocal
def FullRoom(room, person):
    if room.FreeSpaces <= 0:
        return False
    return True


class ConstrainSearch:
    Persons = []
    Rooms = []
    NoOfCalls = 0
    flist = [HighStatus, Smoker, FullRoom, ManyVisitors, LiveAlone]
    Optimization = True

    def __init__(self, persons, rooms):
        self.Persons = persons
        self.Rooms = rooms

    def Start(self, optimization):
        self.NoOfCalls = 0
        self.Optimization = optimization
        return self.Assign(list(self.Persons), list(self.Rooms))

    def Assign(self, persons, rooms):
        self.NoOfCalls += 1
        if self.Optimization:
            current = PopPopMostConststrained(persons, rooms)
        else:
            current = Pop(persons)
        if current is None:
            return rooms
        if self.Optimization:
            rooms = SortForLeastConstrainedRoom(rooms, persons, current)
        for room in rooms:
            if TryPlace(room, current):
                result = self.Assign(persons[:], rooms[:])
                if result:
                    return result
                room.Remove(current)
        return None



