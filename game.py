import os
from graphics import logo

os.system("cls"), logo()

def family_room():
    os.system("cls"), logo()
    print ""
    print "You are in the family room."
    print "There is a piano, a fireplace, table, couch and TV."
    print "There is poop on the floor from Jet."
    print "Tom has more computer shit on the table."
    print "You can see the kitchen behind you."
    print "Through the craftsman windows, is the front porch."
    print ""
    print "(kitchen/porch)"
    print ""
    choice = raw_input("> ")

    if choice == "kitchen":
        kitchen()
    elif choice == "porch":
        porch()
    else:
        print "Please choose one of these: (kitchen/porch)"
        family_room()

def back_room():
    os.system("cls"), logo()
    print ""
    print "This is where homeless items from around the house goes."
    print "This house is 'homeless item friendly'."
    print "Unless you are looking for something other than Dodo, you should leave."
    print "Press Enter to leave now."
    print ""
    print "(Enter)"
    raw_input()
    hallway()

def porch():
    os.system("cls"), logo()
    print ""
    print "The porch is the best place to view Robert Ettleman's front door."
    print "It's been reported that the door was in fact, stolen from him."
    print "You can open the door to the family room or go to the " \
          "front yard and admire Bob's door some more."
    print "Choice?"
    print ""
    print "(door/yard)"

    print ""
    choice = raw_input("> ")

    if choice == "door":
        family_room()
    elif choice == "yard":
        front_yard()
    else:
        print "Please choose one of these: (left: laundry room / right: family room)"
        porch()

def patio():
    os.system("cls"), logo()
    print ""
    print "The covered patio is filled with awesome computers and electronics."
    print "It's where the great computer scientist, Tom Kelly, creates greatness."
    print "But that's another story."
    print "There is poop on the ground from Jet."
    print "beep beep click click beep beep."
    print "You can go to the front yard from here or go back to the laundry room."
    print ""
    print "(front/laundry)"

    print ""
    choice = raw_input("> ")

    if choice == "front":
        front_yard()
    elif choice == "laundry":
        laundry_room()
    else:
        print "Nope... one of these: (front/laundry)"
        patio()

def street():
    os.system("cls"), logo()
    print ""
    print "LOOK OUT! "
    print "There is Peter Carlson and Coral Weston!"
    print "Hurry back to the front yard!"
    print "Press Enter to escape the neighborhood gossip immediately."
    print ""
    print "(Enter)"
    raw_input()
    front_yard()

def laundry_room():
    os.system("cls"), logo()
    print "\n"
    print "This laundry room is filled with clothes and laundry items.\n"
    print "There is piss on the floor from Jack\n"
    print "You can see the covered patio outside and the kitchen is behind you.\n"
    print "(patio/kitchen)?\n"
    choice = raw_input("> ")

    if choice == "patio":
        patio()
    elif choice == "kitchen":
        kitchen()
    else:
        print "\n"
        print "It's simple\n"
        print "Either go outside to the covered patio or back to the kitchen\n"
        print "Try again (patio/kitchen)\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        laundry_room()


def bathroom():
    os.system("cls"), logo()
    print "\n"
    print "Yup, it's a bathroom.\n"
    print "There is piss on the ground from Jack.\n"
    print "You can stop here and rest or go back to the hallway.\n"
    print "Press enter when you are ready.\n\n"
    print "(Enter)\n\n"
    raw_input("> ")
    hallway()

def kitchen():
    os.system("cls"), logo()
    print "\n"
    print "The kitchen is kinda small but it's got everything you needn"
    print "From here you can see the laundry room and the front door in the family room to the right.\n"
    print "Enter the laundry room, front door in the family room or the hallway.\n\n"
    print "(laundry/door/hallway)\n\n"
    choice = raw_input("> ")

    if choice == "laundry":
        laundry_room()
    elif choice == "door":
        family_room()
    elif choice == "hallway":
        hallway()
    else:
        print "\n"
        print "Please choose one of these: (laundry/door/hallway)\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        kitchen()

def front_yard():
    os.system("cls"), logo()
    print "\n"
    print "The front yard looks nice, Manny always keeps the lawn cut.\n"
    print "You can see your house and you like it.\n"
    print "Lot's of choices here.\n"
    print "You can exit to the street through the gate.\n"
    print "You can cross the lawn to the side gate and enter the covered patio.\n"
    print "You can walk to the front porch.\n"
    print "Or you could just go back to the side of the house.\n"
    print "Your thoughts? \n\n"
    print "(street/patio/porch/window)\n\n"
    choice = raw_input("> ")

    if choice == "street":
        street()
    elif choice == "patio":
        patio()
    elif choice == "porch":
        porch()
    elif choice == "window":
        side_house()
    else:
        print "\n"
        print "Please choose one of these: (street/patio/porch/window)\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        front_yard()

def  hallway():
    os.system("cls"), logo()
    print "\n"
    print "You are in a small hallway.\n"
    print "You can go to the kitchen, bathroom or back room from here.\n"
    print "Which way? \n\n"
    print "(kitchen/bathroom/back)\n\n"
    choice = raw_input("> ")

    if choice == "kitchen":
        kitchen()
    elif choice == "bathroom":
        bathroom()
    elif choice == "back":
        back_room()
    else:
        print"\n"
        print "Choose one of these three (kitchen/bathroom/back)\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        hallway()

def side_house():
    os.system("cls"), logo()
    print "\n"
    print "You are outside on the side of the house.\n"
    print "there is an air conditioning unit and an old meat smoker here.\n"
    print "You can walk around the hedges to the front yard or go back in the window that Tess fixed once.\n"
    print "Which way? \n\n"
    print "(front/window)\n\n"
    choice = raw_input("> ")

    if choice == "front":
        front_yard()
    elif choice == "window":
        bedroom()
    else:
        print "\n"
        print "Please choose one of these: (front/window)\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        side_house()

def bedroom():
    os.system("cls"), logo()
    print "\n"
    print "You are in your bedroom.\n"
    print "There is a door on the right.\n"
    print "There is a window on the left.\n"
    print "which way? \n\n"
    print "(door/window)\n\n"
    choice = raw_input("> ")

    if choice == "door":
        hallway()
    elif choice == "window":
        side_house()
    else:
        print "\n"
        print "What don't you understand about (door/window)?\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        bedroom()

def lazy():
    os.system("cls"), logo()
    print "\n"
    print "Yeah, getting up would take too much energy.\n"
    print "Press enter when you are ready.\n\n"
    print "(Enter)\n\n"
    raw_input("> ")
    start()

def start():
    os.system("cls"), logo()
    print"\n"
    print "You are chilling out at home, laying on your bed.\n"
    print "The Bravo Network is on TV.\n"
    print "You're husband, Tom, is next to you on the bed programming on " \
          "his computer as usual.\n"
    print "There are three puppies on the bed: Jill, Jack and Jet.\n"
    print "The fourth puppy, Dodo, is missing!\n"
    print "Do you want to get up and find her? \n\n"
    print "(y/n)\n\n"
    choice = raw_input("> ")

    if choice == "y":
        bedroom()
    elif choice == "n":
        lazy()
    else:
        print "\n"
        print "Can't you read? I said (y/n)!\n"
        print "Press enter when you are ready.\n\n"
        print "(Enter)\n\n"
        raw_input("> ")
        start()
start()
