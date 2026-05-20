"""
-----------------------------------------------------------------------------------------------
Título: TP N° 1 - Entrega1.py
Fecha: Mayo 2026 
Autor: 
Lázaro Martina - Legajo: 1238503
Mastronardi Milena - Legajo: 1233930
Lacava Giuliana - Legajo: 1239334
Cebreiros Juana - Legajo: 1238673
Bianciotto Sofía - Legajo: 1241171

Descripción:
Este programa permite cargar y trabajar con una lista de números enteros.
A través de un menú de opciones, el usuario puede:
   1. Generar números al azar de 1, 3 y 5 dígitos.
   2. Mostrar los datos en una tabla ordenada de 10 columnas.
   3. Eliminar los números repetidos sin cambiar el orden original.
   4. Filtrar los números (mayores, menores, pares, impares o en rango).
   5. Desdoblar la lista en varias listas según diferentes criterios.
   6. Ver un ranking con los "N" valores más altos.
   7. Buscar el máximo y el mínimo y mostrarlos destacados en la tabla.

 Todo el código está hecho usando funciones separadas y respetando las
 reglas de la cátedra (sin usar funciones automáticas como max, min o sort).

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def pedir_entero (mensaje):
    """
    Solicita un número entero al usuario por teclado y lo valida.
    Asegura que la entrada esté compuesta únicamente por dígitos utilizando 
    el método .isdigit(), repitiendo el pedido en caso de error.
    Recibe:
        mensaje (str): El texto explicativo que se le muestra al usuario para pedir el dato.   
    Devuelve:
        int: El número entero ingresado por el usuario, una vez comprobado que es válido.
    """
    while True:
        cadena = input(mensaje)
        if cadena.isdigit():
            return int(cadena)
        else:
            print("Error: Debe ingresar un número entero válido (solo digitos). Intente nuevamente.")



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ DEL PROGRAMA           ")
            print("---------------------------")
            print("[1] Opción 1")
            print("[2] Opción 2")
            print("[3] Opción 3")
            print("[4] Opción 4")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            ...
        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()