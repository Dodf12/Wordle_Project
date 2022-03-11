import math
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
from player import Player

# TODO - make WordlePlayer
class WordlePlayer(Player):
    def __init__(self, name, maxTry):
        super().__init__(name)
        self.maxTry = 6 #maximum amt of tries p/game
        self.gamesplayed = 0 #total games played
        self.winpercent = 0
        self.winstreak = 0 #current win streak
        self.maxstreak = 0 #highest amount of wins in a row ever
        self.wins = 0 #variable for number of times one
        self.total_tries = 0 #varaible for total tries attemtped by player through
        self.current_tries = [] #Tracks tries in game being played currently by the player and stores in list
        self.losses = 0

    def updateStats(self, won, tries): #updates the amount of tries
        if won:
            self.winstreak += 1
            if self.winstreak > self.maxstreak:
                self.maxstreak = self.winstreak
            self.total_tries = tries + 1
            self.wins = self.wins + 1
            self.current_tries.append(tries)
            self.gamesplayed = self.gamesplayed + 1
        elif won == False:
            self.losses+=1
            self.total_tries = tries + 1
            self.winstreak = 0
            self.gamesplayed = self.gamesplayed + 1
            
    
    def winPercentage(self):
        winpercent = ""
        return float(self.wins / self.gamesplayed) * 100
        
    def gamesPlayed(self):
        return self.gamesplayed
    def currentStreak(self):
        return self.winstreak
    def maxStreak(self): 
        return self.maxstreak
    
    # def guessDist(self): #prints guess distribution stats
    #     # #These variables keeep track of how many tries player attempted befor win

    #     one_try = 0 
    #     two_try = 0
    #     three_try = 0
    #     four_try = 0
    #     five_try = 0
    #     six_try = 0
    #     for idx in range(len(self.current_tries)):           
    #         if self.current_tries[idx] == 1:
    #             one_try = one_try + 1
    #         elif self.current_tries[idx] == 2:
    #             two_try = two_try +  1
    #         elif self.current_tries[idx] == 3:
    #             three_try = three_try + 1
    #         elif self.current_tries[idx] == 4:
    #             four_try = four_try + 1
    #         elif self.current_tries[idx] == 5:
    #             five_try = five_try + 1
    #         elif self.current_tries[idx] == 6:
    #             six_try = six_try + 1

    #     x = [one_try, two_try, three_try, four_try, five_try, six_try]
    #     index_list = x #in order to get index

    #     unique_x = []
    #     for irr in x:
    #         if (irr not in unique_x) and (irr>0):
    #             unique_x.append(irr)

    #     barlist = ['1', '2', '3', '4', '5', '6']
    #     print("Guess Distribution")     
    #     #getting the largest numbers in the "x" list and getting their indexes
    #     #print(x[0],x[1],x[2],x[3],x[4],x[5])

    #     y=[one_try, two_try, three_try, four_try, five_try, six_try]
    #     y.sort()
        
    #     i=0
    #     if ( len(unique_x) > 2):
    #         while i < 6:
                
    #             if (x[i]==0):
    #                 print (" " + str(i+1)+": #"+ " " + str(x[i]))
    #             elif (x[i]==1):
    #                 print (" " + str(i+1) +": #####" +" " + str(x[i])) 

    #             elif (x[i]==2): 
    #                 print (" " + str(i+1) +": #########"+ str(x[i]))         
    #             elif (x[i]==3): 
    #                 print (" " + str(i+1) + ": #############"+ str(x[i]))     
    #             elif (x[i]==4): 
    #                 print (" " + str(i+1) + ": #################"+ str(x[i]))   
    #             elif (x[i]==5): 
    #                 print (" " + str(i+1) +": #####################"+ str(x[i]))                           
    #             i=i+1

    #     elif ( len(unique_x) == 1 ):
    #         while i < 6:
                
    #             if (x[i]==0):
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### " + str(x[i]))
    #                 else:
    #                     print (" " + str(i+1) +": # "+ str(x[i]))
    #             elif (x[i]==1):
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### " +  str(x[i]))
    #                 else:
    #                     print (" " + str(i+1) +": ##### "+ str(x[i]))                                       
    #             elif (x[i]==2): 
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### " + str(x[i]))
    #                 else:                  
    #                     print (" " + str(i+1) +": ######### "+" " +   str(x[i]))         
    #             elif (x[i]==3): 
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### " +  str(x[i]))
    #                 else:
    #                     print (" " + str(i+1) + ": ############# "+ str(x[i]))     
    #             elif (x[i]==4):
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### " + str(x[i]))
    #                 else:                     
    #                     print (" " + str(i+1) +": ################# "+ str(x[i]))   
    #             elif (x[i]==5): 
    #                 if (x[i]==y[5]):
    #                     print (" " + str(i+1) +": ##################### "+ str(x[i]))
    #                 else:
    #                     print (" " + str(i+1) +": ##################### "+ str(x[i]))                           
    #             i=i+1
        




    def displayStats(self):
        print("Games Played: " + str(self.gamesplayed))
        print("Win %: " + str(int(self.winPercentage())) + "%")
        print("Current Streak: " + str(self.winstreak))
        print("Max Streak: " + str(self.maxstreak))
        #print("aBefore")
        
        #printing out guess distrubtion
        one_try = 0 
        two_try = 0
        three_try = 0
        four_try = 0
        five_try = 0
        six_try = 0
        for idx in range(len(self.current_tries)):           
            if self.current_tries[idx] == 1:
                one_try = one_try + 1
            elif self.current_tries[idx] == 2:
                two_try = two_try +  1
            elif self.current_tries[idx] == 3:
                three_try = three_try + 1
            elif self.current_tries[idx] == 4:
                four_try = four_try + 1
            elif self.current_tries[idx] == 5:
                five_try = five_try + 1
            elif self.current_tries[idx] == 6:
                six_try = six_try + 1

        x = [one_try, two_try, three_try, four_try, five_try, six_try]
        index_list = x #in order to get index

        unique_x = []
        for irr in x:
            if (irr not in unique_x) and (irr>0):
                unique_x.append(irr)

        barlist = ['1', '2', '3', '4', '5', '6']
        print("Guess Distribution")     

        y=[one_try, two_try, three_try, four_try, five_try, six_try]
        y.sort()
        #print("after Guess Distribution)", x, unique_x)
        i=0
        if ( len(unique_x) > 2):
            while i < 6:
                
                if (x[i]==0):
                    print (" " + str(i+1)+": # "+ str(x[i]))
                elif (x[i]==1):
                    print (" " + str(i+1) +": #####" + str(x[i])) 

                elif (x[i]==2): 
                    print (" " + str(i+1) +": #########"+ str(x[i]))         
                elif (x[i]==3): 
                    print (" " + str(i+1) + ": #############"+ str(x[i]))     
                elif (x[i]==4): 
                    print (" " + str(i+1) + ": #################"+ str(x[i]))   
                elif (x[i]==5): 
                    print (" " + str(i+1) +": #####################"+ str(x[i]))                           
                i=i+1

        elif ( len(unique_x) == 1 ):
            while i < 6:
                
                if (x[i]==0):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": # " + str(x[i]))
                    else:
                        print (" " + str(i+1) +": # "+ str(x[i]))
                elif (x[i]==1):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### "+str(x[i]))
                    else:
                        print (" " + str(i+1) +": ##### "+ str(x[i]))                                       
                elif (x[i]==2): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " + str(x[i]))
                    else:                  
                        print (" " + str(i+1) +": ######### "+ str(x[i]))         
                elif (x[i]==3): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " +  str(x[i]))
                    else:
                        print (" " + str(i+1) + ": ############# "+ str(x[i]))     
                elif (x[i]==4):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " + str(x[i]))
                    else:                     
                        print (" " + str(i+1) +": ################# "+ str(x[i]))   
                elif (x[i]==5): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### "+ str(x[i]))
                    else:
                        print (" " + str(i+1) +": ##################### "+ str(x[i])) 
                i=i+1                          
        elif ( len(unique_x) == 2 ):
            while i < 6:
                
                if (x[i]==0):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " + str(x[i]))
                    else:
                        print (" " + str(i+1) +": # "+ str(x[i]))
                elif (x[i]==1):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " +  str(x[i]))
                    else:
                        print (" " + str(i+1) +": ########### "+ str(x[i]))                                       
                elif (x[i]==2): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " + str(x[i]))
                    else:                  
                        print (" " + str(i+1) +": ########### " + str(x[i]))         
                elif (x[i]==3): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " +  str(x[i]))
                    else:
                        print (" " + str(i+1) + ": ########### "+ str(x[i]))     
                elif (x[i]==4):
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### " + str(x[i]))
                    else:                     
                        print (" " + str(i+1) +": ########### "+ str(x[i]))   
                elif (x[i]==5): 
                    if (x[i]==y[5]):
                        print (" " + str(i+1) +": ##################### "+ str(x[i]))
                    else:
                        print (" " + str(i+1) +": ########### "+ str(x[i]))                         
                i=i+1
        else:
            print (" 1: # 0")
            





# p = WordlePlayer("Mark", 6) 
# p.updateStats(True, 2) 

# p.displayStats() 

# p1 = WordlePlayer("Mark", 6) 
# p1.updateStats(True, 2) 
# p1.updateStats(False, 0) 

# p1.displayStats() 
