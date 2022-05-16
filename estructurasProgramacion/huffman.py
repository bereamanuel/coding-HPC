
class Nodo:
    """
    Implementamos la clase nodo, que será nuestra base del arbol
    Va a tener dos parámetros, la letra y la frecuencia. 
    """

    def __init__(self,char: str or None = None,freq:float = 0):
        """
        Inicializamos el nodo. Tiene tres propiedades:
            -(char) El carácter al que hace referencia.
            -(frec) La frecuencia con la que aparece en el texto. En caso de ser padre
                será la suma de sus hijos
            -(hijo) Los nodos hijos
        """
        self.char = char or None 
        self.freq = freq or None
        self.hijos = list()
    
class Arbol:
    """
    Para implementar el árbol.
    """

    def __init__(self, freq_dict):
        """
        Inicializamos el arbol dado un diccionario de letra -> frecuencia
        La construccion de abajo a arriba. 
        """
        # En caso de que solo hay un elemento, entonces esa es la raiz con valor de frecuencia 1 y si no hay frecuencia, entonces no devolvemos nada.
        self.raiz = None if not len(freq_dict)==1 else Nodo(list(freq_dict.keys())[0],1)  
        if not freq_dict:
            return    
        ## Como tenemos que tener el diccionario ordenado, es lo primero que hacemos. 
        dictOrder = sorted(freq_dict.items(), key=lambda x: x[1])

        ##Vamos a crear un nodo por cada valor del diccionario.
        nodos = [Nodo(x[0].upper(),x[1]) for x in dictOrder]
        
        #Mientras queden por agregar
        while nodos:
            x1 = nodos.pop(0)
            x2 = nodos.pop(0)

            padre = Nodo(freq= x1.freq + x2.freq)
            padre.hijos = [x1,x2]

            if not nodos:
                self.raiz = padre
            else:
                # Si aún quedan items, agregar el nodo de conexión a la lista y ordenarla por frecuencias
                nodos.append(padre)
                nodos.sort(key=lambda x: x.freq)


    def amplitud(self):
        """
        Genera una lista de los nodos ordenados por amplitud.
        """
        from cola import Cola
        l = []
        if not self.raiz:
            return l
        c = Cola()
        c.encolar(self.raiz)
        while not c.estaVacia():
            x = c.desencolar()
            l.append({"char":x.char, "freq": x.freq, "hijos": x.hijos})
            for child in x.hijos:
                c.encolar(child)        
        return l

    def toCode(self):
        #Si no tiene hijos, entonces le asignamos un 0
        if not self.raiz.hijos:
            return {self.raiz.char: '0'}

        #En caso de que tengamos hijos, inicializamos el diccionario y llamamos a la función auxiliar que es recursiva.
        codeDict = dict()
        self.__asignarCodeChar(codeDict, self.raiz, '')

        return codeDict

    def __asignarCodeChar(self, codeDict, nodo, codigo):
        """
        Esta función, le metemos el diccionario que estamos generando, 
        el nodo y le vamos añadiendo el código que le corresponde, 
        en función de su posición en la lista que contiene los hijos,
        la posición 0 de la lista se le asigna un 0 y en la posición 1, le añadimos un 1.
        """
        #Le asignamos codigo, solo a las letras asignadas, por eso los nodos tienen valor None 
        #cuando son padres.
        if nodo.char:
            codeDict[nodo.char] = codigo
        
        #Si tiene longitud 2, quiere decir que tiene hijos, entonces llamamos recursivamente a la función.
        #Así, vamos añadiendo el código que le corresponda a cada una de las letras.
        if len(nodo.hijos) == 2:
            self.__asignarCodeChar(codeDict, nodo.hijos[0], codigo +'0')
            self.__asignarCodeChar(codeDict,  nodo.hijos[1],  codigo +'1')

    def codificar(self,string):
        """
        Dada una cadena de caracteres, codificación de la cadena.
        """
        codificacion = ''
        for c in string:
            codificacion += self.toCode()[c.upper()]
        return codificacion


