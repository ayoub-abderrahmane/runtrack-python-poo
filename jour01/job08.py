import math
class Cercle:
    def __init__(self):
        self.cercle1 = 4
    
    def changerRayon(self, rayon):
        self.cercle1 = rayon
    
    def diametre(self ,diametre):
        diametre = self.cercle1 * 2
        return diametre
    def circonference(self ,circonference ):
        circonference = 2 * 3,14 * self.cercle1
        return circonference
    
    def aire(self):
        carré = pow(self.cercle1 ,2)
        aire = carré * 3,14
        print (aire)
    
    def afficherInfos(self ,circonference ,diametre):
        print ("Les infos du cercle sont" ,"circonférence : ",circonference ,"diametre : ",diametre)


call = Cercle()
call.afficherInfos()