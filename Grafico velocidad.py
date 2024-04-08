import matplotlib.pyplot as plt
import numpy as np

# Función para calcular la velocidad utilizando la diferencia finita
def calcular_velocidad(posicion, tiempo):
    velocidad = np.diff(posicion) / np.diff(tiempo)
    tiempo_velocidad = (tiempo[:-1] + tiempo[1:]) / 2  # Tomar el punto medio de cada intervalo de tiempo
    return tiempo_velocidad, velocidad

# Archivos a procesar, la cantidad depende de ti.
archivos = ['CanicaBajada1.txt', 'GolfBajada1.txt', 'Ping-PongBajada1.txt']

# Orden de los archivos, sin esto la leyenda mostrada sera errónea. Es el orden y nombre para cada curva en el gráfico.
Datos = ['Canica', 'Golf', 'Ping-Pong']


# Crear el gráfico
plt.figure()

#No tocar :).
i = 0
for archivo in archivos:
    tiempo = []
    posicion = []
    with open(archivo, 'r') as f:
        for linea in f:
            campos = linea.split()
            tiempo.append(float(campos[0].replace(',', '.')))
            posicion.append(float(campos[1].replace(',', '.')))
    
    tiempo = np.array(tiempo)
    posicion = np.array(posicion)
    
    # Calcular la velocidad
    tiempo_velocidad, velocidad = calcular_velocidad(posicion, tiempo)
    
    # Graficar la velocidad en función del tiempo
    plt.plot(tiempo_velocidad, velocidad, marker='o', linestyle='-', label=f'{Datos[i]}')
    i+= 1

# Configurar etiquetas y título
plt.xlabel('Tiempo [s]')
plt.ylabel('Velocidad [m/s]')
plt.title('Velocidad en función del tiempo')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
