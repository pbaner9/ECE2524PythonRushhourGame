#this documents containing functions relating to the movement of game pieces
#created by Noah Davis & Pia Banerjee

#this function translates user inputs into machine readable variables
def move(endpos, piece, pos, direction):
        distance = posDistance(piece, pos)
        endEndPos = endpos + distance
        #put old values into grid
        for i in range (0,36):
                if pos[i] == piece:
                        pos[i]= '  '
        #add new values into grid
        if (direction == 'vertical'):
                for i in range (endpos, endEndPos, 6):
                    pos[i] = piece
        elif direction == 'horizontal':
                for j in range (endpos, endEndPos):
                    pos[j] = piece
        else:
                print ("Something is wrong")
        return pos

#converts user data to machine data
def readUser(ans):
    if ans == 'Aa':
        return 0
    elif ans == 'Ba':
        return 1
    elif ans == 'Ca':
        return 2
    elif ans == 'Da':
        return 3
    elif ans == 'Ea':
        return 4
    elif ans == 'Fa':
        return 5
    elif ans == 'Ab':
        return 6
    elif ans == 'Bb':
        return 7
    elif ans == 'Cb':
        return 8
    elif ans == 'Db':
        return 9
    elif ans == 'Eb':
        return 10
    elif ans == 'Fb':
        return 11
    elif ans == 'Ac':
        return 12
    elif ans == 'Bc':
        return 13
    elif ans == 'Cc':
        return 14
    elif ans == 'Dc':
        return 15
    elif ans == 'Ec':
        return 16
    elif ans == 'Fc':
        return 17
    elif ans == 'Ad':
        return 18
    elif ans == 'Bd':
        return 19
    elif ans == 'Cd':
        return 20
    elif ans == 'Dd':
        return 21
    elif ans == 'Ed':
        return 22
    elif ans == 'Fd':
        return 23
    elif ans == 'Ae':
        return 24
    elif ans == 'Be':
        return 25
    elif ans == 'Ce':
        return 26
    elif ans == 'De':
        return 27
    elif ans == 'Ee':
        return 28
    elif ans == 'Ef':
        return 29
    elif ans == 'Af':
        return 30
    elif ans == 'Bf':
        return 31
    elif ans == 'Cf':
        return 32
    elif ans == 'Df':
        return 33
    elif ans == 'Ef':
        return 34
    elif ans == 'Ff':
        return 35
    else: 
        print ("You enterd the wrong command")
        return -1

#this function finds the size of the cars
def posDistance(piece, pos):    
    isBegin = True
    
    #scans the list for car pieces of the same type
    for i in range(0, 36):
        if piece == pos[i]:
            #end is only tracked once
            if isBegin == True:
                isBegin = False
                begin = i 
            end = i+1 
    
    #finds the distance between the beginning of the car and end
    #finds how large the car is
    distance = end - begin
    
    return distance
    
#this function finds the direction of the cars
def carDirection(piece, pos):
    distance = posDistance(piece, pos)
    if distance < 6:
        return 'horizontal'
    else :
        return 'vertical'

#checking position for moving piece into 
def correctMove (endpos, piece, pos):
    carLength = 0
    canMove = True
    
    #finds the starting position and length of the car
    for i in range (0,35):
        if piece == pos[i]:
            startpos = i
            carLength = carLength +1

    #finds the direction of the car
    direction = carDirection (piece, pos)

    #if it is horizontal it can only move horizontally
    #and if it is vertical it can only move vertically
    if direction == 'horizontal':
        if (endpos < horizontalMin(startpos)) or (endpos > horizontalMax(startpos)):
            print ("Piece can only move horizontal")
            canMove = False
    else:
        #all elements in a row have the same remainder
        if (endpos%6) != (startpos%6):
            print ("Piece can only move vertical")
            canMove = False

    #checks if other pieces are in the way
    if direction == 'horizontal':
        for i in range (startpos,(endpos+carLength) ):
            if (pos[i] == '  ') or (pos[i] == piece):
                canMove = canMove
            else:
                canMove = False
    elif direction == 'vertical':
        for i in range (startpos,(endpos+(carLength*6)), 6):
            if (pos[i] == '  ') or (pos[i] == piece):
                canMove = canMove
            else:
                canMove = False

    #if no pieces are in the way the piece is moved
    if canMove == True:
        output = move(endpos, piece, pos, direction)
        return output
    else:
        print ("Piece cannot move here!")
        return pos

#checks that the piece is only moving horizontal
def horizontalMax(startpos):
   if 0 <= startpos <= 5:
       return 5
   elif 6 <= startpos <= 11:
       return 11
   elif 12 <= startpos <= 17:
       return 16
   elif 18 <= startpos <= 23:
       return 23
   elif 24 <= startpos <= 29:
       return 29
   else:
       return 35

def horizontalMin(startpos):
   if 0 <= startpos <= 5:
       return 0
   elif 6 <= startpos <= 11:
       return 6
   elif 12 <= startpos <= 17:
       return 12
   elif 18 <= startpos <= 23:
       return 18
   elif 24 <= startpos <= 29:
       return 24
   else:
       return 30

    
    
