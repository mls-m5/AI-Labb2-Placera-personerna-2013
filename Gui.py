from tkinter import *
from Room import *
from Person import *


def loadPhoto(filename):
    photo = PhotoImage(file=filename)
    subphoto = photo.subsample(4, 4)
    return subphoto


class ResultView(Frame):
    ViewedRooms = 0
    RoomContent = dict()
    TypeDictionary = dict()

    def __init__(self):
        Frame.__init__(self, Tk())
        self.pack()
        self.HeadPhoto = loadPhoto("head.gif")
        self.TypeDictionary[Person.StatusEnum.Head] = self.HeadPhoto

        self.ProfessorPhoto = loadPhoto("professor.gif")
        self.TypeDictionary[Person.StatusEnum.Professor] = self.ProfessorPhoto

        self.ResearcherPhoto = loadPhoto("researcher.gif")
        self.TypeDictionary[Person.StatusEnum.Researcher] = self.ResearcherPhoto

        self.PhdPphoto = loadPhoto("phd.gif")
        self.TypeDictionary[Person.StatusEnum.PhD] = self.PhdPphoto

        self.SmokePhoto = loadPhoto("smoke.gif")
        self.NoSmokePhoto = loadPhoto("nosmoke.gif")

    def CreateRoom(self, root, room):
        x = 0
        for person in room.Inhabitants:
            extraInfo = ""
            if person.Visitors == Person.VisitorEnum.Many:
                extraInfo = " (many)"
            personFrame = LabelFrame(root, text=person.Name + extraInfo)
            label = Label(personFrame, image=self.TypeDictionary[person.Status])
            label.grid(row=1, column=0)
            personFrame.grid(row=1, column=x)

            smokeLabel = None
            if person.Smoking == person.SmokingEnum.Smoker:
                smokeLabel = Label(personFrame, image=self.SmokePhoto)
            else:
                smokeLabel = Label(personFrame, image=self.NoSmokePhoto)
            smokeLabel.grid(row=0, column=0)
            x += 1

    def AddRoom(self, room):
        self.SetRoom(self.ViewedRooms, room)
        self.ViewedRooms += 1

    def SetRoom(self, index, room):
        roomInfo = roomSizeArray[room.RoomSize]
        frame = LabelFrame(self, text=room.Name + " (" + roomInfo + ")")
        frame.grid(row=1, column=index)
        self.CreateRoom(frame, room)

    def ShowInfo(self, text):
        label = Label(self, text=text)
        label.grid(row=2, column=0)


if __name__ == "__main__":
    pA = Person("A", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Many, Person.StatusEnum.Head)
    pB = Person("B", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Many, Person.StatusEnum.Professor)

    t10 = Room("T10", Room.RoomEnum.SuperLarge)
    t10.Assign(pA)
    t10.Assign(pB)

    resView = ResultView()
    resView.AddRoom(t10)

    mainloop()


