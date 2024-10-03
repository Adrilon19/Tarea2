#Explicacion del metodo numerico de Runge Kutta

El metodo es para aproximar un valor 
y
0
 de una ecuacion diferencial asociado a un cierto valor 
x
0
.

Este metodo evalua de manera reitarada valores en base a cierto paso, llamese h, para aproximar el valor.

\begin{equation} y_{n+1} = y_{n} + \frac{1}{6}(k_{1} + 2k_{2} + 2k_{3} + k_{4})\ \end{equation}

En las que las 
k
1
, 
k
2
, 
k
3
 y 
k
4
 estan dadas por:

\begin{equation} k_{1} = hf(x_{n} , y_{n} )\ \end{equation}

\begin{equation} k_{2} = hf(t_{n} + \frac{h}{2},y_{n} + \frac{k_{1}}{2})\ \end{equation}

\begin{equation}
k_{3} = hf(t_{n} + \frac{h}{2},y_{n} + \frac{k_{1}}{2})\ \end{equation}

\begin{equation} k_{4} = hf(t_{n} + h,y_{n} + k_{3})\ \end{equation}
