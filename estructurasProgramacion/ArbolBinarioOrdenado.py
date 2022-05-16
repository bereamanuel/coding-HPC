class ArbolBinarioOrdenado:

    def __init__(self):
        self.__raiz = None
        self.__arbolIzdo = None
        self.__arbolDcho = None

    def raiz(self):
        return self.__raiz
    
    def arbolIzdo(self):
        return self.__arbolIzdo

    def arbolDcho(self):
        return self.__arbolDcho

    def estVacio(self):
        return self.__raiz == None

    def insertarElem(self,elemento):
        if self.estVacio():
            self.__raiz = elemento
            self.__arbolIzdo = ArbolBinarioOrdenado()
            self.__arbolDcho = ArbolBinarioOrdenado()
        elif elemento<=self.__raiz:
            self.__arbolIzdo.insertarElem(elemento)
        elif elemento>self.__raiz:
            self.__arbolDcho.insertarElem(elemento)
        else:
            None
    def tieneElemento(self, elemento):
        if self.estVacio():
            return False
        elif self.__raiz==elemento:
            return True
        elif elemento<self.__raiz:
            return self.__arbolIzdo.tieneElemento(elemento)
        else:
            return elf.__arbolDcho.tieneElemento(elemento)

    def numElementos(self):
        if self.estVacio():
            return 0
        else:
            return self.__arbolIzdo.numElementos() + self.__arbolDcho.numElementos() +1
    
    def preOrden(self):
        l=[]
        l.append(self.__raiz)
        if not self.__arbolIzdo.estVacio():
            l += self.__arbolIzdo.preOrden()
        if not self.__arbolDcho.estVacio():
            l += self.__arbolDcho.preOrden()
        return l
    
    def inOrden(self):
        l=[]
        if not self.__arbolIzdo.estVacio():
            l += self.__arbolIzdo.inOrden()
        l.append(self.__raiz)
        if not self.__arbolDcho.estVacio():
            l += self.__arbolDcho.inOrden()
        return l

        
    def preorder(self):
        from pila import Pila
        
        l = []
        #Si nuestro árbol está vacio, devuelve una lista vacía.
        if self.__raiz is None:
            return l 

        #Inicializamos una pila e introducimos nuestro árbol completo.
        p = Pila()
        p.apilar(self)

        #Empezamos la iteración, hasta que la pila esté vacía, entonces habremos acabado.
        while not p.estaVacia():
            #Generamos un marcador, desapilando el ultimo elemento en entrar en la pila. 
            x = p.desapilar()

            #Añadimos la raiz a la lista que será nuestra solución.
            l.append(x.__raiz)  

            #Si tenemos arbol derecho, lo metemos en la pila.
            if not x.__arbolDcho.estVacio():
                p.apilar(x.__arbolDcho)
                
            #Si tenemos arbol izquierdo, lo metemos en la pila
            if not x.__arbolIzdo.estVacio():
                p.apilar(x.__arbolIzdo)     
                
        return l



    def inorder(self):
        from pila import Pila 
        l = []

        #Inicializamos una pila e introducimos nuestro árbol completo.
        p = Pila()
        x = self
        
        #Empezamos la iteración, hasta que la pila esté vacía o el nodo distinto de None, entonces habremos acabado.
        while x!=None or not p.estaVacia():

            #Si el nodo tiene información, entonces apilamos e nos colocamos el arbol izquierdo(sea vacio o no).
            if x != None :
                p.apilar (x)
                x = x.__arbolIzdo
            #En caso de que el nodo sea vacío(quiere decir que que no había arbol izquierdo), entramos en esta parte del codigo.
            else:
                #Sacamos el ultimo nodo introducido en la pila y lo marcamos.
                x = p.desapilar()
                #Si tiene información, entonces lo añadimos a la lista
                if x.__raiz:
                    l.append(x.__raiz)

                #asignamos al marcado el arbol derecho.
                x = x.__arbolDcho        
        return l

    def amplitud(self):
        from cola import Cola

        l = []
        #Comprobamos si el arbol esta vacío.
        if self.estVacio():
            return l

        #Inicializamos la cola e introducimos el árbol, ya que la raíz será el primero en salir.
        c = Cola()
        c.encolar(self)
        
        #Vamos a realizar un bucle hasta que no haya elementos en la cola.
        while not c.estaVacia():
            #Desencolamos y añadimos a la solucion
            x = c.desencolar()
            l.append(x.__raiz)

            #Si tenemos arbol izquierdo lo añadimos a la cola
            if not x.__arbolIzdo.estVacio():
                c.encolar(x.__arbolIzdo)
            
            #Si tenemos arbol derecho lo añadimos a la cola
            if not x.__arbolDcho.estVacio():
                c.encolar(x.__arbolDcho)
        return l
            



        