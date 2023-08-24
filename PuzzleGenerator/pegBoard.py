
import random

# Enumerations for slot types, peg types, and plane orientations
class PlaneOrientation:
    XY = "BASE"
    XZ = "LEFT"
    YZ = "RIGHT"

class SlotType:
    highCircle = 1
    highSquare = 2
    highHex = 3
    lowCircle = 4
    lowSquare = 5
    lowHex = 6

class Slot:
    def __init__(self, slot_type):
        self.slot_type = slot_type
        self.peg = None 
        self.is_filled = False 

    def set_peg(self, peg):
        self.peg = peg
        self.is_filled = True

class Plane:
    def __init__(self, orientation, slot_stock):
        self.orientation = orientation
        self.slot_stock = slot_stock
        self.slots = [[self.random_slot(slot_stock) for _ in range(3)] for _ in range(3)]

    def random_slot(self, slot_stock):
        available_slot_types = [slot_type for slot_type, count in slot_stock.items() if count > 0]

        if not available_slot_types:
            raise Exception("No more available slots on the pegboard.")

        slot_type = random.choice(available_slot_types)
        self.slot_stock[slot_type] -= 1  # Decrease the count of the used slot type
        return Slot(slot_type)

class Pegboard:
    def __init__(self):
        # Generate a valid pegboard
        self.generate_valid_pegboard()
        
    def generate_valid_pegboard(self):
        while True:
            slot_stock = {
            SlotType.highCircle: 4, SlotType.highSquare: 4, SlotType.highHex: 4,
            SlotType.lowCircle: 5, SlotType.lowSquare: 5, SlotType.lowHex: 5
        }
            # Generate a new set of planes with slots
            new_planes = [Plane(PlaneOrientation.XZ, slot_stock), Plane(PlaneOrientation.XY, slot_stock), Plane(PlaneOrientation.YZ, slot_stock)]
            #self.print_board(new_planes)
            #print("-----------------------------")

            # Validate the pegboard
            if self.validate_pegboard(new_planes):
                # If the pegboard is valid, update the planes list and break the loop
                self.planes = new_planes
                break

    def validate_pegboard(self, planes):
        conflicting_Slot_types = [1, 2, 3]
        
        leftPlane = planes[0]
        basePlane = planes[1]
        rightPlane = planes[2]

        # check base-left conflict 1
        if (leftPlane.slots[2][0].slot_type in conflicting_Slot_types) and (basePlane.slots[0][0].slot_type in conflicting_Slot_types):
            #print("failed at base - left 1 ")
            return False
        # check base-left conflict 2
        if (leftPlane.slots[2][1].slot_type in conflicting_Slot_types) and (basePlane.slots[0][1].slot_type in conflicting_Slot_types):
            #print("failed at base - left 2 ")
            return False
        # check base-left conflict 3
        if (leftPlane.slots[2][2].slot_type in conflicting_Slot_types) and (basePlane.slots[0][2].slot_type in conflicting_Slot_types):
            #print("failed at base - left 3 ")
            return False
        
        # check base-right conflict 1
        if (rightPlane.slots[2][0].slot_type in conflicting_Slot_types) and (basePlane.slots[0][2].slot_type in conflicting_Slot_types):
            #print("failed at base - right 1 ")
            return False
        # check base-right conflict 2
        if (rightPlane.slots[2][1].slot_type in conflicting_Slot_types) and (basePlane.slots[1][2].slot_type in conflicting_Slot_types):
            #print("failed at base - right 2 ")
            return False
        # check base-right conflict 3
        if (rightPlane.slots[2][2].slot_type in conflicting_Slot_types) and (basePlane.slots[2][2].slot_type in conflicting_Slot_types):
            #print("failed at base - right 3 ")
            return False
        
        # check left-right conflict 1
        if (leftPlane.slots[0][2].slot_type in conflicting_Slot_types) and (rightPlane.slots[0][0].slot_type in conflicting_Slot_types):
            #print("failed at base - right 1 ")
            return False
        # check left-right conflict 2
        if (leftPlane.slots[1][2].slot_type in conflicting_Slot_types) and (rightPlane.slots[1][0].slot_type in conflicting_Slot_types):
            #print("failed at base - right 2 ")
            return False
        # check left-right conflict 3
        if (leftPlane.slots[2][2].slot_type in conflicting_Slot_types) and (rightPlane.slots[2][0].slot_type in conflicting_Slot_types):
            #print("failed at base - right 3 ")
            return False
        
        return True  # If no conflicting slots found, pegboard is valid

    # Function to print the pegboard for visualization
    def print_board(self, planes):
        slot_symbols = {
            SlotType.highCircle: 'HC',
            SlotType.highSquare: 'HS',
            SlotType.highHex: 'HH',
            SlotType.lowCircle: 'LC',
            SlotType.lowSquare: 'LS',
            SlotType.lowHex: 'LH'
        }

        filled_symbol = "(X)"
        empty_symbol = "(_)"

        left_plane = planes[0]
        right_plane = planes[2]
        base_plane = planes[1]

        max_row_height = max(len(left_plane.slots), len(right_plane.slots), len(base_plane.slots))
        
        print("Left:\t\t\t\tRight:")
        for row in range(max_row_height):
            left_row_str = ""
            right_row_str = ""
            base_row_str = ""

            if row < len(left_plane.slots):
                for slot in left_plane.slots[row]:
                    slot_peg = filled_symbol if slot.peg else empty_symbol
                    left_row_str += slot_symbols[slot.slot_type] + slot_peg + " "
            
            if row < len(right_plane.slots):
                for slot in right_plane.slots[row]:
                    slot_peg = filled_symbol if slot.peg else empty_symbol
                    right_row_str += slot_symbols[slot.slot_type] + slot_peg + " "
            
            if row < len(base_plane.slots):
                for slot in base_plane.slots[row]:
                    slot_peg = filled_symbol if slot.peg else empty_symbol
                    base_row_str += slot_symbols[slot.slot_type] + slot_peg + " "

            print(left_row_str.ljust(30) + right_row_str)
        
        print("\nBase:")
        for row in range(len(base_plane.slots)):
            base_row_str = ""
            for slot in base_plane.slots[row]:
                slot_peg = filled_symbol if slot.peg else empty_symbol
                base_row_str += slot_symbols[slot.slot_type] + slot_peg + " "
            print(base_row_str)
        print("")