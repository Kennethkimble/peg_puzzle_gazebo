import random

class PegType:
    Circle = 1
    Square = 2
    Hex = 3
    
class PegFeeder:
    def __init__(self, feeder=None):
        self.feeder = feeder

    def getfeeder(self):
        self.feeder = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
        while True:
            test = True
            random.shuffle(self.feeder)
            i = 0
            j = 0
            while j < len(self.feeder)-1:
                j = i+1
                target = self.feeder[i]
                comparable = self.feeder[j]
                count = 1
                while target == comparable:
                    count +=1
                    if count == 5:
                        test = False
                        break
                    else:
                        if j < len(self.feeder)-1:
                            comparable = self.feeder[j+1]
                            j += 1
                        else:    
                            return
                if test == True:
                    i=j
                else:
                    break

        
    def pull_peg(self):
        if not self.feeder:
            print("Feeder is empty.")
            return None
        pulled_peg = self.feeder.pop(0)
        if pulled_peg == 1:
            print("pulled a Circle peg")
        if pulled_peg == 2:
            print("pulled a Square peg")
        if pulled_peg == 3:
            print("pulled a Hex peg")
        return pulled_peg

    
    def print_feeder(self):
        feeder = self.feeder
        for peg in feeder:
            if peg == 1:
                print("Circle")
            elif peg == 2:
                print("Square")
            elif peg == 3:
                print("Hex")
            else:
                print("Empty feeder")
