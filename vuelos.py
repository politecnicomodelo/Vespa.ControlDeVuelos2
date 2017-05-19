from datetime import datetime
class vuelo (object):
    avion=None
    fecha=None
    hora=None
    pasajeros=[]
    tripulacion=[]
    origen=""
    destino=""
    ocupantes=[]
    codigo_vuelo=None

    def __init__(self):
        self.tripulacion = []
        self.pasajeros = []

    def setAvion(self,a):
        self.avion=a
    def setCodigoVuelo(self,v):
        self.codigo_vuelo=v

    def setFecha(self,f):
        self.fecha=f

    def addPasajeros(self,p):
        self.pasajeros.append(p)
        self.ocupantes.append(p)

    def addTrip(self,t):
        self.tripulacion.append(t)
        self.ocupantes.append(t)

    def setOrigen(self,o):
        self.origen=o

    def setDestino(self,d):
        self.destino=d

    def setHora(self,h):
        self.hora=h

    def especiales(self):
        especiales=[]
        for item in self.pasajeros:
            if item.VIP==True or item.necesidades_esp!="":
                especiales.append(item)
        return especiales

    def Joven(self):
        joven=None
        hoy= datetime.today().date()
        for item in self.pasajeros:
            if hoy - item.fecha_nac < hoy - joven.fecha_nac:
                joven=item

    def autorizados(self,v):
        ti=[]
        for item in self.tripulacion:
            for item1 in item.modelo_avion:
                if(item1!=self.avion.modelo):
                    ti.append(item)
        return ti
