import random
#Function to print out the board
# Board box pieces are from https://en.wikipedia.org/wiki/Box-drawing_character
def printBoard(board):
  l=" │ "
  d="━━━┼"
  e="───┼"
  #Prints the row title and numbers
  print("  col:"+1*" "+"1"+3*" "+"2"+3*" "+"3"+3*" "+"4"+3*" "+"5"+3*" "+"6"+3*" "+"7"+3*" "+"8")
  #Prints column title and top edge of board
  print("row: "+"┌"+3*((3*"─"+"┬")+(3*"━"+"┬"))+(3*"─"+"┬")+3*"━"+"┐")
  #Prints the sections of the rows, and the numbers beside them, with the actual array part of the board to allow pieces to move and be placed
  for r in range(8):
    print(3*" "+str(r+1)+l+board[r][0]+l+board[r][1]+l+board[r][2]+l+board[r][3]+l+board[r][4]+l+board[r][5]+l+board[r][6]+l+board[r][7]+l)
     #Prints the row seperator lines
    if (r==0 or r==2 or r==4 or r==6):
      print(3*" "+"~"+1*" "+"├"+d+e+d+e+d+e+d+"───┤")
    elif (r==1 or r==3 or r==5):
      print(3*" "+"~"+1*" "+"├"+e+d+e+d+e+d+e+"━━━┥")
    #Prints the bottom edge of board
    elif (r==7):
      print(5*" "+"└"+3*((3*"─"+"┴")+(3*"━"+"┴"))+(3*"─"+"┴")+3*"━"+"┘")
      print(" ")
#Function that spawns all 24 starting pieces onto the board in their respective spots
def spawnStartingPieces(blackPiece,whitePiece,board):
  columnList=[1, 3, 5, 7, 0, 2, 4, 6, 1, 3, 5, 7, 0, 2, 4, 6, 1, 3, 5, 7, 0, 2, 4, 6]
  rowList=[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7] 
  blackPiece="■"
  whitePiece="□"
  for i in range(len(rowList)):
    if i < 12:
      r = rowList[i]
      c = columnList[i]
      blackPiece="■"
      board[r][c]=blackPiece
    if i >= 12:
      r = rowList[i]
      c = columnList[i]
      whitePiece="□"
      board[r][c]=whitePiece
#Main Function that runs the game
def checkersMain():
  #Section for defining all the variables beforehand, so the computer doesn't tell you 'No'
  board=[[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
  start=""
  r=""
  c=""
  r2=""
  c2=""
  newR=int()
  newC=int()
  blackPiece="■"
  whitePiece="□"
  gameOver=False
  turn=0
  start=input("Hello, and welcome to the Checkers v1.0.  Would you like to start?\n  1.) Type 'start' to start the program\n  2.) Type 'quit' at any time to quit the program\n\nType here: ")
  if start == "start":
    spawnStartingPieces(blackPiece,whitePiece,board)
  if start == "start":
    while r!="quit" or c!="quit" or r2!="quit" or c2!="quit" and gameOver!=True:
      #Sets up and prints the board before game begins
      printBoard(board)
#Function that allows for the White Team's pieces to move, and checks the legallity of the requested movement.
      if turn % 2==0:
       print("It is the White team's turn, which piece do you want to move? \nType in the row and column number of the piece you want to move to continue.\n    Reminder: you can type 'quit' at any time to quit the program")
       r = int(input("row: "))-1
       c = int(input("column: "))-1
       if board[r][c]==whitePiece:
         print("\nEnter where you would like to move it to.")
         r2 = int(input("row: "))-1
         c2 = int(input("column: "))-1
         if board[r2][c2]==" " and c2==r-1 and r2==r+1 or r-1:
           board[r][c]=" "
           board[r2][c2]=whitePiece
           turn+=1
           printBoard(board)
         elif board[r2][c2]!=" ":
            print("another piece already already occupies movement coordinates, please try again.")
         elif not(c2==r-1 and r2==r+1 or r-1):
           print("movement coordinates outside of range, please try again and only use numbers 1-8.")
       elif board[r][c]!=whitePiece: 
         print("No piece in that spot, please try again.")
       else:
         print("Invalid input, please try again.")
#Function that allows for the Black Team's pieces to move, and checks the legallity of the requested movement.
      if turn % 2==1:
       print("It is the Black team's turn, which piece do you want to move? \nType in the row and column number of the piece you want to move to continue.\n    Reminder: you can type 'quit' at any time to quit the program")
       r = int(input("row: "))-1
       c = int(input("column: "))-1
       if board[r][c]==blackPiece:
         print("\nEnter where you would like to move it to.")
         r2 = int(input("row: "))-1
         c2 = int(input("column: "))-1
         if board[r2][c2]==" " and c2==r-1 and r2==r+1 or r-1:
           board[r][c]=" "
           board[r2][c2]=blackPiece
           turn+=1
           printBoard(board)
         elif board[r2][c2]!=" ":
           print("another piece already already occupies movement coordinates, please try again.")
         elif not(c2==r-1 and r2==r+1 or r-1):
           print("movement coordinates outside of range, please try again and only use numbers 1-8.")
       elif board[r][c]!=blackPiece: 
         print("No piece in that spot, please try again.")
       else:
         print("Invalid input, please try again.")
checkersMain()