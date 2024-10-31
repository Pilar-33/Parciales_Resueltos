from os import system
system("cls")

inventario = [
    ["Manzanas", 2.50, 50],
    ["Plátanos", 1.80, 30],
    ["Peras", 3.00, 20],
    ["Naranjas", 2.20, 40],
    ["Uvas", 4.00, 15],
    ["Sandías", 7.50, 10],
    ["Melones", 5.00, 12],
    ["Kiwi", 1.50, 25],
    ["Piñas", 6.20, 8],
    ["Fresas", 3.80, 35]
]

# Mostrar la matriz inventario no 1
#inventario = cargar_datos()
"""print(" ")
print(f"{'Nombre':<15} | {'Precio':^10} | {'Cantidad':^10}")
print("-" * 40)
for producto in inventario:
    print(f"{producto[0]:^15} | {producto[1]:^10.2f} | {producto[2]:^10}")
"""
# Mostrar la matriz inventario n0 2
"""print(" ")  
print("Inventario = [")
for producto in inventario:
    print(f"    {producto},")
print(" ]")
"""
def ordenar_bubllesort(inventario):
    n = len(inventario)
    for i in range(n):
        for j in range(0, n - i - 1):
            if inventario[j][2] > inventario[j + 1][2]:
                menor = inventario[j + 1]
                inventario[j + 1] = inventario[j]
                inventario[j] = menor
    ordenado =  inventario
    return ordenado

def ordenar_insertsort(inventario: list) -> list:
    for i in range(len(inventario)):
        aux = inventario[i]
        j = i - 1
        while j >= 0 and aux < inventario[j][1]:
            inventario[j + 1] = inventario[j] 
            j -= 1
        inventario[ j + 1] = aux
    return inventario 

def ordenar_selccionsort(inventario: list) -> list:
    for i in range(len(inventario)):
        indice_menor = i
        for j in range(i + 1, len(inventario)):
            if inventario[j][2] < inventario[indice_menor][2]:
                indice_menor = j
        if indice_menor != i:
            menor = inventario[indice_menor]
            inventario[indice_menor] = inventario[i]
            inventario[i] = menor
    return inventario

def ordenar_quicksort(inventario: list) -> list:
    menores = []
    iguales = []
    mayores = []
    if len(inventario) > 1:
        pivot = inventario[0][2]
        for elemento in inventario:
            if elemento[2] < pivot:
                menores += [elemento]
            elif elemento[2] == pivot:
                iguales += [elemento]
            else:
                mayores += [elemento]
        ordenada = ordenar_quicksort(menores) + iguales + ordenar_quicksort(mayores)
        return  ordenada
    else:
        return inventario 
    


ordenar = ordenar_bubllesort(inventario)
#ordenar = ordenar_insertsort(inventario)
#ordenar = ordenar_selccionsort(inventario)
#ordenar = ordenar_quicksort(inventario)
print(f"{'Producto':^15} | {'Precio':^10} | {'Cantidad':^10}")
print("-"*45)
for producto in ordenar:
    print(f"{producto[0]:^15} | {producto[1]:^10} | {producto[2]:^10} ")
    