# Cody Conaty

def movement(location, direction, rooms):
    # movement func.
    location = rooms[location][direction]
    return location

def get_item(location, direction, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[location]['Item'])
    del rooms[location]['Item']

def instructions():
    print('Welcome to the Dragon Themed Adventure Game.')
    print("You must collect all SIX items to win the game.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'Item Name'" )



def main():
    rooms = {
        'Main Dining': {'North': 'Armory', 'South': 'Living Quarters', 'East': 'Great Library', 'West':
            'Wizards Landing', },
        'Armory': {'South': 'Main Dining', 'East': 'Dungeon', 'Item': 'Sword'},
        'Dungeon': {'West': 'Armory', 'Item': 'Daggers'},
        'Wizards Landing': {'East': 'Main Dining', 'Item': 'Potion'},
        'Living Quarters': {'North': 'Main Dining', 'East': 'Kitchen', 'Item': 'Armor'},
        'Kitchen': {'West': 'Living Quarters', 'Item': 'Cheese'},
        'Courtyard': {'South': 'Great Library', 'Item': 'DRAGON!!!!'},
        'Great Library': {'North': 'Courtyard', 'West': 'Main Dining', 'Item': 'Book'}
    }

    # Setting direction, location, inventory, etc.
    direction = ""
    location = 'Main Dining'
    inventory = []
    # Main Menu Function :)
    instructions()

    while True:
        if location == 'Courtyard':
            if len(inventory) == 6:
                print('YOOO! You have beaten the game! That is fire.')
                print('Thanks for playing homie.')
                break
            else:
                print('\nBruh. You literally didnt collect all the items.')
        print('You are in ' + location)
        print(inventory)
        if location != 'Courtyard' and 'Item' in rooms[location].keys():
            print("You see the {}".format(rooms[location]['Item']))
        possible_moves = rooms[location].keys()
        print('Your possible moves are', *possible_moves)
        direction = input('Enter your direction: ').title().split()

        if len(direction) >= 2 and direction[1] in rooms[location].keys():
            location = movement(location, direction[1], rooms)
            continue
        elif len(direction[0]) == 3 and direction[0] == 'Get' and ' '.join(direction[1:]) in rooms[location]['Item']:
            print('You pick up the {}'.format(rooms[location]['Item']))
            print('------------------------------')
            get_item(location, direction, rooms, inventory)
            continue
        else:
            print('Invalid command, please try again.')
            continue

main()