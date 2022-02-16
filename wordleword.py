#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from fancyword import FancyWord

# TODO - make WordleWord
class wordleword(FancyWord):
    def setCorrect(pos):
        setColorAt(pos, "green")
    def setMisplaced(pos):
        setColorAt(pos, "yellow")
    def setUnused(pos):
        setColorAt(pos, "grey")
    def isCorrect(pos):
        if colorAt(pos, "green"):
            return True          
    def isMisplace(pos):
        if colorAt(pos, "yellow"):
            return True
    def isNotUsed(pos):
        if colorAt(pos, "grey"):
            return True

# given a word from common letter text
# inherit the word into this class
# double check to make sure it is 5 letters and a real word
# 