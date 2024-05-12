# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.optimize import linprog
import numpy as np

# Costo de energía por hora para los dos aparatos
costo_aparato1 = [10, 12, 14, 16, 14, 12, 10, 8, 6, 8, 10, 12, 14, 16, 14, 12, 10, 8, 6, 8, 10, 12, 14, 16]
costo_aparato2 = [1.0, 1.2, 1.4, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]

# Vector de costos c
c = costo_aparato1 + costo_aparato2

# Restricciones de encendido/apagado para un aparato
A_eq_aparato = [[1 if j == i or j == i + 1 or j == i + 2 or j == i + 3 else 0 for j in range(24)] for i in range(21)]

# Restricciones para ambos aparatos
A_eq = []
for row in A_eq_aparato:
    A_eq.append(row + [0] * 24)
for row in A_eq_aparato:
    A_eq.append([0] * 24 + row)

# Vector b_eq
b_eq = [1] * 42

# Límites para las variables
bounds = [(0, 1)] * 48

# Resolver el problema de programación lineal
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Imprimir el resultado
if resultado.success:
    print("Solución óptima encontrada:")
    for i in range(24):
        print(f"Aparato 1, Hora {i}: {'Encendido' if resultado.x[i] > 0.5 else 'Apagado'}")
        print(f"Aparato 2, Hora {i}: {'Encendido' if resultado.x[i + 24] > 0.5 else 'Apagado'}")
    print(f"Costo total mínimo: ${resultado.fun}") # Aquí se imprime el costo total mínimo
else:
    print("La optimización no fue exitosa.")
    print("Mensaje:", resultado.message)
