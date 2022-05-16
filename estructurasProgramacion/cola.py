class Cola:
    def __init__(self):
        #Inicialiazamos la cola con una lista vacía.
        self.__cola=list()
    
    def estaVacia(self):
        #Creamos una función que nos dice si la cola está vacía o no.
        return not self.__cola

    def primero(self):
        #Con esta función obtenemos el siguiente elemento en salir.
        try:
            return self.__cola[0]
        except:
            return None
    
    def encolar(self,elemento):
        #Con esta función modificamos el estado de nuestra cola, añadimos un elemento
        self.__cola.append(elemento)

    def desencolar(self):
        #Con esta función modificamos el estado de nuestra cola, además,
        #nos devuelve el elemento que tenía que salir, es decir, el primero en entrar.
        try:
            return self.__cola.pop(0)
        except:
            None