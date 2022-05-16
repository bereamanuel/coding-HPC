class Pila():
    """
    Definición de mi primera pila
    Propiedades, se carga y descarga. Lo primero en entrar, es lo ultimo en salir.
    Se podría comprar con un tubo de lacasitos. El primero en introducirse, es el ultimo en comerse.

    Tenemos un objeto que podemos consultar si está vacio, ver el ultimo elemento en entrar, que recordarmos
    que es el último en salir. Y además tenemos la opción de introducir más elementos o sacarlos.
    """

    def __init__(self):
        self.__pila = list()
    
    def estaVacia(self):
        return not self.__pila

    def cima(self):
        try:
            return self.__pila[-1]
        except:
            return None 
    
    def apilar(self, elemento):
        self.__pila.append(elemento)
        

    def desapilar(self):
        try:
            return self.__pila.pop()
        except:
            None