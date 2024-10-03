import numpy as np

def dyn_generator(y):
    """
    Genera la dinámica del sistema dada una matriz O y un estado y(t).
    
    Esta función calcula la evolución temporal de un sistema dinámico, 
    utilizando una matriz constante O y el estado actual del sistema y(t).
    
    Parameters:
    ----------
    y : ndarray
        El estado actual del sistema, representado como un array de números complejos.
        
    Returns:
    -------
    dy_dt : ndarray
        La derivada temporal del estado y(t), calculada como -i[O, y].
    
    Example:
    --------
    >>> O = np.array([[0, -1], [1, 0]])  # Matriz O (constante)
    >>> y = np.array([1, 0], dtype=complex)  # Estado inicial
    >>> dyn_generator(y)
    array([0.+1.j, 0.+0.j])
    """
    O = np.array([[0, -1], [1, 0]])  # Matriz O (ajustable según el problema)
    return -1j * np.dot(O, y)


def rk4(dyn_generator, y0, t0, tf, dt):
    """
    Implementa el método de Runge-Kutta de cuarto orden (RK4) para resolver 
    ecuaciones diferenciales ordinarias (EDOs).
    
    Esta función resuelve una ecuación diferencial de la forma dy/dt = f(t, y)
    utilizando el método de Runge-Kutta de cuarto orden (RK4).
    
    Parameters:
    ----------
    dyn_generator : function
        La función que genera la dinámica del sistema, que toma el estado `y`
        como argumento y devuelve la derivada temporal dy/dt.
    y0 : ndarray
        El estado inicial del sistema.
    t0 : float
        El tiempo inicial.
    tf : float
        El tiempo final.
    dt : float
        El paso de tiempo para el método numérico.
        
    Returns:
    -------
    t_values : ndarray
        Los valores de tiempo a lo largo de la simulación.
    y_values : ndarray
        Los valores del estado del sistema en cada paso de tiempo.
    
    Example:
    --------
    >>> y0 = np.array([1, 0], dtype=complex)  # Estado inicial
    >>> t0 = 0  # Tiempo inicial
    >>> tf = 10  # Tiempo final
    >>> dt = 0.01  # Paso de tiempo
    >>> t_values, y_values = rk4(dyn_generator, y0, t0, tf, dt)
    """
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

