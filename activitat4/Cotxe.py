class Cotxe: 
    # Constructor
    def __init__(self, color, cavalls, preu):
        #Atributs
        self.color = color
        self.cavalls = cavalls
        self.preu = preu

    # Getter i Setters
    def getColor(self): 
        return self.color
    def setColor(self, new_color):
        self.color = new_color

    def getCavalls(self):
        return self.cavalls
    def setCavalls(self, new_cavalls):
        self.cavalls = new_cavalls

    def getPreu(self):
        return self.preu
    def setPreu(self, new_preu):
        self.preu = new_preu
            