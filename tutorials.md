# Método RK4 para Resolver Ecuaciones Diferenciales

El objetivo de este tutorial es mostrar cómo utilizar el método de Runge-Kutta de orden 4 (RK4) para resolver el problema dinámico de valor inicial:

$$
\frac{dy}{dt} = f(t, y), \quad y(t_0) = y_0.
$$

En este caso específico, consideramos la función:

$$
f(t, y) = -i[O, y(t)],
$$

donde no hay dependencia explícita del tiempo en la función \(f(t, y)\).

## Ejemplo de Uso

A continuación, se presenta un ejemplo de cómo implementar el método RK4 para resolver la ecuación mencionada.

```python
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función dinámica
def dyn_generator(y):
    # Ejemplo de una dinámica, ajuste según sea necesario
    return -1j * np.dot(O, y)  # O es una matriz que debes definir

# Implementación del método RK4
def rk4(dyn_generator, y0, t0, tf, dt):
    t_values = np.arange(t0, tf, dt)
    y_values = np.zeros((len(t_values), len(y0)), dtype=complex)
    y_values[0] = y0

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        k1 = dt * dyn_generator(y)
        k2 = dt * dyn_generator(y + 0.5 * k1)
        k3 = dt * dyn_generator(y + 0.5 * k2)
        k4 = dt * dyn_generator(y + k3)
        y_values[i] = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values

# Parámetros iniciales
y0 = np.array([1, 0])  # Estado inicial
t0 = 0  # Tiempo inicial
tf = 10  # Tiempo final
dt = 0.01  # Paso de tiempo

# Ejecución del RK4
t_values, y_values = rk4(dyn_generator, y0, t0, tf, dt)

# Gráfica de resultados
plt.plot(t_values, np.abs(y_values[:, 0]), label='|y1|')
plt.plot(t_values, np.abs(y_values[:, 1]), label='|y2|')
plt.title('Evolución Temporal del Estado')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

