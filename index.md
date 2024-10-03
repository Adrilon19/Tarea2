# Documentación del Método RK4

## Introducción al Problema a Resolver

En el campo de la dinámica, uno de los problemas más comunes es resolver ecuaciones diferenciales de valor inicial, que se pueden expresar en la forma general:

\[
\frac{dy}{dt} = f(t, y)
\]

con la condición inicial \( y(t_0) = y_0 \). Este tipo de problemas es fundamental en diversas aplicaciones de la física y la ingeniería, ya que nos permite modelar el comportamiento de sistemas dinámicos a lo largo del tiempo.

En esta tarea, nos enfocaremos en el método de Runge-Kutta de cuarto orden (RK4) para resolver el problema específico donde la función \( f(t, y) \) está dada por:

\[
f(t, y) = -i[O, y(t)]
\]

En este caso, es importante destacar que la función \( f(t, y) \) no presenta una dependencia explícita del tiempo \( t \). Esto simplifica el análisis y la implementación del método RK4, ya que se puede considerar que la evolución del sistema está dictada únicamente por el estado actual \( y(t) \).

El método RK4 es un algoritmo numérico que proporciona una aproximación precisa de la solución de la ecuación diferencial a través de una serie de pasos iterativos, permitiendo calcular el valor de \( y \) en instantes discretos de tiempo. A lo largo de esta documentación, exploraremos la formulación del método, su implementación y aplicaremos el RK4 al problema mencionado, analizando su comportamiento y resultados.

