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
from FancyWord import FancyWord

# TODO - make WordleWord
class WordleWord(FancyWord):
    def __init__(self, w):
        super().__init__(w)           
    def setCorrect(self,pos):
        self.setColorAt(pos, "green")
    def setMisplaced(self,pos):
        self.setColorAt(pos, "yellow")
    def setUnused(self,pos):
        self.setColorAt(pos, "gray")
    def isCorrect(self,pos):
        if self.colorAt(pos, "green"):
            return True          
    def isMisplace(self,pos):
        if self.colorAt(pos, "yellow"):
            return True
    def isUnUsed(self,pos):
        if self.colorAt(pos, "blue"):
            return True
            


# given a word from common letter text
# inherit the word into this class
# double check to make sure it is 5 letters and a real word
# 