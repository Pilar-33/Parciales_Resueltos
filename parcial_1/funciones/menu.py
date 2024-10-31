from funciones.funcion import *

def menu(pacientes: list) -> None:
    while True:
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
        opcion = input(f"""
                        SISTEMA DE GESTIÓN DE CLÍNICA
        =========================================================
        1. Mostrar todos los pacientes.
        2. Buscar paciente por número de Historia Clinica.
        3. Ordenar pacientes por número de Historia clínica.
        4. Mostrar paciente con más días de  internación.
        5. Mostrar paciente con menos días de internación.
        6. Cantidad de pacientes con más de  5 días de internación.
        7. Promedio de días de internación de todos los pacientes.
        8. Salir
        Elije una opción (1 al 8): """)
        while opcion not in numeros:
            opcion = input("Ërror!!. Ingrese una opción (1 al 8): ")
        opcion = int(opcion)
        
        match opcion:
            case 1:
                print("\npacientes = [")
                for paciente in pacientes:
                    print(f"    {paciente},")
                print(" ]")
            case 2:
                buscar_paciente(pacientes)
            case 3:
                ordenada = oredenar_x_historia_clinica(pacientes)
                print(" ")
                print(f"{'Historia Clinica':^20} | {'Nombre':^20} | {'Edad':^10} | {'Diagnóstico':^20} | {'Días de internacíon':^10}")
                print("-" * 100)
                for paciente in ordenada:
                    print(f"{paciente[0]:^20} | {paciente[1]:^20} | {paciente[2]:^10} | {paciente[3]:^20} | {paciente[4]:^10}")         
            case 4:
                internar_mas_dias(pacientes)
            case 5:
                internar_menos_dias(pacientes)
            case 6:
                mayor_cinco_dias = listar_pacientes_mayor_5dias(pacientes)
                print(" ")
                print(f"{'Historia Clinica':^20} | {'Nombre':^20} | {'Edad':^10} | {'Diagnóstico':^20} | {'Días de internacíon':^10}")
                print("-" * 100)
                for paciente in mayor_cinco_dias:
                    print(f"{paciente[0]:^20} | {paciente[1]:^20} | {paciente[2]:^10} | {paciente[3]:^20} | {paciente[4]:^10}")    
            case 7:
                promedio = promedio_dias_internacion(pacientes)
                print(f"El promedio de días de internación de todos los pacientes: {promedio}")
            case 8:
                print("Gracias por usar nuestro sistema!!!")
                break
            
        seguir = ["s", "n", "S", "N"]
        continuar = input("Desea continuar en el programa(s/n): ")
        while continuar not in seguir:
            continuar = input("Inválido!!!. Desea continuar en el programa(s/n): ")
        
        if continuar in ["n", "N"]:
            print("Gracias por usar el sistema.")
            break
            
        