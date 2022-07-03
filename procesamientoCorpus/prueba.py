import pandas as pd
import multiprocessing as mp
import  time



#funcion principal
def procesar_df(df):
  #crea nuevo dataframe
  nuevo=pd.DataFrame(columns=['Team',"Media Anotadas","Media Recibidas"])
  #obtiene el nombre del grupo
  nombre=set(df['Team']).pop()
  #calcula medias
  media_anotadas=df['RS'].mean()
  media_recibidas=df['RA'].mean()
  #añade la fila al dataframe
  nuevo=nuevo.append({'Team':nombre,'Media Anotadas':media_anotadas,'Media Recibidas':media_recibidas},ignore_index=True)
  return nuevo

if __name__=="__main__":
    #crea nuevo dataframe a partir de csv
    dataframe= pd.read_csv("D:\\Universidad\\MASTER UNIR\\Programación científica\\trabajos\\Recorrido de arboles\\procesamientoCorpus\\baseball.csv")
    #agrupa el dataframe por equipos
    dataframe_agrupado=dataframe.groupby("Team")
    
    lista_grupos=list(dataframe_agrupado)
    print("--------")
    print(lista_grupos[0])
    
    #crea lista de nombres sin repetición
    lista=set(dataframe['Team'])
    
    nuevo=pd.DataFrame()
    
    inicio=time.time()
    for nombre in lista:
        nuevo=nuevo.append(procesar_df(dataframe_agrupado.get_group(nombre)))
    print("Ejecucion secuencial",time.time()-inicio)
    print(nuevo)
    #crea los trozos que se van a enviar en paralelo
    trozos=list()
    for nombre in lista:
        
        trozos.append(dataframe_agrupado.get_group(nombre))
   
    #se crea el pool de procesos, decide cuantos procesos crear
    with mp.Pool(2) as pool:
    #se invoca a la función y se concatenan los resultados de cada trozo con pd.concat(resultados del map)
        inicio=time.time()
        nuevo = pd.concat(pool.map(procesar_df, trozos),ignore_index=True)
        print(f"Con multiprocessing {time.time()-inicio} s")
    print(nuevo)