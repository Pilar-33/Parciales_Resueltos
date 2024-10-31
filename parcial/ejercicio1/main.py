from os import system
system("cls")
from paquetes.funciones import *
from paquetes.menu import *

depositos = ["PBA", "Jujuy", "Neuquen"]
tipo_articulos = [
    "quimicos", "trapos", "escobas", 
    "cepillos", "papel higienico", 
    "jabon", "pañuelos descartables"
    ]

existencias = [
    ["PBA", "quimicos", 150000],
    ["Jujuy", "trapos", 55050],
    ["Neuquen", "escobas", 7500],
    ["PBA", "cepillos", 2000],
    ["Jujuy", "papel higienico", 3002030],
    ["Neuquen", "jabon", 9000],
    ["PBA", "pañuelos descartables", 500000],
    ["Jujuy", "quimicos", 119000],
    ["Neuquen", "trapos", 2300],
    ["PBA", "escobas", 2500000]
]
#carga de existencias
"""existencias = []
cantidad = validar_numero("Ingrese cantidad de datos a cargar: ")
print("\n         CARGA DE EXISTENCIAS")
print("="* 40)
for i in range(cantidad):
    lugar = input(f"provincia no{i+1}: ")
    while lugar not in depositos:
        lugar = input(f"Error!!. provincia no{i+1}: ")
        
    tipo_articulo = input(f"Tipo artículo no{i+1}: ")
    while tipo_articulo not in tipo_articulos:
        tipo_articulo = input(f"Error!!. Tipo artículo no{i+1}: ")
            
    cantidad = validar_numero(f"Cantidad de artículos no{i+1}: ")
    existencias += [[lugar, tipo_articulo, cantidad]]
"""
menu_opciones(existencias, depositos, tipo_articulos)