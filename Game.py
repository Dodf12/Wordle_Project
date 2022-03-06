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

def markGuessHard(word, guess, alphabet): #function for hard mode(It is the same as above, but without yellow)   
    #NOTE-I know I can use function above for hard mode, but I didnt want to alter what I was supposed to have
    # markguess only requires 3 inputs   
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
     
                if (g[idx] != w[jdx]):  #marks gray
                    guess.setUnused(idx)

                    alphaidx= alphabet.getWord().find(g[idx])
                    alphabet.setUnused(alphaidx)
                    g=guess.getWord()             


def playRound(player, words, all_words, settings, hardmode):
    ranWord = words.getRandom() 
    print(ranWord)
    guess_list = [1,2,3,4,5,6] #used to number guesses
    alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")

    if hardmode: #goes if player activates hardmode
        tries_counter = 0
        for i in range(6):             #Game has six rounds, so it is looping six times                                                           
                                                                                                                                                        
            player_guess = input("Enter your guess!: ") 
            if player_guess == "h":       #EXTRA FEATURE, GIVES HINT(WHICH IS AN UNCOLORED LETTER)
                for idx in range(len(alphaObj.getWord())):
                    for jdx in range(len(ranWord)):
                        if (alphaObj.colorAt(idx) == 'green' or alphaObj.colorAt(idx) and (alphaObj.getWord()[idx] == ranWord[jdx])):
                            hint = alphaObj.getWord()[idx]

                    


                print("Ok Here is your hint. One of the letters is: " + hint)
            
            
            if player_guess == ranWord:
                tries_counter+=1
                player_guess_obj = WordleWord(player_guess)              
                
                markGuessHard(ranWord, player_guess_obj, alphaObj)
                print(str(guess_list[i]) + ":",player_guess_obj)
                print(" Alphabet ",alphaObj)
                print("Congratulations! You have guessed the correct word")
                player[0].updateStats(True,1)
                return    
            else:
                tries_counter+=1
                if len(player_guess) != 5 or not all_words.contains(player_guess):  #checks if word doesn't have 5 letters
                    while len(player_guess) != 5:
                        player_guess = input("Please guess a proper 5 letter valid word: ")

                else:
                    
                    player_guess_obj = WordleWord(player_guess)              
                    markGuessHard(ranWord, player_guess_obj, alphaObj)
                    print(str(guess_list[i]) + ":",player_guess_obj)
                    print(" Alphabet ",alphaObj)
        print("Sorry, you weren't able to guess the word within the allowed number of attempts")
        print("The correct word was: " + ranWord )
        player[0].updateStats(False, tries_counter)

    else:
            #goes here if it is normal mode
        tries_counter = 0
        for i in range(6):             #Game has six rounds, so it is looping six times                                                           
                                                                                                                                                        
            player_guess = input("Enter your guess!: ") 
            if player_guess == "h":       #EXTRA FEATURE, GIVES HINT(WHICH IS AN UNCOLORED LETTER)
                for idx in range(len(alphaObj.getWord())):
                    for jdx in range(len(ranWord)):
                        if (alphaObj.colorAt(idx) == 'green' or alphaObj.colorAt(idx) and (alphaObj.getWord()[idx] == ranWord[jdx])):
                            hint = alphaObj.getWord()[idx]

                    


                print("Ok Here is your hint. One of the letters is: " + hint)
            
            
            if player_guess == ranWord:
                tries_counter+=1
                player_guess_obj = WordleWord(player_guess)              
                
                markGuess(ranWord, player_guess_obj, alphaObj)
                print(str(guess_list[i]) + ":",player_guess_obj)
                print(" Alphabet ",alphaObj)
                print("Congratulations! You have guessed the correct word")
                player[0].updateStats(True,1)
                return    
            else:
                tries_counter+=1
                if len(player_guess) != 5 or not all_words.contains(player_guess):  #checks if word doesn't have 5 letters
                    while len(player_guess) != 5:
                        player_guess = input("Please guess a proper 5 letter valid word: ")

                else:
                    
                    player_guess_obj = WordleWord(player_guess)              
                    markGuess(ranWord, player_guess_obj, alphaObj)
                    print(str(guess_list[i]) + ":",player_guess_obj)
                    print(" Alphabet ",alphaObj)
        print("Sorry, you weren't able to guess the word within the allowed number of attempts")
        print("The correct word was: " + ranWord )
        player[0].updateStats(False, tries_counter)




    

def playWordle():

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    five_letter_words = WordBank("common5letter.txt")

    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    #Intro Sequence
    gui()
    print("Let's play the game of Wordle!!")
    name = input("Enter your name: ")
    ready_to_play = input("Welcome " + name + " Do you wish to play? (Enter Yes or No & Please Use Çaps): ") #part 1 of intro, welcoming
  
    if ready_to_play == "Yes":
        print("Loading You In To The Game . . .")
        print("You may ask for a hint by typing h, but it does take one of your tries so use it wisely")
        print("")
 
    elif ready_to_play == "No":
        print("Exiting You Out Of The Game . . .")
        return
  
    else:    
         new_attempt = ""
         while (new_attempt != "Yes" and new_attempt != "No"):        
             new_attempt = input("That is not a valid input, please try again!: ")
  
         if new_attempt == "Yes":
             print("Loading You In To The Game . . .")
         elif new_attempt == "No":
             print("Exiting You Out Of The Game . . .")

    
    # make the player
    player = WordlePlayer(name, 6)
    player_list = []
    player_list = player_list + [player]
    

    # start playing rounds of Wordle
    hard_mode = input("Would you like to activate hard mode? ")
    while (hard_mode  != "Yes" and hard_mode  != "No"):        
        hard_mode  = input("That is not a valid input, please try again!: ")
    if hard_mode == "Yes":
        playRound(player_list, five_letter_words, all_words, settings, True)

    elif hard_mode == "No":
        playRound(player_list, five_letter_words, all_words, settings, False)


    # Finding out of another round is being player and end game by displaying player stats
    play_again = input("Would you like to play another round?: ")

    while (play_again  != "Yes" and play_again  != "No"):        
             play_again  = input("That is not a valid input, please try again!: ")
   
    
    if play_again == "Yes":  #code to activate hardmode
            hard_mode = input("Would you like to activate hard mode? ")
            while (hard_mode  != "Yes" and hard_mode  != "No"):        
                hard_mode  = input("That is not a valid input, please try again!: ")
            if hard_mode == "Yes":
                while hard_mode == "Yes":
                    playRound(player_list, five_letter_words, all_words, settings, True)

            elif hard_mode == "No":
                while hard_mode == "No":
                    playRound(player_list, five_letter_words, all_words, settings, False)


    
    if play_again == "No":
        player.displayStats()
        return

    while play_again.lower() == "Yes":
        playRound(player_list, five_letter_words, all_words, settings)
        play_again = input("Would you like to play another round?: ")


    



playWordle()
# word = "candy"
# guess = WordleWord("crane")
# alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")
# markGuess(word, guess, alpha)
# print(guess)
# print(alpha)
