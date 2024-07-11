import re

def get_move():
    coords = input("What is your move? (Write two digits Row then Column like '02'): ")

    if(not coords.isdigit()):
        print("Please only input numbers")
        return
    elif(len(coords) != 2):
        print("Please only input 2 digits")
        return
    elif(not bool(re.match(r'^[0-2]{2}$', coords))):
        print("Please only put numbers 0-2")
        return
    

    array_coords = [int(coord) for coord in coords]
    
    print(array_coords)