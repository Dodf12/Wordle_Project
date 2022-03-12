class Ranks:
    def __init__(self, won):
        self.won = won
        self.tries = 0
        self.trophies = 0
        self.rank = "novice"
    def current_rank_update(self, trophies):
        if self.trophies <= 100:
            self.rank = "novice"
        elif 100< self.trophies <= 200:
            self.rank = "OG"
        elif 200<self.trophies<=300:
            self.rank = "Tier 1"
        elif 300<self.trophies<=400:
            self.rank = "Tier 2"
        elif 400<self.trophies<=500:
            self.rank = "Tier 3"
        elif 600<self.trophies<=700:
            self.rank = "Bronze"
        elif 800<self.trophies<=900:
            self.rank = "Silver"
        elif 900<self.trophies<=1000:
            self.rank = "Gold"
        elif 1000<self.trophies<=1100:
            self.rank = "Platinum"
        elif 1100<self.trophies<=1200:
            self.rank = "Diamond"
        elif 1200<self.trophies<=1300:
            self.rank = "P.E.K.K.A"
        elif self.trophies>1300:
            self.rank = "God"
    def trophies_update(self, tries, hardmode):
        self.tries = tries

        if hardmode == False:
            if self.tries == 1:
                self.trophies = self.trophies + 10
            if self.tries == 2:
                self.trophies = self.trophies + 8
            if self.tries == 3:
                self.trophies = self.trophies + 6
            if self.tries == 4:
                self.trophies = self.trophies + 4
            if self.tries == 5:
                self.trophies = self.trophies + 2
        elif hardmode:
            if self.tries == 1:
                self.trophies = self.trophies + 20
            if self.tries == 2:
                self.trophies = self.trophies + 16
            if self.tries == 3:
                self.trophies = self.trophies + 12
            if self.tries == 4:
                self.trophies = self.trophies + 8
            if self.tries == 5:
                self.trophies = self.trophies + 4



    def get_score(self):
        return self.trophies
    def get_rank(self):
        return self.rank
        
# player_rank = Ranks(True) #updating rank and trophiesp
# player_rank.trophies_update(3,True)
# player_rank.current_rank_update(player_rank.get_score())
# player_rank.get_rank()
# print("Trophies: " + str(player_rank.get_score())) 
# print("Ranks: " + player_rank.get_rank())
