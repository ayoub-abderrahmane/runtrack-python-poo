class Personne:
    
    def __init__(self,prenom,nom,prenom2,nom2):
        self.prenom = prenom
        self.nom = nom
        self.prenom2 = prenom2
        self.nom2 = nom2
    
    def SePresenter(self):
        print("Je suis",self.prenom ,self.nom)
        print("Je suis",self.prenom2 ,self.nom2)

noms = Personne('John' ,'Doe' ,'Jean' ,'Dupond')

noms.SePresenter()
