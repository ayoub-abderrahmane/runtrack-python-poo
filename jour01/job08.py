import math
class Cercle:
    def __init__(self):
        self.cercle1 = 4
    
    def changerRayon(self, rayon):
        self.cercle1 = rayon
    
    def diametre(self):
        diametre = self.cercle1 * 2
        print (diametre)
    
    def circonference(self):
        circonference = 2 * 3,14 * self.cercle1
        print (circonference)
    
    def aire(self):
        carré = self.cercle1 * self.cercle1
        aire = carré * 3,14
        print (aire)
    
    # def afficherInfos(self ,circonference ,diametre):
    #     print ("Les infos du cercle sont" ,"circonférence : ",circonference ,"diametre : ",diametre)


call = Cercle()
call.aire()