import string
from Setting import Setting
from WordBank import WordBank
from WordleWord import WordleWord
from WordlePlayer import WordlePlayer
from Greetings import Greetings

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
            g.isCorrect(idx)
    
    for idx in range(len(g)):
        if g[idx] != w[0] and g[idx] != w[1] and g[idx] != w[2] and g[idx] != w[3] and g[idx] != w[4]:
            g.setUnused(idx)

    for idx in range(len(g)):
        if g.colorAt(idx) != "green" or g.colorAt(idx) != "yellow":
            g.setMisplaced(idx)
    


             

def playRound(players, words, all_words, settings):
    WordBank("common5letter.txt")

    for i in range(6):
        player_guess = input("Enter your guess")
        if len(guess) !=5:
            player_guess = input("Please guess a proper 5 letter word")

        markGuess(word, player_guess, "abcdefghijklmnopqrstuvwxyz")

        print(player_guess)
        print(alphabet)
    
    updateStats()

    
    


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
    name = Greetings() #calling the greeting function, which outputs player name
    

    player = Player(name)
    player_list = player
    # start playing rounds of Wordle
    playRound(player_list, five_letter_words, all_words, settings)
    # end game by displaying player stats
    player.displayStats

    play_again = input("Play again")
    play_again_bool = False

    if play_again == "yes":
        play_again_bool = True
    
    else:
        play_again_bool = False

    while play_again_bool:
        playRound(player_list, five_letter_words, all_words, settings)

    if play_again_bool == False:
        displayStats()

def main():

    playWordle()


