import string
from Setting import Setting
from WordBank import WordBank
from WordleWord import WordleWord
from WordlePlayer import WordlePlayer
from Greetings import Intro

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
    g = guess
    w = word
    a = alphabet

    for idx in range(len(g)): #seeing if character in guess algins with character in word
        if guess[idx] == w[idx]:
            g.isCorrect()
    
    for idx in range(len(g)):
        if g[idx] != w[0] and g[idx] != w[1] and g[idx] != w[2] and g[idx] != w[3] and g[idx] != w[4]:
            g.set
             

def playRound(players, words, all_words, settings):
    WordBank("common5letter.txt")
    
    


def playWordle():

    # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    five_letter_words = WordBank("words_alpha.txt")


    # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # make the player
    Greetings.Intro()
    name = Greetings.getName() #getting name since player gave in Greetings class

    player = Player(name)
    # start playing rounds of Wordle
    
    # end game by displaying player stats

def main():

    playWordle()

if __name__ == "__main__":
    main()
