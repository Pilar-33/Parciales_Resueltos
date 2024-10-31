from os import system
system("cls")

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

#7. Porcentaje de artículos de cada tipo sobre el total 
# de artículos almacenados. Realizar
#una función que muestre el porcentaje de cada uno.

def porcentaje_articulos(existencias: list, tipo_articulos: list) -> list:
    total_unidades = 0
    cantidades_por_articulo = [0] * len(tipo_articulos)
    for  i in range(len(existencias)):
        for j in range(len(tipo_articulos)):
            if existencias[i][1] == tipo_articulos[j]:
                cantidades_por_articulo[j] += existencias[i][2]
                total_unidades += existencias[i][2]
    
    #calcular porcentaje
    porcentajes = []
    for i in range(len(tipo_articulos)):
        porcentaje = (cantidades_por_articulo[i] / total_unidades) * 100
        porcentajes += [porcentaje]

    return porcentajes

porcentaje = porcentaje_articulos(existencias, tipo_articulos)
for i in range(len(existencias)):
    for j in range(len(tipo_articulos)):
        if existencias[i][1] == tipo_articulos[j]:
            print(f"{tipo_articulos[j]} = {porcentaje[j]:.2f}%")
        
            
        
    
    