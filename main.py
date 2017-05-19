from tripulacion import tripulacion
from pasajeros import pasajeros
from piloto import piloto
from servicio_abordo import servicio_abordo
from avion import avion
from persona import persona
from vuelos import vuelo
from datetime import date, datetime, timedelta

lista_personas=[]
lista_aviones=[]
lista_vuelos=[]
lista = []
personas = open("personas.dat", "r")
for line in personas:
    lista = line.split('|')
    if (lista[0]=="Pasajero"):
        new_pasajero=pasajeros()
        new_pasajero.setNombre(str(lista[1]))
        new_pasajero.setApellido(str(lista[2]))
        new_pasajero.setFecha(lista[3])
        new_pasajero.setDni(str(lista[4]))
        new_pasajero.setVIP(lista[5])
        new_pasajero.addNecesidad(str(lista[6]))
        lista_personas.append(new_pasajero)

    elif (lista[0]=="Piloto"):
        l2=[]
        new_piloto=piloto()
        new_piloto.setNombre(str(lista[1]))
        new_piloto.setApellido(str(lista[2]))
        new_piloto.setFecha(lista[3])
        new_piloto.setDni(str(lista[4]))
        l2=(lista[5].split(','))
        for item in l2:
            for item2 in lista_aviones:
                if(item==item2.modelo):
                    new_piloto.addAvion(item2)
        lista_personas.append(new_piloto)

    elif (lista[0]=="Servicio"):
        new_servicio=servicio_abordo()
        lista = line.split('|')
        new_servicio.setNombre(str(lista[1]))
        new_servicio.setApellido(str(lista[2]))
        l2 = lista[3].split('-')
        new_servicio.setFecha(date (int(l2[2]) , int(l2[1]), int(l2[0])))
        new_servicio.setDni(str(lista[4]))
        l2 = (lista[5].split(','))
        for item in l2:
            for item2 in lista_aviones:
                if(item==item2.modelo):
                    new_servicio.addAvion(item2)
        l2 = (lista[6].split(','))
        for item in l2:
            new_servicio.addIdioma(item)
        lista_personas.append(new_servicio)

personas.close()

aviones = open("aviones.dat","r")
for line in aviones:
    new_avion=avion()
    lista = line.split('|')
    new_avion.setModelo(str(lista[0]))
    new_avion.setCapacidad(lista[1])
    new_avion.setTrip(lista[2])
    lista_aviones.append(new_avion)
aviones.close()

vuelos = open("vuelos.dat","r")
for line in vuelos:
    new_vuelo=vuelo()
    lista = line.split('|')
    l2=lista[0]
    for item in lista_aviones:
        if(item.modelo==l2):
            new_vuelo.setAvion(item)
    new_vuelo.setHora(str(lista[2]))
    new_vuelo.setOrigen(str(lista[3]))
    new_vuelo.setDestino(str(lista[4]))
    new_vuelo.setCodigoVuelo(str(lista[3])+str(lista[4])+str(lista[0]))
    l2 = (lista[5].split(','))
    for item in l2:
        for item2 in lista_personas:
            if(item2.dni==item):
                new_vuelo.addPasajeros(item2)
    l2 = (lista[6].split(','))
    for item in l2:
        for item2 in lista_personas:
            if(item2.dni==item):
                new_vuelo.addTrip(item2)
    lista_vuelos.append(new_vuelo)
vuelos.close()

print("Ej 1")
for item in lista_vuelos:
    print(str(item.origen)+" a "+(item.destino))
    for item2 in item.ocupantes:
        print(str(item2.nombre)+'|'+(item2.apellido)+'|'+ str(item2.fecha_nac)+'|'+(item2.dni))

print("Ej 3")
