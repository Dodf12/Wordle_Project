import string
from Setting import Setting
from WordBank import WordBank
from WordleWord import WordleWord
from WordlePlayer import WordlePlayer
from FancyWord import FancyWord
from gui import gui

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

def markGuess(word, guess, alphabet):
    g = guess.getWord()
    #string
    w = word 
    #seeing if character in guess algins with character in word
    for idx in range(len(g)): #using double loop, one for guess and the other for the actual word    

            for jdx in range(len(w)):
                a = alphabet.getWord() 
                if (g[idx] == w[idx]):   #marks letter green
                    guess.setCorrect(idx)

                    alphaidx= alphabet.getWord().find(g[idx])             #finds index of correct letter in the alphabet object
                    alphabet.setCorrect(alphaidx)
                    g=guess.getWord()
                    break           
     
                if (g[idx] == w[jdx]):         #makrs letter yellow
                    guess.setMisplaced(idx)

                    alphaidx= alphabet.getWord().find(g[idx])
                    alphabet.setMisplaced(alphaidx)
                    g=guess.getWord()
                    break
                if (g[idx] != w[jdx]):  #marks gray
                    guess.setUnused(idx)

                    alphaidx= alphabet.getWord().find(g[idx])
                    alphabet.setUnused(alphaidx)
                    g=guess.getWord()         

def playRound(player, words, all_words, settings):
    ranWord = words.getRandom() 
    print("") #all of these blank strings are to keep spaces
    print(ranWord)
    guess_list = [1,2,3,4,5,6] #used to number guesses
    alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")
      #goes here if it is normal mode
    tries_counter = 0

    i = 0
    guessObjList = []
    while i < 6:
        player_guess = input("Enter your guess!: ") 
        player_guess_obj = WordleWord(player_guess)  


        print("\n")

        if player_guess == "h":       #EXTRA FEATURE, GIVES HINT(WHICH IS AN UNCOLORED LETTER)
            for idx in range(len(alphaObj.getWord())):
                for jdx in range(len(ranWord)):
                    if (alphaObj.colorAt(idx) == 'green' or alphaObj.colorAt(idx) and (alphaObj.getWord()[idx] == ranWord[jdx])):
                            hint = alphaObj.getWord()[idx]
                            i+=1
        if player_guess == ranWord:
            guessObjList.append(player_guess_obj)
            markGuess(ranWord, player_guess_obj, alphaObj)
            #print(str(guess_list[i]) + ":",player_guess_obj)
            indexval = 0
            for p in guessObjList:                    
                indexval = indexval + 1
                print(indexval,":",p,"\n")

            print(" Alphabet ",alphaObj)
            print("Congratulations! You have guessed the correct word")
            player[0].updateStats(True,i)
            return  
        else:
            if len(player_guess) != 5 or not all_words.contains(player_guess):  #checks if word doesn't have 5 letters
                while len(player_guess) != 5 or not all_words.contains(player_guess):
                    print("It seems you have not typed a valid")
                    player_guess = input("Please enter a proper guess here: ")
                    print("Ok, Thank you. Our system has verfied your word. Please type it again to confirm and continue playing the game")
                    i += 0

            else:
                guessObjList.append(player_guess_obj)
                #player_guess_obj = WordleWord(player_guess)              
                markGuess(ranWord, player_guess_obj, alphaObj)
                #print(str(guess_list[i]) + ":",player_guess_obj)
                indexval = 0
                for p in guessObjList:                    
                    indexval = indexval + 1
                    print(indexval,":",p,"\n")

                print(" Alphabet ",alphaObj)
                i+=1
    print("Sorry, you weren't able to guess the word within the allowed number of attempts")
    print("The correct word was: " + ranWord )
    player[0].updateStats(False, i)




    


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
    gui()
    print("Let's play the game of Wordle!!")
    name = input("Enter your name: ")
    print("")

    ready_to_play = input("Welcome " + name + " Do you wish to play? (Enter Yes or No): ") #part 1 of intro, welcoming
    if ready_to_play.lower() == "yes":
        print("Loading You In To The Game . . .")
    elif ready_to_play.lower() == "no":
        print("Exiting You Out Of The Game . . .")
        return
    else:    
         new_attempt = ""
         while (new_attempt.lower() != "yes" and new_attempt.lower() != "no"):        
             new_attempt = input("That is not a valid input, please try again!: ")
         if new_attempt.lower() == "yes":
             print("Loading You In To The Game . . .")
             print("")
         elif new_attempt.lower() == "no":
             print("Exiting You Out Of The Game . . .")



    # make the player
    #actually created the player object here
    player = WordlePlayer(name, 6)
    player_list = []
    player_list = player_list + [player]
    # start playing rounds of Wordle
    playRound(player_list, five_letter_words, all_words, settings)
    # Finding out of another round is being player and end game by displaying player stats
    play_again = input("Would you like to play another round?: ")
    #play_again_bool = True

    
    
    if play_again.lower() == "no":
        player.displayStats()
        return

    while play_again.lower() == "yes":
        #print("eddumoham")
        playRound(player_list, five_letter_words, all_words, settings)
        #print("pandimoham")
        play_again = input("Would you like to play another round?: ")

    



playWordle()
# word = "candy"
# guess = WordleWord("crane")
# alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")
# markGuess(word, guess, alpha)
# print(guess)
# print(alpha)