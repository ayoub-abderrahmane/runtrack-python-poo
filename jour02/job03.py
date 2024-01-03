class Livre:
    def __init__(self ,titre ,auteur ,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
        self.__emprunter = True
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages

    def set_titre(self ,titre):
        self.__titre = titre
    
    def set_auteur(self ,auteur):
        self.__auteur = auteur
    
    def set_pages(self ,pages):
        if pages > 0:
            self.__pages = pages
        else:
            print ("Le nombre doit être un entier supérieur a zéro")
    
    def verification(self):
        if self.__disponible == True:
            self.__emprunter == False
            return self.__emprunter
    
    def emprunter(self):
        if self.__emprunter == True:
            print ("Le livre est indisponible")
    
    def rendre(self):
        if self.__emprunter == False:
            self.__disponible == False
            print ("Le livre est a nouveau disponible")
    
       


call = Livre('Berserk' ,'Kentaro Miura' ,'224')

call.verification()
call.emprunter()
