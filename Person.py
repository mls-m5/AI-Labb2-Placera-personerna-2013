statusArray = {0: "Head", 1: "Professor", 2: "Researcher", 3: "PhD"}
smokingArray = {0: "Non Smoker", 1: "Smoker"}
visitorsArray = {0: "Few", 1: "Many"}

class Person:
    class StatusEnum:
        Head = 0
        Professor = 1
        Researcher = 2
        PhD = 3

    class SmokingEnum:
        NonSmoker = 0
        Smoker = 1

    class VisitorEnum:
        Few = 0
        Many = 1

    Name = ""
    Status = StatusEnum.Head
    Smoking = SmokingEnum.NonSmoker
    Visitors = VisitorEnum.Few
    StayingIn = 0

    def __init__(self, name, smoking, visitors, status):
        self.Name = name
        self.Smoking = smoking
        self.Visitors = visitors
        self.Status = status
        self.StayingIn = None

    def Print(self):
        print("Name: " + self.Name)
        print("Smoking: " + smokingArray[self.Smoking])
        print("Visitors: " + visitorsArray[self.Visitors])
        print("Status: " + statusArray[self.Status])
        print("")

        
    
    