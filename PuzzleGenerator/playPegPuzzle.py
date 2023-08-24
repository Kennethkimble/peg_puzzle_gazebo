import pegBoard
import pegFeeder

class insertPeg:
    def __init__(self, plane, row, column, pegboard, peg):
        self.plane = plane
        self.row = row
        self.column = column
        self.pegboard = pegboard
        self.peg = peg
        self.conflictingSlots, self.conflictingPlane = self.findConflicts()

    def attemptInsertion(self, conflictingSlots):
        slot = pegboard.planes[self.plane].slots[self.row][self.column]
        fail_Slot_types = [1, 2, 3]

        # check if  slot matches peg type and if the slot is already filled
        if slot.is_filled:
            print("Slot is already filled.")
            return False
        elif (slot.slot_type == 1 or slot.slot_type == 4) and self.peg != 1:
            print("Cannot be inserted:\nMismatch peg and slot type")
            return False
        elif (slot.slot_type == 2 or slot.slot_type == 5) and self.peg != 2:
            print("Cannot be inserted:\nMismatch peg and slot type")
            return False
        elif (slot.slot_type == 3 or slot.slot_type == 6) and self.peg != 3:
            print("Cannot be inserted:\nMismatch peg and slot type")
            return False
                
        # check for conflicts with prevsiously inserted pegs
        if len(conflictingSlots) > 0:
            for cslots in conflictingSlots:
                # Create peg name for conflict
                if cslots.slot_type == 1 or cslots.slot_type == 4:
                    pegName = "Circle"
                elif cslots.slot_type == 2 or cslots.slot_type == 5:
                    pegName = "Square"
                elif cslots.slot_type == 3 or cslots.slot_type == 6:
                    pegName = "Hex"
                else:
                    pegName = "NULL"

                if cslots.is_filled and (cslots.slot_type in fail_Slot_types):
                    print("Insertion path blocked by previous peg: ", pegName)
                    return False
                
            # Set the peg in the specified slot
            slot = pegboard.planes[self.plane].slots[self.row][self.column]
            slot.set_peg(self.peg)
            print("Peg inserted successfully!")
            return True
        
        else:
        # Set the peg in the specified slot
            slot = pegboard.planes[self.plane].slots[self.row][self.column]
            slot.set_peg(self.peg)
            print("Peg inserted successfully!")
            return True
        
    def findConflicts(self):
        conflictingSlots = []
        conflictingPlane = None
        # Set conflicting plane
        # if the plane is RIGHT and in the bottom row it conflicts with BASE
        if self.plane == 2 and self.row == 2:
            conflictingPlane = pegboard.planes[1]
            if self.column == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[0][2])
            if self.column == 1:
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[1][2])
            if self.column == 2:
                conflictingSlots.append(conflictingPlane.slots[2][0])
                conflictingSlots.append(conflictingPlane.slots[2][1])
                conflictingSlots.append(conflictingPlane.slots[2][2])

        # if the plane is RIGHT and in the left column it conflicts with LEFT
        if self.plane == 2 and self.column == 0:
            conflictingPlane = pegboard.planes[0]
            if self.row == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[0][2])
            if self.row == 1:
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[1][2])
            if self.row == 2:
                conflictingSlots.append(conflictingPlane.slots[2][0])
                conflictingSlots.append(conflictingPlane.slots[2][1])
                conflictingSlots.append(conflictingPlane.slots[2][2])

        # if the plane is LEFT and in the bottom row it conflicts with BASE
        if self.plane == 0 and self.row == 2:
            conflictingPlane = pegboard.planes[1]
            if self.column == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[2][0])
            if self.column == 1:
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[2][1])
            if self.column == 2:
                conflictingSlots.append(conflictingPlane.slots[0][2])
                conflictingSlots.append(conflictingPlane.slots[1][2])
                conflictingSlots.append(conflictingPlane.slots[2][2])
        
        # if the plane is LEFT and in the right column it conflicts with RIGHT
        if self.plane == 0 and self.column == 2:
            conflictingPlane = pegboard.planes[2]
            if self.row == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[0][2])
            if self.row == 1:
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[1][2])
            if self.row == 2:
                conflictingSlots.append(conflictingPlane.slots[2][0])
                conflictingSlots.append(conflictingPlane.slots[2][1])
                conflictingSlots.append(conflictingPlane.slots[2][2])

        # if the plane is BASE and in the top row it conflicts with LEFT
        if self.plane == 1 and self.row == 0:
            conflictingPlane = pegboard.planes[0]
            if self.column == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[2][0])
            if self.column == 1:
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[2][1])
            if self.column == 2:
                conflictingSlots.append(conflictingPlane.slots[0][2])
                conflictingSlots.append(conflictingPlane.slots[1][2])
                conflictingSlots.append(conflictingPlane.slots[2][2])
        
        # if the plane is BASE and in the Right column it conflicts with RIGHT
        if self.plane == 1 and self.column == 2:
            conflictingPlane = pegboard.planes[2]
            if self.row == 0:
                conflictingSlots.append(conflictingPlane.slots[0][0])
                conflictingSlots.append(conflictingPlane.slots[1][0])
                conflictingSlots.append(conflictingPlane.slots[2][0])
            if self.row == 1:
                conflictingSlots.append(conflictingPlane.slots[0][1])
                conflictingSlots.append(conflictingPlane.slots[1][1])
                conflictingSlots.append(conflictingPlane.slots[2][1])
            if self.row == 2:
                conflictingSlots.append(conflictingPlane.slots[0][2])
                conflictingSlots.append(conflictingPlane.slots[1][2])
                conflictingSlots.append(conflictingPlane.slots[2][2])

        return conflictingSlots, conflictingPlane

        
