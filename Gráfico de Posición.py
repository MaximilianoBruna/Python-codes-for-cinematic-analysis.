import matplotlib.pyplot as plt
import numpy as np

# Listas para almacenar los datos de tiempo y posición de cada archivo
tiempo_total = []
posicion_total = []

# Archivos a procesar, la cantidad depende de ti.
archivos = ['canicasubida1.txt', 'golfsubida1.txt', 'pinponsubida1.txt']

# Orden de los archivos, sin esto la leyenda mostrada sera errónea. Es el orden y nombre para cada curva en el gráfico.
Datos = ['Canica','Golf','Ping-Pong']


# Iterar sobre los archivos, esto no se toca.
for archivo in archivos:
    tiempo = []
    posicion = []
    with open(archivo, 'r') as f:
        for linea in f:
            campos = linea.split()
            tiempo.append(float(campos[0].replace(',', '.')))
            posicion.append(float(campos[1].replace(',', '.')))
    # Convertir listas a arrays de NumPy y almacenarlos
    tiempo_total.append(np.array(tiempo))
    posicion_total.append(np.array(posicion))

# Crear el gráfico
for i in range(len(archivos)):
    plt.plot(tiempo_total[i], posicion_total[i], marker='o', linestyle='--', label=f'{Datos[i]}')

# Configurar etiquetas y título
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m]')
plt.title('Posición en función del tiempo')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()