class WheelOfMisfortune():
  import random
# Nathan sent this to me, this is his, I just moved the items around.
  wheelOptions = [500,"Bankrupt!",1000,800,800,"Bankrupt!",500,700,550,500,"Bankrupt!",3500,500,550,"Free Play!",500,600,600,700,"Bankrupt!",700,700,5000,5000,"Lose A Turn!",1000000,"Bankrupt!",800,800,700,"Free Play!",700,900,900,900,800,800,"Bankrupt!",800,650,650,700,700,600,600,550,"Lose A Turn!",550,650,650,"Bankrupt!",900,900,800,800,"Free Play!",3500,5000,1000,700,900,1000,3500,"Lose A Turn!",650,650,550,550,"Bankrupt!",500,600,600]

#   **Important**
#Move all of these functions inside of the spinTheWheel Function.
#   **Important**


  #Function for if the wheel 'lands' on the 'Free Play' option.
  def freePlay():
    free==True
    while free==True:
      vowelPrice==0
      letterPrice==0
      if vowelPick==True:
        free==False


  #Function for if the wheel 'lands' on the "Bankrupt" option.
  def bankrupt(playerScore,playerTurn):
    if playerTurn==0:
      p1Score==0
    elif playerTurn==1:
      p2Score==0
    elif playerTurn==2:
      p3Score==0


  #Function that switches to the next person's turn.
  def nextTurn(playerTurn): #also works the Lose a turn function.
    if playerTurn<=3:
      playerTurn+=1
    elif playerTurn>=3:
      playerTurn==0


  #Function that randomly selects an item from the list of wheel options.
  def spinTheWheel(wheelOptions): 
    wheelOutput=random.choice(wheelOptions)# https://pynative.com/python-random-choice/
    if wheelOutput=='Free Play!':
      freePlay()

    elif wheelOutput=='Bankrupt!':
      bankrupt(playerScore)

    elif wheelOutput=='Lose a Turn!':
      nextTurn(playerTurn)

    elif wheelOutput=="One Million!":
      millionOutput=random.choice(millionList)
      if millionOuput=1000000:
        playerScore+=1000000
      elif millionOutput=500:
        playerScore+=500

    elif wheelOutput==int:
      playerScore+=wheelOutput

#class Probability:
  #https://www.dataquest.io/blog/basic-statistics-in-python-probability/