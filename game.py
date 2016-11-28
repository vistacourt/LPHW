def back_room():
    print ""

def bathroom():
    print ""

def kitchen():
    print ""

def front_yard():
    print ""

def  hallway():
    print ""
    print "You are in a small hallway."
    print "You can go to the kitchen,  bathroom or back room from here."


def side_house():
    print ""
    print "you are outside on the side of the house."



def bedroom():
    print ""
    print "You are in your bedroom."
    print "There is a door on the right."
    print "There is a window on the left."
    print "which way? (door/window)"

    choice = raw_input("> ")

    if choice == "door":
        hallway()
    elif choice == "window":
        side_house()
    else:
        print "What don't you understand about (door/window)?"
        bedroom()



def lazy():
    print ""
    print "Yeah, getting up would take too much energy."
    print "Press enter when you are ready."
    raw_input("> ")
    start()

def start():
    print""
    print "You are in the bedroom, laying on the bed."
    print "The Bravo Network is on TV."
    print "You're husband, Tom, is next to you on the bed programming on\
    his computer as usual."
    print "There are three puppies on the bed: Jill, Jack and Jet."
    print "The fourth puppy, Dodo, is missing!"
    print "Do you want to get up and find her? (y/n)"

    choice = raw_input("> ")

    if choice == "y":
        bedroom()
    elif choice == "n":
        lazy()
    else:
        print ""
        print "Can't you read? I said (y/n)!"
        print "Press enter when you are ready"
        raw_input("> ")
        start()

start()
