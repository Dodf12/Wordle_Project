def Intro():
     print("Let's play the game of Wordle!!")
     name = input("Player 1, Enter your name")
     print("Welcome", name +"!")
     a = ("Ok " + name," Are You Ready? (Enter Yes or No)")
     ready = input(a)
     if ready == "Yes":
         print("Loading You In To The Game . . .")
     elif ready == "No":
         print("Exiting You Out Of The Game . . .")
     else:    
         new_attempt = ""
         while (new_attempt != "Yes" and new_attempt != "No"):        
             new_attempt = input("That is not a valid input, please try again!")
         if new_attempt == "Yes":
             print("Loading You In To The Game . . .")
         elif new_attempt == "No":
             print("Exiting You Out Of The Game . . .")
