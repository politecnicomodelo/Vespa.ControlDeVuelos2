from persona import persona

class pasajeros (persona):
    millas=None
    VIP=False
    necesidades_esp=""

    def addMillas(self,m):
        self.millas=m

    def setVIP(self,v):
        self.VIP=v

    def addNecesidad(self,n):
        self.necesidades_esp=n
