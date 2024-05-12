# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:42:19 2023

@author: Jaime
"""
#==============================================================================
# EJEMPLO 1 DE SMART GRID ALGORITMO
#============================================================================== 
from scipy.optimize import linprog

# Tarifas de electricidad por hora (por ejemplo, 24 horas)
tarifas = [10, 12, 14, 16, 14, 12, 10, 8, 6, 8, 10, 12, 14, 16, 14, 12, 10, 8, 6, 8, 10, 12, 14, 16]

# Consumo de energía del dispositivo por hora (por ejemplo, lavadora)
consumo_por_hora = 2

# Duración total del dispositivo en horas (por ejemplo, 4 horas)
duracion_total = 4

# Coeficientes para la función objetivo (minimizar el costo total)
c = tarifas

# Matriz de restricciones de igualdad (asegurar que el dispositivo funcione durante la duración total)
A_eq = [[1 if i <= j < i + duracion_total else 0 for j in range(24)] for i in range(24 - duracion_total + 1)]
b_eq = [1] * (24 - duracion_total + 1)

# Restricciones de límites (el dispositivo puede estar encendido o apagado en cada hora)
bounds = [(0, 1)] * 24

# Resolver el problema de programación lineal
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Imprimir la programación óptima
print("Programación óptima del dispositivo:")
for hora, x in enumerate(resultado.x):
    if x > 0.5:
        print(f"Hora {hora}: Encendido")
    else:
        print(f"Hora {hora}: Apagado")

# Imprimir el costo total
print(f"Costo total: ${sum(tarifas[i] * consumo_por_hora * x for i, x in enumerate(resultado.x))}")
