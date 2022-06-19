import random, time
from threading import Thread, Lock , Event




class Barbero:
    #La clase barbero va a tener 3 métodos, dormir, despertar y cortar el pelo. Mientras no hay nadie esperando
    #el barbero se duerme, cuando entra alguien a la tienda, entonces despierta y se pone a cortar el pelo.
    trabajando = Event()
    mutex = Lock()
    #Intervalos de tiempo para cada componente
    clienteIntervaloMin = 0
    clienteIntervaloMax = 8 
    corteMin = 5 
    corteMax = 15
    def dormir(self):
        self.trabajando.wait()

    def despertar(self):
        self.trabajando.set()


    def cortarPelo(self, cliente):
        self.trabajando.clear()

        print("\tEl barbero esta cortando el pelo a {0}.\n".format(cliente.nombre))

        tiempoCorte = random.randrange(self.corteMin, self.corteMax)

        time.sleep(tiempoCorte)

        print("\t{0} ya tiene el pelo cortado.\n".format(cliente.nombre))
