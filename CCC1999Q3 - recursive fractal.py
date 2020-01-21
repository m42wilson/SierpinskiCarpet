#The premise is to generate a fractal when given a number n.
#The fractal is made of the '*' character and is a sierpinski carpet.
#The number of columns and rows of '*'s are equal, and both are
#calculated as 3^n.

#give to Fractal the board, as a list of strings
#If I have a 9x9 board:
#["*********","*********","*********","*********","*********","*********","*********","*********","*********"]
#I want it to become 9 3x3 boards. This is the first step.

#[["***","***","***"],["***","***","***"],["***","***","***"],["***","***","***"],["***","***","***"],
#["***","***","***"],["***","***","***"],["***","***","***"],["***","***","***"]]

#Next, repace the fifth, (#4) subsection of n/3 x n/3 with n/3 lines, n/3 spaces long


#divideBoard needs to output 3 lists of n/3 by n/3 boards, giving it n/3 1 by n long boards
#I give it 9 27-long rows, I get 3 lists of 9x9 boards.
def divideBoard(rows):
    output = []
    hold = []
    for i in range(len(rows)):
        hold.append(rows[i][:len(rows[i])/3])
    output.append(hold)
    hold = []
    for i in range(len(rows)):
        hold.append(rows[i][len(rows[i])/3:2*(len(rows[i])/3)])
    output.append(hold)
    hold = []
    for i in range(len(rows)):
        hold.append(rows[i][2*(len(rows[i])/3):])
    output.append(hold)
    return output

#Takes 9 boxes and turns it back into an arbitrary number of strings
def reconstruct(boxes):
    #input is 9 n by n boxes. No idea how long.
    #it becomes 3n 1 by 3n lines.
    output = []
    hold = ""
    #This is for each set of 3 boxes
    for j in range(3):
        #now, for each set of three, we need to 
        for i in range(len(boxes[0])):
            hold = ""
            for k in range(3):
                hold += boxes[3*j+k][i]
            output.append(hold)

    return output
def Fractal(board):
    #print len(board)
    #print board
    if len(board[0]) >= 3:
        hold1 = divideBoard(board[:len(board)/3])
        hold2 = divideBoard(board[len(board)/3:2*(len(board)/3)])
        hold3 = divideBoard(board[2*(len(board)/3):])
        #this is a list of lists, not a list of three lists of lists. Is that right? yup.
        board = [hold1[0],hold1[1],hold1[2],hold2[0],hold2[1],hold2[2],hold3[0],hold3[1],hold3[2]]

        #Once the board is divided into 9, we perform Fractal on each of the 9 boxes.
        #If the box is the center one, we don't need to, and set it to blank.
        for i in range(9):
            if i != 4:
                board[i] = Fractal(board[i])

            else:
                board[i] = len(board[i]) * [len(board[i][0])*" "]
      #  print board
        #When I return board, I want it to be in the same format in which I got it.
        #yay, new Function! oh wait, that's not a yay.
        
        return reconstruct(board)
    else:
        #in this case, board will always equal "*", but this works for debugging.
        return board

#-------------------------------------------------------------------------------------------------
#this is just to print the fractal for fun. Comment it out to run the contest input and see
#the cut-out fractals.
while True:
    n = input("please input a number n. The fractal will be 3^n by 3^n. 3 or 4 is recommended.")
    enter = (3**n)*[(3**n)*"*"]
    almost = Fractal(enter)
    for i in almost:
        for j in i:
            print j,
        print
    print
    print
#-------------------------------------------------------------------------------------------------

textfile = open ("D:\Coding\Contest\Reference\Data\CCC 1999\Windows\drac.in")
d = int(textfile.readline())
textfile.readline()
for we in range(d):
    n = int(textfile.readline())
    textfile.readline()
    b = int(textfile.readline())
    #in a 9x9 square, this turns a bottom of 3 to a bottom of 6,
    #which is exactly what we need to index it. Same goes for top.
    b = 3**n - b
    textfile.readline()
    t = int(textfile.readline())
    t = 3**n - t
    textfile.readline()
    l = int(textfile.readline())
    textfile.readline()
    r = int(textfile.readline())
    textfile.readline()

#    if we == 1:
 #       continue

    enter = (3**n)*[(3**n)*"*"]

    almost = Fractal(enter)
#the boundaries for the print are a bit broken. Can fix later.
    for i in range(len(almost)):
        if i >= t and i <= b:
            for j in range(len(almost[i])):
                if j+1 >= l and j+1 <= r:
                    print almost[i][j],
            print

    print
    print 
