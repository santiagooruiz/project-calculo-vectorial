import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
num_bodies = 5
np.random.seed(0)

# Posiciones iniciales aleatorias
positions = np.random.rand(num_bodies, 2) * 10 - 5
velocities = np.random.randn(num_bodies, 2) * 0.05

# Masa (todas iguales para simplificar)
mass = np.ones(num_bodies)

# Constante gravitacional (ajustada para que no salgan volando)
G = 0.1

# Función para actualizar posiciones y velocidades
def update(frame):
    global positions, velocities
    
    # Calcular fuerzas gravitacionales
    for i in range(num_bodies):
        force = np.zeros(2)
        for j in range(num_bodies):
            if i != j:
                r = positions[j] - positions[i]
                dist = np.linalg.norm(r) + 0.1  # Evitar división por 0
                force += G * mass[i] * mass[j] * r / dist**3
        velocities[i] += force
    positions += velocities

    # Actualizar puntos en el gráfico
    scat.set_offsets(positions)
    return scat,

# Configurar la figura
fig, ax = plt.subplots()
scat = ax.scatter(positions[:, 0], positions[:, 1], s=50)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Crear animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)
plt.show()
