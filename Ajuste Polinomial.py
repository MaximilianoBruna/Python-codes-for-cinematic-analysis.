import numpy as np
from scipy.optimize import curve_fit

# Función polinomial para ajustar los datos
def funcion_polinomial(tiempo, a, b, c):
    return a * tiempo ** 2 + b * tiempo + c

# Archivo a procesar
archivos = ['canicasubida1.txt']

# Listas para almacenar los datos de tiempo y posición de todos los archivos
tiempo_total = []
posicion_total = []

# Iterar sobre los archivos
for archivo in archivos:
    tiempo = []
    posicion = []
    with open(archivo, 'r') as f:
        for linea in f:
            campos = linea.split()
            tiempo.append(float(campos[0].replace(',', '.')))
            posicion.append(float(campos[1].replace(',', '.')))
    # Almacenar los datos de tiempo y posición
    tiempo_total.extend(tiempo)
    posicion_total.extend(posicion)

# Convertir listas a arrays de NumPy
tiempo_total = np.array(tiempo_total)
posicion_total = np.array(posicion_total)

# Ajustar una curva polinomial a los datos
parametros_optimizados, _ = curve_fit(funcion_polinomial, tiempo_total, posicion_total)

# Imprimir los parámetros de la función ajustada
print("Parámetros de la función ajustada:")
print("a =", parametros_optimizados[0])
print("b =", parametros_optimizados[1])
print("c =", parametros_optimizados[2])

# Definir la función ajustada
def posicion_funcion(tiempo,a,b,c):
    return a * tiempo ** 2 + b * tiempo + c
def velocidad_funcion(tiempo,a,b,c):
    return 2*a*tiempo + b + c*0
def aceleracion_funcion(tiempo,a,b,c):
    return 2*a+ b*0 + c*0

# Ejemplo de uso de la función ajustada
tiempo_ejemplo = 0.43  # Ejemplo de tiempo
posicion_ejemplo = posicion_funcion(tiempo_ejemplo,*parametros_optimizados)
velocidad_ejemplo= velocidad_funcion(tiempo_ejemplo,*parametros_optimizados)
aceleración_ejemplo= aceleracion_funcion(tiempo_ejemplo,*parametros_optimizados)
print(f"La posición en el tiempo {tiempo_ejemplo} es {posicion_ejemplo}")
print(f"La velocidad en el tiempo {tiempo_ejemplo} es {velocidad_ejemplo}")
print(f"La aceleración promedio es {aceleración_ejemplo}")