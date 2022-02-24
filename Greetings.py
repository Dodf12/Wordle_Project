

class Greetings:
    def __init__(self):
        self.name = ""
    def getName(self):
        return self.name
    def Intro(self):
        print("Let's play the game of Wordle!!")
        self.name = input("Player 1, Enter your name: ")
        a = "Welcome " + self.name + ", Are You Ready To Play The Game Of Wordle? (Enter Yes or No): "
        b = "If You Wanted To Say Maybe, Then Why Are You Playing The Game In The First Place 🙄 "
        ready = input(a)
        mayb = input(b)
        if ready == "Yes":
            print("Loading You In To The Game . . .")
        elif ready == "No":
            print("Exiting You Out Of The Game . . .")
        elif mayb == "Maybe":
            input(b)
            new_attempt = ""
            while (new_attempt != "Yes" and new_attempt != "No"):        
                new_attempt = input("That is not a valid input, please try again!: ")
            if new_attempt == "Yes":
                print("Loading You In To The Game . . .")
            elif new_attempt == "No":
                print("Exiting You Out Of The Game . . .")
            elif new_attempt == "Maybe":
                print("Done Taking Maybes From You, Im Kicking You Out Of The Game Instead 🙄 ")
        else:    
            new_attempt = ""
            while (new_attempt != "Yes" and new_attempt != "No" and new_attempt != "Maybe"):        
                new_attempt = input("That is not a valid input, please try again!: ")
            if new_attempt == "Yes":
                print("Loading You In To The Game . . .")
            elif new_attempt == "No":
                print("Exiting You Out Of The Game . . .")
            elif new_attempt == "Maybe":
                print("Done Taking Maybes From You, Im Kicking You Out Of The Game Instead 🙄 ")
c = Intro()
print(c)


                  
