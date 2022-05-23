class Newton:

    def __init__(self,x,f):
        self.f = f
        self.x = x
        self.y = self.f(x)
        self.polinomio = self.__polinomio(self.coefs)
        self.est = None
        self.mse = None
        self.mae = None
        self.matrix = self.__divididas(x, y)
        self.coefs = self.matrix.drop(["xi"], axis = 1).iloc[0]

    def __divididas(self,xi,fi):
        import pandas as pd
        df = pd.DataFrame([xi,fi]).transpose()
        df.columns = ["xi","fi"]     
        for i in range(1,len(df)):
            name = f"matrix{i}"
            df[name] = df.fi.diff(periods= -i)   
        df.fillna(0, inplace= True)
        return df

    def __polinomio(self,df):


    def __errores(self):
        self.mse = self.__mse(y,est)
        self.mae = self.__mae(y,est)
        return
    
    def __mse(vR , vE):
        """Para calcular el error cuadrático medio de una estimación"""
        import numpy as np 
        n = len(vR)
        if n == len(vE):
            error = np.array((vE - vR) ** 2)
            return np.sum(error)/n
        else:
            return print("Ambos vectores deben tener la misma longitud")

    def __mae(vR , vE):
        """Para calcular el error absoluto medio de una estimación"""
        import numpy as np 
        n = len(vR)
        if n == len(vE):
            error = np.abs((vE - vR))
            return np.sum(error)/n
        else:
            return print("Ambos vectores deben tener la misma longitud")

    def plot(self):
        return