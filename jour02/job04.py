class Student:
    def __init__(self,nom,prenom,num):
        self.__nom = nom
        self.__prenom = prenom
        self.__num = num
        self.__credits = 0
        self.__level = 90
    
    def get_info(self):
        return self.__nom ,self.__prenom ,self.__num,self.__level
    
    def add_credits(self):
        self.__credits += 10
        self.__credits += 10
        self.__credits += 10
        print ("Le nombre de credits de John Doe est de" ,self.__credits ,"points")
        return self.__credits
    
    def __studentEval(self):
        if self.__level >= 90:
            return "Excellent"
        if 90 > self.__level >= 80:
            return "Très bien"
        if 80 > self.__level >= 70:
            return "Bien"
        if 70 > self.__level >= 60:
            return "Passable"
        if self.__level <= 60:
            return "Insuffisant"
    
    def studentInfo(self):
        print ("Nom =" ,self.__nom)
        print ("Prénom =" ,self.__prenom)
        print ("id =" ,self.__num)
        print ("Niveau =" , self.__studentEval())


call = Student("John","Doe",145)

# call.add_credits()

call.studentInfo()