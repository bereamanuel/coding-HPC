def mse(vR , vE):
    """Para calcular el error cuadrático medio de una estimación"""
    import numpy as np 
    n = len(vR)
    if n == len(vE):
        error = np.array((vE - vR) ** 2)
        return np.sum(error)/n
    else:
        return print("Ambos vectores deben tener la misma longitud")

def mae(vR , vE):
    """Para calcular el error absoluto medio de una estimación"""

    import numpy as np 
    n = len(vR)
    if n == len(vE):
        error = np.abs((vE - vR))
        return np.sum(error)/n
    else:
        return print("Ambos vectores deben tener la misma longitud")
        