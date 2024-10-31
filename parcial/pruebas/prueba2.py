from os import system
system("cls")

def validar_numero(mensaje):
    while True:
        entrada = input(mensaje)
        es_valido = True
        
        if entrada < '0' or entrada > '9':
            es_valido = False
            break
        
        if es_valido and len(entrada) > 0:
            return int(entrada)
        else:
            print("Solo se permiten números enteros!!!")
        
        
            
depositos = ["PBA", "Jujuy", "Neuquen"]
tipo_articulos = [
    "quimicos", "trapos", "escobas", 
    "cepillos", "papel higienico", 
    "jabon", "pañuelos descartables"
    ]

n_deposito = len(depositos)
n_tipo = len(tipo_articulos)
existencias = []
for i in range(n_deposito):
    fila = [0] * n_tipo
    existencias += [fila]
    
print("existencias = [")
for i in existencias:
    print(f"  {i},")
print("]")
        

for i in range(n_deposito):
    print(f"  \nExistencias para deepósito {depositos[i]}\n" + "=" * 35)
    for j in range(n_tipo):
        cantidad = validar_numero(f"Cantidad de {tipo_articulos[j]}: ")
        existencias[i][j] = cantidad
        
# Mostrar las existencias cargadas
"""print("\n       Resumen de existencias:" + "="*30)
for i in range(n_deposito):
    print(f"\n  Existencias en {depositos[i]}")
    print("========================================")
    for j in range(n_tipo):
        print(f"{tipo_articulos[j]}: {existencias[i][j]} unidades")"""


# Mostrar las existencias en formato de tabla
print("\nTabla de existencias:\n")
# Imprimir encabezado
print(f"{'Provincias':<12}", end="")
for articulo in tipo_articulos:
    print(f"{articulo:<18}", end="")
print()

# Imprimir las filas con los datos de cada depósito
for i in range(n_deposito):
    print(f"{depositos[i]:<12}", end="")  # Imprimir nombre de la provincia
    for j in range(n_tipo):
        print(f"{existencias[i][j]:<18}", end="")  # Imprimir cantidades con alineación
    print()  # Nueva línea para la siguiente provincia