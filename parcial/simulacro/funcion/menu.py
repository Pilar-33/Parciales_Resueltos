from funcion.funciones import *

# Menú principal
def menu_principal() -> None:
    """
    Muestra el menú principal para que el usuario elija una opción. 
    Las opciones permiten cargar productos, buscar un producto, 
    ordenar el inventario, mostrar el producto más caro y más barato, 
    o listar productos con precio superior a 15000.

    El ciclo continúa hasta que el usuario elige salir.
    
    No retorna ningún valor.
    """

    # iNVENTARIO
    """inventario = [
        ["Manzanas", 2500, 50],
        ["Plátanos", 1800, 30],
        ["Peras", 3500, 20],
        ["Naranjas", 2800, 40],
        ["Uvas", 9000, 15],
        ["Sandías", 15000, 10],
        ["Melones", 30000, 12],
        ["Kiwi", 18000, 25],
        ["Piñas", 13000, 8],
        ["Fresas", 25000, 35]
    ]"""
    
    while True:
        numeros = ["1", "2", "3", "4", "5", "6"]
        opcion = input(f"""
                            MENÚ PRINCIPAL
            ==============================================
            1. Cargar producto/s.
            2. Buscar Producto.
            3. Ordenar inventario
            4. Mostrar producto más caro y más barato.
            5. Mostrar productos con precio mayor a 15000
            6. Salir
            Ingrese una opción (1 al 6): """)
        while opcion not in numeros:
            opcion = input("Opción no válida. Ingrese una opción (1 al 6): ")
        opcion = int(opcion)
        
        match opcion:
            case 1:
                inventario = cargar_datos()
                # Mostrar la matriz inventario
                print(" ")  
                print("Inventario = [")
                for producto in inventario:
                    print(f"    {producto},")
                print(" ]")
            case 2:
                print("               PRODUCTO BUSCADO\n" + "=" * 50)
                buscar = buscar_producto(inventario)
                print(f"""
                            PRODUCTO ENCONTRADO
                    ===============================
                    Producto: {buscar[0]}
                    Precio: ${buscar[1]}
                    Cantidad: {buscar[2]}""")
            case 3:
                ordenar = ordenar_datos(inventario)
                # Mostrar la matriz inventario no 1
                print(" ")
                print(f"{ 'Nombre':<15} | {'Precio':^10} | {'Cantidad':^10}")
                print("-" * 40)
                for producto in ordenar:
                    print(f"{producto[0]:^15} | {producto[1]:^10.2f} | {producto[2]:^10}")
            case 4:
                caro_barato = mostrar_producto_caro_barato(inventario)
                producto_caro = caro_barato[0]
                producto_barato = caro_barato [1]
                print(f"""
                            PRODUCTO CARO
                    ===============================
                    Product0: {producto_caro[0]}
                    Precio: ${producto_caro[1]}
                    Cantidad: {producto_caro[2]}
                    
                            PRODUCTO BARATO
                    ================================
                    Product0: {producto_barato[0]}
                    Precio: ${producto_barato[1]}
                    Cantidad: {producto_barato[2]}""")
            case 5:
                precios_altos = evaluar_precios_altos(inventario)
                print(" ")
                print(f"{'Nombre':<15} | {'Precio':^10} | {'Cantidad':^10}")
                print("-" * 40)
                for producto in precios_altos:
                    print(f"{producto[0]:^15} | {producto[1]:^10.2f} | {producto[2]:^10}")   
            case 6:
                print("Gracias por elegirnos.")
                break
            
        continuar = input("Desea continuar? (s/n): ")
        while continuar not in ["s", "n", "S", "N"]:
            continuar = input("Debe ingresar (s/n). Desea continuar?: ")
            
        if continuar in ["n", "N"]:
            print("Gracias por usar el programa.")
            break