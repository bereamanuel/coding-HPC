import pandas as pd 
class ContarLetras:
    def __init__(self, texto):
        #Creamos el texto sin puntos ni comas, además normalizamos a mayuculas.
        texto = "".join([str(x).upper() for x in texto if x not in {'.',' '}])

        #Gracias a la librería pandas, podemos contar las letras de forma sencilla y así calcular las frecuencias.
        self.serie = pd.Series(list(texto)).value_counts() / len(texto)

        #Además, podemos acceder al texto normalizado.
        self.texto = texto

        #Dada la serie generada por pandas, generar el diccionario.
        self.diccionario = self.serie.to_dict()

    


    
