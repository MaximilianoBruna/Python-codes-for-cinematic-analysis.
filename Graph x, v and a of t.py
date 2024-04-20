import numpy as np
import matplotlib.pyplot as plt
import argparse
import math 


def smooth_acc(t_start,t_end,x_start,x_end):
    t_raw = []
    i = 0.0
    while i <= 1.0:
        t_raw.append(i)
        i += 0.05
    x_raw = [(math.tanh((i*math.e*2)-math.e)/2.0)+0.5 for i in t_raw]
    t = [t_start + (t_end - t_start)*float(i) for i in t_raw]
    x = [x_start + (x_end - x_start)*float(i) for i in x_raw]
    return t, x


# Recibir un archivo desde la línea de comandos 
parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()

# Definir listas para cada valor
t = []
x = []
#y = []

# Abrir el archivo
with open(args.file) as f:
    # Leer sus líneas
    lines = f.readlines()

    for line in lines:
        # Para cada línea, separarla en valores
        values = line.strip().split()

        if len(values) != 2:
            # Si no son 3 valores, ignorar esa línea
            continue

        # Si son 3 valores, asignarlos
        ti, xi, = values
        # Y agregarlos a las listas
        t.append(float(ti.replace(',', '.')))
        x.append(float(xi.replace(',', '.')))
        #y.append(float(yi.replace(',', '.')))


# Calcular la velocidad
vx = np.gradient(x, t)  # Velocity in x direction
#vy = np.gradient(y, t)  # Velocity in y direction
speed = vx  # Magnitude of velocity

# Calcular la aceleración
ax = np.gradient(vx, t)  # Acceleration in x direction
#ay = np.gradient(vy, t)  # Acceleration in y direction
acceleration = ax  # Magnitude of acceleration

# Ploteo
fig, axs = plt.subplots(3, 1, figsize=(7, 7))

# Trajectory plot (t vs. x)
axs[0].plot(t, x, label='Posición', color='blue')
axs[0].set_xlabel('Tiempo [s]')
axs[0].set_ylabel('Posición [m]')
axs[0].set_title('')
axs[0].legend()

# Speed plot (time vs. speed)
axs[1].plot(t, speed, label='Velocidad', color='orange')
axs[1].set_xlabel('Tiempo [s]')
axs[1].set_ylabel('Velocidad [m/s]')
axs[1].set_title('')
axs[1].legend()

# Acceleration plot (time vs. acceleration)
axs[2].plot(t, acceleration, label='Aceleración', color='red')
axs[2].set_xlabel('Tiempo [s]')
axs[2].set_ylabel('Aceleración [m/s^2]')
axs[2].set_title('')
axs[2].legend()

plt.tight_layout()
plt.show()
