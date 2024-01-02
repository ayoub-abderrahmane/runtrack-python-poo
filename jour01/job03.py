class Operation:
    
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        

    def addition(self):
        result = self.nombre1 + self.nombre2
        print (result)

nombre = Operation(17,3)
nombre.addition()