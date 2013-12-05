from Person import *
from Room import *
from ConstrainSearch import *
from Gui import *

pA = Person("A", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Many, Person.StatusEnum.Head)
pB = Person("B", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Many, Person.StatusEnum.Professor)
pC = Person("C", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Few, Person.StatusEnum.Professor)
pD = Person("D", Person.SmokingEnum.Smoker, Person.VisitorEnum.Many, Person.StatusEnum.Professor)
pE = Person("E", Person.SmokingEnum.Smoker, Person.VisitorEnum.Many, Person.StatusEnum.Researcher)
pF = Person("F", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Few, Person.StatusEnum.Researcher)
pG = Person("G", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Few, Person.StatusEnum.Researcher)
pH = Person("H", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Many, Person.StatusEnum.PhD)
pI = Person("I", Person.SmokingEnum.Smoker, Person.VisitorEnum.Few, Person.StatusEnum.PhD)
pJ = Person("J", Person.SmokingEnum.Smoker, Person.VisitorEnum.Few, Person.StatusEnum.PhD)
pK = Person("K", Person.SmokingEnum.NonSmoker, Person.VisitorEnum.Few, Person.StatusEnum.PhD)

t10 = Room("T10", Room.RoomEnum.SuperLarge)
t11 = Room("T11", Room.RoomEnum.Large)
t12 = Room("T12", Room.RoomEnum.Large)

t13 = Room("T13", Room.RoomEnum.Small)
t14 = Room("T14", Room.RoomEnum.Small)
t15 = Room("T15", Room.RoomEnum.Small)
t16 = Room("T16", Room.RoomEnum.Small)

#Extra som vi lagt till
t17 = Room("T17", Room.RoomEnum.Large)
t18 = Room("T18", Room.RoomEnum.SuperLarge)

persons = [pA, pB, pC, pD, pE, pF, pG, pH, pI, pJ, pK]
rooms = [t10, t11, t12, t13, t14, t15, t16, t17, t18]

if __name__ == "__main__":
    cS = ConstrainSearch(persons, rooms)
    result = cS.Start(True)
    print("Number of calls: {0}".format(cS.NoOfCalls))

    if not result is None:
        for r in result:
            r.Print()

    resultView = ResultView()
    if result:
        for r in result:
            resultView.AddRoom(r)
    resultView.ShowInfo("Numuber of calls: " + str(cS.NoOfCalls))

    mainloop()




