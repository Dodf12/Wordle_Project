#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from tkinter.font import names
from unicodedata import name
from player import Player

# TODO - make WordlePlayer
class WorldPlayer(Player):
    de
    def __init__(self, name, maxTry):
        self.name = name
        self.maxTry = maxTry
        self.GamesPlayed = 0
        self.WinPercentage = 0.0
    def updateStats(self, won, tries):

    def winPercentage(self):
        
    def gamesPlayed(self):
    def currentStreak(self):
    def maxStreak(self):
    def displayStats(self):
        