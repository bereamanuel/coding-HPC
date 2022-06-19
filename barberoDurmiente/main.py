from threading import Thread, Lock, Event
import time, random
from cliente import Cliente
from barbero import Barbero
from barberShop import BarberShop

mutex = Lock()

#Intervalos de tiempo para cada componente
clienteIntervaloMin = 0
clienteIntervaloMax = 8
corteMin = 5 
corteMax = 15

if __name__=='__main__':
    clientes = []
    clientes.append(Cliente("Manuel"))
    clientes.append(Cliente("Alba"))
    clientes.append(Cliente("Miriam"))
    clientes.append(Cliente("Jose"))
    clientes.append(Cliente("Rodrigo"))
    clientes.append(Cliente("Ana"))

    barbero = Barbero()

    barberia = BarberShop(barbero, numeroSitios = 3)
    barberia.abrir()

    while len(clientes) >0 or len(barberia.clientesReintentar) > 0:
        if len(barberia.clientesReintentar) > 0:
            barberia.reintentar(barberia.clientesReintentar)
            tiempoEspera = random.randrange(clienteIntervaloMin, clienteIntervaloMax)
            time.sleep(tiempoEspera)
        else:
            #Sacamos el primero en entrar en la cola
            c = clientes.pop(0)
            barberia.entrar(c)
            tiempoEspera = random.randrange(clienteIntervaloMin, clienteIntervaloMax)
            time.sleep(tiempoEspera)