class CompteBancaire:
    def __init__(self ,num_compte ,prenom ,nom ,solde):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.decouvert = True
    
    def get_num_compte(self):
        return self.__num_compte
    
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def afficher(self):
        print ("Ce compte appartient à " ,self.__prenom , self.__nom)

    def afficherSolde(self):
        print ("Le solde du compte est de :" ,self.__solde)
    
    def versement(self ,envoi):
        if self.decouvert == True:
            self.__solde += envoi
            print ("Le solde après versement est de :" ,self.__solde)
        else:
            print ("Solde a découvert ,opération impossible")
    
    def retrait(self ,retrait):
        if self.decouvert == True:
            self.__solde -= retrait
            print ("Le solde après le retrait est de :",self.__solde)
        else:
            if retrait < self.__solde:
                self.__solde -= retrait
                print ("Le solde après le retrait est de :",self.__solde)
            else:
                print("Retrait impossible ,fond insuffisant")
    
    def agios(self):
        if self.__solde < 0:
            self.__solde -= 50
            print ("Une penalité de 50 est appliquée a cause d'un découvert")
    
    def virement(self ,ref ,cb ,montant):
        self.ref = ref
        self.cb = cb
        self.montant = montant
        print (self.montant ,"on été viré vers" ,self.cb)
        self.__solde += montant
        print ("Le solde du compte est de" ,self.__solde)

    
compte = CompteBancaire(150 ,"John" ,"DOE" ,-30)

compte.virement(32 ,"pog", 30)
