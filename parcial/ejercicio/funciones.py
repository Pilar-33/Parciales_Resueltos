def validar_numero(mensaje):
    while True:
        es_valido = True
        entrada = input(mensaje)   

        for caracter in entrada:
            if caracter < "0" or caracter > "9":
                es_valido = False
                break
            
        if es_valido and len(entrada) > 0:
            return int(entrada)
        else:
            print("Error. Ingrese un número entero.")

def calcular_cantidad_total(existencias: list, depositos: list) -> list:
    totales = []
    suma = 0
    for i in range(len(depositos)):
        for j in range(len(existencias)):
            suma += existencias[i][j]
        totales += [suma]
    return totales

def reponer_x_deposito(existencias: list, depositos: list, tipo_articulos) -> list:
    reponer = []
    for i in range(len(depositos)):
        for j in range(len(existencias[i])):
            if existencias[i][j] < 3000:
                reponer += [[depositos[i], tipo_articulos[j], existencias[i][j]]]
    return reponer

def encontrar_maxima_cantidad(existencias: list, depositos: list, tipo_articulos: list) -> list:
    maxima = []
    for i in range(len(depositos)):
        for j in range(len(existencias)):
            if existencias[i][j] > 3000:
                maxima += [[depositos[i], tipo_articulos[j], existencias[i][j]]]
    return maxima

def corregir_carga(existencias: list, depositos: list, tipo_articulos: list) -> None:
    continuar = "s"
    while continuar == "s":
        print("\nMODIFICACIÓN DE DATOS\n" + "=" * 35)
        deposito = input(F"Que depósito desea modificar datos?: ")
        while deposito not in depositos:
            print("Error. Depósito no válido.")
            deposito = input("Que depósito desea modificar datos?: ")
        
        indice_deposito = 0
        for i in range(len(depositos)):
            if deposito == depositos[i]:
                indice_deposito = i
                break
        
        articulo = input("Que tipo de artículo desea corregir?: ")
        while articulo not in tipo_articulos:
            print("Error. Artículo no válido.")
            articulo = input("Que tipo de artículo desea corregir?: ")
        
        indice_articulo = 0
        for j in range(len(tipo_articulos)):
            if articulo == tipo_articulos[j]:
                indice_articulo = j
                break
            
        cantidad =validar_numero(f"Ingrese la nueva cantidad de {articulo}: ")
        existencias[indice_deposito][indice_articulo] = cantidad
        print("\nDatos modificados correctamente.")
        
        continuar = input("Desea corregir otro despósito?(s/n): ")
        while continuar not in ["S", "s", "N", "n"]:
            continuar = input("Error!!!. Desea corregir otro despósito?(s/n): ")
            
        if continuar == ["N", "n"]:
            print("\nGracias por usar el programa.")
            break
    
    # mostar información
    print("\nInformación actualizada:")
    print(f"{'Deposito':<12} | {'Artículo':<25} | {'Cantidad':<12}")
    print("----------------------------------------------------")
    for i in range(len(depositos)):
        for j in range(len(existencias[i])):
            print(f"{depositos[i]:<12} | {tipo_articulos[j]:<25} | {existencias[i][j]:<12}")
    
            

                