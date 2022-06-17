# define all the rooms
print ("Welcome to escape /THBACKROOMS room! The rooms are 11,3,2,12,19,")
print ("____________________________________________________")
room1 = (   
    11, #The room number
    "You have arrived at the start of wonders!", # greeting
    ["gun","cookies","raw potato"],# objects
    [ # doors
        ["N", 3, True], # direction, destination, is it locked
        ["E", 12, False],
         ["W", 10,True],
         ["S", 19,False]
         ]
    )
room2 = (
    3, #The room number
    "You have arrived at the OP armoury!", # greeting
    ["mini gon","Netherite armour","Netherite sword"],# objects
    [ # doors # direction, destination, is it locked
        ["W", 2, True],
        ["S", 11,False]
         ]
    )

room3 = (
    2, #The room number
    "You have arrived at not too bad", # greeting
    ["Light"],# objects
    [ # doors
         # direction, destination, is it locked
        ["E", 3, False]
                 ]
    )

room4 = (
    12, #The room number
    "You have arrived at the Terror room! What will you do?!", # greeting
    ["Killer_shark","bear","Key"],# objects
    [ # doors
        ["N", 4, False], # direction, destination, is it locked
        ["E", 13, False],
        ["W", 11, True],
        ["S", 20,False]
         ]
    )

room5 = (
    19, #The room number
    "You have arrived at the portals!", # greeting
    [""],# objects
    [ # doors
        ["N", 11, False], # direction, destination, is it locked
        ["E", 20, False],
        ["W", 18, True],
        ["S", 26,False]
         ]
    )

# dictionary for all my rooms
rooms = {
    11: room1,
    3: room2,
    2: room3,
    12: room4,
    19: room5,
      }
def show_room(room):
    global inventory
    
    (number, greeting, objects, doors) = room
    # print the greeting
    print(greeting)
    print ("________________________________")
    #list inventory
    print ("You have the following items:")
    for item in inventory:
        print("* " + item)
    print()
    #list any objects
    
    print ("You see the following items:")
    for item in objects:
        print ("* " + item)
    print ()
    # list the exits
    print ("You see the following exits:")
    for door in doors:
        (direction, dest, locked) = door
        if locked:
            print ("* " + direction + "(locked)")
        else:
                print("* " + direction)
    print ()
        
def go(direction):
    """
    FOR DEV PPL
    Moves from the current room.
    Parameters:
    __________
    direction(string) The direction to move (N,E,E,S)
    Updates the current_room if move is invalid
    """
    global current_room
    doors = current_room[3]
    #doors[3] = False
    
    # doors is a list that looks like this:
    #("N", 3, True),    ("E", 12, False),
    for door in doors:
        #(door_direction, destination, locked) = door
        door_direction = door[0]
        destination = door[1]
        locked = door[2]
        if door_direction.lower() == direction.lower():
            if locked:
                print ("That door is loocked! NOO ENTRY!............................")
                print()
                return
            else:
                current_room = rooms[destination]
                return
            print ("Sorry,you can't go that way.")

def take(thing):
    """
    Takes an object - remove it from room, and add it to inventory
    Parameters:
    ___________
    thing (str): the objact to take
    """
    global current_room
    global inventory

    #TODO:check if the item is in the room
    objects = current_room[2]
    if (thing in objects):
        #TODO:add it to invintory
        objects.remove(thing)
        inventory.append(thing)
        if thing.lower() == "killer_shark":
            print("He eats you as you get acid over you and get demolished nomnomnom... Gets aLt F4d Muahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahaha Thank You for wasting your time triying to take a bear... ")
            exit()
            
        if thing.lower() == "bear":
            print("He eats you as you get acid over you and get demolished nomnomnom... Gets aLt F4d Muahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahahahahahahahahahahahahahahahahaahahahahahahhahahahahahahahahaha Thank You for wasting your time triying to take a bear...")
            exit()
   
    else:
        #TODO:warn user item is not inr room
        print ("I don't see one of those around here.")
        
        
def unlock():
    """
    Unlocks all the doors
    """
    global current_room
    doors =  curent_room[3]
    for door in doors:
        #TODO unlock the doors
        (direction, destination, locked) = door
        new_door = (direction, destination,False)
    
        
        

def use (thing):
    """
    uses the specified thing in the current room.
    Parameters:
    ____________
    thing (str): The thing to use
    """
    global inventory
    global current_room
    #TODO: check that thing is in inventory
    if (thing in inventory):
        #TODO: an if statment for each supported things
        if thing == "gun":
            print ("GUN GO BANG" )
        elif thing == "Key":
            unlock()
        elif thing == "cookies":
            print ("COOKIES CHOCO\ATE CHIP Get it?")
        elif thing == "raw_potato":
            print ("POTATO GOES FRIIIIE MEEEEEEEEEEEEEEEEEEEEEEEEEEEEHH")
            
        else:
           #TODO: wrn user that they don't have th e object
           print ("You don't have one of those")
           print ()
               
            
       
current_room = rooms[11]

inventory = []

while True:
    show_room(current_room)
    cmd = input ("Enter command: >")
    bits = cmd.split(' ')
    action = bits[0]
    qualifier = bits[1]
    print ("Action:" + action)
    print ("Qualifier:" + qualifier)
    action = action.lower()
    if action == "go":
        go(qualifier)
    elif action == "take":
        take(qualifier)
    elif action == "use":
        pass
    else:
        print ("Invalid command no hacking allowed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'_'")
        print("______________________________________________________________________________________________")