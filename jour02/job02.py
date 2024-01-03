class Livre:
    def __init__(self ,titre ,auteur ,pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
    
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
    
call = Livre('Berserk' ,'Kentaro Miura' ,'224')
print(call.get_auteur())

call.set_pages(-15)
print (call.get_pages())
