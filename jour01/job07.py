class Personnage:
    def __init__(self):
        self.x = 400
        self.y = 400
    
    def position(self):
        print ("Les cordonnées du point sont",(self.x,self.y))
    
    def gauche(self):
        self.x -= 200
    
    def droite(self):
        self.x += 200
    
    def haut(self):
        self.y -= 200
    
    def bas(self):
        self.y += 200

call = Personnage()
call.gauche()
call.droite()
call.haut()
call.bas()
call.position()