import numpy as np
from scipy.optimize import curve_fit
import argparse
from scipy.integrate import quad
# Función exponencial para ajustar los datos
def funcion_exponencial(tiempo, a, b, c):
    return a * np.exp(b * tiempo) + c

# Función para calcular la velocidad (primera derivada de la función exponencial)
def velocidad_funcion_exponencial(tiempo, a, b, c):
    return a * b * np.exp(b * tiempo)

# Función para calcular la aceleración (segunda derivada de la función exponencial)
def aceleracion_funcion_exponencial(tiempo, a, b, c):
    return a * (b ** 2) * np.exp(b * tiempo) 

# Archivo a procesar
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

# Listas para almacenar los datos de tiempo y posición
tiempo_total = []
posicion_total = []

# Leer los datos del archivo
with open(args.file) as f:
    for linea in f:
        campos = linea.split()
        # Convertir los datos de tiempo y posición a tipo flotante
        tiempo_total.append(float(campos[0].replace(',', '.')))
        posicion_total.append(float(campos[1].replace(',', '.')))

# Convertir las listas a arrays de NumPy
tiempo_total = np.array(tiempo_total)
posicion_total = np.array(posicion_total)

# Especificar valores iniciales para los parámetros de la función exponencial
parametros_iniciales = [1, 0.1, 0]  # Ajusta los valores según los datos

# Ajustar una curva exponencial a los datos
parametros_optimizados, _ = curve_fit(funcion_exponencial, tiempo_total, posicion_total, p0=parametros_iniciales, maxfev=2000)

# Imprimir los parámetros de la función ajustada
print("Parámetros de la función exponencial ajustada:")
print(f"a = {parametros_optimizados[0]}")
print(f"b = {parametros_optimizados[1]}")
print(f"c = {parametros_optimizados[2]}")

# Tiempo de ejemplo para calcular la velocidad y la aceleración
tiempo_ejemplo = 5

# Calcular la velocidad en el tiempo de ejemplo
posicion_ejemplo = funcion_exponencial(tiempo_ejemplo, *parametros_optimizados)
print(f"La posición en el tiempo {tiempo_ejemplo} es {posicion_ejemplo}")

# Calcular la velocidad en el tiempo de ejemplo
velocidad_ejemplo = velocidad_funcion_exponencial(tiempo_ejemplo, *parametros_optimizados)
print(f"La velocidad en el tiempo {tiempo_ejemplo} es {velocidad_ejemplo}")

# Calcular la aceleración en el tiempo de ejemplo
aceleracion_ejemplo = aceleracion_funcion_exponencial(tiempo_ejemplo, *parametros_optimizados)
print(f"La aceleración en el tiempo {tiempo_ejemplo} es {aceleracion_ejemplo}")

# Intervalo de tiempo para calcular el promedio de la aceleración
ti = 5  # Tiempo inicial del intervalo
tf = 5.5  # Tiempo final del intervalo

# Calcular la integral de la función de aceleración en el intervalo de tiempo
# Usamos la función lambda para pasar los parámetros `a`, `b`, y `c` a la función `aceleracion_funcion_exponencial`
integral, error = quad(lambda t: aceleracion_funcion_exponencial(t, *parametros_optimizados), ti, tf)

# Calcular el promedio de la aceleración en el intervalo de tiempo
promedio_aceleracion = integral / (tf - ti)
print(f"El promedio de la aceleración entre {ti} y {tf} es {promedio_aceleracion}")