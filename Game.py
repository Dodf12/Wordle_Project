   
import string
import sys #used to forcibly quit program
from Setting import Setting
from WordBank import WordBank
from WordleWord import WordleWord
from WordlePlayer import WordlePlayer
from FancyWord import FancyWord

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
    #alphabet obj
    a = alphabet.getWord(); 
    #seeing if character in guess algins with character in word
    #for idx in range(len(g)):


    for idx in range(len(g)): #using double loop, one for guess and the other for the actual word    

            for jdx in range(len(w)):
                if (g[idx] == w[idx]):   #marks letter green
                    #print(idx)
                    guess.setCorrect(idx)

                    alphaidx= a.find(g[idx])             #finds index of correct letter in the alphabet object
                    alphabet.setCorrect(alphaidx)

                    g=guess.getWord()
                    break           
                    print(g[idx],"-",w[idx])       
                if (g[idx] == w[jdx]):         #makrs letter green
                    guess.setMisplaced(idx)

                    alphaidx= a.find(g[idx])
                    alphabet.setMisplaced(alphaidx)

                    g=guess.getWord()
                    break
                if (g[idx] != w[jdx]):  #marks gray
                    guess.setUnused(idx)

                    alphaidx= a.find(g[idx])
                    alphabet.setUnused(alphaidx)

                    g=guess.getWord()
                    

def playRound(player, words, all_words, settings):
    ranWord = words.getRandom() #getting random word
    print(ranWord)
    guess_list = [1,2,3,4,5,6]
    # ===== REAL CODE< DO NOT TOUCH>

    for i in range(6):             #Game has six rounds, so it is looping six times                                                           
                                                                                              #                                                      
        #print("Hi")
        player_guess = input("Enter your valid guess: ") 
        #print("player guess",player_guess)
        if player_guess == ranWord:
            player_guess_obj = WordleWord(player_guess)              
            alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")
            markGuess(ranWord, player_guess_obj, alphaObj)
            print(str(guess_list[i]) + ":",player_guess_obj)
            print(" Alphabet ",alphaObj)
            print("Congratulations! You have guessed the correct word")
            player.updateStats(True,1)
            break        
        else:
            if len(player_guess) != 5 or not all_words.contains(player_guess):  #checks if word doesn't have 5 letters
                while len(player_guess) != 5:
                    player_guess = input("Please guess a proper 5 letter valid word: ")
            else:
                #print("player guess in else",player_guess)
                player_guess_obj = WordleWord(player_guess)              
                alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")
                markGuess(ranWord, player_guess_obj, alphaObj)
                print(str(guess_list[i]) + ":",player_guess_obj)
                print(" Alphabet ",alphaObj)
    print("Sorry, you weren't able to guess the word within the allowed number of attempts")




    

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

    a = "Welcome " + name + ", Do you wish to play? (Enter Yes or No & Please Use Çaps): "
    #b = "If You Wanted To Say Maybe, Then Why Are You Playing The Game In The First Place 🙄 "
    ready = input(a)
    #mayb = input(b)
    if ready == "Yes":
        print("Loading You In To The Game . . .")
    elif ready == "No":
        print("Exiting You Out Of The Game . . .")
        sys.exit()
    # elif mayb == "Maybe":
    #     input(b)
    #     new_attempt = ""
    #     while (new_attempt != "Yes" and new_attempt != "No"):        
    #         new_attempt = input("That is not a valid input, please try again!: ")
    #     if new_attempt == "Yes":
    #         print("Loading You In To The Game . . .")
    #     elif new_attempt == "No":
    #         print("Exiting You Out Of The Game . . .")
    #     elif new_attempt == "Maybe":
    #         print("Done Taking Maybes From You, Im Kicking You Out Of The Game Instead 🙄 ")
    # else:    
    #     new_attempt = ""
    #     while (new_attempt != "Yes" and new_attempt != "No" and new_attempt != "Maybe"):        
    #         new_attempt = input("That is not a valid input, please try again!: ")
    #     if new_attempt == "Yes":
    #         print("Loading You In To The Game . . .")
    #     elif new_attempt == "No":
    #         print("Exiting You Out Of The Game . . .")
    #     elif new_attempt == "Maybe":
    #         print("Done Taking Maybes From You, Im Kicking You Out Of The Game Instead 🙄 ")


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

    
    
    if play_again == "no":
        sys.exit()

    while play_again.lower() == "yes":
        #print("eddumoham")
        playRound(player_list, five_letter_words, all_words, settings)
        #print("pandimoham")
        play_again = input("Would you like to play another round?: ")


    player.displayStats()
    



playWordle()

