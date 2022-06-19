import random, time
from threading import Thread, Lock, Event
from cliente import Cliente
from barbero import Barbero 


class BarberShop:

    def __init__(self, barbero, numeroSitios):
        self.barbero = Barbero()
        self.numeroSitios = numeroSitios

        self.mutex = Lock()
        #Intervalos de tiempo para cada componente
        self.clienteIntervaloMin = 0
        self.clienteIntervaloMax = 8 
        self.corteMin = 5
        self.corteMax = 15
        self.clientesEsperando = []
        self.clientesReintentar = []


        print("La Barberia se abre con {0} sitios.\n".format(numeroSitios))
        print("Tiene un tiempo de espera por cliente entre {0} y {1} min.\n".format(self.clienteIntervaloMin, self.clienteIntervaloMax))
        print("El Barbero tarda en cortar el pelo entre {0} y {1} min.\n".format(self.corteMin,self.corteMax))

    def abrir(self):
        """Para inicializar la apertura de la barbería."""
        print("Abre la barbaeria.\n")
        worker = Thread(target=self.trabajar)     
        worker.start()


    def trabajar(self):
        """
        Esta funcion es la que direcciona si tiene que cortar el pelo el barbero o irse a dormir.
        Estará activa durante todo el programa.
        """
        while True:
            #Trabajamos solo con un cliente a la vez, entonces activamos el cerrojo.
            self.mutex.acquire()

            if len(self.clientesEsperando) > 0:
                #Sacamos al primero de la lista de espera
                c = self.clientesEsperando.pop(0)
                #Liberamos el cerrojo antes de que termine de cortar el pelo, para que entren mas cliente.
                self.mutex.release()
                self.barbero.cortarPelo(c)            
            
            else:
                self.mutex.release()
                print("\tEl barbero duerme.\n")
                self.barbero.dormir()
                print("\tEl barbero despierta.\n")
        

    def entrar(self, cliente):
        """
        Esta función intenta entrar en la barberia, si no hay asientos, va a la cola de espera reintentar
        En caso de tener sitio, se sienta en la sala de espera y cuando el barbero termina, va atendiendo al resto de clientes.
        """
        self.mutex.acquire()
        print("{0} ha entrado en la barberia, busca un asiento.\n".format(cliente.nombre))
        if len(self.clientesEsperando) == self.numeroSitios :
            print("La sala de espera esta llena, {0} volvera a intentarlo.\n".format(cliente.nombre))
            self.clientesReintentar.append(cliente)
            self.mutex.release()
        else:
            print("{0} se ha sentado a esperar su corte de pelo.\n".format(cliente.nombre))
            self.clientesEsperando.append(cliente)
            self.mutex.release()
            self.barbero.despertar()


    def reintentar(self, clientesReintentar):  
        """
        Esta funcion es analoga a entrar, lo único que no volverá a intentarlo.
        """    
        self.mutex.acquire()
        c = clientesReintentar.pop(0)
        print("{0} ha entrado en la barberia, busca un asiento.\n".format(c.nombre))  
        if len(self.clientesEsperando) == self.numeroSitios :
            print("La sala de espera siguen estando llena, {0} se marcha.\n".format(c.nombre))
            self.mutex.release()
        else:
            print("{0} se ha sentado a esperar su corte de pelo.\n".format(c.nombre))
            self.clientesEsperando.append(c)
            self.mutex.release()
            self.barbero.despertar()


    
