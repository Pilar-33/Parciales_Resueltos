from os import system
system("cls")

depositos = ["PBA", "CABA", "Chubut", 
            "Tucumán", "Mendoza"]

juguetes = [
    "autos", "muñecas", "trenes",
    "peluches", "spinners", "cartas"
]
    #autos|muñcas|trenes|peluches|spinners|cartas   
existencias = [
    [1000, 200, 800, 400, 500],  #PBA
    [150, 2500, 350, 4500, 550], #CABA
    [2000, 300, 600, 5000, 900], #Chubut
    [250, 3500, 450, 550, 6050], #Tucuman
    [1000, 400, 5000, 600, 70]   #Mendoza
]

# sumar por filas
totales = []
for i in range(len(existencias)):
    suma = 0
    for j in range(len(existencias[0])):
        suma += existencias[i][j]
    totales += [suma]

print(totales)

#print("""
            #TOTAL DE JUGUETES POR DEPÓSITO
            #================================""")  
"""for i in range(len(totales)):
    print(f"\t\t* {depositos[i]}: {totales[i]} unidades")"""
    
# sumar por columnas
totales1 = []
for i in range(len(existencias[0])):
    suma1 = 0
    for j in range(len(existencias)):
        suma1 += existencias[j][i]
    totales1 += [suma1]

#print(totales1)
#print("""
                #TOTAL DE JUGUETES POR TIPO
            #=================================""")  
"""for i in range(len(totales1)):
    print(f"\t\t* {juguetes[i]}: {totales1[i]} unidades")"""
