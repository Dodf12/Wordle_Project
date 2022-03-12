import random
import string
import math
import sys #used to forcibly quit program
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from fancyword import FancyWord


# testing github

#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======

#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game test
#======

def markGuess(word, guess, alphabet, hardmode):
    
    if (hardmode == False):
        g = guess.getWord()
        w = word 
        a = alphabet.getWord()

        for idx in range(len(g)): #using double loop, one for guess and the other for the actual word so            
            for jdx in range(len(w)): 
                if (guess.getWord()[idx] == w[idx]):   #marks letter green
                    guess.setCorrect(idx)

                    alphaidx= alphabet.getWord().find(guess.getWord()[idx]) #gets word from alphabet object and finds the character at position idx
                    if alphabet.colorAt(alphaidx) != "gray":            #makes sure word is not gray before coloring green
                        alphabet.setCorrect(alphaidx)
            
                        break
                if (guess.getWord()[idx] == w[jdx]):         #makrs letter yellow
                    guess.setMisplaced(idx)
                    alphaidx= alphabet.getWord().find(guess.getWord()[idx])  
                    if alphabet.colorAt(alphaidx) != "green":                 #makes sure its not green before making yellow  

                        alphabet.setMisplaced(alphaidx)
                        break
                if (guess.getWord()[idx] != w[jdx]):  #marks gray
                    alphaidx1= alphabet.getWord().find(guess.getWord()[idx])
                    if ((alphabet.colorAt(alphaidx1) != "green") and (alphabet.colorAt(alphaidx1) != "yellow")): #makes sure not green or yellow before passing
                        alphabet.setNotUsed(alphaidx1)
    else:
        g = guess.getWord()
        w = word 
        a = alphabet.getWord()

        for idx in range(len(g)): #using double loop, one for guess and the other for the actual word so            
            for jdx in range(len(w)): 
                if (guess.getWord()[idx] == w[idx]):   #marks letter green
                    guess.setCorrect(idx)

                    alphaidx= alphabet.getWord().find(guess.getWord()[idx]) #gets word from alphabet object and finds the character at position idx
                    if alphabet.colorAt(alphaidx) != "gray":            #makes sure word is not gray before coloring green
                        alphabet.setCorrect(alphaidx)
            
                        break
                if (guess.getWord()[idx] != w[jdx]):  #marks gray
                    alphaidx1= alphabet.getWord().find(guess.getWord()[idx])
                    if ((alphabet.colorAt(alphaidx1) != "green") and (alphabet.colorAt(alphaidx1) != "yellow")): #makes sure not green or yellow before passing
                        alphabet.setNotUsed(alphaidx1)        

                
                    
def playRound(player, words, all_words, settings, hardmode):
    
    ranWord = words.getRandom() #getting random word
    alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")
    hint_check = 0
    i = 0 #loop variable
    guessObjList = []
    while i < 6:
        player_guess = input("Enter your guess!: ") 
        if (len(player_guess) != 5 or player_guess == "h" or not all_words.contains(player_guess)):  #checks if word doesn't have 5 letters or not in file of words
            while len(player_guess) != 5 or not all_words.contains(player_guess): #while so that it keeps asking if player hasnt provided a proper word
                print("Our system has detected that you have given an incorrect word: ")
                player_guess = input("Please guess a valid 5 letter word: ")
                i += 0 #making sure incorrect words do not count towards the total six tries
        if len(player_guess) == 5 and all_words.contains(player_guess):
            player_guess = player_guess
        
        player_guess_obj = WordleWord(player_guess)  

        guessObjList.append(player_guess_obj) 
        print("\n")


        if player_guess == ranWord: #goes here if players's guess is green
            
            markGuess(ranWord, player_guess_obj, alphaObj, hardmode)

            indexval = 0
            for p in guessObjList:               #making sure it prints all the previous guesses     
                indexval = indexval + 1
                print(indexval,":",p,"\n")   #index val is used to number guess

            print(" Alphabet ",alphaObj,"\n")
            print("Congratulations! You have guessed the correct word")
            player[0].updateStats(True, i)
            return #in order to exit out of function
        else:
                                           
                markGuess(ranWord, player_guess_obj, alphaObj, hardmode)
                indexval = 0

                for p in guessObjList:                   
                    indexval = indexval + 1
                    print(indexval,":",p,"\n")

                print(" Alphabet ",alphaObj,"\n")
                i+=1 #adds to the number of tries
    
    #comes here if maximum tries has been exceeded
    print("Sorry, you weren't able to guess the word within the allowed number of attempts")
    print("The correct word was: " + ranWord )
    player[0].updateStats(False, 0)

  

def playWordle():

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    five_letter_words = WordBank("common5letter.txt")


    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

  

    #-NOTE-This is the intro sequence that we created as a little easter egg

    print("Let's play the game of Wordle!!")
    name = input("Enter your name: ")

    ready_to_play = input("Welcome " + name + " Do you wish to play? (y/n): ") #part 1 of intro, welcoming
    if ready_to_play == "y":
        hardmode = input("Would you like to activate hard mode?(y/n) There is no turning back from here ") #askss user a one time decision of going to hardmode or not

        print("Loading You In To The Game . . .")
        print("")
        print("Ok, you may begin. Please enter your first guess into the following line")
        print("")
    elif ready_to_play == "n":
        print("Exiting You Out Of The Game . . .")
        return
    else:    
         new_attempt = ""
         while (new_attempt != "y" and new_attempt != "n"):        
             new_attempt = input("That is not a valid input, please try again!: ")
         if new_attempt == "Yes":
             print("Loading You In To The Game . . .")
         elif new_attempt == "No":
             print("Exiting You Out Of The Game . . .")
             return



    # make the player
    #actually created the player object here
    player = WordlePlayer(name, 6)
    player_list = []
    player_list = player_list + [player]
    if hardmode == "n":
        playRound(player_list, five_letter_words, all_words, settings, False)    
    elif hardmode == "y":
        # start playing rounds of Wordle
        playRound(player_list, five_letter_words, all_words, settings, True)
    
    # Finding out of another round is being player and end game by displaying player stats
    play_again = input("Would you like to play another round?(y/n): ") #asks after first round played by player if more than multiple rounds are played, it shifts to the while loop below
    #play_again_bool = True



    
    
    if play_again.lower() == "n":
        player.displayStats()


    while play_again.lower() == "y":
        if hardmode == "n":
            playRound(player_list, five_letter_words, all_words, settings, True)    
        else:
            # start playing rounds of Wordle
            playRound(player_list, five_letter_words, all_words, settings, False)
        play_again = input("Would you like to play another round?: ")
        if play_again.lower() == "n":
            player.displayStats()




def main():
    playWordle()

if __name__ == "__main__":
    main()   

