   
import string
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

def markGuess(word, guess, alphabet):
    g = guess.getWord()
    #string
    w = word 
    #alphabet obj
    #a = alphabet.getWord() 
    #seeing if character in guess algins with character in word
    #for idx in range(len(g)):


    for idx in range(len(g)): #using double loop, one for guess and the other for the actual word    

            for jdx in range(len(w)):
                a = alphabet.getWord() 
                if (g[idx] == w[idx]):   #marks letter green
                    guess.setCorrect(idx)

                    alphaidx= alphabet.getWord().find(g[idx])             #finds index of correct letter in the alphabet object
                    alphabet.setCorrect(alphaidx)
                    g=guess.getWord()
                    break           
     
                if (g[idx] == w[jdx]):         #makrs letter green
                    guess.setMisplaced(idx)

                    alphaidx= alphabet.getWord().find(g[idx])
                    alphabet.setMisplaced(alphaidx)
                    g=guess.getWord()
                    break
                if (g[idx] != w[jdx]):  #marks gray
                    guess.setNotUsed(idx)

                    alphaidx= alphabet.getWord().find(g[idx])
                    alphabet.setNotUsed(alphaidx)
                    g=guess.getWord()
                    
def playRound(player, words, all_words, settings):
    ranWord = words.getRandom() #getting random word
    print(ranWord)
    guess_list = [1,2,3,4,5,6]
    # ===== REAL CODE< DO NOT TOUCH>
    alphaObj = WordleWord("abcdefghijklmnopqrstuvwxyz")

    i = 0
    guessObjList = []
    while i < 6:
        player_guess = input("Enter your guess!: ") 
        if len(player_guess) != 5 or not all_words.contains(player_guess):  #checks if word doesn't have 5 letters
            while len(player_guess) != 5 or not all_words.contains(player_guess):
                print("Our system has detected that you have given an incorrect word: ")
                player_guess = input("Please guess a valid 5 letter word: ")
                i += 0
        if len(player_guess) == 5 and all_words.contains(player_guess):
            player_guess = player_guess
        
        player_guess_obj = WordleWord(player_guess)  

        guessObjList.append(player_guess_obj)
        print("\n")

        if player_guess == ranWord:
            markGuess(ranWord, player_guess_obj, alphaObj)
            #print(str(guess_list[i]) + ":",player_guess_obj)
            indexval = 0
            for p in guessObjList:                    
                indexval = indexval + 1
                print(indexval,":",p,"\n")

            print(" Alphabet ",alphaObj,"\n")
            print("Congratulations! You have guessed the correct word")
            player[0].updateStats(True, i)
            return  

            


        else:
                    
                            
                markGuess(ranWord, player_guess_obj, alphaObj)
                #print(guess_list[i],":",player_guess_obj)
                indexval = 0

                for p in guessObjList:
                    
                    indexval = indexval + 1
                    print(indexval,":",p,"\n")


                #print(guess_list[i],":","\n")
                print(" Alphabet ",alphaObj,"\n")
                i+=1
    print("Sorry, you weren't able to guess the word within the allowed number of attempts")
    print("The correct word was: " + ranWord )
    player[0].updateStats(False, 0) #comeayns;dyu

  

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

    ready_to_play = input("Welcome " + name + " Do you wish to play? (Enter Yes or No & Please Use Çaps): ") #part 1 of intro, welcoming
    if ready_to_play == "Yes":
        print("Loading You In To The Game . . .")
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


    


def main():
    playWordle()

if __name__ == "__main__":
    main()   
# word = "candy"
# guess = WordleWord("crane")
# alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")
# markGuess(word, guess, alpha)
# print(guess)
# print(alpha)