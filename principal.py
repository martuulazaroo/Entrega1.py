"""
-----------------------------------------------------------------------------------------------
Título: TP N° 1 - Entrega1.py
Fecha:
Autor: 
Lázaro Martina - Legajo: 1238503
Mastronardi Milena - Legajo: 1233930
Lacava Giuliana - Legajo: 1239334
Cebreiros Juana - Legajo: 1238673
Bianciotto Sofía - Legajo: 1241171

Descripción:

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

def desdoblarValores(lista):
    listaTrabajo = lista
    criterio = input("\nIngrese le cirterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]\t").upper()

    while (criterio != P) and (criterio != C) and (criterio != U):
        criterio = input("\nERROR - Ingrese le cirterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]\t").upper()

    if criterio == P:
        pares = []
        impares = []
        for i in range(len(listaTrabajo)):
            if listaTrabajo[i] % 2 == 0:
                pares.append(listaTrabajo[i])
            else:
                impares.append(listaTrabajo[i])
        listados = [pares, impares]
    
    elif criterio == C:
        unaCifra = []
        tresCifras = []
        cincoCifras = []

        for i in range(len(listaTrabajo)):
            cifras = len(str(listaTrabajo[i]))
            if cifras == 1:
                unaCifra.append(listaTrabajo[i])
            elif cifras == 3:
                tresCifras.append(listaTrabajo[i])
            elif cifras == 5:
                cincoCifras.append(listaTrabajo[i])
                
        listados = [unaCifra, tresCifras, cincoCifras]
    
    else:
        hastaUmbral = []
        encimaUmbral = []
        umbral = int(input("\n Ingrese el numero umbral:\t"))
        
    return listados

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    ...


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