if __name__ == "__main__":

    print("Welcome to the peg puzzle game. \n"
          "Complete the assembly of the pegboard by inserting all the pegs into their correct slots.\n"
          "Be careful where you place each peg as it could block the enterance to a future peg.\n"
          "Here is the board. And your first peg.\n")
    
# Make a pegboard
    pegboard = pegBoard.Pegboard()

# Make a Feeder
    feeder = pegFeeder.PegFeeder()
    feeder.getfeeder()

    while True:
    # Print the current pegboard
        pegboard.print_board(pegboard.planes)

        current_peg = feeder.pull_peg()
        if current_peg == 1:
            pegName = "Circle"
        elif current_peg == 2:
            pegName = "Square"
        elif current_peg == 3:
            pegName = "Hex"
        else:
            pegName = "NULL"

        if current_peg is None:
            print("Congratualtions! PegBoard Complete.")
            break

        while True:
            print("Enter a plane you would like to insert the peg into: L, B, or R (Left, Base, Right)")
            while True:
                choicePlane = input("PLANE: ").upper()
                if choicePlane not in ["L", "B", "R"]:
                    print("Invalid entry, please enter L, B, or R")
                    continue
                if choicePlane == "L":
                    choicePlane = 0
                if choicePlane == "B":
                    choicePlane = 1
                if choicePlane == "R":
                    choicePlane = 2
                break
            print(choicePlane)

            print("Enter a row for the peg by chosing T, M, B (top, middle, or bottom)")
            while True:
                choiceRow = input("ROW: ").upper()
                if choiceRow not in ["T", "M", "B"]:
                    print("Invalid entry, please enter T, M or B")
                    continue
                if choiceRow == "T":
                    choiceRow = 0
                if choiceRow == "M":
                    choiceRow = 1
                if choiceRow == "B":
                    choiceRow = 2
                break
            print(choiceRow)

            print("Enter a column for the peg by chosing L, M, R (Left, Middle, or Right)")
            while True:
                choiceColumn = input("COLUMN: ").upper()
                if choiceColumn not in ["L", "M", "R"]:
                    print("Invalid entry, please enter L, M or R")
                    continue
                if choiceColumn == "L":
                    choiceColumn = 0
                if choiceColumn == "M":
                    choiceColumn = 1
                if choiceColumn == "R":
                    choiceColumn = 2
                break
            print(choiceColumn)
            
            insertion = insertPeg(choicePlane, choiceRow, choiceColumn, pegboard, current_peg)
            
            if insertion.attemptInsertion(insertion.conflictingSlots):
                break

            else:
                print("Try Again")
                pegboard.print_board(pegboard.planes)
                print("Current peg: ", pegName)
                continue