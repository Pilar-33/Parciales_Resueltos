from os import system
system("cls")

from funciones import*
from menu import*

depositos = ["PBA", "Jujuy", "Neuquen"]
tipo_articulos = [
    "quimicos", "trapos", "escobas", 
    "cepillos", "papel higienico", 
    "jabon", "pañuelos descartables"
    ]

existencias = [
    [2800, 457956, 1899, 13353, 2345, 65478, 89565],
    [1235, 1780, 23456, 98765, 2321, 11223, 2445],
    [98765, 45678, 34567, 2234, 67890, 1223, 44556],
]

#inicializando la matriz
"""n_depositos = len(depositos)
n_tipo_articulos = len(tipo_articulos)
existencias = []
for i in range(n_depositos):
    fila = [0] * n_tipo_articulos
    existencias += [fila]

# cargando existencias
for i in range(n_depositos):
    print(f"Existencias del depósito {depositos[i]}\n" + "=" * 30)
    for j in range(n_tipo_articulos):
        cantidad = validar_numero(f"Cantidad de {tipo_articulos[j]}: ")
        existencias[i][j] = cantidad
    print("")"""
menu(existencias, depositos, tipo_articulos)