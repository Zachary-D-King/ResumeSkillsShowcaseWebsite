def wheelOfFortuneMain():
  gameOver=False
  while gameOver!=True:
    print("")



#Function that asks the user if they would like to start the program, introduces the game and hosts, then introduces the three contestants.
start=input("Would you like to initiate the Wheel of Fortune program?\n    Type 'start' to start the program.\n    Type 'quit' to quit the program.\nEnter: ")
while start!='quit':
  if start=="start":
    #Introduction to game.
    print("Hello, and welcome to America's game, Wheel!... Of!... Fortune!*Applause*I'm your host, SHAFT, and joining me is literally Master Chief from the Halo Franchise! Now for our contestants!\n ")
    print("*Reminder: Do not leave the questions blank please.*\n")
    #Intro questions for contestants.
    p1Name=input("What's your name, player one?\n ")
    if p1Name!="":
      p1Living=input("Where do you live "+str(p1Name)+"?\n ")
      if p1Living!="":
        p1Job=input("What do you do "+str(p1Name)+"?\n ")
        if p1Job!="":
          p2Name=input("What is your name, player two?\n ")
          if p2Name!="":
            p2Living=input("Where do you Live "+str(p2Name)+"?\n ")
            if p2Living!="":
              p2Job=input("what do you do "+str(p2Name)+"?\n ")
              if p2Job!="":
                p3Name=input("What is your name, player three ?\n ")
                if p3Name!="":
                  p3Living=input("Where do you live "+str(p3Name)+"?\n ")
                  if p3Living!="":
                    p3Job=input("What do you do "+str(p3Name)+"?\n ")
                    if p3Job!="":
                      wheelOfFortuneMain()
                    else:
                      print("Reminder: Do not leave the questions blank please.\n")
                      p3Job=input("What do you do again "+str(p3Name)+"?\n ")
                  else:
                    print("Reminder: Do not leave the questions blank please.\n")
                    p3Living=input("Where do you live again "+str(p3Name)+"?\n ")
                else:
                  print("Reminder: Do not leave the questions blank please.\n")
                  p3Name=input("Sorry, could you say your name one more time please, player three?\n ")
              else:
                print("Reminder: Do not leave the questions blank please.\n")
                p2Job=input("What do you do again "+str(p2Name)+"?\n ")
            else:
              print("Reminder: Do not leave the questions blank please.\n")
              p2Living=input("Where do you live again "+str(p2Name)+"?\n ")
          else:
            print("Reminder: Do not leave the questions blank please.\n")
            p2Name=input("Sorry, we couldn't hear you, what was your name again player two?\n ")
        else:
          print("Reminder: Do not leave the questions blank please.\n ")
          p1Job=input("Sorry, what do you do again,"+str(p1Name)+"?\n ")
      else:
        print("Reminder: Do not leave the questions blank please.\n")
        p1Living=input("Sorry, where do you live again,"+str(p1Name)+"?\n ")
    else:
      print("Reminder: Do not leave the questions blank please.\n")
      p1Name=input("Sorry, I didn't quite catch that. What was your name again, player one?\n ")
  else:
    start=input("Unrecognized command. Type 'start' to start the Wheel of Fortune program.\n    Type 'quit' to quit the program.\nEnter: ")