def Player(move):
    
    movementInput = move
    global y
    global x
  
    if movementInput == forward or movementInput == backwards or movementInput == left or movementInput == right:
        
        if movementInput == forward:
            y = y + 1
        elif movementInput == backwards: 
            y = y - 1
        elif movementInput == left:   
            x = x - 1
        elif movementInput == right:
            x = x + 1 
    else:
        print("Invalid input.  Try again.")

# Checks for win and resets x and y to 0 if so
def Finish():

    global x
    global y
    global finishLine

    if finishLine == True:
        
        x = 0
        y = 0
        yList = []
        xList = []
        print("You found the exit.  Congrats!")


def Outside_Border(move):

    global x
    global y

    print()
    print("Object position: ", x, y)

    if move == right:
        x = x - 1
    elif move == left:
        x = x + 1
    elif move == forward:
        y = y - 1
    elif move == backwards:
        y = y + 1

    print()
    print("You hit an object")
    Position()

def Position():

    global x
    global y
    print("Your position: ", x, y)

def Path_Blocks(xcoord, ycoord):

    global xList
    global yList

    xList.append(xcoord)
    yList.append(ycoord)

def Room_One(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = False

    # size of room.
    sizeX = 3
    sizeY = 3

    # x and y coords that are blocked.  Player can't go over these.
    Path_Blocks(2,2)
    Path_Blocks(1,1)

    # exit
    endX = 3
    endY = 3
    
    while finishLine == False:

        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)

        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)

        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)
            
        Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()
            

def Room_Two(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = False
    
    # size of room.
    sizeX = 5
    sizeY = 5

    # exit
    endX = 1
    endY = 4

    #blocks
    Path_Blocks(0,2)
    Path_Blocks(1,2)
    Path_Blocks(2,2)
    
    while finishLine == False:

        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)
        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)
        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)
		
	    Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()
    

def Room_Three(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = False
    
    # size of room
    sizeX = 5
    sizeY = 5

    # exit
    endX = 5
    endY = 5

    # blocks
    Path_Blocks(1,5)
    Path_Blocks(2,4)
    Path_Blocks(3,3)
    Path_Blocks(4,2)
    
    while finishLine == False:

        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)

        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)
            

        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)

		Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()

def Room_Four(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = FalsefinishLine = False

    # size of room
    sizeX = 7
    sizeY = 7

    # exit
    endX = 3
    endY = 3
    
    while finishLine == False:

        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)

        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)
            
        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)

	    Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()

def Room_Five(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = False
    
    # size of room
    sizeX = 3
    sizeY = 3

    # exit
    endX = 3
    endY = 3
    
    while finishLine == False:
        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)

        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)
            

        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)

		Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()

def Room_Six(move):

    global x
    global y
    global finishLine
    global xList
    global yList

    finishLine = False
    
    # size of room
    sizeX = 5
    sizeY = 5

    # exit
    endX = 3
    endY = 4
    
    while finishLine == False:
        for (xWall, yWall) in zip(xList, yList):
            if x == xWall and yWall == y:
                print("You have hit an object.")
                Outside_Border(move)

        # Checks if player is at the edge of the room
        if x > sizeX or y > sizeY:
            print("You have reached the edge of the room.")
            Outside_Border(move)

        # Checks if the player is trying to go in to the negatives on the x and y axis
        elif x < 0 or y < 0:
            print("You have reach the edge of the room.")
            Outside_Border(move)
            
        
        else:
            move = input("You are allowed to move now.  Enter a direction.")
            Player(move)

		Position()
        # checks if player reached the end
        if endX == x and endY == y:
            finishLine = True
            Finish()


forward = 'w'
left = 'a'
backwards = 's'
right = 'd'

finishLine = False

xList = []
yList = []


# h is just a placeholder.  Does nothing.
move = 'h'

y = 0
x = 0

print("How to play: ")
print("w = FORWARD    a = LEFT    s = BACKWARD    d = RIGHT")
print("The goal of the game is to find the exit in each room.  You start in each room at x = 0 and y = 0.")

print()
    
print("You have reached the first room.  There is a pillar in the center of the room.  Find a way around it to find the exit.")
print("Hint: The pillar in this case would be located at (2, 2) and (1, 1).  The room is quite small.")
print("You move 1 each time you move.")
Room_One(move)

print()
print("You have reached the second room.  There's a couch in front of you and stairs that look like the exit are behind the couch.")
Room_Two(move)

print()
print("You have reached the thrid room.  The exit is in the opposite corner from you.  There's an large object blocking over half the room.")
Room_Three(move)

print()
print("Fourth room.")
Room_Four(move)

print()
print("Fifth room.")
Room_Five(move)

print()
print("Sixth room.")
Room_Six(move)


