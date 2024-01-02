class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def afficherLesPoints(self):
        print ("x = " ,self.x)
        print("y = " ,self.y)
    
    def afficherX(self):
        print("x = ",self.x)
    
    def afficherY(self):
        print("y = ",self.y)
    
    def changerXY(self ,x ,y):
        self.x = x
        self.y = y
        

call = Point()
call.changerXY(10,15)
call.afficherLesPoints()