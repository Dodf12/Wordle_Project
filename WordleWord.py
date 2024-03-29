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
class WordleWord(FancyWord):
    def __init__(self, w):
        super().__init__(w)           
    def setCorrect(self,pos): #sets char green
        self.setColorAt(pos, "green")
    def setMisplaced(self,pos): #sets char yellow
        self.setColorAt(pos, "yellow")
    def setNotUsed(self,pos): #set char gray
        self.setColorAt(pos, "gray")
    def isCorrect(self,pos):
        return self.colorAt(pos) == "green"         
    def isMisplaced(self,pos):
        return self.colorAt(pos) == "yellow"
    def isNotUsed(self,pos):
        return self.colorAt(pos) == "gray"



# given a word from common letter text
# inherit the word into this class
# double check to make sure it is 5 letters and a real word
# 