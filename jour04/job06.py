class Vehicule:
    def __init__(self ,marque ,modele ,annee ,prix):
            self.marque = marque
            self.modele = modele
            self.annee = annee
            self.prix = prix
    
    def informationsVehicule(self):
          print ("Marque =" ,self.marque)
          print ("Modele =" ,self.modele)
          print ("Annee =" ,self.annee)
          print ("Prix =" ,self.prix)
    
    def demarrer(self):
         print ("Attention je roule")
          

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.porte = 4
    
    def informationsVehicule(self):
         print("NB porte =" ,self.porte)
         return super().informationsVehicule()
    
    def demarrer(self):
         print("drift")
         return super().demarrer()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2
    
    def informationsVehicule(self):
         print("NB porte =" ,self.roue)
         return super().informationsVehicule()
    
    def demarrer(self):
         print("roue avant")
         return super().demarrer()
         
    
        
          

merco = Voiture("mercedes" ,"benz" ,2014 ,1021)

# merco.informationsVehicule()

yamaha = Moto("yamaha" ,"VMAX" ,1987 ,14567)

yamaha.informationsVehicule()

yamaha.demarrer()

