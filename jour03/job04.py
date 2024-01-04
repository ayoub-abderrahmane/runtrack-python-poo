class Joueur:
    def __init__(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
    def marquerUnBut(self):
        self.buts +=1
    def effectuerUnePasseDecisive(self):
        self.passes_D +=1
    def recevoirUnCartonJaune(self):
        self.cartons_jaunes +=1
    def recevoirUnCartonRouge(self):
        self.cartons_rouges +=1
    def afficherStatistiques(self):
        print(f"Satistiques {self.nom} \nnumero : {self.numero} \nposition: {self.position} \nbut:{ self.buts} \npasses_D :{ self.passes_D} \ncartons_jaunes: {self.cartons_jaunes}\ncartons_rouges : {self.cartons_rouges}")
class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.liste_joueurs=[]
    def ajouterJoueur(self,joueur):
         self.liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self): 
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()       
    def mettreAJourStatistiquesJoueur(self,nom, numero, position,buts, passes_D,cartons_jaunes,cartons_rouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passes_D=passes_D
        self.cartons_jaunes=cartons_jaunes
        self.cartons_rouges=cartons_rouges
reus = Joueur("reus",11,"millieu",0,0,0,0)
pewandoski = Joueur("pewandoski",9,"BU",0,0,0,0)
bellingoal = Joueur("Bellingoal",5,"millieu",0,0,0,0)
bvb = Equipe("bvb")
bayern  = Equipe("bay")
bvb.ajouterJoueur(reus)
bvb.ajouterJoueur(pewandoski)
bayern.ajouterJoueur(bellingoal)
bvb.AfficherStatistiquesJoueurs()
reus.marquerUnBut()
pewandoski.effectuerUnePasseDecisive()
pewandoski.recevoirUnCartonRouge()
reus.recevoirUnCartonJaune()
bayern.AfficherStatistiquesJoueurs()